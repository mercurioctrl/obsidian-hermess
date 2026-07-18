# Contexto — shoppingAndGoblins

Ver también: [[shoppingAndGoblins]] · [[arquitectura]] · [[stack]]

## Propósito

Activación de marca para [[Libre Opcion]] (stands, ferias, web). El jugador junta
productos de computación reales del catálogo; al perder deja su nombre en el ranking
del día, con un premio configurable por el organizador (botón ⚙).

## Productos y puntaje

15 productos, puntos según valor real: Placa de video 150, Procesador 120, Celular 100,
Mother 90, RAM 70, Fuente 60, SSD 50, Placa de red 45, Auriculares 40, Parlantes 35,
Cooler 30, Webcam 25, Teclado 20, Mouse 15, Mousepad 10.

## Decisiones de la sesión (2026-07-17)

- **La velocidad no debe depender del hardware.** El bug era físico por-frame + rAF (rápido en
  monitores de alto refresco). Se resolvió con timestep fijo. Ver [[arquitectura#Bucle principal — timestep fijo]].
- **La dificultad se ató al tiempo, no al puntaje**, porque juntar productos inflaba el score y
  disparaba velocidad/obstáculos de golpe. Arranque +5% (`baseSpeed` 6 → 6.3).
- **Ranking compartido con anti-trampa pragmático.** Se asumió explícitamente que un juego
  client-side **no puede ser 100% a prueba de trampas**; el objetivo es subir la barrera para un
  stand/feria, no blindaje total. Nivel elegido: sesión de un solo uso + validación puntaje/tiempo
  + rate-limit. (Descartado: re-simular la partida en el server, demasiado trabajo.)
- **Backend standalone** (no dentro de la API Laravel del monorepo): microservicio PHP + SQLite
  al lado del juego, fácil de deployar en el server del stand.
- **Cameos de fondo pedidos como "cosas locas random que no te esperás"** — incluyen Godzilla
  arrasando la ciudad y un choque de autos; todos cosméticos (no afectan la jugabilidad).

## Gotcha — "ranking del día" no resetea por fecha

La UI dice "RANKING DEL DÍA" pero **no hay reseteo por fecha**: los puntajes persisten (local o
en el server) hasta que el organizador use "Reiniciar ranking". Para un reset diario real habría
que filtrar/limpiar por `t` (timestamp) al cargar.

## ⚠️ Pendiente antes de producción

- **Definir `LIBRERUN_ADMIN_KEY`** en el server: sigue con el placeholder `CAMBIAME-antes-de-usar`.
  Esa clave protege el reset del ranking y el guardado del premio.

## Próximos pasos posibles

- Botón de mute cableado a UI (la variable `muted` ya existe, sin control).
- Reset diario automático del ranking (filtrando por `t`).
- Fix opcional pendiente: la densidad de obstáculos ya usa `frame`; si se quisiera, revisar timing
  fino de los cameos (frecuencia en `bgClock`) y proporciones del Godzilla/choque tras verlos.
- Actualizar en el `README.md` la referencia vieja al remote `BluIncStudio/miniJuegos-shoppingAndGoblins`.
