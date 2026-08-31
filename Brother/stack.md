# Stack

Herramientas usadas para el modelado/edición de STL.

## Entorno

- **Blender 5.2** (headless, `blender --background --python`) — solo para render de
  verificación. NO usar sus booleans (fallan en headless).
- **Python 3.12** con:
  - `trimesh` — geometría de mallas, extrude/revolve, IO STL
  - `manifold3d` — backend de booleans robusto para trimesh
    (`pip install --break-system-packages manifold3d`)
  - `shapely` — polígonos 2D, siluetas, intersecciones
  - `matplotlib` — contornos de fuente (`textpath.TextPath`) para el texto
  - `svgpathtools` — parseo de paths del SVG del logo

## Assets del proyecto

- `llavero final negro brother.stl` — modelo original (no se modifica)
- `Brother_logo.svg` — logo vectorial de Brother
- `build_multicolor.py` — script que genera las 5 piezas
- `README.md` — documentación del proyecto
- `multi_top.png` / `multi_34.png` — renders de vista previa

## Ver también

- [[arquitectura]] · [[Brother]]
