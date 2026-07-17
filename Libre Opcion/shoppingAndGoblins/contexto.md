# Contexto — shoppingAndGoblins

Ver también: [[shoppingAndGoblins]] · [[arquitectura]]

## Propósito

Activación de marca para [[Libre Opcion]] (stands, ferias, web). El jugador junta
productos de computación reales del catálogo; al perder deja su nombre en el ranking
del día, con un premio configurable por el organizador (botón ⚙).

## Productos y puntaje

15 productos, puntos según valor real: Placa de video 150, Procesador 120, Celular 100,
Mother 90, RAM 70, Fuente 60, SSD 50, Placa de red 45, Auriculares 40, Parlantes 35,
Cooler 30, Webcam 25, Teclado 20, Mouse 15, Mousepad 10.

## Gotcha — "ranking del día" no resetea por fecha

La UI dice "RANKING DEL DÍA" y las claves son `..._run_scores`, pero **no hay lógica de
reseteo por fecha**: los puntajes persisten hasta que el organizador use "Reiniciar
ranking". Para un reset diario real habría que filtrar/limpiar por `t` (timestamp) al
cargar los scores.

## Próximos pasos posibles

- Botón de mute cableado a UI (la variable `muted` ya existe, sin control).
- Backend de ranking (reemplazar `loadScores`/`saveScores` por API) si se quiere ranking global.
- Reset diario automático del ranking.
