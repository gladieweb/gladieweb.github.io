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
        if tag == 'html':
            self.lang = a.get('lang')

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
language_pages = json.loads((ROOT / 'content/language-pages.json').read_text(encoding='utf-8'))
for name in language_pages:
    es, en = ROOT / name, ROOT / 'en' / name
    assert documents[es.resolve()].lang == 'es'
    assert documents[en.resolve()].lang == 'en'
    assert documents[es.resolve()].videos == documents[en.resolve()].videos, f'{name}: video mismatch'
    for path in [es, en]:
        content = path.read_text(encoding='utf-8')
        assert 'hreflang="es"' in content and 'hreflang="en"' in content
        assert 'data-language="es"' in content and 'data-language="en"' in content
for name in ['privacypolicy.html', 'account-deletion.html', 'skeleton-warfare.html']:
    assert 'language.js' not in (ROOT / name).read_text(encoding='utf-8-sig'), 'Game/legal pages must not auto-redirect'
for prefix, current_date, pilot in [('', 'Feb 2026 — Actualidad', 'Piloto a desarrollar'), ('en/', 'Feb 2026 — Present', 'Proposed pilot')]:
    profile = (ROOT / prefix / 'perfil.html').read_text(encoding='utf-8')
    assert current_date in profile and 'SciSoft' in profile
    assert 'DrawMate' in profile and 'EasyViewDesigner2' in profile
    for area in ['software', 'visualizacion', 'videojuegos']:
        content = (ROOT / prefix / (area + '.html')).read_text(encoding='utf-8')
        assert 'class="ai-offer"' in content and pilot in content
    # Future technologies belong to proposals, not to completed projects or the skills list.
    for slug in ['scisoft-grafika', 'grafika-mcp', 'streaming-interactivo']:
        content = (ROOT / prefix / 'proyectos' / (slug + '.html')).read_text(encoding='utf-8')
        assert 'NVIDIA ACE' not in content and 'Agentic Gameplay' not in content
print(f'PASS: {len(documents)} pages, links and anchors, {len(language_pages)} language pairs, 14 videos, professional updates, scoped AI pilots, legal pages unchanged.')
