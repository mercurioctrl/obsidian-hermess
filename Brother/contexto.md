# Contexto

## Objetivo

Modificar el llavero `llavero final negro brother.stl` (botellita de tinta Brother)
para que diga **PREMIO** e imprimirse **multicolor**.

## Decisiones del usuario (acordadas en sesión)

- **No** crear una botella 3D nueva: editar el **llavero plano existente**.
- El logo de Brother debe salir del **SVG** (`Brother_logo.svg`), no de una
  tipografía común.
- Texto **PREMIO** en mayúscula, con relieve de **2 mm**.
- Esquema de color: cuerpo blanco, letras negras.
- Separar el diseño en **cuerpo / tapa / etiquetas / texto** (4+ objetos).
- **Reemplazar el "BK"** (código de color de tinta del original) por **PREMIO**.

## Hallazgo clave

El STL original ya traía **grabado** todo el diseño (silueta, tapa con estrías,
etiqueta superior con logo *brother*, etiqueta inferior con "BK"), como surcos de
~1 mm sobre una placa plana. El logo que se había agregado encima era redundante.
A partir de ahí se reconstruyó como ensamble en capas separables por color.

## Qué se intentó y NO funcionó

- Modelar una botella 3D nueva desde cero → no era lo que el usuario quería
  (malinterpretación inicial).
- **Blender booleans en headless** → fallan (destruyen la malla). Se migró a
  trimesh + manifold3d. Ver [[arquitectura]].

## Ver también

- [[Brother]] · [[arquitectura]] · [[changelog]]
