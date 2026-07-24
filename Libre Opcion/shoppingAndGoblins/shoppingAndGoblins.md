# shoppingAndGoblins — LIBRE RUN

Mini-juego *endless runner* (Grinch/Goblin) para [[Libre Opcion]], como activación de marca.
El juego es un único archivo HTML (con una salvedad: usa `music.mp3` externo); el ranking puede
ser local (localStorage) o **compartido** vía un microservicio PHP opcional.

**Repo:** `git@github.com:LibreOpcion/shoppingGoblin.git`
**Working dir:** `/var/www/lo/shoppingGoblin`
**Archivo del juego:** `libre-run-libreopcion_15.html`
**Música:** `music.mp3` (externo, ~28MB, en loop)
**Backend opcional:** `api.php` (PHP + SQLite)
**Última sincronización:** 2026-07-24

## Qué es

Runner infinito estilo el dino de Chrome: el personaje corre con un carrito y junta productos de
computación (10–150 pts). Tres obstáculos: **minas voladoras** (agacharse), **minas de piso** y
**paquetes** (saltar). Música de fondo (`music.mp3`) y toggle de sonido (tecla M / botón 🔊).
Ranking del día + panel de organizador (trabado por contraseña) para configurar el premio. De
fondo hay un **ciclo día/noche** y **cameos random** (pájaros, OVNI, Godzilla, choque de autos, etc.).

## Notas del proyecto

- [[arquitectura|Arquitectura]] — bucle (timestep fijo), estados + guarda anti-reinicio, spawn, colisiones, render, audio, panel organizador, backend, fondo
- [[stack|Stack]] — tecnologías, assets embebidos, música externa y microservicio PHP
- [[changelog|Changelog]] — registro de trabajo por fecha
- [[contexto|Contexto]] — reglas de negocio, obstáculos, decisiones y gotchas
