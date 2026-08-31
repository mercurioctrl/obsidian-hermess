# Memoria

Memoria de Claude para el proyecto Brother, consolidada.

## Proyecto

- Adaptar el llavero botellita de tinta Brother para que diga **PREMIO**, imprimible
  **multicolor**. Entregable: 5 STL separados (cuerpo, tapa, etiquetas, logo,
  texto), generados por `build_multicolor.py`. Ver [[arquitectura]].
- Decisiones acordadas: separar en cuerpo/tapa/etiquetas/texto; reemplazar "BK" por
  PREMIO; logo desde el SVG; texto en mayúscula, relieve 2 mm; cuerpo blanco,
  letras negras. Ver [[contexto]].

## Referencia (flujo técnico validado)

- **Blender booleans headless fallan** → usar **trimesh + manifold3d**.
- Texto con `matplotlib.TextPath`; logo con `svgpathtools`; relleno par-impar para
  huecos. Silueta extraída de la cara inferior (Z=0) del STL original (no estanco).
- Render de verificación: materiales por **nodos** (Base Color), motor
  `BLENDER_EEVEE`, export `bpy.ops.wm.stl_export`.
- El usuario quería **editar el llavero existente**, no modelar de cero. Confirmar
  el objetivo antes de modelar.

## Ver también

- [[Brother]] · [[arquitectura]] · [[stack]]
