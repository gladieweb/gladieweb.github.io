"""Generate the static portfolio. Run with Python 3; no dependencies required."""
from pathlib import Path
from html import escape
import json
from localization import localize_pages

ROOT = Path(__file__).resolve().parent.parent
NOTION = 'https://marvelous-blackbird-ddf.notion.site/Lucas-Villalva-Senior-Game-Developer-2187ed50e2b080508b5affe8f9f265b5'
EMAIL = 'lucas.villalva@gmail.com'
GENERATED_PAGES = []

PROJECTS = [
    dict(slug='visage-ai', area='software', title='Visage AI', category='Gestión & análisis de datos',
         summary='Inventario, ventas y datos de un comercio, reunidos en una misma herramienta.',
         context='Un sistema de gestión para pequeños y medianos comercios que combina operación diaria y análisis de información.',
         role='Desarrollé el sistema de gestión, los dashboards y las integraciones de inteligencia artificial.',
         features=['Módulos de inventario, ventas, reportes y control de stock.', 'Dashboard interactivo con métricas y análisis histórico conectado a SQL.', 'Registro de notas en lenguaje natural mediante NLP.', 'Visión por computadora con modelos preentrenados de PyTorch y optimización con ONNX Runtime.'],
         skills=['Python', 'Dash', 'Plotly', 'SQL', 'PyTorch', 'ONNX Runtime', 'OpenCV', 'Pandas', 'NumPy', 'Scikit-learn'], videos=[], links=[]),
    dict(slug='pagos-backend', area='software', title='Pagos e integraciones', category='Backend & herramientas',
         summary='Una integración de compras con MercadoPago y un backend propio para validar las operaciones.',
         context='Conectar los pagos de una aplicación con un proveedor externo y la validación del lado del servidor.',
         role='Desarrollé el plugin de compras y su integración con la API de MercadoPago a través de un backend en Node.js.',
         features=['Integración con MercadoPago.', 'Validación de compras desde el backend.', 'Comunicación entre la aplicación y el servicio.', 'Desarrollo de herramientas y extensiones reutilizables.'],
         skills=['Node.js', 'MercadoPago', 'Backend', 'Integraciones API', 'Plugins'], videos=[],
         links=[('Plugin publicado en Fab', 'https://fab.com/s/1d53ce3db697')]),
    dict(slug='herramientas-estudios', area='software', title='Herramientas para equipos', category='LemonChili Games / Tools & backend',
         summary='Herramientas, pipelines y backend para acompañar el trabajo de varios proyectos.',
         context='Equipos de arte, diseño y programación que necesitan herramientas compartidas y procesos de producción más ágiles.',
         role='Desarrollé herramientas para los proyectos del estudio y backend para su SDK. También colaboré en gameplay de tres títulos.',
         features=['Herramientas y pipelines para artistas y diseñadores.', 'Automatización con Python, Bash y scripts batch.', 'Backend para el SDK del estudio.', 'Colaboración en gameplay. Los videos muestran los títulos, no una autoría individual completa.'],
         skills=['Tools programming', 'Python', 'Bash', 'Backend', 'SDK', 'Unity3D'],
         videos=[('zMQiz6Zv-jI', 'Boop Kids — gameplay', 'Ernesto Escurra Sanz'), ('R0RjuvMz-Fs', "Floyd’s Sticker Squad — gameplay", 'TapGameplay'), ('BZCppSvD9VM', 'Tower Power — gameplay', 'LemonChili Soft')], links=[]),
    dict(slug='archviz', area='visualizacion', title='Recorrido arquitectónico', category='Arquitectura en tiempo real',
         summary='Explorar una casa en 3D, recorrerla y ver sus materiales e iluminación en tiempo real.',
         context='Una experiencia de visualización arquitectónica creada desde cero en Unreal Engine 5.',
         role='Construí el recorrido, ajusté iluminación y materiales e implementé navegación y control de cámara.',
         features=['Recorrido y navegación en tiempo real.', 'Iluminación dinámica y ajuste de materiales.', 'Control de cámara.', 'Trabajo de optimización y fidelidad visual.'],
         skills=['Unreal Engine 5', 'Archviz', 'Iluminación', 'Materiales', 'Optimización'],
         videos=[('LutnL8qGrjw', 'Archviz 02 — recorrido', 'Lucas Villalva')], links=[]),
    dict(slug='produccion-virtual', area='visualizacion', title='Producción virtual con MetaHuman', category='Cámara, actuación & entorno virtual',
         summary='Actuación y cámara física integradas en una escena virtual con iluminación cinematográfica.',
         context='Una prueba de producción virtual que reúne animación facial, MetaHuman y captura con cámara física.',
         role='Integré el seguimiento facial con LiveLink y micrófono, la cámara física y el entorno 3D. Realicé iluminación y edición con Premiere Pro.',
         features=['Animación facial en tiempo real.', 'Integración con LiveLink y MetaHuman.', 'Cámara física y entorno virtual.', 'Iluminación cinematográfica y edición.'],
         skills=['Unreal Engine', 'LiveLink', 'MetaHuman', 'Virtual production', 'Lighting', 'Premiere Pro'],
         videos=[('hHhe8Pj7_2k', 'Demostración de producción virtual', 'Hijo del Trueno')], links=[]),
    dict(slug='vfx-niagara', area='visualizacion', title='Efectos visuales con Niagara', category='VFX en tiempo real',
         summary='Un efecto de explosión creado desde cero dentro de Unreal Engine.',
         context='Una demostración de efectos visuales en tiempo real con el sistema de partículas Niagara.',
         role='Creé el efecto de explosión desde cero.',
         features=['Creación del sistema de partículas.', 'Composición visual del efecto.', 'Demostración del resultado en Unreal Engine.'],
         skills=['Unreal Engine', 'Niagara', 'VFX', 'Partículas'],
         videos=[('jSBPGL-g0nw', 'Explosion VFX Niagara', 'Lucas Villalva')], links=[]),
    dict(slug='skeleton-warfare', area='videojuegos', engine='Unity3D', title='Skeleton Warfare', category='Proyecto independiente / Mobile',
         summary='Un juego de batallas tácticas, ejércitos y mecánicas de combinación para móviles.',
         context='Un proyecto independiente de estrategia desarrollado con Unity3D y publicado en Google Play.',
         role='Desarrollé los sistemas y los distintos aspectos del juego, excepto los assets de arte.',
         features=['Sistemas de gameplay y combate.', 'Mecánica de combinación de unidades.', 'Desarrollo integral del proyecto.', 'Publicación para dispositivos móviles.'],
         skills=['Unity3D', 'C#', 'Gameplay', 'Mobile', 'Desarrollo integral'],
         videos=[('K8T9sPG7NbQ', 'Skeleton Warfare — versión de enero de 2022', 'Lucas Villalva')],
         links=[('Página del juego', '../skeleton-warfare.html'), ('Google Play', 'https://play.google.com/store/apps/details?id=com.indiesoulgames.skeletonwarfare')]),
    dict(slug='cryptoys', area='videojuegos', engine='Unity3D', title='Cryptoys', category='OnChain Studios / Unity3D',
         summary='Gameplay, SDK y flujo de interfaz para una aplicación móvil.',
         context='Trabajo como Senior Unity Developer en OnChain Studios.',
         role='Trabajé en programación de gameplay, desarrollo del SDK y flujo de UI de la aplicación móvil, además de optimización de rendimiento.',
         features=['Programación de gameplay.', 'Desarrollo de SDK.', 'Implementación del flujo de UI.', 'Optimización de rendimiento.'],
         skills=['Unity3D', 'C#', 'SDK', 'UI', 'Mobile', 'Optimización'],
         videos=[('A7ax7W8wjH0', 'Cryptoys — guía de la aplicación', 'Cryptoys')], links=[('Sitio de Cryptoys', 'https://cryptoys.com/')]),
    dict(slug='games-station', area='videojuegos', engine='Unity3D', title='Gameplay & LiveOps', category='Games Station Studio / Unity3D',
         summary='Nuevas funcionalidades y soporte continuo para títulos móviles.',
         context='Trabajo como Senior Unity3D Developer en Games Station.',
         role='Desarrollé nuevas funcionalidades, trabajé en LiveOps, corregí errores y optimicé el rendimiento. Los videos muestran los títulos del estudio.',
         features=['Desarrollo de funcionalidades de gameplay.', 'LiveOps y soporte de títulos publicados.', 'Corrección de errores.', 'Optimización de rendimiento.'],
         skills=['Unity3D', 'C#', 'Gameplay', 'LiveOps', 'Mobile', 'Optimización'],
         videos=[('q9syOUlt24k', 'Game of Warriors — gameplay', 'Dragon Maniac'), ('kpl2-NypKVQ', 'Grow Empire: Rome — gameplay', 'Tapsuperstar')], links=[]),
    dict(slug='netherak', area='videojuegos', engine='Unreal Engine', title='Netherak Demons', category='Netherak Entertainment / Unreal Engine',
         summary='Sistemas de interfaz para un RPG de horror y fantasía oscura.',
         context='Trabajo como Senior Unreal Engine Engineer en un RPG multijugador.',
         role='Desarrollé elementos de UI, widgets UMG, materiales interactivos y shaders, en colaboración con diseño y programación.',
         features=['Sistemas de interfaz y widgets UMG.', 'Materiales interactivos y shaders para la UI.', 'Integración con el resto de los sistemas del juego.'],
         skills=['Unreal Engine', 'UMG', 'UI', 'Materiales', 'Shaders', 'Multiplayer'],
         videos=[('YnCaIw7X_DE', 'Netherak Demons — teaser del juego', 'Juice Gaming News')], links=[('Ver en Epic Games Store', 'https://store.epicgames.com/es-ES/p/netherak-demons-a419cf')]),
    dict(slug='endless-runner', area='videojuegos', engine='Unreal Engine', title='Endless Runner Tools', category='Plugin publicado / C++',
         summary='Un sistema de endless runner con generación procedural de obstáculos.',
         context='Una herramienta reutilizable para Unreal Engine, publicada en Fab.',
         role='Desarrollé el sistema completo en C++, incluida la generación procedural de obstáculos.',
         features=['Sistema de endless runner.', 'Generación procedural de obstáculos.', 'Implementación como plugin reutilizable.'],
         skills=['Unreal Engine', 'C++', 'Plugins', 'Generación procedural'],
         videos=[('CU27-d8zarc', 'Endless Runner Tools — demostración del plugin', 'Lucas Villalva')], links=[('Ver plugin en Fab', 'https://fab.com/s/27062eb363fc')]),
    dict(slug='fps-ia', area='videojuegos', engine='Unreal Engine', title='FPS & patrullaje con IA', category='Gameplay / Blueprints',
         summary='Enemigos que patrullan, detectan al jugador, lo persiguen y retoman su recorrido.',
         context='Un proyecto de mecánicas en primera persona e inteligencia artificial para enemigos.',
         role='Implementé el gameplay del FPS y el sistema de comportamiento de los enemigos con Blueprints.',
         features=['Mecánicas de juego en primera persona.', 'Patrullaje y detección del jugador.', 'Persecución y retorno al estado de patrulla.'],
         skills=['Unreal Engine', 'Blueprints', 'Gameplay', 'IA'],
         videos=[('Acal2Dv7dfQ', 'FPS Mechanics — demostración', 'Lucas Villalva')], links=[('Código en GitHub', 'https://github.com/gladieweb/UnrealEngine_FPS-Blueprints-')]),
    dict(slug='supervivencia', area='videojuegos', engine='Unreal Engine', title='Sistemas de supervivencia', category='Multiplayer / C++',
         summary='Recolección, inventario y atributos del jugador en un entorno multijugador.',
         context='Un proyecto de sistemas modulares para un juego de supervivencia.',
         role='Desarrollé sistemas de recolección, inventario, atributos y multijugador.',
         features=['Recolección modular de recursos.', 'Inventario y atributos del jugador.', 'Sistemas multijugador en Unreal C++.'],
         skills=['Unreal Engine', 'C++', 'Multiplayer', 'Inventario', 'Sistemas modulares'],
         videos=[('ngBgNhtXkNk', 'Multiplayer Survival — sistema de recolección, enero de 2023', 'Lucas Villalva')], links=[]),
]

AREAS = {
    'software': dict(title='Software para tu negocio.', label='Software & automatización',
        intro='Si necesitás ordenar información, conectar servicios o simplificar una tarea, podemos empezar por ahí.',
        offers=[('Organizar tu operación', 'Aplicaciones de gestión, inventario, ventas y dashboards para consultar la información que importa.'), ('Conectar tus herramientas', 'Integraciones de APIs, pagos y backend para que los sistemas puedan trabajar juntos.'), ('Reducir trabajo manual', 'Herramientas internas, automatización y soluciones de IA aplicadas a una necesidad concreta.')],
        experience='En LemonChili Games desarrollé herramientas y backend compartidos entre proyectos. Como independiente, construí Visage AI e integraciones de pagos con Node.js y MercadoPago.',
        skills=['Python', 'Node.js', 'SQL', 'Dash / Plotly', 'APIs', 'ONNX / PyTorch', 'OpenCV', 'Automatización']),
    'visualizacion': dict(title='Tu idea, en un espacio que se puede explorar.', label='Visualización & experiencias 3D',
        intro='Para presentar un espacio, producir una escena o darle forma a una experiencia visual en tiempo real.',
        offers=[('Mostrar un espacio', 'Recorridos arquitectónicos con navegación, iluminación y materiales en tiempo real.'), ('Producir una escena', 'Integración de actuación, MetaHumans, cámara física y escenarios virtuales.'), ('Crear una experiencia visual', 'Efectos con Niagara, materiales e iluminación dentro de Unreal Engine.')],
        experience='Trabajo con Unreal Engine en visualización arquitectónica y producción virtual: LiveLink, MetaHumans, integración de cámara, iluminación y materiales.',
        skills=['Unreal Engine 5', 'Archviz', 'LiveLink', 'MetaHuman', 'Niagara', 'Lighting / LookDev', 'Materiales', 'Premiere Pro']),
    'videojuegos': dict(title='Llevemos tu juego al siguiente paso.', label='Desarrollo de videojuegos',
        intro='Para construir un prototipo, sumar sistemas a un proyecto o reforzar un equipo de desarrollo.',
        offers=[('Construir gameplay', 'Mecánicas, comportamiento de enemigos, inventarios y sistemas multijugador.'), ('Integrar y optimizar', 'UI, SDK, compras, backend y rendimiento para proyectos móviles, web y de escritorio.'), ('Sumar experiencia a tu equipo', 'Colaboración técnica, herramientas para producción y soporte de títulos publicados.')],
        experience='Más de 13 años con Unity3D y más de 4 con Unreal Engine. Experiencia en OnChain Studios, Games Station, Netherak, Segritude, Cominted Labs, TECLA, LemonChili y QB9.',
        skills=['Unity3D', 'C#', 'Unreal Engine', 'C++', 'Blueprints', 'Gameplay', 'UI / UMG', 'Multiplayer', 'LiveOps', 'Optimización']),
}

def link(label, url, cls='text-link'):
    external = ' target="_blank" rel="noopener noreferrer"' if url.startswith('https:') else ''
    return f'<a class="{cls}" href="{escape(url, quote=True)}"{external}>{escape(label)} <span aria-hidden="true">↗</span></a>'

def tags(items):
    return '<ul class="tags" aria-label="Tecnologías y habilidades">' + ''.join(f'<li>{escape(i)}</li>' for i in items) + '</ul>'

def page(title, desc, body, depth=0, active='', home=False):
    prefix = '../' * depth
    # Keep words separated when a responsive breakpoint hides a line break.
    body = body.replace('<br>', '<br> ')
    nav = ''.join(f'<a href="{prefix}{url}"' + (' aria-current="page"' if key == active else '') + f'>{label}</a>' for key,url,label in [('servicios','index.html#caminos','Qué necesitás'),('perfil','perfil.html','Perfil / CV'),('contacto','contacto.html','Conversemos')])
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} — Lucas Villalva</title>
  <meta name="description" content="{escape(desc, quote=True)}">
  <meta property="og:title" content="{escape(title, quote=True)} — Lucas Villalva">
  <meta property="og:description" content="{escape(desc, quote=True)}">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#f4f3ed">
  <link rel="stylesheet" href="{prefix}portfolio.css?v=2">
</head>
<body{' class="home"' if home else ''}>
  <a class="skip" href="#contenido">Saltar al contenido</a>
  <header class="site-header wrap">
    <a class="identity" href="{prefix}index.html" aria-label="Lucas Villalva, inicio"><span class="monogram" aria-hidden="true">lv<span>·</span></span><span>Lucas Villalva<small>Desarrollo &amp; experiencias digitales</small></span></a>
    <div class="header-tools"><nav aria-label="Principal">{nav}</nav><!--language-switch--></div>
  </header>
  <main id="contenido">{body}</main>
  <footer class="site-footer"><div class="wrap footer-row"><span>© <span id="year">2026</span> Lucas Villalva <span class="footer-brand">/ gladieweb</span></span><nav class="legal" aria-label="Skeleton Warfare: información legal"><span>Skeleton Warfare</span><a href="{prefix}skeleton-warfare.html">Juego</a><a href="{prefix}privacypolicy.html">Privacy Policy</a><a href="{prefix}account-deletion.html">Account deletion</a></nav></div></footer>
  <script src="{prefix}script.js?v=3"></script>
</body>
</html>
'''

def write(name, content):
    target = ROOT / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding='utf-8')
    if name.endswith('.html'):
        GENERATED_PAGES.append(name)

def breadcrumb(label, depth=0):
    return f'<nav class="breadcrumb" aria-label="Ruta de navegación"><a href="{"../" * depth}index.html">Inicio</a><span aria-hidden="true">/</span><span>{escape(label)}</span></nav>'

def cta(area='', prefix=''):
    url = prefix + 'contacto.html' + (f'?tema={area}' if area else '')
    return f'<section class="closing wrap"><div><p class="eyebrow">El siguiente paso</p><h2>Contame qué necesitás resolver.</h2><p>Podés venir con una idea, un proyecto en marcha o una pregunta.</p></div>{link("Conversemos", url, "button")}</section>'

def card(p, prefix=''):
    visual = f'<img src="https://i.ytimg.com/vi/{p["videos"][0][0]}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">' if p['videos'] else '<div class="abstract-art" aria-hidden="true"><span></span><span></span><span></span><b>↗</b></div>'
    return f'<article class="project-card"><a class="project-preview" href="{prefix}proyectos/{p["slug"]}.html" aria-label="Ver proyecto: {escape(p["title"], quote=True)}">{visual}<span class="preview-label">{"Ver proyecto + video" if p["videos"] else "Explorar proyecto"} ↗</span></a><div class="card-copy"><p class="eyebrow">{escape(p["category"])}</p><h3><a href="{prefix}proyectos/{p["slug"]}.html">{escape(p["title"])}</a></h3><p>{escape(p["summary"])}</p></div></article>'

home = '''
  <section class="welcome wrap">
    <p class="eyebrow">Un buen proyecto empieza por una necesidad.</p>
    <h1>¿Qué <em>necesitás?</em></h1>
    <p class="welcome-intro">Elegí por dónde empezar. Te muestro cómo puedo ayudarte.</p>
    <div class="route-grid" id="caminos">
      <a class="route route-software" href="software.html"><span class="route-icon" aria-hidden="true">⌘</span><h2>Resolver algo<br>con software</h2><p>Una aplicación, una integración<br>o menos tareas manuales.</p><span class="route-bottom">Software &amp; automatización <b aria-hidden="true">↗</b></span></a>
      <a class="route route-visual" href="visualizacion.html"><span class="route-icon" aria-hidden="true">◇</span><h2>Visualizar un espacio<br>o una idea</h2><p>Recorridos 3D, escenas<br>y producción virtual.</p><span class="route-bottom">Visualización &amp; experiencias 3D <b aria-hidden="true">↗</b></span></a>
      <a class="route route-games" href="videojuegos.html"><span class="route-icon" aria-hidden="true">＋</span><h2>Desarrollar<br>un videojuego</h2><p>De una mecánica a un proyecto.<br>O un refuerzo para tu equipo.</p><span class="route-bottom">Unity3D &amp; Unreal Engine <b aria-hidden="true">↗</b></span></a>
    </div>
    <div class="welcome-note"><p>¿Todavía no sabés por dónde empezar?</p><a class="text-link" href="contacto.html">Contame tu idea <span aria-hidden="true">↗</span></a></div>
  </section>'''
write('index.html', page('¿Qué necesitás?', 'Software, automatización, visualización 3D o videojuegos. Elegí qué necesitás resolver y explorá proyectos y experiencia de Lucas Villalva.', home, home=True))

for area, data in AREAS.items():
    offers = ''.join(f'<article><span class="step">0{i+1}</span><h3>{escape(t)}</h3><p>{escape(d)}</p></article>' for i,(t,d) in enumerate(data['offers']))
    projects = [p for p in PROJECTS if p['area']==area]
    groups = ''
    if area == 'videojuegos':
        for engine in ['Unity3D', 'Unreal Engine']:
            groups += f'<section class="project-group" id="{"unity" if engine == "Unity3D" else "unreal"}"><h3 class="group-title">{engine}</h3><div class="project-grid">' + ''.join(card(p) for p in projects if p['engine']==engine) + '</div></section>'
        groups += '<p class="related-note">También desarrollé herramientas y backend para LemonChili Games. <a href="proyectos/herramientas-estudios.html">Explorar ese trabajo ↗</a></p>'
    else:
        groups = '<div class="project-grid">' + ''.join(card(p) for p in projects) + '</div>'
    jump = '<nav class="section-nav" aria-label="En esta página"><a href="#servicios">Cómo puedo ayudarte</a><a href="#proyectos">Proyectos</a><a href="#experiencia">Experiencia &amp; habilidades</a></nav>'
    if area == 'videojuegos':
        jump += '<div class="engine-nav"><span>Explorar por motor:</span><a href="#unity">Unity3D ↓</a><a href="#unreal">Unreal Engine ↓</a></div>'
    body = f'<div class="wrap">{breadcrumb(data["label"])}</div><section class="page-intro wrap"><p class="eyebrow">{data["label"]}</p><h1>{data["title"]}</h1><p class="lede">{data["intro"]}</p>{jump}</section><section class="section wrap" id="servicios"><div class="section-heading"><p class="eyebrow">Según lo que necesitás</p><h2>Cómo puedo ayudarte</h2></div><div class="offer-grid">{offers}</div></section><section class="section wrap" id="proyectos"><div class="section-heading"><p class="eyebrow">Trabajo en contexto</p><h2>Explorá los proyectos</h2><p>Abrí cada proyecto para conocer mi participación, las tecnologías y las demostraciones disponibles.</p></div>{groups}</section><section class="section wrap experience-panel" id="experiencia"><div><p class="eyebrow">Experiencia aplicada</p><h2>Detrás de cada proyecto.</h2><p>{data["experience"]}</p>{link("Conocer mi trayectoria", "perfil.html")}</div><div><h3>Herramientas &amp; habilidades</h3>{tags(data["skills"])}</div></section>{cta(area)}'
    write(area+'.html', page(data['label'], data['intro'], body, active='servicios'))

for p in PROJECTS:
    area = p['area']
    videos = ''
    for vid, title, author in p['videos']:
        videos += f'<figure class="video-block"><div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0" title="{escape(title, quote=True)}" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div><figcaption><span>{escape(title)}<small>Video: {escape(author)}</small></span>{link("Abrir en YouTube", "https://www.youtube.com/watch?v="+vid)}</figcaption></figure>'
    if videos:
        videos = '<section class="section wrap narrow"><div class="section-heading"><p class="eyebrow">El proyecto en acción</p><h2>Videos &amp; demostraciones</h2></div>' + videos + '</section>'
    details = '<ul class="feature-list">' + ''.join(f'<li>{escape(x)}</li>' for x in p['features']) + '</ul>'
    links = '<div class="resource-links">' + ''.join(link(t,u,'button secondary') for t,u in p['links']) + '</div>' if p['links'] else ''
    body = f'<div class="wrap"><nav class="breadcrumb" aria-label="Ruta de navegación"><a href="../index.html">Inicio</a><span>/</span><a href="../{area}.html">{AREAS[area]["label"]}</a><span>/</span><span>{escape(p["title"])}</span></nav></div><section class="page-intro wrap narrow"><p class="eyebrow">{escape(p["category"])}</p><h1>{escape(p["title"])}</h1><p class="lede">{escape(p["summary"])}</p>{links}</section><section class="section wrap narrow project-story"><div><p class="eyebrow">El contexto</p><h2>Qué se necesitaba</h2><p>{escape(p["context"])}</p></div><div><p class="eyebrow">Mi participación</p><h2>Qué desarrollé</h2><p>{escape(p["role"])}</p>{details}</div></section>{videos}<section class="section wrap narrow"><p class="eyebrow">Con qué trabajé</p><h2>Tecnologías &amp; habilidades</h2>{tags(p["skills"])}</section><div class="wrap narrow project-return">{link("Volver a "+AREAS[area]["label"], "../"+area+".html#proyectos")}</div>{cta(area, "../")}'
    write('proyectos/'+p['slug']+'.html', page(p['title'],p['summary'],body,depth=1))

jobs = [
    ('2013 — Actualidad', 'Indie Soul Games', 'Independent Game Developer · Freelance', 'Desarrollo integral, LiveOps, consultoría en Unreal y producción virtual. Herramientas, gestión de stock y soluciones de IA.'),
    ('Ago — Nov 2025', 'Netherak Entertainment', 'Senior Unreal Engine Engineer', 'Sistemas UI, widgets UMG, materiales interactivos y shaders para un RPG multijugador.'),
    ('May — Ago 2025', 'Segritude Games', 'Senior Unreal Engine Developer', 'Implementación y depuración de multiplayer e IA en C++ para Lunaris.'),
    ('Ago 2024 — May 2025', 'Cominted Labs', 'Technical Lead Developer', 'Proyectos Unity3D para WebGL y móviles, coordinación con clientes y equipos, investigación y optimización.'),
    ('Ago 2023 — Jul 2024', 'TECLA', 'Senior Unity3D Developer', 'Aplicación móvil, C#, integración con GraphQL, UI Toolkit y visual scripting.'),
    ('Ago 2020 — Sep 2022', 'Games Station', 'Senior Unity3D Developer', 'Gameplay, nuevas funcionalidades y optimización de rendimiento.'),
    ('Oct 2019 — Sep 2020', 'LemonChili Games', 'Senior Tools Programmer', 'Herramientas y pipelines para arte y diseño. Automatización con Python, Bash y scripts batch.'),
    ('May 2014 — Ene 2019', 'QB9 Entertainment', 'Unity3D Game Developer', 'Desarrollo de funcionalidades y contenido para juegos móviles y web.'),
    ('Sep — Oct 2014', 'Image Campus', 'Instructor de IA en videojuegos', 'Curso intensivo de pathfinding, toma de decisiones y comportamientos procedurales.'),
    ('Ene — Mar 2014', 'Zupcat', 'Junior Game Developer', 'Desarrollo de mecánicas y niveles para juegos móviles con Unity3D.'),
]
timeline = ''.join(f'<article><span>{date}</span><div><h3>{company}</h3><p class="job-role">{role}</p><p>{desc}</p></div></article>' for date,company,role,desc in jobs)
profile = f'''<div class="wrap">{breadcrumb('Perfil / CV')}</div><section class="page-intro wrap"><p class="eyebrow">Perfil / CV</p><h1>Lucas Villalva</h1><p class="lede">Desarrollo software y experiencias interactivas. Mi trayectoria conecta programación, herramientas de producción y tecnología en tiempo real.</p><div class="profile-meta"><span>Buenos Aires, Argentina</span><span>Trabajo remoto · Freelance · Contratos</span></div><div class="resource-links">{link('GitHub', 'https://github.com/gladieweb', 'button secondary')}{link('Plugins en Fab', 'https://fab.com/sellers/Lucas%20Villalva', 'button secondary')}{link('CV original en Notion', NOTION, 'button secondary')}</div></section><section class="section wrap experience-panel"><div><p class="eyebrow">Sobre mi trabajo</p><h2>De los sistemas a la experiencia.</h2><p>Más de 13 años de experiencia en Unity3D y más de 4 con Unreal Engine. Me especializo en sistemas técnicos, gameplay, interfaces, plugins, integración de backend y herramientas para equipos.</p><p>También desarrollo soluciones en Python, integraciones con Node.js, análisis de datos e IA aplicada, además de visualización arquitectónica y producción virtual.</p></div><div><h3>Habilidades</h3>{tags(['C#', 'C++', 'Blueprints', 'Python', 'Node.js', 'Unity3D', 'Unreal Engine', 'SQL', 'GraphQL', 'Git', 'Scrum / Agile', 'OOD / UML', 'Patrones de diseño', 'Optimización', 'Shaders / materiales'])}</div></section><section class="section wrap"><div class="section-heading"><p class="eyebrow">Trayectoria</p><h2>Experiencia profesional</h2></div><div class="timeline">{timeline}</div></section><section class="section wrap offer-grid"><article><p class="eyebrow">Formación</p><h3>Image Campus</h3><p>Técnico Superior en Desarrollo de Videojuegos (2009–2012).</p><h3>UADE</h3><p>Estudios en desarrollo de videojuegos (2022).</p></article><article><p class="eyebrow">Certificaciones</p><h3>Unreal Engine</h3><p>Unreal Engine 5 Blueprints — First Person Shooter (FPS).</p><p>Unreal Engine C++ Multiplayer Master.</p></article><article><p class="eyebrow">Idiomas</p><h3>Español &amp; inglés</h3><p>Español nativo.<br>Inglés intermedio / avanzado.</p></article></section>{cta()}'''
write('perfil.html', page('Perfil & CV', 'Experiencia profesional, formación y habilidades de Lucas Villalva. Software, herramientas y experiencias interactivas.',profile,active='perfil'))

contact = f'''<div class="wrap">{breadcrumb('Contacto')}</div><section class="page-intro wrap contact-intro"><p class="eyebrow">Empecemos por una conversación</p><h1>¿Qué tenés<br>en mente?</h1><p class="lede">Contame qué querés lograr y en qué punto estás. No hace falta tener una especificación técnica para empezar.</p><div class="contact-box"><span class="eyebrow">Escribime directamente</span><a class="contact-email" href="mailto:{EMAIL}">{EMAIL} <span aria-hidden="true">↗</span></a><p>Buenos Aires, Argentina · Colaboraciones remotas</p></div></section><section class="section wrap contact-details"><div><h2>Para arrancar, alcanza con esto.</h2><ol class="contact-prompts"><li>¿Qué necesitás resolver o construir?</li><li>¿Ya hay algo en marcha o empezamos desde cero?</li><li>¿Tenés algún plazo o alcance en mente?</li></ol></div><aside><p class="eyebrow">¿Estás armando un equipo?</p><p>También estoy disponible para propuestas freelance, contratos y posiciones remotas.</p>{link('Ver experiencia y CV', 'perfil.html')}<hr><p class="eyebrow">Soporte de Skeleton Warfare</p><p>Para privacidad o eliminación de datos del juego, usá las páginas específicas.</p>{link('Account deletion', 'account-deletion.html')}{link('Privacy Policy', 'privacypolicy.html')}</aside></section>'''
write('contacto.html', page('Conversemos', 'Contame qué necesitás resolver: desarrollo de software, visualización 3D, videojuegos o una colaboración profesional.',contact,active='contacto'))

# Keep a small, auditable record of the original media, without signed or expiring URLs.
write('content/media-sources.json', json.dumps({'source':NOTION,'projects':[{k:p[k] for k in ['slug','videos','links']} for p in PROJECTS]},ensure_ascii=False,indent=2)+'\n')
localize_pages(ROOT, GENERATED_PAGES)
print(f'Generated {len(GENERATED_PAGES)} pages in Spanish and English.')
