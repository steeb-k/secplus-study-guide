#!/usr/bin/env python3
"""Concatenate the study guide into one markdown file: STUDY-GUIDE-FULL.md
Order: 00, 01-05, 90, 91, 92. Each file's headings are demoted one level under a single H1.
The per-file 'AI-generated' note is dropped in favour of one disclaimer at the top."""
import re, glob, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
files = sorted(glob.glob('[0-9][0-9]-*.md'))
NOTE = re.compile(r'^> \*\*Note:\*\* AI-generated content.*\n\n?', re.M)
out = ['# CompTIA Security+ SY0-701 — Complete Study Guide\n',
       '> **⚠ AI-generated, not yet vetted.** This guide was written by AI from its knowledge of the CompTIA SY0-701 objectives and has '
       '**not yet been reviewed by a human for accuracy**. Cross-check anything surprising against the official objectives before relying on it.\n',
       '## Contents\n']
sections = []
for f in files:
    s = open(f, encoding='utf-8').read()
    s = NOTE.sub('', s, count=1)
    m = re.match(r'#\s+(.*)', s)
    title = m.group(1).strip() if m else f
    sections.append((f, title, s))
    slug = re.sub(r'[^a-z0-9 -]', '', title.lower()).strip().replace(' ', '-')
    out.append(f'- [{title}](#{slug})')
out.append('\n---\n')
in_code = False
for f, title, s in sections:
    body = []
    for line in s.split('\n'):
        if line.startswith('```'): in_code = not in_code
        if not in_code and re.match(r'#{1,5}\s', line): line = '#' + line
        body.append(line)
    out.append('\n'.join(body).rstrip() + '\n\n---\n')
open('STUDY-GUIDE-FULL.md', 'w', encoding='utf-8').write('\n'.join(out))
print('wrote STUDY-GUIDE-FULL.md from', len(files), 'files')
