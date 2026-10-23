"""Client-facing capabilities and case studies based on Lucas's stated experience."""
from html import escape
from portfolio_updates import t

EXTRA_PROJECTS = [
    dict(slug='valoracion-acciones-python', area='software',
         title=t('Valoración de acciones con Python', 'Stock valuation with Python'),
         category=t('Software financiero / Script Python implementado', 'Financial software / Implemented Python script'),
         summary=t('Consulta de acciones por ticker, estimación del valor intrínseco y porcentaje de infravaloración o sobrevaloración frente al precio de mercado.', 'Stock lookup by ticker, intrinsic value estimation, and the percentage of undervaluation or overvaluation relative to market price.'),
         context=t('Automatizar una parte del análisis de value investing mediante un componente que pueda integrarse en una web.', 'Automating part of value investing research through a component that can be integrated into a website.'),
         role=t('Desarrollé un script Python que recibe un ticker, como AAPL, o una lista de tickers. Consulta información mediante APIs como Yahoo Finance, estima el valor intrínseco, obtiene el precio de mercado y muestra el porcentaje de infravaloración o sobrevaloración.', 'I developed a Python script that accepts one ticker, such as AAPL, or a list of tickers. It retrieves information through APIs such as Yahoo Finance, estimates intrinsic value, fetches the market price, and shows the percentage of undervaluation or overvaluation.'),
         features=[t('Entrada de uno o varios tickers de acciones.', 'Input of one or multiple stock tickers.'), t('Obtención de información y precios mediante APIs como Yahoo Finance.', 'Retrieval of information and prices through APIs such as Yahoo Finance.'), t('Cálculo de valor intrínseco estimado y comparación porcentual con la cotización.', 'Estimated intrinsic value calculation and percentage comparison with the quoted price.'), t('Estado: script Python implementado, pensado como componente de un microservicio. La web todavía no está desarrollada.', 'Status: implemented Python script, intended as a microservice component. The website has not yet been developed.')],
         skills=['Python', t('APIs de datos financieros', 'Financial data APIs'), t('Yahoo Finance', 'Yahoo Finance'), t('Valoración de acciones', 'Stock valuation'), t('Value investing', 'Value investing')], videos=[], links=[]),
    dict(slug='auto-landscape-material', area='visualizacion',
         title=t('Auto Landscape Material', 'Auto Landscape Material'),
         category=t('Unreal Engine / Materiales para terrenos', 'Unreal Engine / Landscape materials'),
         summary=t('Un material propio para automatizar el tratamiento visual de paisajes en Unreal Engine.', 'A custom material for automating the visual treatment of landscapes in Unreal Engine.'),
         context=t('Trabajo de materiales aplicado a paisajes dentro de Unreal Engine.', 'Material development applied to landscapes in Unreal Engine.'),
         role=t('Desarrollé un Auto Landscape Material como parte de mi trabajo con materiales e iluminación en Unreal Engine.', 'I developed an Auto Landscape Material as part of my work with materials and lighting in Unreal Engine.'),
         features=[t('Desarrollo de un material propio para paisajes.', 'Development of a custom landscape material.'), t('Automatización del tratamiento visual del terreno mediante materiales.', 'Automation of terrain appearance through materials.')],
         skills=['Unreal Engine', t('Materiales', 'Materials'), t('Landscape', 'Landscape')], videos=[], links=[]),
]

def group(title, value, skills):
    return dict(title=title, value=value, skills=skills)

ARCHITECTURE = group(
    t('Arquitectura & diseño de software', 'Software architecture & design'),
    t('Sistemas que se pueden extender, mantener y adaptar a las reglas del proyecto.', 'Systems that can be extended, maintained, and adapted to the project’s rules.'),
    [t('Programación orientada a objetos (OOP)', 'Object-oriented programming (OOP)'), t('Arquitectura orientada a componentes', 'Component-based architecture'), t('Data-driven development', 'Data-driven development'), t('Principios SOLID', 'SOLID principles'), t('Design Patterns', 'Design Patterns')])
GRAPHICS_SOFTWARE = group(
    t('Software, gráficos & contexto para IA', 'Software, graphics & context for AI'),
    t('Desarrollo de aplicaciones, librerías compartidas e integraciones que conectan asistentes con el código del producto.', 'Applications, shared libraries, and integrations that connect assistants to product code.'),
    ['TypeScript', 'Python', t('JavaScript / Node.js', 'JavaScript / Node.js'), 'SQL', 'GraphQL', t('Programación gráfica', 'Graphics programming'), 'MCP servers', 'Copilot', 'AI Skills'])
UNITY = group(
    t('Unity / C# & herramientas de producción', 'Unity / C# & production tools'),
    t('Gameplay, interfaces y herramientas para que el equipo pueda iterar sobre un proyecto.', 'Gameplay, interfaces, and tools that help a team iterate on a project.'),
    ['Unity3D', 'C#', t('ScriptableObjects', 'ScriptableObjects'), t('Editor tools', 'Editor tools'), 'SDK', t('UI Toolkit', 'UI Toolkit'), 'Gameplay', t('Data-driven development', 'Data-driven development')])
UNREAL = group(
    t('Unreal / gameplay, animación & multiplayer', 'Unreal / gameplay, animation & multiplayer'),
    t('Sistemas de juego, habilidades, animación y sincronización para experiencias interactivas.', 'Gameplay, abilities, animation, and synchronization systems for interactive experiences.'),
    ['Unreal Engine', 'C++', 'Blueprints', t('Gameplay Ability System (GAS)', 'Gameplay Ability System (GAS)'), t('Animation Blueprints', 'Animation Blueprints'), t('Replication', 'Replication'), 'Multiplayer', t('UI / UMG', 'UI / UMG')])
VISUAL = group(
    t('Materiales, iluminación & producción en tiempo real', 'Materials, lighting & real-time production'),
    t('Presentación visual de espacios, personajes y escenas, con interacción 2D y 3D.', 'Visual presentation of spaces, characters, and scenes, with 2D and 3D interaction.'),
    [t('Lighting', 'Lighting'), t('Materials', 'Materials'), 'Shaders', t('Auto Landscape Material', 'Auto Landscape Material'), 'Niagara', 'LiveLink', 'MetaHuman', 'Archviz', t('Livestreaming', 'Livestreaming')])
MOBILE = group(
    t('Integraciones, monetización & analítica', 'Integrations, monetization & analytics'),
    t('Conectar los servicios que acompañan la operación y el seguimiento de una aplicación o un juego.', 'Connecting the services that support application or game operations and measurement.'),
    [t('Firebase', 'Firebase'), t('In-app purchases (IAP)', 'In-app purchases (IAP)'), t('AppsFlyer', 'AppsFlyer'), t('Ads SDKs', 'Ads SDKs'), t('Analytics', 'Analytics'), 'LiveOps', t('Integraciones API', 'API integrations')])
PERFORMANCE = group(
    t('Rendimiento & entornos de desarrollo móvil', 'Performance & mobile development environments'),
    t('Diagnóstico de rendimiento y trabajo con las herramientas del ciclo de desarrollo móvil.', 'Performance diagnosis and work with the tools used throughout mobile development.'),
    [t('Profiling', 'Profiling'), t('Optimización', 'Optimization'), t('Xcode', 'Xcode'), t('Android Studio', 'Android Studio'), 'Git'])

ALGORITHMS = group(
    t('Algoritmos & resolución de problemas', 'Algorithms & problem solving'),
    t('Fundamentos para resolver problemas de búsqueda, selección y optimización según las necesidades del sistema.', 'Foundations for solving search, selection, and optimization problems according to the system’s needs.'),
    [t('Búsqueda binaria', 'Binary search'), t('Problema de la mochila (Knapsack)', 'Knapsack problem'), t('Algoritmos genéticos + redes neuronales', 'Genetic algorithms + neural networks')])
GAME_AI = group(
    t('IA de gameplay, decisiones & movimiento', 'Gameplay AI, decision-making & movement'),
    t('Experiencia con técnicas de navegación, toma de decisiones y comportamiento de agentes, también como docente de IA para videojuegos.', 'Experience with navigation, decision-making, and agent behavior techniques, including teaching game AI.'),
    [t('Pathfinding A*', 'A* pathfinding'), t('Máquinas de estados finitos (FSM)', 'Finite State Machines (FSM)'), t('Behavior Trees', 'Behavior Trees'), t('Flocking', 'Flocking'), t('Steering Behaviors', 'Steering Behaviors')])
ENGINE_FOUNDATIONS = group(
    t('Fundamentos de motores & rendering', 'Engine & rendering foundations'),
    t('Desarrollé un motor propio con fixed-function pipeline como proyecto histórico. Esa experiencia forma parte de mis fundamentos de motores y gráficos; mi trabajo actual está descrito en los proyectos de software, Unity y Unreal.', 'I developed a custom engine using a fixed-function pipeline as a historical project. That experience is part of my engine and graphics foundations; my current work is described in the software, Unity, and Unreal projects.'),
    [t('Motor propio / Proyecto histórico', 'Custom engine / Historical project'), t('Fixed-function pipeline / Histórico', 'Fixed-function pipeline / Historical'), t('Fundamentos de rendering', 'Rendering foundations')])

MATH_PHYSICS = group(
    t('Matemáticas 3D, álgebra & física de videojuegos', '3D math, linear algebra & game physics'),
    t('Sólidos fundamentos matemáticos y físicos para razonar sobre movimiento, relaciones espaciales y sistemas de gameplay y gráficos.', 'Strong mathematical and physics foundations for reasoning about motion, spatial relationships, and gameplay and graphics systems.'),
    [t('Matemáticas 3D (3D math)', '3D math'), t('Álgebra lineal (Linear algebra)', 'Linear algebra'), t('Física para videojuegos', 'Game physics')])
SHADER_PROGRAMMING = group(
    t('Programación de shaders & optimización visual', 'Shader programming & visual optimization'),
    t('Experiencia escribiendo vertex y fragment shaders en Cg para Unity. Evaluación del coste matemático, la precisión necesaria y el resultado visual al plantear simplificaciones y aproximaciones en shaders.', 'Experience writing vertex and fragment shaders in Cg for Unity. Evaluating mathematical cost, required precision, and visual results when considering shader simplifications and approximations.'),
    [t('Programación manual de shaders', 'Handwritten shader programming'), t('Vertex shaders', 'Vertex shaders'), t('Fragment shaders', 'Fragment shaders'), t('Cg (Unity)', 'Cg (Unity)'), t('Optimización de shaders', 'Shader optimization'), t('Precisión numérica & calidad visual', 'Numerical precision & visual quality')])

CAPABILITIES = {
    'software': [GRAPHICS_SOFTWARE, ARCHITECTURE, MATH_PHYSICS, SHADER_PROGRAMMING, ALGORITHMS, MOBILE],
    'visualizacion': [VISUAL, SHADER_PROGRAMMING, MATH_PHYSICS, GRAPHICS_SOFTWARE, ENGINE_FOUNDATIONS, PERFORMANCE],
    'videojuegos': [UNITY, UNREAL, GAME_AI, MATH_PHYSICS, SHADER_PROGRAMMING, ARCHITECTURE, ALGORITHMS, ENGINE_FOUNDATIONS, MOBILE, PERFORMANCE],
    'perfil': [GRAPHICS_SOFTWARE, MATH_PHYSICS, SHADER_PROGRAMMING, ARCHITECTURE, ALGORITHMS, UNITY, UNREAL, GAME_AI, VISUAL, ENGINE_FOUNDATIONS, MOBILE, PERFORMANCE],
}

def teaching_section():
    return f'<section class="section wrap experience-panel" id="docencia"><div><p class="eyebrow">{t("Docencia / IA para videojuegos", "Teaching / Game AI")}</p><h2>{t("Fundamentos que también enseñé.", "Foundations I have also taught.")}</h2><p>{t("Fui profesor de técnicas de inteligencia artificial para videojuegos. Los temas incluyeron máquinas de estados finitos (FSM), árboles de comportamiento, algoritmos genéticos, redes neuronales, pathfinding, flocking y steering behaviors.", "I taught artificial intelligence techniques for games. Topics included finite state machines (FSM), behavior trees, genetic algorithms, neural networks, pathfinding, flocking, and steering behaviors.")}</p></div><div><h3>{t("Una base para trabajar con equipos", "A foundation for working with teams")}</h3><p>{t("Esta experiencia docente complementa mi trabajo de programación y mis conocimientos de algoritmos y comportamiento de agentes.", "This teaching experience complements my programming work and my knowledge of algorithms and agent behavior.")}</p></div></section>'

def capability_section(area):
    heading = t('La profundidad técnica, cuando la necesitás.', 'Technical depth, when you need it.')
    intro = t('Mi experiencia cubre distintas etapas del desarrollo. Explorá las capacidades relevantes para tu equipo o proyecto.', 'My experience spans different stages of development. Explore the capabilities relevant to your team or project.')
    items = ''
    for g in CAPABILITIES[area]:
        pills = ''.join(f'<li>{escape(s)}</li>' for s in g['skills'])
        items += f'<details class="capability"><summary><strong>{g["title"]}</strong><span aria-hidden="true">+</span></summary><div class="capability-body"><p>{g["value"]}</p><ul class="tags">{pills}</ul></div></details>'
    return f'<section class="section wrap" id="capacidades"><div class="section-heading"><p class="eyebrow">{t("Capacidades / Para clientes & equipos técnicos", "Capabilities / For clients & technical teams")}</p><h2>{heading}</h2><p>{intro}</p></div><div class="capability-grid">{items}</div></section>'

def hiring_section():
    roles = [
        (t('Software & Graphics Developer', 'Software & Graphics Developer'),
         t('TypeScript, Python, librerías gráficas e integración de asistentes mediante MCP y Skills. Experiencia actual en SciSoft y aplicaciones propias, con base en matemáticas 3D y álgebra lineal.', 'TypeScript, Python, graphics libraries, and assistant integration through MCP and Skills. Current experience at SciSoft and independently developed applications, grounded in 3D math and linear algebra.'), 'software.html'),
        (t('Senior Unity & Unreal Developer', 'Senior Unity & Unreal Developer'),
         t('Más de 13 años con Unity3D y más de 4 con Unreal Engine. Gameplay, física de videojuegos, arquitectura, herramientas, UI, multiplayer e integraciones móviles.', 'Over 13 years with Unity3D and more than 4 with Unreal Engine. Gameplay, game physics, architecture, tools, UI, multiplayer, and mobile integrations.'), 'videojuegos.html'),
        (t('Real-time 3D Developer', 'Real-time 3D Developer'),
         t('Archviz, shaders, materiales, iluminación y producción virtual. Experiencias de livestreaming con Python y Unreal Engine.', 'Archviz, shaders, materials, lighting, and virtual production. Livestreaming experiences with Python and Unreal Engine.'), 'visualizacion.html')
    ]
    cards = ''.join(f'<article><h3>{title}</h3><p>{body}</p><a class="text-link" href="{url}">{t("Ver experiencia relacionada", "View related experience")} ↗</a></article>' for title,body,url in roles)
    return f'<section class="section wrap"><div class="section-heading"><p class="eyebrow">{t("Contratación / Colaboración", "Hiring / Collaboration")}</p><h2>{t("Qué puedo aportar a tu equipo.", "What I can bring to your team.")}</h2><p>{t("Trabajo por proyecto y considero propuestas de contratación remota. Acordamos disponibilidad, responsabilidad y alcance según la necesidad.", "I work on projects and consider remote employment opportunities. We agree on availability, responsibility, and scope based on your needs.")}</p></div><div class="offer-grid">{cards}</div></section>'

FAQ = {
    'software': [
        (t('¿Podés integrar un asistente con nuestra librería o aplicación?', 'Can you connect an assistant to our library or application?'), t('Sí. Desarrollé un servidor MCP para que Copilot consulte el código de Grafika desde las aplicaciones que la usan. Podemos definir una integración de contexto y herramientas para tu caso.', 'Yes. I developed an MCP server that lets Copilot consult Grafika’s code from applications using it. We can define a context and tool integration for your use case.')),
        (t('¿Tenés experiencia en software financiero?', 'Do you have experience with financial software?'), t('Desarrollé un script Python que consulta datos por ticker mediante APIs como Yahoo Finance, estima el valor intrínseco y muestra la diferencia porcentual frente al precio de mercado. Está pensado para una integración web futura.', 'I developed a Python script that retrieves ticker data through APIs such as Yahoo Finance, estimates intrinsic value, and shows the percentage difference from market price. It is intended for a future web integration.')),
    ],
    'visualizacion': [
        (t('¿Podés conectar un livestream con una escena 3D?', 'Can you connect a livestream to a 3D scene?'), t('Desarrollé proyectos personales con Python y Unreal Engine que convierten alertas, reacciones e interacciones del chat en elementos 2D y 3D.', 'I developed personal projects with Python and Unreal Engine that turn alerts, reactions, and chat interactions into 2D and 3D elements.')),
        (t('¿Trabajás también con materiales e iluminación?', 'Do you also work with materials and lighting?'), t('Sí. Trabajo con materiales, iluminación, Niagara y visualización arquitectónica; también desarrollé un Auto Landscape Material propio en Unreal Engine.', 'Yes. I work with materials, lighting, Niagara, and architectural visualization; I also developed a custom Auto Landscape Material in Unreal Engine.')),
    ],
    'videojuegos': [
        (t('¿Podés sumarte a un proyecto que ya está en producción?', 'Can you join a project that is already in production?'), t('Sí. Mi experiencia incluye gameplay, UI, SDK, herramientas, LiveOps y optimización en equipos como Games Station, OnChain Studios, LemonChili Games y Netherak.', 'Yes. My experience includes gameplay, UI, SDKs, tools, LiveOps, and optimization in teams such as Games Station, OnChain Studios, LemonChili Games, and Netherak.')),
        (t('¿Qué experiencia tenés con Unity y Unreal?', 'What is your experience with Unity and Unreal?'), t('Más de 13 años con Unity3D y más de 4 con Unreal Engine, con C#, C++, Blueprints, sistemas multijugador, Animation Blueprints, materiales e integraciones de servicios móviles.', 'Over 13 years with Unity3D and more than 4 with Unreal Engine, using C#, C++, Blueprints, multiplayer systems, Animation Blueprints, materials, and mobile service integrations.')),
    ],
}

def faq_section(area):
    items = ''.join(f'<details class="capability"><summary><strong>{q}</strong><span aria-hidden="true">+</span></summary><div class="capability-body"><p>{a}</p></div></details>' for q,a in FAQ[area])
    return f'<section class="section wrap" id="preguntas"><div class="section-heading"><p class="eyebrow">{t("Antes de conversar", "Before we talk")}</p><h2>{t("Preguntas frecuentes", "Frequently asked questions")}</h2></div><div class="faq-list">{items}</div></section>'

CV_TEXT = t('CV en texto', 'Plain-text resume')
CAPABILITY_NAV = t('Capacidades técnicas', 'Technical capabilities')
