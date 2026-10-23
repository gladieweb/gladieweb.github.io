"""Search metadata and crawlable identity, using only visible, supported content."""
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET
from localization import translate

SITE = 'https://gladieweb.github.io'
PERSON_ID = SITE + '/#lucas-villalva'
SAME_AS = [
    'https://github.com/gladieweb',
    'https://fab.com/sellers/Lucas%20Villalva',
    'https://marvelous-blackbird-ddf.notion.site/Lucas-Villalva-Senior-Game-Developer-2187ed50e2b080508b5affe8f9f265b5',
]
TITLES = {
    'index.html': ('Lucas Villalva | Software, gráficos y experiencias 3D', 'Lucas Villalva | Software, Graphics & Real-Time 3D Developer'),
    'software.html': ('Desarrollo de software, TypeScript, Python & MCP | Lucas Villalva', 'Software Developer, TypeScript, Python & MCP | Lucas Villalva'),
    'visualizacion.html': ('Visualización 3D, Archviz & producción virtual | Lucas Villalva', 'Real-Time 3D, Archviz & Virtual Production | Lucas Villalva'),
    'videojuegos.html': ('Desarrollador senior Unity & Unreal Engine | Lucas Villalva', 'Senior Unity & Unreal Engine Developer | Lucas Villalva'),
    'perfil.html': ('Lucas Villalva | CV de software, Unity & Unreal Engine', 'Lucas Villalva | Software, Unity & Unreal Engine Resume'),
    'contacto.html': ('Contactar a Lucas Villalva | Desarrollo & colaboración', 'Contact Lucas Villalva | Development & Collaboration'),
}

def canonical(name, lang='es'):
    path = ('' if lang == 'es' else 'en/') + name
    if path.endswith('index.html'):
        path = path[:-len('index.html')]
    return SITE + '/' + path

class MainText(HTMLParser):
    """Plain-text resume from the same visible content as the HTML profile."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.active, self.parts, self.link = False, [], None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'main': self.active = True
        if not self.active: return
        if tag in ['section', 'h1', 'h2', 'h3', 'h4', 'p', 'summary', 'li', 'br', 'dt', 'dd', 'div']:
            self.parts.append('\n')
        if tag == 'span': self.parts.append(' ')
        if tag == 'a': self.link = a.get('href')

    def handle_endtag(self, tag):
        if tag == 'main': self.active = False
        if not self.active: return
        if tag == 'a' and self.link:
            if self.link.startswith('https:'): self.parts.append(' (' + self.link + ')')
            self.link = None
            self.parts.append('\n')
        if tag in ['section', 'h1', 'h2', 'h3', 'h4', 'p', 'summary', 'li', 'dt', 'dd', 'div']:
            self.parts.append('\n')

    def handle_data(self, data):
        if self.active: self.parts.append(data)

    def text(self):
        lines = [' '.join(line.split()) for line in ''.join(self.parts).splitlines()]
        return '\n'.join(line for line in lines if line) + '\n'

def build_discovery(root, names, projects, areas, capabilities):
    projects_by_path = {'proyectos/' + p['slug'] + '.html': p for p in projects}
    for lang in ['es', 'en']:
        tr = (lambda text: text) if lang == 'es' else translate
        profile_url = canonical('perfil.html', lang)
        home_url = canonical('index.html', lang)
        person_ref = {'@type': 'Person', '@id': PERSON_ID, 'name': 'Lucas Villalva', 'url': profile_url}
        for name in names:
            path = root / ('' if lang == 'es' else 'en') / name
            html = path.read_text(encoding='utf-8')
            existing_title = unescape(re.search(r'<title>(.*?)</title>', html, re.S).group(1))
            title = TITLES[name][lang == 'en'] if name in TITLES else existing_title
            description = unescape(re.search(r'<meta name="description" content="([^"]*)"', html).group(1))
            url = canonical(name, lang)
            html = re.sub(r'<title>.*?</title>', lambda _: '<title>' + escape(title) + '</title>', html, count=1, flags=re.S)
            html = re.sub(r'<meta property="og:title" content="[^"]*">', lambda _: '<meta property="og:title" content="' + escape(title, quote=True) + '">', html, count=1)
            # Absolute reciprocal alternates are unambiguous to crawlers.
            html = re.sub(r'  <link rel="alternate" hreflang="(?:es|en)"[^>]*>\n', '', html)
            head = f'  <link rel="canonical" href="{url}">\n'
            for code in ['es', 'en']:
                head += f'  <link rel="alternate" hreflang="{code}" href="{canonical(name, code)}">\n'
            default = canonical('index.html') if name == 'index.html' else canonical(name, 'en')
            head += f'  <link rel="alternate" hreflang="x-default" href="{default}">\n'
            head += f'  <meta name="robots" content="index, follow, max-image-preview:large">\n  <meta name="author" content="Lucas Villalva">\n  <meta property="og:url" content="{url}">\n  <meta property="og:locale" content="{"es_AR" if lang == "es" else "en_US"}">\n'

            site = {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'Lucas Villalva · Gladieweb', 'inLanguage': ['es', 'en'], 'publisher': {'@id': PERSON_ID}}
            webpage = {'@type': 'ProfilePage' if name == 'perfil.html' else 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title, 'description': description, 'inLanguage': lang, 'isPartOf': {'@id': site['@id']}, 'author': person_ref}
            graph = [site, webpage]

            if name == 'perfil.html':
                skills = list(dict.fromkeys(tr(skill) for g in capabilities['perfil'] for skill in g['skills']))
                person = dict(person_ref, sameAs=SAME_AS, description=description, jobTitle='Graphics Programmer / Software & Game Developer', worksFor={'@type': 'Organization', 'name': 'SciSoft'}, knowsAbout=skills, knowsLanguage=['Spanish', 'English'], homeLocation={'@type': 'Place', 'name': 'Buenos Aires, Argentina'})
                graph.append(person)
                webpage['mainEntity'] = {'@id': PERSON_ID}
            elif name in projects_by_path:
                p = projects_by_path[name]
                work_id = url + '#project'
                graph.append({'@type': 'CreativeWork', '@id': work_id, 'name': tr(p['title']), 'description': tr(p['summary']), 'url': url, 'inLanguage': lang, 'contributor': person_ref, 'keywords': [tr(skill) for skill in p['skills']]})
                webpage['mainEntity'] = {'@id': work_id}
            elif name.removesuffix('.html') in areas:
                area = areas[name.removesuffix('.html')]
                service_id = url + '#service'
                # Only established offers are marked up. Proposed AI pilots are not credentials.
                graph.append({'@type': 'Service', '@id': service_id, 'name': tr(area['label']), 'description': tr(area['intro']), 'url': url, 'provider': person_ref, 'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': tr(area['label']), 'itemListElement': [{'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': tr(label), 'description': tr(desc), 'provider': person_ref}} for label,desc in area['offers']]}})
                webpage['mainEntity'] = {'@id': service_id}

            crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'Inicio' if lang == 'es' else 'Home', 'item': home_url}]
            if name in projects_by_path:
                p = projects_by_path[name]
                crumbs.append({'@type': 'ListItem', 'position': 2, 'name': tr(areas[p['area']]['label']), 'item': canonical(p['area'] + '.html', lang)})
            if name != 'index.html':
                crumbs.append({'@type': 'ListItem', 'position': len(crumbs)+1, 'name': title.split(' | ')[0], 'item': url})
                breadcrumb_id = url + '#breadcrumb'
                graph.append({'@type': 'BreadcrumbList', '@id': breadcrumb_id, 'itemListElement': crumbs})
                webpage['breadcrumb'] = {'@id': breadcrumb_id}
            payload = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
            head += '  <script type="application/ld+json">' + payload + '</script>\n'
            html = html.replace('</head>', head + '</head>', 1)
            path.write_text(html, encoding='utf-8')

        # A straightforward format for recruiters, ATS tools and text-only readers.
        parser = MainText()
        parser.feed((root / ('' if lang == 'es' else 'en') / 'perfil.html').read_text(encoding='utf-8'))
        resume = 'Lucas Villalva\nlucas.a.villalva@gmail.com\n' + profile_url + '\n\n' + parser.text()
        (root / ('' if lang == 'es' else 'en') / 'perfil.txt').write_text(resume, encoding='utf-8')

    ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    xhtml = 'http://www.w3.org/1999/xhtml'
    ET.register_namespace('', ns)
    ET.register_namespace('xhtml', xhtml)
    sitemap = ET.Element(f'{{{ns}}}urlset')
    for name in sorted(names):
        for lang in ['es', 'en']:
            entry = ET.SubElement(sitemap, f'{{{ns}}}url')
            ET.SubElement(entry, f'{{{ns}}}loc').text = canonical(name, lang)
            for code in ['es', 'en']:
                ET.SubElement(entry, f'{{{xhtml}}}link', {'rel':'alternate', 'hreflang':code, 'href':canonical(name, code)})
    for name in ['skeleton-warfare.html', 'privacypolicy.html', 'account-deletion.html']:
        entry = ET.SubElement(sitemap, f'{{{ns}}}url')
        ET.SubElement(entry, f'{{{ns}}}loc').text = canonical(name)
    ET.indent(sitemap)
    ET.ElementTree(sitemap).write(root / 'sitemap.xml', encoding='utf-8', xml_declaration=True)
    (root / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nSitemap: ' + SITE + '/sitemap.xml\n', encoding='utf-8')
