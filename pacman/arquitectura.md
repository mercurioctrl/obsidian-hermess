# arquitectura

Decisiones de arquitectura del juego Pac-Man.

## Estructura general

Juego sin build system: `index.html` carga todos los `<script>` en orden y
`lib/app.js` arranca todo en `window.onload`. No hay módulos ES — todo son
funciones/prototipos globales conectados con `Object.assign()` para mixins.

## Bucle principal

`game.start(update, render)` en `lib/classes/game.js` corre con `setInterval`
cada `TIME_DELTA` ms (`1000/FPS`, con `FPS = 120`). En cada tick llama a
`update()` (lógica) y `render()` (dibujo).

## Clases principales

- `game.js` — máquina de estados: inicializa entidades, colisiones, score, vidas,
  niveles y oleadas (scatter/chase) de fantasmas.
- `world.js` — mapa con dos matrices: `graphic_map` (visual) y `logical_map`
  (lógico). Construye el canvas de `path` doblado. Maneja pellets.
- `mobile.js` — clase base de movimiento. Valida posición con lookup de color de
  pixel sobre `assets/path.png`.
- `ghost.js` — IA base de fantasmas: modos scatter/chase/frightened/returning,
  sistema de oleadas, elección de camino en intersecciones.
- `blinky.js` / `inky.js` / `pinky.js` / `clyde.js` — estrategia de targeting de
  cada fantasma. Inky usa la posición de un Blinky de referencia (`blinky_ref`).
- `pacman.js` — movimiento de Pac-Man, comer bolitas, disparar modo frightened.
- `display.js` — render con doble buffer (offscreen → canvas final).
- `animator.js` — animación de sprites por contador de frames.
- `controller.js` — input de teclado y gestos swipe.
- `config.js` — **todas las constantes del juego** (FPS, tamaños, posiciones,
  scoring, sonidos, dimensiones del banner).

## Mapa y espejado

- `TILE_SIZE` = 12px, `SPRITE_SIZE` = 24px (sprites ocupan 2x2 tiles).
- `graphic_map` y `logical_map` arrancan con 28 columnas y se **espejan** a 56
  (mitad derecha = espejo de la izquierda, con `TILE_MIRRORS` para invertir tiles).
- `logical_map`: `0` pared, `1` camino, `2` punto de decisión, `3` punto de
  decisión especial, `4` entrada al home.
- `path.png` es una imagen aparte: los pixeles verdes (RGB `0,252,30`) marcan
  dónde puede ir el sprite TL (top-left). `world.js` arma un canvas de path
  doblado: mitad izquierda = original, mitad derecha = espejo.

## Colisión

1. **Movimiento:** nivel de pixel sobre `path.png` (`checkNextPositionTry` en
   `mobile.js`). El `offset_x = 24` alinea coordenadas del mundo con el path.
2. **Fantasma ↔ Pac-Man:** intersección de rectángulos de tamaño
   `COLLISION_SIZE` centrados dentro del sprite.

## IA de fantasmas

Alternan scatter (objetivo: esquina fija) y chase (objetivo: Pac-Man) según un
calendario de oleadas definido por nivel en `ghost.js`. En frightened eligen
dirección al azar. Al ser comidos pasan a returning y vuelven al home. Hay 8
fantasmas (4 por lado), guardados en el array `game.ghosts`.

## Banner de Pac-Man Day

El juego no ocupa toda la ventana: vive centrado dentro de un banner de
**1440×360** (`#banner` en `index.html`). Layout con flexbox: panel izquierdo +
`#canvas` (650×360 fijo) + panel derecho. Los paneles son branding puro
HTML/CSS (logo "PAC-MAN DAY", fecha, fantasmas y Pac-Man animados con CSS, botón
"JUGAR AHORA"); el marcador (`#score`) y las vidas (`#lives`) viven en el panel
derecho.

- El canvas del juego tiene tamaño fijo (`GAME_WIDTH`×`GAME_HEIGHT` en
  `config.js`); el buffer interno sigue siendo `SCREEN_WIDTH`×`SCREEN_HEIGHT`
  (672×372) y `display` lo escala al canvas — la lógica del juego no cambia.
- `resize()` en `app.js` ya no ajusta el canvas a la ventana: fija el canvas al
  tamaño del juego y escala el banner completo con `transform: scale()` para que
  entre en pantallas más chicas.

## Ver también

- [[stack]] — tecnologías y cómo correr el proyecto
- [[contexto]] — decisiones y detalles no obvios
- [[changelog]] — historial de cambios
- [[pacman]] — índice del proyecto
