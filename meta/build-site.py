#!/usr/bin/env python3
"""Build the HTML study-guide data file from the markdown chapters.

Reads the 00..92 *.md files in the repo root (the only source of truth), converts them with python-markdown and
writes guide/data/guide.js (window.SEC_GUIDE = {...}) in the practice-site repo. See meta/GUIDE-SITE.md.

  python3 meta/build-site.py [--out PATH] [--src DIR]
"""
import argparse, glob, hashlib, html, json, os, re, subprocess, sys, unicodedata
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OUT = os.path.normpath(os.path.join(ROOT, '..', 'steeb-k.github.io', 'sec-plus-test', 'guide', 'data', 'guide.js'))

# md filename prefix -> route slug (the quiz site hard-codes the same slugs in js/ui.js)
SLUGS = {
    '00': 'exam-overview',
    '01': 'domain-1-general-security-concepts',
    '02': 'domain-2-threats-vulnerabilities-mitigations',
    '03': 'domain-3-security-architecture',
    '04': 'domain-4-security-operations',
    '05': 'domain-5-program-management-oversight',
    '90': 'ports-protocols',
    '91': 'acronyms',
    '92': 'formulas-numbers',
}
NOTE_RE = re.compile(r'^> \*\*Note:\*\* AI-generated[^\n]*\n(?:[ \t]*\n)?', re.M)
HEAD_RE = re.compile(r'<h([1-6])(?: id="[^"]*")?>(.*?)</h\1>', re.S)
OBJ_RE = re.compile(r'^(\d)\.(\d+) ')


def slugify(text):
    t = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii').lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')


def plain(fragment):
    """HTML fragment -> plain text with single spaces."""
    t = re.sub(r'<[^>]+>', ' ', fragment)
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()


def heading_id(text, used):
    m = OBJ_RE.match(text)
    base = 'obj-%s-%s' % (m.group(1), m.group(2)) if m else (slugify(text) or 'section')
    cand, n = base, 2
    while cand in used:
        cand = '%s-%d' % (base, n)
        n += 1
    used.add(cand)
    return cand


LIST_RE = re.compile(r'^\s*(?:[-*+]|\d+[.)])\s')


def blank_before_lists(md_text):
    """python-markdown needs a blank line between a paragraph and the list that follows it; GitHub does not.
    Insert one (outside fenced code) so the chapters render the same as on GitHub."""
    out, fence, prev = [], False, ''
    for line in md_text.split('\n'):
        if line.lstrip().startswith('```'):
            fence = not fence
        elif (not fence and LIST_RE.match(line) and prev.strip() and not LIST_RE.match(prev)
              and not prev[:1].isspace() and prev[:1] not in '|>#'):
            out.append('')
        out.append(line)
        prev = line
    return '\n'.join(out)


BQ_SPLIT = '<!--bq-split-->'


def split_blockquotes(md_text):
    """python-markdown merges '> a' + blank + '> b' into ONE blockquote; GitHub renders two callouts. Put a raw-HTML
    marker between them (outside fenced code) so they stay separate; convert() strips the marker afterwards."""
    out, fence, last = [], False, ''
    for line in md_text.split('\n'):
        if line.lstrip().startswith('```'):
            fence = not fence
        if not fence and line.startswith('>') and out and not out[-1].strip() and last.startswith('>'):
            out.extend([BQ_SPLIT, ''])
        out.append(line)
        if line.strip():
            last = line if not fence else ''
    return '\n'.join(out)


def convert(md_text):
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'sane_lists', 'md_in_html'])
    return re.sub(r'\n?' + re.escape(BQ_SPLIT) + r'\n*', '\n', md.convert(md_text))


def add_heading_ids(body):
    """Replace/insert ids on every heading; return (html, [(level, id, text)])."""
    used, heads = set(), []

    def sub(m):
        level, inner = int(m.group(1)), m.group(2)
        text = plain(inner)
        hid = heading_id(text, used)
        heads.append((level, hid, text))
        return '<h%d id="%s">%s</h%d>' % (level, hid, inner, level)
    return HEAD_RE.sub(sub, body), heads


def add_acronym_rows(body, anchors):
    """Give every row of the acronym tables an id (first cell is the key)."""
    used = set()

    def sub(m):
        key = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
        base = 'acr-' + (re.sub(r'[^a-z0-9]+', '-', key.lower()).strip('-') or 'x')
        cand, n = base, 2
        while cand in used:
            cand = '%s-%d' % (base, n)
            n += 1
        used.add(cand)
        anchors.setdefault(key, cand)
        alt = re.match(r'^(\S+) \((\S+)\)$', key)       # "IMAP (IMAP4)": both spellings point at this row
        if alt:
            anchors.setdefault(alt.group(1), cand)
            anchors.setdefault(alt.group(2), cand)
        return '<tr id="%s">\n<td>%s</td>' % (cand, m.group(1))
    return re.sub(r'<tr>\s*<td>(.*?)</td>', sub, body, flags=re.S)


def fix_internal_links(body, slug):
    """Same-file '#x' anchors become SPA routes '#/<slug>/x'."""
    return re.sub(r'href="#([^/"][^"]*)"', lambda m: 'href="#/%s/%s"' % (slug, m.group(1)), body)


def short_label(title):
    m = re.match(r'(Domain \d)', title)
    return m.group(1) if m else title


def git(src, *args):
    try:
        return subprocess.check_output(['git', '-C', src] + list(args), stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=DEFAULT_OUT)
    ap.add_argument('--src', default=ROOT)
    a = ap.parse_args()

    paths = sorted(glob.glob(os.path.join(a.src, '[0-9][0-9]-*.md')), key=os.path.basename)
    if len(paths) != len(SLUGS):
        sys.exit('expected %d chapter files, found %d' % (len(SLUGS), len(paths)))
    sha = hashlib.sha256()
    files, sections, anchors = [], [], {}
    for p in paths:
        raw = open(p, 'rb').read()
        sha.update(raw)
        name = os.path.basename(p)
        fid = name[:2]
        slug = SLUGS[fid]
        text = NOTE_RE.sub('', raw.decode('utf-8'), count=1)
        body = convert(split_blockquotes(blank_before_lists(text)))
        body, heads = add_heading_ids(body)
        if fid == '91':
            body = add_acronym_rows(body, anchors)
        body = fix_internal_links(body, slug)
        title = next(t for l, _, t in heads if l == 1)
        title = re.sub(r'\s*\(\d+%\)\s*$', '', title)
        toc = [{'level': l, 'id': i, 'text': t} for l, i, t in heads if l in (2, 3)]
        files.append({'id': fid, 'slug': slug, 'title': title, 'src': name, 'html': body, 'toc': toc})
        sections.extend(build_sections2(slug, title, body, heads))
    commit = git(a.src, 'rev-parse', '--short', 'HEAD') or 'uncommitted'
    # builtAt = the guide repo's HEAD commit date (not the wall clock) so rebuilding unchanged sources is byte-identical
    built = git(a.src, 'log', '-1', '--format=%cI') or ''
    data = {
        'sourceCommit': commit,
        'sourceHash': sha.hexdigest(),
        'builtAt': built,
        'files': files, 'sections': sections, 'acronymAnchors': anchors,
    }
    write_js(a.out, data)
    print('wrote %s: files=%d sections=%d acronymAnchors=%d (%d KB)' % (
        a.out, len(files), len(sections), len(anchors), os.path.getsize(a.out) // 1024))


def build_sections2(file_slug, title, body, heads):
    """Sections from the final html: heads[i] corresponds to the i-th heading match."""
    out, stack = [], {}
    pieces = list(HEAD_RE.finditer(body))
    assert len(pieces) == len(heads)
    for i, m in enumerate(pieces):
        level, hid, text = heads[i]
        if level > 3:
            continue
        end = pieces[i + 1].start() if i + 1 < len(pieces) else len(body)
        stack[level] = text
        for l in [l for l in stack if l > level]:
            del stack[l]
        if level == 1:
            path = short_label(text)
        else:
            path = ' \u203a '.join([short_label(stack.get(1, title))] + [stack[l] for l in (2, 3) if l in stack])
        out.append({'file': file_slug, 'id': hid, 'title': text, 'path': path, 'text': plain(body[m.end():end])})
    return out


def js_str(v):
    s = json.dumps(v, ensure_ascii=False)
    return s.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')


def write_js(path, d):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = ['// GENERATED by meta/build-site.py from the guide repo markdown. Do not edit by hand.',
             'window.SEC_GUIDE = {']
    for k in ('sourceCommit', 'sourceHash', 'builtAt'):
        lines.append('  %s: %s,' % (k, js_str(d[k])))
    lines.append('  files: [')
    lines.append(',\n'.join('    ' + js_str(f) for f in d['files']))
    lines.append('  ],')
    lines.append('  sections: [')
    lines.append(',\n'.join('    ' + js_str(s) for s in d['sections']))
    lines.append('  ],')
    lines.append('  acronymAnchors: ' + js_str(d['acronymAnchors']))
    lines.append('};')
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
