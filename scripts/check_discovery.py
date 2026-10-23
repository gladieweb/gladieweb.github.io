"""Validate search metadata, bilingual discovery and truthful profile markup."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from urllib.robotparser import RobotFileParser
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = 'https://gladieweb.github.io'
PAGES = json.loads((ROOT / 'content/language-pages.json').read_text(encoding='utf-8'))

class Metadata(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.canonical, self.alternates, self.description, self.payload = [], {}, None, []
        self.structured = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'link':
            if a.get('rel') == 'canonical': self.canonical.append(a['href'])
            if a.get('rel') == 'alternate': self.alternates[a['hreflang']] = a['href']
        if tag == 'meta' and a.get('name') == 'description': self.description = a['content']
        if tag == 'script' and a.get('type') == 'application/ld+json': self.structured = True

    def handle_endtag(self, tag):
        if tag == 'script': self.structured = False

    def handle_data(self, text):
        if self.structured: self.payload.append(text)

expected = set()
for name in PAGES:
    for prefix, language in [('', 'es'), ('en/', 'en')]:
        path = prefix + name
        html = (ROOT / path).read_text(encoding='utf-8')
        meta = Metadata(html)
        suffix = path.removesuffix('index.html') if path.endswith('index.html') else path
        url = ORIGIN + '/' + suffix
        expected.add(url)
        assert meta.canonical == [url], f'{path}: wrong canonical'
        assert set(meta.alternates) == {'es', 'en', 'x-default'}
        assert meta.alternates[language] == url, f'{path}: missing self alternate'
        assert all(value.startswith(ORIGIN + '/') and '?' not in value for value in meta.alternates.values())
        data = json.loads(''.join(meta.payload))
        assert data['@context'] == 'https://schema.org'
        graph = data['@graph']
        webpage = next(n for n in graph if n['@type'] in ['WebPage', 'ProfilePage'])
        assert webpage['url'] == url and webpage['inLanguage'] == language
        assert webpage['description'] == meta.description
        assert not any('aggregateRating' in n or 'review' in n for n in graph)
        if name == 'perfil.html':
            person = next(n for n in graph if n['@type'] == 'Person')
            assert person['name'] == 'Lucas Villalva' and person['worksFor']['name'] == 'SciSoft'
            assert 'Gameplay Ability System (GAS)' in person['knowsAbout']
            assert 'Firebase' in person['knowsAbout']
            assert any('Knapsack' in skill for skill in person['knowsAbout'])
            assert 'Behavior Trees' in person['knowsAbout']
            assert 'Steering Behaviors' in person['knowsAbout']
            assert any('Fixed-function pipeline' in skill for skill in person['knowsAbout'])
            assert 'Vertex shaders' in person['knowsAbout'] and 'Fragment shaders' in person['knowsAbout']
            assert 'Cg (Unity)' in person['knowsAbout']
            assert any('3D math' in skill for skill in person['knowsAbout'])
            assert any('Linear algebra' in skill for skill in person['knowsAbout'])
            assert not any(term in ' '.join(person['knowsAbout']) for term in ['NVIDIA ACE', 'Agentic Gameplay', 'RAG'])
            text = (ROOT / prefix / 'perfil.txt').read_text(encoding='utf-8')
            assert 'lucas.villalva@gmail.com' in text and 'SciSoft' in text and 'AppsFlyer' in text
            assert '<script' not in text and 'schema.org' not in text
        if name.endswith('valoracion-acciones-python.html'):
            assert 'Yahoo Finance' in html and 'AAPL' in html and 'Python' in html
            assert 'microservice' in html if language == 'en' else 'microservicio' in html

ns = {'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
tree = ET.parse(ROOT / 'sitemap.xml')
locations = [el.text for el in tree.findall('s:url/s:loc', ns)]
expected.update(ORIGIN + '/' + name for name in ['skeleton-warfare.html', 'privacypolicy.html', 'account-deletion.html'])
assert len(locations) == len(set(locations)), 'Duplicate sitemap URLs'
assert set(locations) == expected, 'Sitemap must contain every language pair and legal page'
for url in locations:
    path = urlsplit(url).path.lstrip('/')
    if not path or path.endswith('/'): path += 'index.html'
    assert (ROOT / path).is_file(), f'Sitemap target missing: {url}'

robots = RobotFileParser()
robots.parse((ROOT / 'robots.txt').read_text(encoding='utf-8').splitlines())
for bot in ['Googlebot', 'Bingbot', 'OAI-SearchBot']:
    assert all(robots.can_fetch(bot, url) for url in expected), bot
assert robots.site_maps() == [ORIGIN + '/sitemap.xml']
print(f'PASS: {len(PAGES)*2} canonical pages, reciprocal language metadata, valid JSON-LD, truthful skills, text resumes and {len(locations)} sitemap URLs.')
