# Stack — shoppingAndGoblins

Ver también: [[shoppingAndGoblins]] · [[arquitectura]]

## Frontend (el juego)

- **Render:** HTML5 Canvas 2D (todo: personajes, obstáculos, parallax, grilla en perspectiva,
  ciclo día/noche, cameos de fondo).
- **Audio:** Web Audio API — efectos sintetizados en runtime (osciladores), sin archivos.
- **Persistencia local:** `localStorage` (ranking/premio/personaje), con fallback en memoria.
- **Fuente:** `VT323` (Google Fonts) — única carga externa.
- **Assets:** logo PNG + íconos SVG de productos, todos embebidos en base64.
- **Sin dependencias, sin build.** Un único archivo HTML portable/offline.

## Backend opcional (ranking compartido)

- **`api.php`** — microservicio PHP + **SQLite** (`data/ranking.sqlite`), sin dependencias ni build.
- Requiere PHP 8 con `pdo_sqlite`. Portátil (sin `mbstring`: helper `clip()` unicode-safe).
- Endpoints: `start`, `submit`, `top`, `prize`, `setprize`, `reset`.
- Clave de organizador via env `LIBRERUN_ADMIN_KEY` (protege reset y guardado del premio).
- `data/.htaccess` bloquea el acceso HTTP a la base.

## Cómo ejecutar

- **Solo juego (ranking local):** abrir el HTML, o servirlo (recomendado, evita bloqueos de
  localStorage en `file://`): `python3 -m http.server 8080`.
- **Con ranking compartido:** servir `libre-run-*.html` + `api.php` + `data/` juntos en un
  server con PHP; definir `LIBRERUN_ADMIN_KEY`. El cliente detecta el server solo (constante
  `API_BASE="api.php"`) y cae a local si no responde.
