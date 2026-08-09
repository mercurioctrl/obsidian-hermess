# Arquitectura — muestra-fravega

Cada versión es **un solo `.html`** con CSS y JS inline. Sin build, sin servidor, sin
dependencias (solo Google Fonts opcionales). Render sobre **Canvas 2D**.

## El corazón: un test de refresh rate *honesto* (no simulado)

La idea es que la diferencia 200Hz vs 60Hz la produzca el **hardware**, no un truco:

1. **Movimiento por tiempo real** — la posición se calcula con `performance.now()`
   (`posAt(t)`), así la **velocidad real es idéntica** en cualquier monitor.
2. **`requestAnimationFrame` sin throttle** — el navegador pinta al ritmo del **refresh
   físico** del monitor (200Hz → 200 pinturas/seg; 60Hz → 60).
3. **Se registra 1 posición por frame** en la estela → a 200Hz los sellos quedan densos
   (estela fluida/continua), a 60Hz separados (estela "a saltos").

> Requisito clave: el monitor de 200Hz debe estar **configurado a 200Hz en el SO** y Chrome
> en **pantalla completa**. Si vsync/GPU fuerza 60, ambos se ven iguales. Ver [[contexto]].

## Decisiones de diseño (aprendizajes de la sesión)

- **La estela con glow difuso disimulaba el salto** → se pasó a **objeto sólido de borde
  nítido** (bola con contorno blanco). Lo que más delata el 60Hz es **seguir el objeto con
  la vista** (smooth pursuit): ahí el de 60 "trepida" y el de 200 se ve limpio.
- **Velocidad**: se subió (period ~1.7s/vuelta) porque a más velocidad, más obvia la
  diferencia. Modo horizontal (`?path=h`) es aún más sensible (estilo testUFO).
- **Órbita elíptica acotada** (en `gemini-code`): los límites verticales se calculan
  dejando margen para el **título** (arriba), el **footer** (abajo) **y el alto del propio
  personaje**, para que no se superpongan en **ninguna proporción** de pantalla. La órbita
  es más ancha que alta (elipse), centro y radios derivados de `W/H` y `CHAR_H`.
- **Personaje orientado hacia donde corre**: se voltea con `ctx.scale(-1,1)` según el signo
  de la velocidad horizontal (`faceLeft`).

## Detalles de canvas

- `resize()` fija el backing store a `getBoundingClientRect()*dpr` (dpr cap 2) → nítido.
- Blend `lighter` solo para la estela; el personaje va en `source-over` (usa PNG con alpha).
- En **`index.html`**: lienzo de diseño fijo **1512×1000** escalado con `transform: scale`
  para llenar cualquier pantalla; el quiz asigna **aleatoriamente** qué monitor es 200/60,
  la animación refleja esa verdad y **CONFIRMAR** revela aciertos (verde/rojo).

## Procesamiento de assets (ImageMagick)

- **Personaje** (`character.png`): recorte del fondo negro con **floodfill desde los bordes**
  (`-draw "matte 0,0 floodfill"`), para conservar las **líneas negras internas** del dibujo.
- **Logo Frávega** (`logo-fravega-dark.png`): del oficial `logo-fravega@3x.png` se saca el
  fondo blanco (`-transparent white`) y se **recolorea el texto negro a blanco**
  (`-fuzz 18% -fill white -opaque black`) **sin tocar el swoosh** violeta/magenta.

## Ver también

- [[stack]] · [[contexto]] · [[muestra-fravega]]
