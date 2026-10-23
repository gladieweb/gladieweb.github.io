"""Build English HTML with the same content, media and local navigation as Spanish.

Translations are exact text entries, not runtime replacements. An untranslated
string fails the build so new Spanish content cannot silently leak into English.
"""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import posixpath
import json

EN = {
    '2013 — Actualidad': '2013 — Present',
    'Abrir en YouTube': 'Open on YouTube',
    'Abrí cada proyecto para conocer mi participación, las tecnologías y las demostraciones disponibles.': 'Open a project to explore my role, the technologies used, and the available demos.',
    'Actuación y cámara física integradas en una escena virtual con iluminación cinematográfica.': 'Performance and a physical camera brought together in a virtual scene with cinematic lighting.',
    'Ago 2020 — Sep 2022': 'Aug 2020 — Sep 2022',
    'Ago 2023 — Jul 2024': 'Aug 2023 — Jul 2024',
    'Ago 2024 — May 2025': 'Aug 2024 — May 2025',
    'Ago — Nov 2025': 'Aug — Nov 2025',
    'Animación facial en tiempo real.': 'Real-time facial animation.',
    'Aplicaciones de gestión, inventario, ventas y dashboards para consultar la información que importa.': 'Management apps, inventory, sales, and dashboards that put the information you need within reach.',
    'Aplicación móvil, C#, integración con GraphQL, UI Toolkit y visual scripting.': 'Mobile application development, C#, GraphQL integration, UI Toolkit, and visual scripting.',
    'Archviz 02 — recorrido': 'Archviz 02 — walkthrough',
    'Arquitectura en tiempo real': 'Real-time architectural visualization',
    'Automatización': 'Automation',
    'Automatización con Python, Bash y scripts batch.': 'Automation with Python, Bash, and batch scripts.',
    'Backend & herramientas': 'Backend & tools',
    'Backend para el SDK del estudio.': 'Backend development for the studio’s SDK.',
    'Buenos Aires, Argentina · Colaboraciones remotas': 'Buenos Aires, Argentina · Remote collaboration',
    'CV original en Notion': 'Original resume on Notion',
    'Certificaciones': 'Certifications',
    'Colaboración en gameplay. Los videos muestran los títulos, no una autoría individual completa.': 'Gameplay contributions. The videos showcase the games, not work created entirely by me.',
    'Colaboración técnica, herramientas para producción y soporte de títulos publicados.': 'Technical collaboration, production tools, and support for released titles.',
    'Composición visual del efecto.': 'Visual composition of the effect.',
    'Comunicación entre la aplicación y el servicio.': 'Communication between the application and the service.',
    'Con qué trabajé': 'The tools behind the work',
    'Conectar los pagos de una aplicación con un proveedor externo y la validación del lado del servidor.': 'Connecting in-app payments to an external provider, with server-side validation.',
    'Conectar tus herramientas': 'Connect your tools',
    'Conocer mi trayectoria': 'Explore my background',
    'Construir gameplay': 'Build gameplay systems',
    'Construí el recorrido, ajusté iluminación y materiales e implementé navegación y control de cámara.': 'I built the walkthrough, refined the lighting and materials, and implemented navigation and camera controls.',
    'Contacto': 'Contact',
    'Contame qué necesitás resolver.': 'Tell me what you need to solve.',
    'Contame qué necesitás resolver: desarrollo de software, visualización 3D, videojuegos o una colaboración profesional.': 'Tell me what you need: software development, 3D visualization, game development, or professional collaboration.',
    'Contame qué querés lograr y en qué punto estás. No hace falta tener una especificación técnica para empezar.': 'Tell me what you want to achieve and where you are now. You don’t need a technical specification to get started.',
    'Contame tu idea': 'Tell me about your idea',
    'Control de cámara.': 'Camera controls.',
    'Conversemos': 'Let’s talk',
    'Corrección de errores.': 'Bug fixing.',
    'Creación del sistema de partículas.': 'Particle system creation.',
    'Crear una experiencia visual': 'Create a visual experience',
    'Creé el efecto de explosión desde cero.': 'I created the explosion effect from scratch.',
    'Cryptoys — guía de la aplicación': 'Cryptoys — application guide',
    'Curso intensivo de pathfinding, toma de decisiones y comportamientos procedurales.': 'An intensive course on pathfinding, decision-making, and procedural behaviors.',
    'Cámara física y entorno virtual.': 'Physical camera and virtual environment.',
    'Cámara, actuación & entorno virtual': 'Camera, performance & virtual environment',
    'Código en GitHub': 'Code on GitHub',
    'Cómo puedo ayudarte': 'How I can help',
    'Dashboard interactivo con métricas y análisis histórico conectado a SQL.': 'An interactive dashboard with metrics and historical analysis connected to SQL.',
    'De los sistemas a la experiencia.': 'From systems to experiences.',
    'De una mecánica a un proyecto.': 'From a mechanic to a full project.',
    'Demostración de producción virtual': 'Virtual production demo',
    'Demostración del resultado en Unreal Engine.': 'A demo of the result in Unreal Engine.',
    'Desarrollar': 'Develop',
    'Desarrollo & experiencias digitales': 'Development & digital experiences',
    'Desarrollo de SDK.': 'SDK development.',
    'Desarrollo de funcionalidades de gameplay.': 'Gameplay feature development.',
    'Desarrollo de funcionalidades y contenido para juegos móviles y web.': 'Feature and content development for mobile and web games.',
    'Desarrollo de herramientas y extensiones reutilizables.': 'Development of reusable tools and extensions.',
    'Desarrollo de mecánicas y niveles para juegos móviles con Unity3D.': 'Mechanics and level development for mobile games in Unity3D.',
    'Desarrollo de videojuegos': 'Game development',
    'Desarrollo integral': 'End-to-end development',
    'Desarrollo integral del proyecto.': 'End-to-end project development.',
    'Desarrollo integral, LiveOps, consultoría en Unreal y producción virtual. Herramientas, gestión de stock y soluciones de IA.': 'End-to-end development, LiveOps, Unreal consulting, and virtual production. Tools, inventory management, and AI solutions.',
    'Desarrollo software y experiencias interactivas. Mi trayectoria conecta programación, herramientas de producción y tecnología en tiempo real.': 'I develop software and interactive experiences. My background brings together programming, production tools, and real-time technology.',
    'Desarrollé el plugin de compras y su integración con la API de MercadoPago a través de un backend en Node.js.': 'I developed the purchase plugin and its MercadoPago API integration through a Node.js backend.',
    'Desarrollé el sistema completo en C++, incluida la generación procedural de obstáculos.': 'I developed the complete system in C++, including procedural obstacle generation.',
    'Desarrollé el sistema de gestión, los dashboards y las integraciones de inteligencia artificial.': 'I developed the management system, dashboards, and AI integrations.',
    'Desarrollé elementos de UI, widgets UMG, materiales interactivos y shaders, en colaboración con diseño y programación.': 'I developed UI elements, UMG widgets, interactive materials, and shaders in collaboration with designers and programmers.',
    'Desarrollé herramientas para los proyectos del estudio y backend para su SDK. También colaboré en gameplay de tres títulos.': 'I developed tools for the studio’s projects and the backend for its SDK. I also contributed to gameplay on three titles.',
    'Desarrollé los sistemas y los distintos aspectos del juego, excepto los assets de arte.': 'I developed the game’s systems and other aspects of the project, except for the art assets.',
    'Desarrollé nuevas funcionalidades, trabajé en LiveOps, corregí errores y optimicé el rendimiento. Los videos muestran los títulos del estudio.': 'I developed new features, worked on LiveOps, fixed bugs, and optimized performance. The videos showcase the studio’s titles.',
    'Desarrollé sistemas de recolección, inventario, atributos y multijugador.': 'I developed harvesting, inventory, player attribute, and multiplayer systems.',
    'Detrás de cada proyecto.': 'Behind every project.',
    'Efectos con Niagara, materiales e iluminación dentro de Unreal Engine.': 'Niagara effects, materials, and lighting in Unreal Engine.',
    'Efectos visuales con Niagara': 'Visual effects with Niagara',
    'El contexto': 'The context',
    'El proyecto en acción': 'The project in action',
    'El siguiente paso': 'The next step',
    'Elegí por dónde empezar. Te muestro cómo puedo ayudarte.': 'Choose where to start. Let’s see how I can help.',
    'Empecemos por una conversación': 'Let’s start with a conversation',
    'En LemonChili Games desarrollé herramientas y backend compartidos entre proyectos. Como independiente, construí Visage AI e integraciones de pagos con Node.js y MercadoPago.': 'At LemonChili Games, I developed tools and backend services shared across projects. As an independent developer, I built Visage AI and payment integrations with Node.js and MercadoPago.',
    'En esta página': 'On this page',
    'Endless Runner Tools — demostración del plugin': 'Endless Runner Tools — plugin demo',
    'Ene — Mar 2014': 'Jan — Mar 2014',
    'Enemigos que patrullan, detectan al jugador, lo persiguen y retoman su recorrido.': 'Enemies that patrol, detect and chase the player, then return to their route.',
    'Equipos de arte, diseño y programación que necesitan herramientas compartidas y procesos de producción más ágiles.': 'Art, design, and programming teams that need shared tools and more efficient production workflows.',
    'Escribime directamente': 'Email me directly',
    'Español & inglés': 'Spanish & English',
    'Español nativo.': 'Native Spanish.',
    'Estudios en desarrollo de videojuegos (2022).': 'Coursework in game development (2022).',
    'Experiencia & habilidades': 'Experience & skills',
    'Experiencia aplicada': 'Relevant experience',
    'Experiencia profesional': 'Professional experience',
    'Experiencia profesional, formación y habilidades de Lucas Villalva. Software, herramientas y experiencias interactivas.': 'Lucas Villalva’s professional experience, education, and skills. Software, tools, and interactive experiences.',
    'Explorar ese trabajo ↗': 'Explore that work ↗',
    'Explorar por motor:': 'Explore by engine:',
    'Explorar proyecto ↗': 'Explore project ↗',
    'Explorar una casa en 3D, recorrerla y ver sus materiales e iluminación en tiempo real.': 'Explore a home in 3D, walk through it, and view its materials and lighting in real time.',
    'Explorá los proyectos': 'Explore the projects',
    'FPS & patrullaje con IA': 'FPS & AI patrol',
    'FPS Mechanics — demostración': 'FPS Mechanics — demo',
    'Formación': 'Education',
    'Gameplay, SDK y flujo de interfaz para una aplicación móvil.': 'Gameplay, SDK, and UI flow for a mobile application.',
    'Gameplay, nuevas funcionalidades y optimización de rendimiento.': 'Gameplay, new features, and performance optimization.',
    'Generación procedural': 'Procedural generation',
    'Generación procedural de obstáculos.': 'Procedural obstacle generation.',
    'Gestión & análisis de datos': 'Management & data analytics',
    'Habilidades': 'Skills',
    'Herramientas & habilidades': 'Tools & skills',
    'Herramientas internas, automatización y soluciones de IA aplicadas a una necesidad concreta.': 'Internal tools, automation, and AI solutions built around a specific need.',
    'Herramientas para equipos': 'Tools for teams',
    'Herramientas y pipelines para arte y diseño. Automatización con Python, Bash y scripts batch.': 'Tools and pipelines for art and design. Automation with Python, Bash, and batch scripts.',
    'Herramientas y pipelines para artistas y diseñadores.': 'Tools and pipelines for artists and designers.',
    'Herramientas, pipelines y backend para acompañar el trabajo de varios proyectos.': 'Tools, pipelines, and backend services supporting multiple projects.',
    'IA': 'AI',
    'Idiomas': 'Languages',
    'Iluminación': 'Lighting',
    'Iluminación cinematográfica y edición.': 'Cinematic lighting and editing.',
    'Iluminación dinámica y ajuste de materiales.': 'Dynamic lighting and material refinement.',
    'Implementación como plugin reutilizable.': 'Implementation as a reusable plugin.',
    'Implementación del flujo de UI.': 'UI flow implementation.',
    'Implementación y depuración de multiplayer e IA en C++ para Lunaris.': 'Multiplayer and AI implementation and debugging in C++ for Lunaris.',
    'Implementé el gameplay del FPS y el sistema de comportamiento de los enemigos con Blueprints.': 'I implemented the FPS gameplay and enemy behavior system with Blueprints.',
    'Inglés intermedio / avanzado.': 'Intermediate / advanced English.',
    'Inicio': 'Home',
    'Instructor de IA en videojuegos': 'Game AI Instructor',
    'Integraciones API': 'API integrations',
    'Integraciones de APIs, pagos y backend para que los sistemas puedan trabajar juntos.': 'API, payment, and backend integrations that let your systems work together.',
    'Integración con LiveLink y MetaHuman.': 'LiveLink and MetaHuman integration.',
    'Integración con MercadoPago.': 'MercadoPago integration.',
    'Integración con el resto de los sistemas del juego.': 'Integration with the game’s other systems.',
    'Integración de actuación, MetaHumans, cámara física y escenarios virtuales.': 'Bringing together performance, MetaHumans, a physical camera, and virtual sets.',
    'Integrar y optimizar': 'Integrate and optimize',
    'Integré el seguimiento facial con LiveLink y micrófono, la cámara física y el entorno 3D. Realicé iluminación y edición con Premiere Pro.': 'I integrated facial tracking with LiveLink and a microphone, the physical camera, and the 3D environment. I handled the lighting and editing in Premiere Pro.',
    'Inventario': 'Inventory',
    'Inventario y atributos del jugador.': 'Inventory and player attributes.',
    'Inventario, ventas y datos de un comercio, reunidos en una misma herramienta.': 'A store’s inventory, sales, and data, brought together in one tool.',
    'Juego': 'Game',
    'LiveOps y soporte de títulos publicados.': 'LiveOps and support for released titles.',
    'Llevemos tu juego al siguiente paso.': 'Let’s take your game to the next step.',
    'Lucas Villalva, inicio': 'Lucas Villalva, home',
    'Materiales': 'Materials',
    'Materiales interactivos y shaders para la UI.': 'Interactive UI materials and shaders.',
    'May 2014 — Ene 2019': 'May 2014 — Jan 2019',
    'May — Ago 2025': 'May — Aug 2025',
    'Mecánica de combinación de unidades.': 'Unit merging mechanics.',
    'Mecánicas de juego en primera persona.': 'First-person gameplay mechanics.',
    'Mecánicas, comportamiento de enemigos, inventarios y sistemas multijugador.': 'Mechanics, enemy behavior, inventories, and multiplayer systems.',
    'Mi participación': 'My contribution',
    'Mostrar un espacio': 'Showcase a space',
    'Multiplayer Survival — sistema de recolección, enero de 2023': 'Multiplayer Survival — harvesting system, January 2023',
    'Más de 13 años con Unity3D y más de 4 con Unreal Engine. Experiencia en OnChain Studios, Games Station, Netherak, Segritude, Cominted Labs, TECLA, LemonChili y QB9.': 'Over 13 years with Unity3D and more than 4 with Unreal Engine. Experience at OnChain Studios, Games Station, Netherak, Segritude, Cominted Labs, TECLA, LemonChili, and QB9.',
    'Más de 13 años de experiencia en Unity3D y más de 4 con Unreal Engine. Me especializo en sistemas técnicos, gameplay, interfaces, plugins, integración de backend y herramientas para equipos.': 'Over 13 years of experience with Unity3D and more than 4 with Unreal Engine. I specialize in technical systems, gameplay, interfaces, plugins, backend integration, and tools for teams.',
    'Módulos de inventario, ventas, reportes y control de stock.': 'Inventory, sales, reporting, and stock management modules.',
    'Netherak Demons — teaser del juego': 'Netherak Demons — game teaser',
    'Nuevas funcionalidades y soporte continuo para títulos móviles.': 'New features and ongoing support for mobile titles.',
    'O un refuerzo para tu equipo.': 'Or extra support for your team.',
    'Optimización': 'Optimization',
    'Optimización de rendimiento.': 'Performance optimization.',
    'Organizar tu operación': 'Organize your operations',
    'Pagos e integraciones': 'Payments & integrations',
    'Para arrancar, alcanza con esto.': 'Here’s all we need to get started.',
    'Para construir un prototipo, sumar sistemas a un proyecto o reforzar un equipo de desarrollo.': 'Whether you’re building a prototype, adding systems to a project, or strengthening your development team.',
    'Para presentar un espacio, producir una escena o darle forma a una experiencia visual en tiempo real.': 'For showcasing a space, producing a scene, or shaping a real-time visual experience.',
    'Para privacidad o eliminación de datos del juego, usá las páginas específicas.': 'For game privacy or data deletion requests, please use the dedicated pages.',
    'Partículas': 'Particles',
    'Patrones de diseño': 'Design patterns',
    'Patrullaje y detección del jugador.': 'Patrolling and player detection.',
    'Perfil & CV': 'Profile & resume',
    'Perfil / CV': 'Profile / resume',
    'Persecución y retorno al estado de patrulla.': 'Chasing and returning to the patrol state.',
    'Plugin publicado / C++': 'Published plugin / C++',
    'Plugin publicado en Fab': 'Plugin on Fab',
    'Plugins en Fab': 'Plugins on Fab',
    'Podés venir con una idea, un proyecto en marcha o una pregunta.': 'Bring an idea, a project in progress, or a question.',
    'Principal': 'Main navigation',
    'Producción virtual con MetaHuman': 'Virtual production with MetaHuman',
    'Producir una escena': 'Produce a scene',
    'Programación de gameplay.': 'Gameplay programming.',
    'Proyecto independiente / Mobile': 'Independent project / Mobile',
    'Proyectos': 'Projects',
    'Proyectos Unity3D para WebGL y móviles, coordinación con clientes y equipos, investigación y optimización.': 'Unity3D projects for WebGL and mobile, client and team coordination, research, and optimization.',
    'Publicación para dispositivos móviles.': 'Publishing for mobile devices.',
    'Página del juego': 'Game website',
    'Qué desarrollé': 'What I developed',
    'Qué necesitás': 'What do you need?',
    'Qué se necesitaba': 'What was needed',
    'Recolección modular de recursos.': 'Modular resource harvesting.',
    'Recolección, inventario y atributos del jugador en un entorno multijugador.': 'Harvesting, inventory, and player attributes in a multiplayer environment.',
    'Recorrido arquitectónico': 'Architectural walkthrough',
    'Recorrido y navegación en tiempo real.': 'Real-time walkthrough and navigation.',
    'Recorridos 3D, escenas': '3D walkthroughs, scenes,',
    'Recorridos arquitectónicos con navegación, iluminación y materiales en tiempo real.': 'Architectural walkthroughs with real-time navigation, lighting, and materials.',
    'Reducir trabajo manual': 'Reduce manual work',
    'Registro de notas en lenguaje natural mediante NLP.': 'Natural language note-taking with NLP.',
    'Resolver algo': 'Solve a problem',
    'Ruta de navegación': 'Breadcrumb',
    'Saltar al contenido': 'Skip to content',
    'Según lo que necesitás': 'Built around your needs',
    'Shaders / materiales': 'Shaders / materials',
    'Si necesitás ordenar información, conectar servicios o simplificar una tarea, podemos empezar por ahí.': 'If you need to organize information, connect services, or simplify a task, let’s start there.',
    'Sistema de endless runner.': 'Endless runner system.',
    'Sistemas UI, widgets UMG, materiales interactivos y shaders para un RPG multijugador.': 'UI systems, UMG widgets, interactive materials, and shaders for a multiplayer RPG.',
    'Sistemas de gameplay y combate.': 'Gameplay and combat systems.',
    'Sistemas de interfaz para un RPG de horror y fantasía oscura.': 'Interface systems for a dark fantasy horror RPG.',
    'Sistemas de interfaz y widgets UMG.': 'Interface systems and UMG widgets.',
    'Sistemas de supervivencia': 'Survival systems',
    'Sistemas modulares': 'Modular systems',
    'Sistemas multijugador en Unreal C++.': 'Multiplayer systems in Unreal C++.',
    'Sitio de Cryptoys': 'Cryptoys website',
    'Skeleton Warfare — versión de enero de 2022': 'Skeleton Warfare — January 2022 version',
    'Skeleton Warfare: información legal': 'Skeleton Warfare: legal information',
    'Sobre mi trabajo': 'About my work',
    'Software & automatización': 'Software & automation',
    'Software para tu negocio.': 'Software for your business.',
    'Software, automatización, visualización 3D o videojuegos. Elegí qué necesitás resolver y explorá proyectos y experiencia de Lucas Villalva.': 'Software, automation, 3D visualization, or game development. Choose what you need and explore Lucas Villalva’s projects and experience.',
    'Soporte de Skeleton Warfare': 'Skeleton Warfare support',
    'Sumar experiencia a tu equipo': 'Add experience to your team',
    'También desarrollo soluciones en Python, integraciones con Node.js, análisis de datos e IA aplicada, además de visualización arquitectónica y producción virtual.': 'I also develop Python solutions, Node.js integrations, data analytics, and applied AI, as well as architectural visualization and virtual production.',
    'También desarrollé herramientas y backend para LemonChili Games.': 'I also developed tools and backend services for LemonChili Games.',
    'También estoy disponible para propuestas freelance, contratos y posiciones remotas.': 'I’m also available for freelance work, contracts, and remote roles.',
    'Tecnologías & habilidades': 'Technologies & skills',
    'Tecnologías y habilidades': 'Technologies and skills',
    'Trabajo como Senior Unity Developer en OnChain Studios.': 'Work as a Senior Unity Developer at OnChain Studios.',
    'Trabajo como Senior Unity3D Developer en Games Station.': 'Work as a Senior Unity3D Developer at Games Station.',
    'Trabajo como Senior Unreal Engine Engineer en un RPG multijugador.': 'Work as a Senior Unreal Engine Engineer on a multiplayer RPG.',
    'Trabajo con Unreal Engine en visualización arquitectónica y producción virtual: LiveLink, MetaHumans, integración de cámara, iluminación y materiales.': 'I work with Unreal Engine on architectural visualization and virtual production: LiveLink, MetaHumans, camera integration, lighting, and materials.',
    'Trabajo de optimización y fidelidad visual.': 'Optimization and visual fidelity work.',
    'Trabajo en contexto': 'Work in context',
    'Trabajo remoto · Freelance · Contratos': 'Remote work · Freelance · Contracts',
    'Trabajé en programación de gameplay, desarrollo del SDK y flujo de UI de la aplicación móvil, además de optimización de rendimiento.': 'I worked on gameplay programming, SDK development, and the mobile app’s UI flow, as well as performance optimization.',
    'Trayectoria': 'Background',
    'Tu idea, en un espacio que se puede explorar.': 'Your idea, in a space you can explore.',
    'Técnico Superior en Desarrollo de Videojuegos (2009–2012).': 'Higher Technical Degree in Game Development (2009–2012).',
    'UI, SDK, compras, backend y rendimiento para proyectos móviles, web y de escritorio.': 'UI, SDKs, purchases, backend, and performance for mobile, web, and desktop projects.',
    'Un buen proyecto empieza por una necesidad.': 'A good project starts with a need.',
    'Un efecto de explosión creado desde cero dentro de Unreal Engine.': 'An explosion effect created from scratch in Unreal Engine.',
    'Un juego de batallas tácticas, ejércitos y mecánicas de combinación para móviles.': 'A mobile game with tactical battles, armies, and merging mechanics.',
    'Un proyecto de mecánicas en primera persona e inteligencia artificial para enemigos.': 'A project exploring first-person mechanics and enemy AI.',
    'Un proyecto de sistemas modulares para un juego de supervivencia.': 'A modular systems project for a survival game.',
    'Un proyecto independiente de estrategia desarrollado con Unity3D y publicado en Google Play.': 'An independent strategy game built with Unity3D and published on Google Play.',
    'Un sistema de endless runner con generación procedural de obstáculos.': 'An endless runner system with procedural obstacle generation.',
    'Un sistema de gestión para pequeños y medianos comercios que combina operación diaria y análisis de información.': 'A management system for small and medium-sized retailers, combining daily operations with data analysis.',
    'Una aplicación, una integración': 'An app, an integration,',
    'Una demostración de efectos visuales en tiempo real con el sistema de partículas Niagara.': 'A real-time visual effects demo using the Niagara particle system.',
    'Una experiencia de visualización arquitectónica creada desde cero en Unreal Engine 5.': 'An architectural visualization experience built from scratch in Unreal Engine 5.',
    'Una herramienta reutilizable para Unreal Engine, publicada en Fab.': 'A reusable Unreal Engine tool, published on Fab.',
    'Una integración de compras con MercadoPago y un backend propio para validar las operaciones.': 'A MercadoPago purchase integration with a custom backend for transaction validation.',
    'Una prueba de producción virtual que reúne animación facial, MetaHuman y captura con cámara física.': 'A virtual production test combining facial animation, MetaHuman, and physical camera capture.',
    'VFX en tiempo real': 'Real-time VFX',
    'Validación de compras desde el backend.': 'Server-side purchase validation.',
    'Ver en Epic Games Store': 'View on Epic Games Store',
    'Ver experiencia y CV': 'View experience and resume',
    'Ver plugin en Fab': 'View plugin on Fab',
    'Ver proyecto + video ↗': 'View project + video ↗',
    'Videos & demostraciones': 'Videos & demos',
    'Visión por computadora con modelos preentrenados de PyTorch y optimización con ONNX Runtime.': 'Computer vision with pretrained PyTorch models, optimized with ONNX Runtime.',
    'Visualización & experiencias 3D': 'Visualization & 3D experiences',
    'Visualizar un espacio': 'Visualize a space',
    'con software': 'with software',
    'en mente?': 'in mind?',
    'necesitás?': 'need?',
    'o menos tareas manuales.': 'or less manual work.',
    'o una idea': 'or an idea',
    'un videojuego': 'a game',
    'y producción virtual.': 'and virtual production.',
    '¿Estás armando un equipo?': 'Building a team?',
    '¿Qué': 'What do you',
    '¿Qué necesitás?': 'What do you need?',
    '¿Qué necesitás resolver o construir?': 'What do you need to solve or build?',
    '¿Qué tenés': 'What do you have',
    '¿Tenés algún plazo o alcance en mente?': 'Do you have a timeline or scope in mind?',
    '¿Todavía no sabés por dónde empezar?': 'Not sure where to start yet?',
    '¿Ya hay algo en marcha o empezamos desde cero?': 'Is something already in progress, or are we starting from scratch?',
}

# Proper names, programming terms, and existing English text stay as written.
IDENTITY = set('''/ gladieweb|01|02|03|APIs|Account deletion|Archviz|Backend|Bash|Blueprints|Boop Kids — gameplay|Buenos Aires, Argentina|C#|C++|Cominted Labs|Cryptoys|Dash|Dash / Plotly|Endless Runner Tools|Explosion VFX Niagara|Floyd’s Sticker Squad — gameplay|Game of Warriors — gameplay|Gameplay|Gameplay & LiveOps|Gameplay / Blueprints|Games Station|Games Station Studio / Unity3D|Git|GitHub|Google Play|GraphQL|Grow Empire: Rome — gameplay|Image Campus|Independent Game Developer · Freelance|Indie Soul Games|Junior Game Developer|LemonChili Games|LemonChili Games / Tools & backend|Lighting|Lighting / LookDev|LiveLink|LiveOps|Lucas Villalva|MercadoPago|MetaHuman|Mobile|Multiplayer|Multiplayer / C++|Netherak Demons|Netherak Entertainment|Netherak Entertainment / Unreal Engine|Niagara|Node.js|NumPy|ONNX / PyTorch|ONNX Runtime|OOD / UML|Oct 2019 — Sep 2020|OnChain Studios / Unity3D|OpenCV|Pandas|Plotly|Plugins|Premiere Pro|Privacy Policy|PyTorch|Python|QB9 Entertainment|SDK|SQL|Scikit-learn|Scrum / Agile|Segritude Games|Senior Tools Programmer|Senior Unity3D Developer|Senior Unreal Engine Developer|Senior Unreal Engine Engineer|Sep — Oct 2014|Shaders|Skeleton Warfare|TECLA|Technical Lead Developer|Tools programming|Tower Power — gameplay|UADE|UI|UI / UMG|UMG|Unity3D|Unity3D & Unreal Engine|Unity3D Game Developer|Unity3D ↓|Unreal Engine|Unreal Engine 5|Unreal Engine 5 Blueprints — First Person Shooter (FPS).|Unreal Engine C++ Multiplayer Master.|Unreal Engine ↓|VFX|Virtual production|Visage AI|Zupcat|lucas.villalva@gmail.com|lv|⌘|◇|＋|©|2026|/|·|↗'''.split('|'))

def translate(text):
    clean = text.strip()
    if not clean:
        return text
    if clean in EN:
        result = EN[clean]
    elif clean in IDENTITY or clean.startswith('Video: '):
        result = clean
    elif clean.endswith(' — Lucas Villalva'):
        result = translate(clean.removesuffix(' — Lucas Villalva')) + ' — Lucas Villalva'
    elif clean.startswith('Ver proyecto: '):
        result = 'View project: ' + translate(clean.removeprefix('Ver proyecto: '))
    elif clean.startswith('Volver a '):
        result = 'Back to ' + translate(clean.removeprefix('Volver a '))
    else:
        raise ValueError(f'Missing English translation: {clean!r}')
    return text[:len(text)-len(text.lstrip())] + result + text[len(text.rstrip()):]

class EnglishPage(HTMLParser):
    def __init__(self, name, pages):
        super().__init__(convert_charrefs=True)
        self.name, self.pages, self.parts = name, set(pages), []

    def handle_decl(self, decl):
        self.parts.append('<!' + decl + '>')

    def handle_starttag(self, tag, attrs):
        rendered = []
        attributes = dict(attrs)
        for key, value in attrs:
            if key == 'lang':
                value = 'en'
            elif key in ['aria-label', 'title'] or (tag == 'meta' and key == 'content' and (attributes.get('name') == 'description' or attributes.get('property') in ['og:title', 'og:description'])):
                value = translate(value)
            elif key in ['href', 'src']:
                value = self.rewrite_url(value)
            rendered.append(key if value is None else f'{key}="{escape(value, quote=True)}"')
        self.parts.append('<' + tag + (' ' + ' '.join(rendered) if rendered else '') + '>')

    def rewrite_url(self, value):
        url = urlsplit(value)
        if url.scheme or url.netloc or not url.path:
            return value
        original_target = posixpath.normpath(posixpath.join(posixpath.dirname(self.name), url.path))
        target = 'en/' + original_target if original_target in self.pages else original_target
        relative = posixpath.relpath(target, posixpath.dirname('en/' + self.name))
        return urlunsplit(('', '', relative, url.query, url.fragment))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        self.parts.append(f'</{tag}>')

    def handle_data(self, text):
        self.parts.append(escape(translate(text), quote=False))

    def handle_comment(self, text):
        self.parts.append('<!--' + text + '-->')

def language_navigation(content, name, lang):
    current = name if lang == 'es' else 'en/' + name
    directory = posixpath.dirname(current) or '.'
    es = posixpath.relpath(name, directory)
    en = posixpath.relpath('en/' + name, directory)
    script = posixpath.relpath('language.js', directory)
    content = content.replace(f'<html lang="{lang}">', f'<html lang="{lang}" data-language-es="{es}" data-language-en="{en}">')
    language_label = 'Idioma' if lang == 'es' else 'Language'
    selector = f'<nav class="language-switch" aria-label="{language_label}">'
    for code, label in [('es', 'Español'), ('en', 'English')]:
        target = es if code == 'es' else en
        current_attr = ' aria-current="page"' if code == lang else ''
        selector += f'<a href="{target}?lang={code}" lang="{code}" hreflang="{code}" data-language="{code}" aria-label="{label}"{current_attr}>{code.upper()}</a>'
    selector += '</nav>'
    content = content.replace('<!--language-switch-->', selector)
    # Run before rendering to avoid showing the wrong language briefly.
    content = content.replace('  <meta name="viewport"', f'  <script src="{script}?v=1"></script>\n  <link rel="alternate" hreflang="es" href="{es}">\n  <link rel="alternate" hreflang="en" href="{en}">\n  <meta name="viewport"', 1)
    return content.replace('portfolio.css?v=2', 'portfolio.css?v=3')

def localize_pages(root, names):
    for name in names:
        original = (root / name).read_text(encoding='utf-8')
        parser = EnglishPage(name, names)
        parser.feed(original)
        english = language_navigation(''.join(parser.parts), name, 'en')
        spanish = language_navigation(original, name, 'es')
        (root / name).write_text(spanish, encoding='utf-8')
        target = root / 'en' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(english, encoding='utf-8')
    (root / 'content/language-pages.json').write_text(json.dumps(names, indent=2) + '\n', encoding='utf-8')
