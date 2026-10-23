"""Validate the static site and its important compatibility guarantees."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import subprocess

ROOT = Path(__file__).resolve().parent.parent

class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.refs, self.videos = path, set(), [], []
        self.h1 = 0
        self.feed(path.read_text(encoding='utf-8-sig'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f'{self.path}: duplicate id {a["id"]}'
            self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'a' and 'href' in a: self.refs.append(a['href'])
        if tag == 'link' and a.get('rel') == 'stylesheet': self.refs.append(a['href'])
        if tag == 'script' and 'src' in a: self.refs.append(a['src'])
        if tag == 'iframe':
            assert a.get('title'), f'{self.path}: iframe without title'
            self.videos.append(a.get('src', ''))
            assert a.get('loading') == 'lazy', f'{self.path}: video must load lazily'

documents = {p.resolve(): Document(p) for p in ROOT.glob('**/*.html') if '.git' not in p.parts}
for path, doc in documents.items():
    assert doc.h1 == 1, f'{path}: expected one h1'
    for ref in doc.refs:
        url = urlsplit(ref)
        if url.scheme or url.netloc: continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        assert target.is_file(), f'{path}: missing {ref}'
        if url.fragment and target in documents:
            assert unquote(url.fragment) in documents[target].ids, f'{path}: missing anchor {ref}'
    if path.name not in ['privacypolicy.html', 'account-deletion.html']:
        for required in ['privacypolicy.html', 'account-deletion.html']:
            assert any((path.parent / urlsplit(r).path).resolve() == ROOT / required for r in doc.refs), f'{path}: missing legal link'

sources = json.loads((ROOT / 'content/media-sources.json').read_text(encoding='utf-8'))
original_ids = {video[0] for p in sources['projects'] for video in p['videos']}
actual_ids = {urlsplit(src).path.split('/')[-1] for d in documents.values() for src in d.videos}
assert len(original_ids) == 14, f'Expected 14 original videos, got {len(original_ids)}'
assert original_ids == actual_ids, 'Some original videos are missing'
for name in ['privacypolicy.html', 'account-deletion.html', 'PrivacyPolicy.txt', 'styles.css']:
    committed = subprocess.check_output(['git', 'show', f'HEAD:{name}'], cwd=ROOT).decode('utf-8-sig').replace('\r\n', '\n')
    current = (ROOT / name).read_text(encoding='utf-8-sig').replace('\r\n', '\n')
    assert committed == current, f'{name}: existing legal content or styles changed'

home = (ROOT / 'index.html').read_text(encoding='utf-8')
assert 'class="timeline"' not in home and 'class="project-grid"' not in home, 'Home should remain concise'
print(f'PASS: {len(documents)} pages, all local links and anchors, 14 videos, legal pages unchanged.')
