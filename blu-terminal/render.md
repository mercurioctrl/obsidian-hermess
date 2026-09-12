# Renders y planos

Ilustraciones vectoriales (SVG→PNG) del concepto [[blu-terminal]]. No son fotos ni 3D
fotorrealista. Archivos en `/var/www/blu-terminal/render/` (cada `.png` tiene su `.html`
editable; se re-renderiza con Chrome headless a 2×).

## Set del concepto Droid (camino [[flashear-droid4-postmarketos|flashear]])
- **`blu-terminal-hero.png`** (2400×1800) — product-shot estilo Motorola Droid: slider
  apaisado, cuerpo metálico, `neofetch` de postmarketOS/Droid 4, teclado 5 filas
  retroiluminado, **cruceta dorada** (guiño al [[modelos-droid|A855]]). Cuerpos superpuestos.
- `blu-terminal-droid.png` — versión previa (cerrado + abierto). `blu-terminal-mockup.png` —
  primer boceto vertical (descartado).

## Set del build DIY (camino [[caminos|construir]], piezas verificadas)
- **`blu-terminal-build.png`** (2800×2000) — ficha técnica con callouts: HyperPixel 4.0
  (68% del ancho), Pi Zero 2 W + PiSugar en rayos-X detrás de la pantalla, pogo pins en la
  junta, teclado Bobricius táctil + flechas, cuerpo PETG, BOM al pie. Ver [[bom-construccion]].
- **`blu-terminal-planos.png`** (3600×2680) — lámina de **planos con cotas en mm**, 7
  vistas: frente cerrado/abierto, laterales, canto, posterior (rayos-X LiPo/PowerBoost) y
  **sección A-A** de grosores. Verde = verificada, ámbar `*` = derivada. Versión **slim
  ~24 mm**; `blu-terminal-planos-v1-34mm.png` es la v1 de 34. Ver [[grosor-y-medidas]].
- **`blu-terminal-iso.png`** (3600×2600) — **vistas 3D isométricas** desde 4 ángulos
  (frente-izq cerrado/abierto, atrás-der con puertos, desde abajo con tornillos y batería).
  Mini motor 3D en SVG (rotación, caras ocultas, sombreado). Slim; `-v1-34mm.png` la v1.

## Detalles del concepto representado
- El hero usa cruceta dorada (estético); el Droid 4 real usa teclas de flecha, y el build
  usa T invertida en el PCB ([[grosor-y-medidas]]).
- El build muestra la pantalla al 68% del ancho porque es el techo con Zero 2 W
  ([[pantallas-wide]]).

## Ver también
- [[blu-terminal]] · [[modelos-droid]] · [[caminos]] · [[bom-construccion]]
