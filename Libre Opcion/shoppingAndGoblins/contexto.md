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

## Obstáculos (3 tipos)

- **Minas voladoras** (drones rojos, ~24%): se pasan **agachándose** (↓).
- **Minas de piso** (rojas, `drawMine`, ~26%): se **saltan**.
- **Paquetes** de cartón (~50%): se **saltan**.

Todos usan AABB. Los cameos de fondo (Godzilla, choque, etc.) **no** colisionan.

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

## Decisiones de la sesión (2026-07-21 / 2026-07-22)

- **El choque nunca debe saltarse la pantalla de guardar puntaje.** Había una condición de carrera:
  al spamear salto, la tecla que seguía al choque reiniciaba el juego dentro de la ventana de 60ms
  previa al foco del input. Se resolvió con una **guarda de 500ms** (`overGuard`) tras el game over.
- **Música por archivo, no chiptune.** Se probó primero un motor chiptune 8/16-bit generado en vivo
  (Web Audio), pero el usuario pidió usar `music.mp3`. Se usa un `Audio` externo en loop. Trade-off
  aceptado: **se pierde la portabilidad de "un solo archivo"** (ahora `music.mp3` va al lado del HTML).
- **Las minas también en el piso.** El pedido fue tener minas que obliguen a **saltar** (las
  voladoras obligan a agacharse). Se sumó `drawMine` como tercer obstáculo sin quitar las voladoras.
- **Panel de organizador trabado por contraseña.** El panel se abría libremente; ahora pide
  `ADMIN_PIN`. Es un candado **client-side** (cualquiera que mire el HTML lo ve), a propósito: sirve
  para el stand; la seguridad real de reset/premio sigue en el server (`hash_equals` con `X-Admin-Key`).

## Gotcha — "ranking del día" no resetea por fecha

La UI dice "RANKING DEL DÍA" pero **no hay reseteo por fecha**: los puntajes persisten (local o
en el server) hasta que el organizador use "Reiniciar ranking". Para un reset diario real habría
que filtrar/limpiar por `t` (timestamp) al cargar.

## Gotcha — el juego ya no es un solo archivo

Desde que se usa `music.mp3`, hay que desplegar el HTML **junto con** `music.mp3` (y `api.php` +
`data/` si se quiere ranking compartido). El mp3 pesa ~28MB (quedó commiteado en el repo).

## ⚠️ Pendiente antes de producción

- **Definir la clave de organizador** en los dos lados y que **coincidan**: `ADMIN_PIN` en el HTML
  y `LIBRERUN_ADMIN_KEY` (o `$ADMIN_KEY`) en `api.php`. Ambos siguen con el placeholder
  `CAMBIAME-antes-de-usar`.

## Próximos pasos posibles

- Reset diario automático del ranking (filtrando por `t`).
- Comprimir `music.mp3` (~28MB → ~3-4MB con ffmpeg a 96-128 kbps) o sacarlo del historial de git
  si se prefiere no versionar el binario.
- Actualizar en el `README.md` la referencia vieja al remote `BluIncStudio/miniJuegos-shoppingAndGoblins`
  y las mecánicas nuevas (minas de piso, música, panel con contraseña).
