# Brother

Proyecto de impresión 3D: **llavero con forma de botellita de tinta Brother** que
dice **PREMIO**, preparado para impresión multicolor.

Ubicación del proyecto: `/var/www/brother`

## Descripción

Se parte del STL original de un llavero (botellita de tinta Brother, placa plana
con detalles grabados) y se genera una versión **multicolor** dividida en piezas
independientes, reemplazando el código "BK" del diseño por **PREMIO**.

## Notas del proyecto

- [[contexto]] — objetivo, decisiones del usuario y qué se intentó
- [[arquitectura]] — enfoque técnico de modelado 3D (trimesh + Blender)
- [[stack]] — herramientas y dependencias
- [[changelog]] — registro de trabajo por fecha
- [[memoria]] — memoria consolidada de Claude

## Entregable

Ensamble de **5 STL separados**: cuerpo, tapa, etiquetas, logo brother, texto PREMIO.
Logo y texto sobresalen 2 mm. Ver [[arquitectura]] para alturas y capas.

Última sincronización: 2026-08-31
