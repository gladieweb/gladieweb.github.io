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
```

Los estilos están en portfolio.css. El juego y las páginas legales conservan sus
estilos originales. El contenido se basa en el portfolio de Notion facilitado por
Lucas. content/media-sources.json conserva los enlaces originales de los 14 videos
y los recursos de los proyectos. Los reproductores usan YouTube con carga diferida,
sin reproducción automática, y ofrecen un enlace directo alternativo.

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
