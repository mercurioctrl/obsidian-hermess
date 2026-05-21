# stack

Tecnologías del proyecto.

- **Lenguaje:** JavaScript vanilla (ES5/ES6), sin módulos. Todos los archivos se
  cargan como `<script>` en orden desde `index.html`.
- **Render:** HTML5 Canvas con doble buffer (dibuja en canvas offscreen y luego
  vuelca al canvas visible).
- **Banner:** el canvas va centrado en un banner HTML/CSS de 1440×360; la
  decoración (logo, Pac-Man y fantasmas decorativos) usa animaciones CSS.
- **Sin build:** no hay npm, ni bundler, ni frameworks, ni transpilación.
- **Servidor:** se sirve con `python3 -m http.server 8000`. Debe servirse por
  HTTP (no `file://`) para que carguen los assets.

## Assets

- `assets/spritemap.png` — sprites de Pac-Man, fantasmas, bolitas y frutas.
- `assets/path.png` — máscara de caminos válidos (verde `0,252,30`).
- `assets/map.jpg` / `checkerboard.png` / `ready.png` / `game_over.png` — imágenes.
- `assets/Minecraft.ttf` — fuente pixelada usada en el marcador y el banner.
- `assets/sounds/*.mp3` — efectos y música.
- Archivos `.psd` — fuentes editables de los assets.

## Ver también

- [[arquitectura]] — cómo se estructura el código
- [[pacman]] — índice del proyecto
