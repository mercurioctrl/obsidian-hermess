# Changelog — shoppingAndGoblins

Ver también: [[shoppingAndGoblins]]

## 2026-07-14

- Inicialización del repositorio git y primer commit del juego `LIBRE RUN`
  (`libre-run-libreopcion_15.html`).
- Documentación: `README.md` (uso, controles, mecánicas, tabla de productos) y
  `docs/ARQUITECTURA.md` (referencia técnica: bucle, estados, spawn, colisiones, render).
- Push a `git@github.com:BluIncStudio/miniJuegos-shoppingAndGoblins.git` (rama `main`).

## 2026-07-17

- Vinculación con la bóveda de Obsidian (`Libre Opcion/shoppingAndGoblins/`) y creación
  de notas: [[arquitectura]], [[stack]], [[contexto]], [[changelog]].
- **Migración de repo:** nuevo remote `git@github.com:LibreOpcion/shoppingGoblin.git` (rama
  `main`), working dir `/var/www/lo/shoppingGoblin`. Creado `CLAUDE.md` del proyecto.
- **fix(velocidad):** el juego arrancaba/corría demasiado rápido en monitores de alto refresco
  (física por-frame + `requestAnimationFrame` = 2–3× más rápido en 120/144/165Hz). Solución:
  **timestep fijo** en `loop()` (velocidad independiente del hardware). Además, rampa de
  dificultad atada a `frame` (tiempo) en vez de `score`, para que juntar productos no dispare
  la velocidad ni la densidad de obstáculos. `baseSpeed` 6 → 6.3.
- **feat(ranking compartido):** microservicio `api.php` (PHP + SQLite, sin dependencias) con
  ranking común para todos los que juegan en el server. Anti-trampa pragmático (sesión de un
  solo uso, validación puntaje/tiempo, rate-limit por IP, saneo server-side). Cliente con
  fallback automático a localStorage si no hay server. Reset protegido con `LIBRERUN_ADMIN_KEY`.
- **feat(premio compartido):** endpoints `prize`/`setprize` (tabla `meta`); el premio del
  organizador también se comparte vía server (con clave), con fallback local.
- **feat(fondo):** ciclo **día/noche** ligado a la distancia (cielo dinámico, estrellas que se
  apagan, sol y luna en arco por detrás del skyline).
- **feat(fondo):** 18 **cameos random** cosméticos (pájaros, bandada, OVNI, estrella fugaz,
  globo, avión con banner, superhéroe, paracaídas, dragón, cohete, gato-arcoíris, dirigible,
  fuegos artificiales, pterodáctilo, nubes, lluvia, **Godzilla** y **choque de autos**).

Archivos principales: `libre-run-libreopcion_15.html`, `api.php`, `data/.htaccess`,
`README.md`, `docs/ARQUITECTURA.md`, `CLAUDE.md`.

## 2026-07-18

- Sincronización de la bóveda: actualización de [[arquitectura]], [[stack]], [[contexto]] e
  índice con todo lo de la sesión (repo nuevo, timestep fijo, backend PHP, día/noche, cameos).

## 2026-07-21

- **fix(reinicio):** al chocar mientras se spameaba el salto, la siguiente pulsación de
  Espacio/tap caía en la ventana de 60ms previa al foco del input y disparaba `start()`,
  reiniciando **sin mostrar la pantalla de guardar puntaje**. Solución: **guarda de 500ms**
  (`overGuard`) tras `gameOver()` (teclado y táctil) durante la que se ignora el reinicio, y
  foco inmediato del input. Ver [[arquitectura#Máquina de estados]].

## 2026-07-22

- **feat(música):** música de fondo `music.mp3` en **loop** durante la partida (`startMusic`/
  `stopMusic` con un `Audio`), se corta al chocar. Toggle de sonido con tecla **M** y botón
  `🔊/🔇` en pantalla (resuelve el pendiente del control de mute). Primero se probó un motor
  **chiptune** generado en vivo con Web Audio (osciladores, scheduler), reemplazado luego por el
  mp3 a pedido. ⚠️ El mp3 es un **archivo externo** (~28MB), así que el juego **ya no es un único
  archivo portable**: hay que servir `music.mp3` al lado del HTML.
- **feat(obstáculo):** nueva **mina roja en el piso** (`drawMine`, pixel-art con púas y luz
  parpadeante) que hay que **saltar**. Ahora hay 3 obstáculos: minas voladoras (agacharse) ~24%,
  minas de piso (saltar) ~26%, paquetes (saltar) ~50%.
- **feat(seguridad):** **panel de organizador trabado por contraseña** (`ADMIN_PIN`): al abrirlo
  pide clave; si no coincide, no abre. Se pide **una sola vez** y se reutiliza para guardar premio
  / reiniciar ranking en el server (antes pedía la clave server en cada acción). `ADMIN_PIN` debe
  coincidir con `LIBRERUN_ADMIN_KEY`/`$ADMIN_KEY` de `api.php`. El candado es client-side (el
  server sigue siendo la autoridad real vía `X-Admin-Key`).

Archivos principales: `libre-run-libreopcion_15.html`, `music.mp3`, `api.php`.

## 2026-07-24

- Sincronización de la bóveda: actualización de [[arquitectura]], [[stack]], [[contexto]] e
  índice con la sesión (fix de reinicio, música `music.mp3`, minas de piso, panel con contraseña).
