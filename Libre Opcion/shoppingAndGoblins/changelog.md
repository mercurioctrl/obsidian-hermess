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
