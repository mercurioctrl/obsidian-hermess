# stack

Herramientas usadas para generar los modelos 3D. Todo corre en Linux, sin CAD.

## Generación (Python 3)
- **OpenCV 5.0** — findContours, morfología, fillPoly, connectedComponents, dibujo de palmeras.
- **trimesh 4.11** — `extrude_polygon`, concatenate, repair, export STL. (Requiere `networkx` para exportar 3MF, pero ese exportador se descartó.)
- **shapely 2.1** — Polygon con huecos, `unary_union`, `buffer(±0.02)` para regularizar.
- **numpy** — cuantización de color por distancia (¡usar `int32`, no `int16` — 245² desborda!).
- **Pillow** — render de texto con fuente TTF.

## Fuentes
- **Noto Sans Bold** (`/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf`) — texto de prueba en el posavasos v1. No hay emoji monocromo de palmera → las palmeras se dibujan a mano.
- El lettering "ADATA PARADISE" definitivo se extrae de la **máscara del logo original** (`mask_white.png`), no de una fuente.

## Impresión
- **Bambu Studio 2.5.0.66** — instalado como **Flatpak** (`com.bambulab.BambuStudio`). Permisos: `filesystems=home;/media;/run/media;...` → **solo lee dentro de `home`**.
- **Impresora: Bambu Lab A1 mini + AMS lite** — cama 180×180 mm. AMS lite = **4 filamentos automáticos**; más de 4 → pausas manuales + torre de purga.
- Filamento: PLA.

## Formatos
- **3MF** core-spec escrito a mano (objects + build items + basematerials). Es el entregable principal.
- **STL** por color como respaldo (importar como partes en Bambu).

## Ver también
[[arquitectura]] · [[contexto]] · [[adata-paradise-3d]]
