"""Professional updates provided by Lucas; proposed pilots are not past projects."""
from html import escape

EN_UPDATES = {}

def t(es, en):
    EN_UPDATES[es] = en
    return es

PROJECT_ADDITIONS = [
    dict(slug='scisoft-grafika', area='software', title=t('Grafika · SciSoft', 'Grafika · SciSoft'),
         category=t('Programación gráfica / Febrero 2026 — Actualidad', 'Graphics programming / February 2026 — Present'),
         summary=t('Desarrollo en TypeScript de Grafika, una librería utilizada en programas de diseño de corte.', 'TypeScript development for Grafika, a library used in cutting design applications.'),
         context=t('SciSoft desarrolla software de diseño de corte que utiliza la librería Grafika.', 'SciSoft develops cutting design software that uses the Grafika library.'),
         role=t('Desde febrero de 2026 trabajo en SciSoft como programador gráfico, desarrollando Grafika en TypeScript. También participé en DrawMate y EasyViewDesigner2.', 'Since February 2026, I have worked at SciSoft as a graphics programmer, developing Grafika in TypeScript. I have also contributed to DrawMate and EasyViewDesigner2.'),
         features=[t('Desarrollo de la librería gráfica Grafika en TypeScript.', 'Development of the Grafika graphics library in TypeScript.'), t('Participación en los proyectos DrawMate y EasyViewDesigner2.', 'Contributions to DrawMate and EasyViewDesigner2.'), t('Trabajo en una librería compartida por aplicaciones de diseño de corte.', 'Work on a library shared across cutting design applications.')],
         skills=[t('TypeScript', 'TypeScript'), t('Programación gráfica', 'Graphics programming'), t('Grafika', 'Grafika'), t('DrawMate', 'DrawMate'), t('EasyViewDesigner2', 'EasyViewDesigner2')], videos=[], links=[]),
    dict(slug='grafika-mcp', area='software', title=t('Grafika MCP & Copilot', 'Grafika MCP & Copilot'),
         category=t('Integración de IA / Trabajo realizado', 'AI integration / Completed work'),
         summary=t('Un servidor MCP para que Copilot pueda consultar el código de Grafika desde las aplicaciones que la implementan.', 'An MCP server that lets Copilot consult Grafika’s source code from applications that use the library.'),
         context=t('Al trabajar en una aplicación que depende de Grafika, el asistente necesita contexto sobre el código de la librería.', 'When working on an application that depends on Grafika, the assistant needs context from the library’s source code.'),
         role=t('Creé un servidor MCP de Grafika y lo integré con Copilot para conectar ese contexto con las aplicaciones que utilizan la librería. También desarrollé Skills para asistentes de IA.', 'I created a Grafika MCP server and integrated it with Copilot to connect that context to applications using the library. I also developed Skills for AI assistants.'),
         features=[t('Consulta del código fuente de Grafika desde el contexto de la aplicación que la utiliza.', 'Access to Grafika’s source code from the context of an application using it.'), t('Integración del servidor MCP con Copilot.', 'MCP server integration with Copilot.'), t('Creación de Skills para flujos de trabajo con IA.', 'Creation of Skills for AI workflows.')],
         skills=[t('MCP servers', 'MCP servers'), t('Copilot', 'Copilot'), t('AI Skills', 'AI Skills'), t('Contexto de código', 'Code context')], videos=[], links=[]),
    dict(slug='streaming-interactivo', area='visualizacion', title=t('Livestreams interactivos', 'Interactive livestreams'),
         category=t('Proyecto personal / Python & Unreal Engine', 'Personal project / Python & Unreal Engine'),
         summary=t('Reacciones, alertas e interacciones del chat que se convierten en elementos 2D y 3D durante una transmisión.', 'Reactions, alerts, and chat interactions turned into 2D and 3D elements during a livestream.'),
         context=t('Crear programas para transmisiones en vivo que conecten la participación del chat con elementos visuales.', 'Building livestream applications that connect chat participation with visual elements.'),
         role=t('En mi tiempo libre desarrollé programas con Python y Unreal Engine para personalizar reacciones, alertas e interacciones del chat con elementos 2D y 3D.', 'In my spare time, I developed applications with Python and Unreal Engine to customize reactions, alerts, and chat interactions using 2D and 3D elements.'),
         features=[t('Conexión de interacciones del chat con respuestas visuales.', 'Connecting chat interactions to visual responses.'), t('Reacciones y alertas personalizadas para transmisiones en vivo.', 'Custom reactions and alerts for livestreams.'), t('Elementos 2D y 3D mediante Unreal Engine, integrados con Python.', '2D and 3D elements in Unreal Engine, integrated with Python.')],
         skills=['Python', 'Unreal Engine', t('Livestreaming', 'Livestreaming'), t('Interacciones de chat', 'Chat interactions'), t('2D / 3D', '2D / 3D')], videos=[], links=[]),
]

SCISOFT_JOB = (
    t('Feb 2026 — Actualidad', 'Feb 2026 — Present'),
    t('SciSoft', 'SciSoft'),
    t('Programador gráfico · TypeScript', 'Graphics Programmer · TypeScript'),
    t('Desarrollo de Grafika para aplicaciones de diseño de corte. Participación en DrawMate y EasyViewDesigner2. Servidor MCP para conectar el código de Grafika con Copilot desde las aplicaciones que la implementan.', 'Grafika development for cutting design applications. Contributions to DrawMate and EasyViewDesigner2. An MCP server connecting Grafika’s code to Copilot from applications using the library.')
)

SOFTWARE_EXPERIENCE = t('Desde febrero de 2026 trabajo en SciSoft en programación gráfica con TypeScript: Grafika, DrawMate y EasyViewDesigner2. También desarrollé un servidor MCP de Grafika integrado con Copilot y Skills para IA.', 'Since February 2026, I have worked at SciSoft on graphics programming with TypeScript: Grafika, DrawMate, and EasyViewDesigner2. I also developed a Grafika MCP server integrated with Copilot and AI Skills.')
VISUAL_EXPERIENCE = t('Además de archviz y producción virtual con Unreal Engine, desarrollo proyectos personales de livestreaming con Python: alertas, reacciones e interacciones del chat con elementos 2D y 3D.', 'Alongside archviz and virtual production with Unreal Engine, I develop personal livestreaming projects with Python: alerts, reactions, and chat interactions using 2D and 3D elements.')

CURRENT_PROFILE = f'''<section class="section wrap experience-panel"><div><p class="eyebrow">{t('Actualmente / SciSoft', 'Currently / SciSoft')}</p><h2>{t('Programación gráfica e integración de IA.', 'Graphics programming and AI integration.')}</h2><p>{SOFTWARE_EXPERIENCE}</p><a class="text-link" href="proyectos/scisoft-grafika.html">{t('Conocer el trabajo en Grafika', 'Explore the Grafika work')} ↗</a></div><div><h3>{t('Trabajo realizado con IA', 'Hands-on AI work')}</h3><p>{t('MCP servers, Skills e integración con Copilot para dar contexto de código a los asistentes. En proyectos personales, Python y Unreal Engine conectan el chat del livestream con escenas 2D y 3D.', 'MCP servers, Skills, and Copilot integration to give assistants code context. In personal projects, Python and Unreal Engine connect livestream chat to 2D and 3D scenes.')}</p><a class="text-link" href="proyectos/grafika-mcp.html">{t('Ver el servidor MCP de Grafika', 'Explore the Grafika MCP server')} ↗</a></div></section>'''

APPLIED = t('Experiencia aplicada', 'Relevant experience')
PILOT = t('Piloto a desarrollar', 'Proposed pilot')
EXAMPLE = t('Ejemplo de primer alcance', 'Example starting scope')
DELIVERABLE = t('Primer entregable', 'First deliverable')
BOUNDARY = t('Qué validamos primero', 'What we validate first')
OPEN = t('Ver ejemplo +', 'See example +')

def offer(title, status, example, deliverable, boundary, source=None):
    return dict(title=title, status=status, example=example, deliverable=deliverable, boundary=boundary, source=source)

AI_OFFERS = {
    'software': [
        offer(t('MCP, Skills & tool calling', 'MCP, Skills & tool calling'), APPLIED,
              t('Conectar Copilot con el código o la documentación de una librería, siguiendo la experiencia del servidor MCP de Grafika. Como extensión, exponer una consulta o acción concreta de tu aplicación.', 'Connect Copilot to a library’s code or documentation, drawing on the Grafika MCP server experience. As an extension, expose one specific query or action from your application.'),
              t('Un servidor con una consulta de contexto y una Skill para utilizarla; si necesitás acciones, empezar por una herramienta con entradas y resultados definidos.', 'A server with one context query and a Skill to use it; if actions are needed, start with one tool with defined inputs and outputs.'),
              t('Qué información se comparte, qué cliente lo consume y qué acciones necesitan revisión antes de ejecutarse.', 'What information is shared, which client uses it, and which actions need review before execution.')),
        offer(t('RAG sobre tu documentación', 'RAG over your documentation'), PILOT,
              t('Un asistente que responda preguntas sobre un conjunto pequeño de manuales o documentación interna y muestre las fuentes consultadas.', 'An assistant that answers questions about a small set of manuals or internal documents and shows the sources it used.'),
              t('Una demo con documentos acordados y preguntas de prueba para revisar la calidad de las respuestas.', 'A demo with an agreed document set and test questions to review answer quality.'),
              t('La calidad de la recuperación, la trazabilidad de las fuentes y el comportamiento ante preguntas que los documentos no permiten responder.', 'Retrieval quality, source traceability, and behavior when the documents do not support an answer.')),
        offer(t('Local inference / modelos locales', 'Local inference / on-device models'), PILOT,
              t('Probar un modelo pequeño que clasifique notas o solicitudes en tu propio equipo, para evaluar si conviene evitar un servicio externo en esa tarea.', 'Try a small model that classifies notes or requests on your own machine, to evaluate whether that task can run without an external service.'),
              t('Una prueba en un equipo definido, con mediciones de latencia, memoria y resultados sobre ejemplos acordados.', 'A test on a specified machine, with latency, memory, and output measurements on agreed examples.'),
              t('Compatibilidad del modelo y del hardware, calidad y uso real de recursos antes de decidir una integración.', 'Model and hardware compatibility, quality, and actual resource usage before choosing an integration.')),
        offer(t('AI Automated QA para aplicaciones', 'AI Automated QA for applications'), PILOT,
              t('Un asistente que ejecute un recorrido funcional de prueba, capture errores y prepare un reporte para revisión.', 'An assistant that runs a functional test flow, captures errors, and prepares a report for review.'),
              t('Un caso reproducible con resultados esperados y un reporte contrastado con esas comprobaciones.', 'One reproducible case with expected results and a report checked against those assertions.'),
              t('Qué puede comprobarse automáticamente y qué requiere revisión humana. El piloto no reemplaza la cobertura completa de QA.', 'What can be checked automatically and what needs human review. The pilot does not replace full QA coverage.')),
    ],
    'visualizacion': [
        offer(t('MCP & tool calling para escenas', 'MCP & tool calling for scenes'), PILOT,
              t('Un asistente que consulte los objetos de una escena y proponga un cambio de iluminación o una cámara entre opciones predefinidas.', 'An assistant that inspects scene objects and proposes a lighting change or a camera from predefined options.'),
              t('Una escena de prueba con una consulta y una acción acotada que puedas revisar antes de aplicarla.', 'A test scene with one query and one scoped action that you can review before applying it.'),
              t('La conexión con el editor, los permisos y la repetibilidad del resultado. La base es mi experiencia con MCP; esta integración de escena sería nueva.', 'The editor connection, permissions, and repeatability. This builds on my MCP experience; the scene integration itself would be new.')),
        offer(t('Presentador interactivo / Unreal & ACE', 'Interactive presenter / Unreal & ACE'), PILOT,
              t('Explorar un personaje que responda preguntas sobre una escena y active una de unas pocas presentaciones o vistas preparadas.', 'Explore a character that answers questions about a scene and triggers one of a few prepared presentations or views.'),
              t('Una prueba de viabilidad de un componente de NVIDIA ACE en una escena de Unreal, antes de ampliar la interacción.', 'A feasibility test of one NVIDIA ACE component in an Unreal scene before expanding the interaction.'),
              t('Componentes disponibles, hardware, latencia y alcance de las respuestas. ACE es un área nueva en mi práctica.', 'Available components, hardware, latency, and response scope. ACE is a new area in my practice.'),
              (t('NVIDIA ACE', 'NVIDIA ACE'), 'https://developer.nvidia.com/ace-for-games')),
    ],
    'unity': [
        offer(t('AI Coding Agents para Unity', 'AI Coding Agents for Unity'), PILOT,
              t('Un agente que prepare un script C# sencillo o una herramienta de editor y proponga una prueba, usando las convenciones del proyecto.', 'An agent that prepares a simple C# script or editor tool and proposes a test using the project’s conventions.'),
              t('Una tarea pequeña, cambios revisables y una prueba ejecutada; la aprobación del código queda en manos del equipo.', 'One small task, reviewable changes, and an executed test; code approval stays with the team.'),
              t('Compatibilidad con la versión de Unity y conexión del agente mediante las herramientas admitidas para ese proyecto.', 'Compatibility with the Unity version and the agent connection through tools supported by that project.')),
        offer(t('MCP & tool calling en Unity', 'MCP & tool calling in Unity'), PILOT,
              t('Consultar una escena o la consola desde el asistente y ejecutar una herramienta de editor con parámetros definidos.', 'Query a scene or the console from the assistant and run an editor tool with defined parameters.'),
              t('Una integración mínima con una consulta y una operación revisable, usando CLI o MCP según corresponda a la versión.', 'A minimal integration with one query and one reviewable operation, using CLI or MCP as appropriate for the version.'),
              t('Acceso admitido al editor, permisos y límites de ejecución. Tengo experiencia en MCP con Grafika; aplicarlo a Unity sería un nuevo piloto.', 'Supported editor access, permissions, and execution limits. I have MCP experience with Grafika; applying it to Unity would be a new pilot.')),
        offer(t('AI Automated QA en Unity', 'AI Automated QA in Unity'), PILOT,
              t('Recorrer un menú o cargar una escena de prueba, ejecutar comprobaciones y reunir errores de consola en un reporte.', 'Navigate a menu or load a test scene, run checks, and collect console errors in a report.'),
              t('Un smoke test con condiciones de éxito y fallo explícitas, repetible sobre una escena acordada.', 'A smoke test with explicit success and failure conditions, repeatable on an agreed scene.'),
              t('Estabilidad del recorrido y utilidad del reporte; no se promete encontrar todos los errores ni sustituir al equipo de QA.', 'Flow stability and report usefulness; this does not promise to find every bug or replace the QA team.')),
    ],
    'unreal': [
        offer(t('Agentic Gameplay / Unreal & NVIDIA ACE', 'Agentic Gameplay / Unreal & NVIDIA ACE'), PILOT,
              t('Un NPC de prueba que interprete una petición y elija entre tres acciones autorizadas: dar una pista, señalar un lugar o iniciar un diálogo.', 'A test NPC that interprets a request and chooses between three authorized actions: give a hint, point to a location, or start a dialogue.'),
              t('Primero, validar la integración de un componente de ACE en una escena. Después, conectar una interacción acotada con el gameplay.', 'First, validate the integration of one ACE component in a scene. Then connect one scoped interaction to gameplay.'),
              t('Modelo, componentes de ACE, hardware, latencia y control de acciones. ACE y Agentic Gameplay son áreas nuevas en mi práctica.', 'Model, ACE components, hardware, latency, and action control. ACE and Agentic Gameplay are new areas in my practice.'),
              ('NVIDIA ACE', 'https://developer.nvidia.com/ace-for-games')),
        offer(t('MCP & tool calling en Unreal', 'MCP & tool calling in Unreal'), PILOT,
              t('Dar a un asistente acceso a una consulta del proyecto o a una acción de una herramienta propia, por ejemplo inspeccionar actores o preparar un cambio revisable.', 'Give an assistant access to one project query or an action in a custom tool, such as inspecting actors or preparing a reviewable change.'),
              t('Una consulta de solo lectura y una operación acotada sobre un proyecto de prueba.', 'One read-only query and one scoped operation in a test project.'),
              t('Cómo se conecta el editor y qué acciones quedan habilitadas. Partimos de mi experiencia con Grafika MCP para evaluar una nueva integración en Unreal.', 'How the editor connects and which actions are enabled. We build on my Grafika MCP experience to evaluate a new Unreal integration.')),
        offer(t('RAG & local inference para personajes', 'RAG & local inference for characters'), PILOT,
              t('Un personaje que consulte un pequeño conjunto de notas del mundo para responder preguntas; evaluar por separado si un modelo local puede resolver esa tarea.', 'A character that consults a small set of world notes to answer questions; separately evaluate whether a local model can handle that task.'),
              t('Una demo de texto con fuentes recuperadas y una prueba de rendimiento local en un equipo acordado.', 'A text demo with retrieved sources and a local performance test on an agreed machine.'),
              t('Coherencia con las fuentes, respuestas fuera de contexto y presupuesto de CPU/GPU. Son propuestas de prototipo, no funcionalidades ya implementadas.', 'Consistency with sources, out-of-context answers, and CPU/GPU budget. These are prototype proposals, not already-implemented features.')),
        offer(t('AI Automated QA en Unreal', 'AI Automated QA in Unreal'), PILOT,
              t('Automatizar un recorrido de UI o una interacción de inventario y reunir logs y resultados para revisión.', 'Automate a UI flow or inventory interaction and collect logs and results for review.'),
              t('Un caso de prueba reproducible con comprobaciones definidas y reporte de fallos.', 'One reproducible test case with defined checks and a failure report.'),
              t('Determinismo de la prueba y exactitud del reporte, antes de sumar más escenarios.', 'Test determinism and report accuracy before adding more scenarios.')),
    ],
}

def ai_services(key, level=2):
    labels = {
        'software': t('IA conectada con tu trabajo', 'AI connected to your work'),
        'visualizacion': t('Asistentes para experiencias visuales', 'Assistants for visual experiences'),
        'unity': t('IA para tu flujo de trabajo en Unity', 'AI for your Unity workflow'),
        'unreal': t('Nuevas interacciones con Unreal e IA', 'New interactions with Unreal and AI'),
    }
    intro = t('Integraciones y prototipos con un primer alcance concreto. Abrí una propuesta para ver un ejemplo y qué validaríamos primero.', 'Integrations and prototypes with a concrete starting scope. Open a proposal to see an example and what we would validate first.')
    note = t('Los pilotos son propuestas para desarrollar, no proyectos ya entregados. Empezamos por una prueba de viabilidad con alcance y criterios acordados; la integración completa se define a partir de ese resultado.', 'Pilots are proposals to develop, not previously delivered projects. We start with a feasibility test with agreed scope and criteria; the full integration is defined based on that result.')
    cards = ''
    for item in AI_OFFERS[key]:
        source = ''
        if item['source']:
            label, url = item['source']
            source = f'<a class="text-link" href="{url}" target="_blank" rel="noopener noreferrer">{escape(label)} ↗</a>'
        cards += f'<details class="ai-offer"><summary><span class="offer-status {"applied" if item["status"] == APPLIED else "pilot"}">{item["status"]}</span><strong>{escape(item["title"])}</strong><span class="offer-expand">{OPEN}</span></summary><div class="offer-body"><p class="eyebrow">{EXAMPLE}</p><p>{escape(item["example"])}</p><dl><div><dt>{DELIVERABLE}</dt><dd>{escape(item["deliverable"])}</dd></div><div><dt>{BOUNDARY}</dt><dd>{escape(item["boundary"])}</dd></div></dl>{source}</div></details>'
    discussion = t('Conversemos sobre una integración o un piloto', 'Let’s discuss an integration or a pilot')
    area = 'videojuegos' if key in ['unity', 'unreal'] else key
    return f'<section class="ai-services" id="ia-{key}"><p class="eyebrow">{t("IA / Integraciones & pilotos", "AI / Integrations & pilots")}</p><h{level}>{labels[key]}</h{level}><p>{intro}</p><div class="ai-offers">{cards}</div><p class="pilot-note">{note}</p><a class="text-link" href="contacto.html?tema={area}">{discussion} ↗</a></section>'

def ai_navigation(area):
    if area == 'videojuegos':
        return f'<a href="#ia-unity">{t("IA para Unity", "AI for Unity")}</a><a href="#ia-unreal">{t("IA para Unreal", "AI for Unreal")}</a>'
    return f'<a href="#ia-{area}">{t("IA & pilotos", "AI & pilots")}</a>'
