# Stack — muestra-fravega

## Web
- **HTML + CSS + JS vanilla**, todo inline en cada `.html`. Sin framework, sin build.
- **Canvas 2D API** para la animación (bola / personaje + estela).
- **Google Fonts**: `Rajdhani` (títulos, uppercase) + `Chakra Petch` (etiquetas mono).
  Fallback a fuentes de sistema si no hay red.

## Branding GIGABYTE
- Naranja `#FF6400`, negro `#0a0a0b`, líneas `#26262c`, blanco `#f4f4f5`, grises.
- Motivos: corchetes de esquina naranjas, eyebrow con guion, biseles `clip-path`.
- Tomado de la landing hermana (`Gigabyte/informe-landing`, `landing-ejemplo-ads`).

## Assets
- `character.png` — águila robótica GIGABYTE recortada (transparente). Original:
  `character.jpeg` / `Character_running_on_black_backg…_202608071605.jpeg`.
- `logo-gigabyte.png` — logo GIGABYTE (copiado de `informe-landing/assets`).
- `logo-fravega@3x.png` — logo Frávega **oficial** (color, fondo blanco).
- `logo-fravega-dark.png` — versión procesada para fondo oscuro (swoosh a color + texto
  blanco, transparente).
- `fravega-Logo.svg` — logo Frávega viejo (monocromo, ya no se usa).

## Herramientas de build de assets
- **ImageMagick** (`convert`) para recortes y recoloreo (ver [[arquitectura]]).
- Render/QA con **google-chrome --headless --screenshot** a distintos `--window-size`
  para validar que no se pisen elementos en varias proporciones.

## Parámetros por URL (comunes)
- `?period=` seg/vuelta (velocidad, más bajo = más rápido) · `?path=circle|h`
- `?size=` alto del personaje (% de pantalla) · `?trail=1` estela · `?hue=`
- Teclas del operador: **F** fullscreen · **I** contador de FPS real · **C** modo limpio.

## Ver también
- [[arquitectura]] · [[muestra-fravega]]
