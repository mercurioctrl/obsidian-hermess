# adata-paradise-3d

Proyecto de **impresión 3D multicolor** del logo **ADATA PARADISE — Brasil 2026** (colibrí + fuegos artificiales) para una **Bambu Lab A1 mini con AMS lite**.

A partir de la imagen original del logo (`ada.jpeg`) se generan varios objetos imprimibles: placa plana multicolor, posavasos redondo, y cartel para maceta. Todo el pipeline es programático (Python + OpenCV + trimesh).

## Stack
Python 3 · OpenCV 5 · trimesh · shapely · Pillow/numpy · Noto Sans Bold · Bambu Studio 2.5 (Flatpak). Impresora: **A1 mini + AMS lite** (4 filamentos automáticos).

## Notas
- [[arquitectura]] — pipeline imagen → modelo 3D multicolor, decisiones y por qué
- [[stack]] — herramientas, versiones y dependencias
- [[changelog]] — historial de piezas generadas por fecha
- [[contexto]] — objetivo, gotchas de Bambu/Flatpak, piezas y medidas

## Piezas generadas
- **Placa plana 4 colores** — logo completo, 170×139,6×2,8 mm (`ADATA_PARADISE.3mf`)
- **Versión encastre A1 mini** (`ADATA_PARADISE_A1_MINI_encastre.3mf`)
- **Posavasos redondo** 95 mm, negro+blanco, con palmeras + logo (`ADATA_POSAVASO.3mf`)
- **Posavasos arcoíris** — palmeras con el degradado del logo, 8 filamentos (`ADATA_POSAVASO_RAINBOW.3mf`)
- **Cartel para maceta** — fondo calado siguiendo las letras + pinche (`ADATA_MACETA.3mf`)

> Archivos entregables copiados a `~/Descargas/adata_3d/` (fuente de trabajo en `/var/www/adata`).

---
Última sincronización: 2026-08-24
