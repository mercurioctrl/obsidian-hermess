# Stack — shoppingAndGoblins

Ver también: [[shoppingAndGoblins]] · [[arquitectura]]

- **Render:** HTML5 Canvas 2D (todo: personajes, obstáculos, parallax, grilla en perspectiva).
- **Audio:** Web Audio API — efectos sintetizados en runtime (osciladores), sin archivos.
- **Persistencia:** `localStorage` (ranking, premio, personaje), con fallback en memoria.
- **Fuente:** `VT323` (Google Fonts) — única carga externa.
- **Assets:** logo PNG + íconos SVG de productos, todos embebidos en base64.
- **Sin dependencias, sin build, sin backend.** Un único archivo HTML portable/offline.

## Cómo ejecutar

Abrir el HTML en el navegador, o servirlo (recomendado, evita bloqueos de localStorage
en `file://`): `python3 -m http.server 8080`.
