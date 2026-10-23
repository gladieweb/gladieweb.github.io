# Gladieweb — Lucas Villalva

Portfolio estático para GitHub Pages, organizado por necesidades del cliente.
Los HTML se sirven directamente, sin build en el servidor ni dependencias.

## Navegación

- index.html: entrada breve «¿Qué necesitás?» con tres opciones.
- software.html: software, automatización, integraciones e IA.
- visualizacion.html: arquitectura 3D, producción virtual y VFX.
- videojuegos.html: desarrollo de juegos, con secciones Unity3D y Unreal Engine.
- proyectos/: contexto, participación, habilidades, videos y enlaces de cada proyecto.
- perfil.html: trayectoria, formación y habilidades.
- contacto.html: contacto profesional.
- skeleton-warfare.html: landing del juego existente.

## Editar contenido

El contenido y la estructura del portfolio se mantienen en scripts/build_portfolio.py.
Después de editarlo, ejecutar:

```powershell
python scripts/build_portfolio.py
python scripts/check_site.py
python scripts/check_discovery.py
node scripts/check_language.cjs
```

Los estilos están en portfolio.css. El juego y las páginas legales conservan sus
estilos originales. El contenido se basa en el portfolio de Notion facilitado por
Lucas. content/media-sources.json conserva los enlaces originales de los 14 videos
y los recursos de los proyectos. Los reproductores usan YouTube con carga diferida,
sin reproducción automática, y ofrecen un enlace directo alternativo.

Las actualizaciones profesionales facilitadas directamente por Lucas se mantienen
en `scripts/portfolio_updates.py`, junto con sus traducciones. Incluyen SciSoft
(desde febrero de 2026), Grafika, DrawMate, EasyViewDesigner2, Grafika MCP con
Copilot, Skills para IA y proyectos personales de livestreaming con Python y Unreal.
Los casos nuevos no incluyen videos o enlaces que Lucas aún no haya proporcionado.

Los servicios emergentes se presentan en paneles desplegables, con ejemplos,
primer entregable y aspectos a validar. Los pilotos de ACE, Agentic Gameplay,
AI Coding Agents, AI Automated QA, RAG e inferencia local se distinguen de los
proyectos realizados y no se agregan a la lista de experiencia acreditada.

`scripts/positioning.py` agrupa las capacidades técnicas y las preguntas para
clientes, y mantiene los casos de valoración de acciones con Python y Auto
Landscape Material. El detalle financiero refleja un script implementado para
integración futura, sin atribuirle una web terminada o resultados de inversión.

## Descubrimiento en buscadores y asistentes

`scripts/discovery.py` genera canónicas absolutas, alternates ES/EN/x-default,
metadatos sociales y JSON-LD (Person, ProfilePage, WebSite, Service, CreativeWork
y BreadcrumbList). Se utiliza la URL pública del repositorio:
https://gladieweb.github.io/. Si cambia el dominio, actualizar esa constante.

También genera sitemap.xml, robots.txt y CVs en texto (perfil.txt y en/perfil.txt).
El marcado describe contenido visible; los pilotos futuros no figuran como
experiencia de la persona ni como proyectos realizados. Las páginas legales
existentes no se reescriben. Ver docs/search-visibility.md para publicación,
verificación y medición. Estos cambios no garantizan indexación, citas ni ranking.

## Idiomas

El portfolio tiene versiones estáticas en español (rutas originales) e inglés
(`en/`, con las mismas subpáginas). Las traducciones se mantienen en
`scripts/localization.py`; el generador falla si falta traducir contenido nuevo.

`language.js` detecta el idioma principal del navegador: `es` y sus variantes
usan español; cualquier otro idioma o un valor desconocido usa inglés. El
selector ES / EN conserva la página y sección actuales y guarda la elección
manual en localStorage. Si el almacenamiento está bloqueado, la elección se
mantiene mediante `?lang=es` o `?lang=en` durante la navegación. Los enlaces
directos a `en/` siempre permiten compartir la versión inglesa.

Las páginas legales y la landing de Skeleton Warfare mantienen sus URLs y su
contenido original en inglés, sin detección ni redirección de idioma.

## URLs legales de Google Play

Se conservan sin cambios privacypolicy.html y account-deletion.html, el contenido
de la política y las instrucciones de eliminación de cuenta y datos. La ruta
privacypolicy que resuelve GitHub Pages también permanece disponible.
Hay enlaces HTML directos a ambas páginas en todos los footers, sin JavaScript.
Los enlaces antiguos a /#account-deletion redirigen a la página dedicada.
No cambiar las URLs configuradas en Play Console al publicar este rediseño.

## Previsualizar

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

Abrir http://127.0.0.1:8765/. La publicación sigue la configuración existente de
GitHub Pages. Los cambios locales no se publican hasta subirlos al repositorio.
