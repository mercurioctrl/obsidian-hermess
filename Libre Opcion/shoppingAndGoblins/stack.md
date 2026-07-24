# Stack — shoppingAndGoblins

Ver también: [[shoppingAndGoblins]] · [[arquitectura]]

## Frontend (el juego)

- **Render:** HTML5 Canvas 2D (todo: personajes, obstáculos, parallax, grilla en perspectiva,
  ciclo día/noche, cameos de fondo).
- **Audio:**
  - **Efectos:** Web Audio API — osciladores sintetizados en runtime, sin archivos.
  - **Música de fondo:** `music.mp3` externo en loop (elemento `Audio`). ⚠️ Es un **archivo
    aparte** (~28MB), así que el juego **ya no es un único archivo portable**: hay que servir
    `music.mp3` junto al HTML.
- **Persistencia local:** `localStorage` (ranking/premio/personaje), con fallback en memoria.
- **Fuente:** `VT323` (Google Fonts) — carga externa.
- **Assets embebidos:** logo PNG + íconos SVG de productos, todos en base64 (el resto del juego
  sigue inline; la única salvedad a la portabilidad es `music.mp3`).
- **Sin dependencias, sin build.**

## Backend opcional (ranking compartido)

- **`api.php`** — microservicio PHP + **SQLite** (`data/ranking.sqlite`), sin dependencias ni build.
- Requiere PHP 8 con `pdo_sqlite`. Portátil (sin `mbstring`: helper `clip()` unicode-safe).
- Endpoints: `start`, `submit`, `top`, `prize`, `setprize`, `reset`.
- Clave de organizador via env `LIBRERUN_ADMIN_KEY` (protege reset y guardado del premio). Debe
  **coincidir** con `ADMIN_PIN` del HTML (el candado del panel client-side).
- `data/.htaccess` bloquea el acceso HTTP a la base.

## Cómo ejecutar

- **Solo juego (ranking local):** servir el HTML **con `music.mp3` al lado** (recomendado por
  HTTP para evitar bloqueos de localStorage/autoplay en `file://`): `python3 -m http.server 8080`.
- **Con ranking compartido:** servir `libre-run-*.html` + `music.mp3` + `api.php` + `data/`
  juntos en un server con PHP; definir `LIBRERUN_ADMIN_KEY` (= `ADMIN_PIN`). El cliente detecta
  el server solo (constante `API_BASE="api.php"`) y cae a local si no responde.
