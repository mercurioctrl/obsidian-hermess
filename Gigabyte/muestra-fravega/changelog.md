# Changelog — muestra-fravega

## 2026-08-07

- **Build inicial** del test de fluidez (Canvas 2D): motor de círculo que orbita dejando
  estela, con FPS configurable para comparar 60Hz vs 144Hz.
- **`index.html`** — composición del mockup: dos monitores dibujados (marco + cuello +
  base), títulos, logo Frávega, 3 pasos, tarjeta "¿Cuál es cuál?" **interactiva** (asigna
  200/60 al azar y revela aciertos), "¿Sabías qué?" y footer. Lienzo fijo 1512×1000 escalado.
- **`pura.html`** — versión pura: un solo objeto a pantalla completa para los **dos
  monitores reales**. Movimiento por tiempo real + 1 sello por frame (test honesto, la
  diferencia la hace el hardware). Branding GIGABYTE (naranja/negro, Rajdhani + Chakra Petch,
  corchetes de esquina) + logos GIGABYTE y Frávega. Teclas F/I/C, params por URL.
- **UX**: se quitó la estela con glow (disimulaba el salto) → **bola sólida de borde nítido**;
  velocidad aumentada; instrucción "seguí la bola con la vista".
- **`gemini-code-1786126802527.html`** — variante con **personaje** (águila robótica
  GIGABYTE) que corre y deja la estela naranja. Cutout `character.png` con ImageMagick
  (floodfill desde bordes). El personaje se **voltea según la dirección**.
- Ajustes de layout: **órbita → elipse acotada** (no pisa título/footer/personaje en ninguna
  proporción); título subido; eyebrow unificado y centrado.
- **Logos 1.5×** y cambio al **logo Frávega oficial** (`logo-fravega@3x.png` → procesado a
  `logo-fravega-dark.png`: fondo transparente + texto blanco, swoosh a color).

## 2026-08-09

- Corrección de copy en toda la web: **144Hz → 200Hz** (el otro queda en 60Hz).
- Sincronización inicial con Obsidian (`Gigabyte/muestra-fravega`).
