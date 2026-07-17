# Arquitectura — shoppingAndGoblins

Ver también: [[shoppingAndGoblins]] · [[stack]] · [[contexto]]

Todo el código vive en un único archivo `libre-run-libreopcion_15.html` (~556 líneas):
`<style>` + markup + un script de assets (base64) + una IIFE con toda la lógica.

## Layout de UI

`#stage` (canvas + overlays CRT/viñeta/HUD + pantallas título/game over) a la izquierda
y `#board` (ranking del día) a la derecha. El canvas se dibuja en resolución física
(`W*DPR × H*DPR`, DPR cap a 2). `GROUND = H * 0.80` es la línea de piso.

## Máquina de estados

`S = { TITLE:0, PLAY:1, OVER:2 }`. `draw()` corre siempre; `update()` solo en PLAY.
- TITLE → PLAY: `start()` (Espacio/tap)
- PLAY → OVER: `gameOver()` (colisión con obstáculo)
- OVER → PLAY: `start()` o `commitScore()`

## Bucle principal

`loop()` con `requestAnimationFrame`. Asume ~60 fps: las constantes físicas están
calibradas por frame, no por delta-time. `update()`: física del jugador (gravedad,
salto/doble salto), spawn por relojes (`spawnClock`/`itemClock`), movimiento y
reciclado de entidades, colisiones, partículas y textos flotantes.

## Spawn

- **Obstáculos** (`spawnObstacle`): paquetes de cartón (a veces apilados) y, con score>160,
  drones rojos voladores (26%). Cadencia `gap = max(50, 94 - score/120)`.
- **Productos** (`spawnItemRun`): tandas de 2–4, 55% en arco senoidal para premiar el salto.

## Colisiones

AABB. La caja del jugador se achica al agacharse (`playerBox()`). El test de productos
es más permisivo (centro ± s/2), se sienten "imanados".

## Render

`draw()` por capas: cielo → estrellas → skyline parallax → horizonte glow → piso en
perspectiva → productos → obstáculos → estela → jugador → partículas → floaters.
Personajes dibujados pixel-a-pixel (`drawGoblin`/`drawGrinch`) + carrito (`drawCart`).

## Persistencia

Wrapper `store` sobre localStorage con fallback en memoria. Claves:
`libreopcion_run_scores` (top 50), `libreopcion_run_prize`, `libreopcion_run_char`.
