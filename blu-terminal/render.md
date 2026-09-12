# Render conceptual

Renders vectoriales (SVG→PNG) del concepto [[blu-terminal]], estilo Motorola Droid.
No son fotos ni 3D fotorrealista — son ilustraciones de producto de alta calidad.

## Archivos (en el repo del proyecto)
`/var/www/blu-terminal/render/`
- **`blu-terminal-hero.png`** (2400×1800) — el render principal, alta calidad: slider
  apaisado, cuerpo metálico, pantalla con `neofetch` de postmarketOS/Droid 4, teclado
  retroiluminado de 5 filas y **cruceta dorada** (guiño al [[modelos-droid|Droid A855]]).
  Los dos cuerpos son del mismo tamaño y se superponen (pantalla sobre el cuerpo del
  teclado, que asoma apenas por debajo, como en el Droid abierto).
- `blu-terminal-droid.png` — versión previa (cerrado + abierto, apaisado).
- `blu-terminal-mockup.png` — primer boceto (vertical, descartado).
- `.html` de cada uno — editables (teclado y textos generados por JS/SVG).

## Cómo re-renderizar
Chrome headless a 2×:
`google-chrome --headless --screenshot --force-device-scale-factor=2 --window-size=1200,900 file://.../blu-terminal-hero.html`

## Detalles del concepto representado
- Pantalla apaisada = mismo footprint que el teclado.
- Cruceta dorada a la derecha = flechas físicas (estético; el Droid 4 real usa teclas de
  flecha dedicadas, no d-pad dorado — ver [[modelos-droid]]).
- Corriendo postmarketOS sobre [[flashear-droid4-postmarketos|Droid 4]].

## Ver también
- [[blu-terminal]]
- [[modelos-droid]]
- [[caminos]]
