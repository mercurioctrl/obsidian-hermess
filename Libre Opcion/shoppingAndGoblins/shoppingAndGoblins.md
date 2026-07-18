# shoppingAndGoblins — LIBRE RUN

Mini-juego *endless runner* (Grinch/Goblin) para [[Libre Opcion]], como activación de marca.
El juego es un único archivo HTML sin dependencias; el ranking puede ser local (localStorage)
o **compartido** vía un microservicio PHP opcional.

**Repo:** `git@github.com:LibreOpcion/shoppingGoblin.git`
**Working dir:** `/var/www/lo/shoppingGoblin`
**Archivo del juego:** `libre-run-libreopcion_15.html`
**Backend opcional:** `api.php` (PHP + SQLite)
**Última sincronización:** 2026-07-18

## Qué es

Runner infinito estilo el dino de Chrome: el personaje corre con un carrito, salta
paquetes de cartón y drones rojos, y junta productos de computación (10–150 pts).
Ranking del día + panel de organizador para configurar el premio. De fondo hay un
**ciclo día/noche** y **cameos random** (pájaros, OVNI, Godzilla, choque de autos, etc.).

## Notas del proyecto

- [[arquitectura|Arquitectura]] — bucle (timestep fijo), estados, spawn, colisiones, render, backend, fondo
- [[stack|Stack]] — tecnologías, assets embebidos y microservicio PHP
- [[changelog|Changelog]] — registro de trabajo por fecha
- [[contexto|Contexto]] — reglas de negocio, decisiones y gotchas
