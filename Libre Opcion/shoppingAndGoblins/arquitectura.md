# Arquitectura — shoppingAndGoblins

Ver también: [[shoppingAndGoblins]] · [[stack]] · [[contexto]]

Todo el código del juego vive en un único archivo `libre-run-libreopcion_15.html`:
`<style>` + markup + un script de assets (base64) + una IIFE con toda la lógica.
El ranking compartido (opcional) vive en `api.php` (PHP + SQLite), desplegado al lado del HTML.
La música es un archivo externo `music.mp3` (ver [[stack]] y [[contexto]]).

## Layout de UI

`#stage` (canvas + overlays CRT/viñeta/HUD + pantallas título/game over + botón de sonido) a la
izquierda y `#board` (ranking del día) a la derecha. El canvas se dibuja en resolución física
(`W*DPR × H*DPR`, DPR cap a 2). `GROUND = H * 0.80` es la línea de piso.

## Máquina de estados

`S = { TITLE:0, PLAY:1, OVER:2 }`. `draw()` corre siempre; `update()` solo en PLAY.
- TITLE → PLAY: `start()` (Espacio/tap) — arranca la música (`startMusic()`).
- PLAY → OVER: `gameOver()` (colisión con obstáculo) — corta la música (`stopMusic()`).
- OVER → PLAY: `start()` o `commitScore()`.

**Guarda anti-reinicio (`overGuard`):** tras `gameOver()` se setea `overGuard = now + 500ms`.
Durante esa ventana, tanto el teclado (Espacio/↑/W) como el táctil (`pointerdown`) **ignoran** el
reinicio, y el input de nombre se enfoca de inmediato. Esto evita la condición de carrera por la
que, al spamear salto, la tecla que seguía al choque reiniciaba el juego **sin mostrar la pantalla
de guardar puntaje** (antes el foco del input llegaba con 60ms de retraso).

## Bucle principal — timestep fijo

Las constantes físicas están calibradas **por frame a 60fps**. Para que la velocidad no
dependa del monitor/GPU (en 120/144/165Hz el juego corría 2–3× más rápido), `loop()` usa
un **timestep fijo con acumulador** (`STEP=1000/60`): `update()` corre ~60×/seg en cualquier
pantalla y `draw()` en cada frame. Clamp `dt>250` evita el salto tras un lag / pestaña en 2º plano.

`update()`: física del jugador (gravedad, salto/doble salto), spawn por relojes, movimiento y
reciclado de entidades, colisiones, partículas, floaters y cameos de fondo.

## Dificultad ligada al tiempo, no al puntaje

Para que juntar productos (que inflan el score) no dispare la dificultad, la rampa se ató a
`frame` (tiempo) en vez de `score`:
- **Velocidad:** `speed = baseSpeed + min(9, frame/700)`, `baseSpeed = 6.3`.
- **Cadencia de obstáculos:** `gap = max(50, 94 - frame/120)`.
- **Umbral de minas voladoras:** aparecen con `frame > 160`.

## Spawn

- **Obstáculos** (`spawnObstacle`), 3 tipos elegidos por `Math.random()`:
  - **Mina voladora** (`fly:true`, ~24% con `frame>160`): dron rojo alto, se **agacha** por debajo.
  - **Mina de piso** (`mine:true`, ~26%): apoyada en el suelo (`GROUND-h`, h=20), se **salta**.
  - **Paquete** de cartón (resto, a veces apilado): se **salta**.
- **Productos** (`spawnItemRun`): tandas de 2–4, 55% en arco senoidal para premiar el salto.

## Colisiones

AABB. La caja del jugador se achica al agacharse (`playerBox()`). El test de productos
es más permisivo (centro ± s/2), se sienten "imanados". Los cameos de fondo NO colisionan.

## Render

`draw()` por capas: cielo (día/noche) → estrellas → sol/luna → skyline parallax → cameos →
horizonte glow → piso en perspectiva → productos → obstáculos → estela → jugador →
partículas → floaters. Personajes pixel-a-pixel (`drawGoblin`/`drawGrinch`) + carrito (`drawCart`).

Obstáculos: `drawBox` (paquete de cartón), `drawMine` (mina roja de piso: cuerpo redondeado con
`roundRect` + 3 púas + luz amarilla parpadeante) y el dron rojo volador (rects rojos con `flap`).

### Ciclo día/noche

Atado a la distancia (`cyc = dist/DAYCYCLE`, `DAYCYCLE=12000` ≈ 30s por ciclo al arrancar).
El cielo interpola paletas noche→día (`SKY_N`/`SKY_D`) con tinte crepuscular naranja (`DUSK`);
las estrellas se apagan de día; `drawCelestial` dibuja el **sol** o la **luna** en arco, por
detrás del skyline.

### Cameos random de fondo

Sistema `bgFx`/`spawnBgFx`/`drawBgFx`: eventos cosméticos que cruzan el cielo cada ~4–14s
(`bgClock`), sin colisión. 18 tipos (`BGFX`): bird, flock, ufo, shootingstar, balloon, plane
(banner), superhero, parachute, dragon, rocket, nyancat, blimp, fireworks, ptero, cloud, rain,
godzilla, carcrash. Los tipos con estado propio (godzilla — ciudad en llamas + aliento atómico;
carcrash — debris + humo + "CRASH"; rain; rocket) tienen ramas dedicadas en el loop de `update()`.

## Audio

- **Efectos** (`beep`, `sJump`, `sGet`, `sCrash`): sintetizados en runtime con osciladores (Web Audio).
- **Música de fondo:** `music.mp3` externo, reproducido en **loop** con un `Audio` (`startMusic`/
  `stopMusic`), volumen 0.5. Arranca en `start()` y se corta en `gameOver()`.
- **Mute:** variable `muted` (silencia efectos + música). Toggle con tecla **M** y botón `#sndBtn`
  (`🔊/🔇`) en el stage (`toggleMute`).

## Panel de organizador (trabado por contraseña)

El botón ⚙ (`#cfgBtn`) abre el panel solo si se ingresa la contraseña correcta (`ADMIN_PIN`,
constante en el HTML). La clave ingresada se guarda en `adminKey` y se **reutiliza** para las
acciones contra el server (guardar premio, reiniciar ranking) sin volver a pedirla. Es un candado
**client-side**; `ADMIN_PIN` debe coincidir con `LIBRERUN_ADMIN_KEY`/`$ADMIN_KEY` de `api.php`,
que es donde está la validación real (`hash_equals` con `X-Admin-Key`).

## Persistencia y ranking compartido

Wrapper `store` sobre localStorage con fallback en memoria. Claves: `libreopcion_run_scores`
(top 50, fallback local), `libreopcion_run_prize` (fallback local), `libreopcion_run_char`.

Con `api.php` desplegado, el ranking y el premio son **compartidos** (SQLite del server); el
cliente (`API_BASE`, `apiStart/apiTop/apiSubmit`, `refreshBoard`, `refreshPrize`) usa el server
si responde y **cae a localStorage** si no hay red. Endpoints: `start`, `submit`, `top`, `prize`,
`setprize`, `reset`. Anti-trampa **pragmático** (juego client-side, no infalible): sesión de un
solo uso, validación puntaje/tiempo, rate-limit por IP, saneo de nombre server-side. El reset del
ranking y el guardado del premio piden `X-Admin-Key` (== env `LIBRERUN_ADMIN_KEY`).
