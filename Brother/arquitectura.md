# Arquitectura

Enfoque técnico para editar/generar los STL del llavero.

## Ensamble en capas (5 objetos)

Cada pieza es un STL independiente, alineado en coordenadas para que al importarlas
juntas se ensamblen solas. El color se asigna en el slicer.

| # | Objeto | Archivo | Z (mm) | Color |
|---|--------|---------|--------|-------|
| 1 | Cuerpo | `llavero premio - cuerpo (blanco).stl` | 0 – 2.0 | blanco |
| 2 | Tapa | `llavero premio - tapa (azul).stl` | 0 – 2.0 | azul Brother |
| 3 | Etiquetas | `llavero premio - etiquetas (blanco).stl` | 2.0 – 2.8 | blanco |
| 4 | Logo brother | `llavero premio - logo brother (negro).stl` | 2.8 – 4.8 | negro |
| 5 | Texto PREMIO | `llavero premio - texto PREMIO (negro).stl` | 2.8 – 4.8 | negro |

- **Cuerpo y tapa** salen de partir la silueta real del original a la altura del
  cuello (Y = 17 mm).
- **Logo y texto** sobresalen 2 mm (Z 2.8 → 4.8).

## Pipeline (script `build_multicolor.py`)

1. Cargar el STL original y extraer la **silueta desde la cara inferior (Z=0)** con
   `shapely` (unión de triángulos proyectados). El original no es estanco, por eso
   se reconstruye limpio en vez de editar la malla directamente.
2. Partir la silueta en cuerpo/tapa con intersecciones de medios planos (`box`).
3. Definir etiquetas como rectángulos redondeados, recortadas a la silueta.
4. Generar **texto** con `matplotlib.textpath.TextPath` y **logo** parseando el SVG
   con `svgpathtools`; ambos con relleno **par-impar** para respetar huecos de
   letras y el símbolo ®.
5. Extruir cada región (`trimesh.creation.extrude_polygon`) a su altura de capa.

## Lecciones (qué funciona en este entorno)

- **Blender booleans headless FALLAN** (solver EXACT rompe la malla). Usar
  **trimesh + manifold3d** para geometría robusta.
- **Verificación con render Blender headless**: materiales por **nodos**
  (Principled BSDF → Base Color); `diffuse_color` NO afecta el render EEVEE.
  Motor = `BLENDER_EEVEE`. Export = `bpy.ops.wm.stl_export`.

## Ver también

- [[stack]] · [[contexto]] · [[Brother]]
