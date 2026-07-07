---
tipo: changelog
proyecto: LibreOpción
area: Gestión / Datos
creado: 2026-07-01
tags:
  - libreopcion
  - changelog
---

# Changelog — Gestión X

Registro de trabajo por fecha. Detalle de arquitectura en [[arquitectura]] y decisiones en [[contexto]].

## 2026-07-01

- **feat: pipeline de combos/PCs armables** — `gen-combos-match.py` cruza los kits y PCs de [[09 - Estudio de Catálogo - Compra Gamer|Compra Gamer]] contra el catálogo de la distribuidora (`items/catalogoDistribuidoraJulio.csv`) y genera [[combos-armables]]: **31 combos** (CPU+Mother, GPU+Fuente, Gabinete+Fuente, +variante con RAM) y **15 PCs armadas** (oficina → gamer tope), cada uno con SKU y costo. Hallazgo: **hueco de gama media AM5**.
- **feat: catálogo de arranque en la landing** — [[Plan-Estrategico-LibreOpcion-Marca.html|landing Marca]]: secciones desplegables "Qué combos/PCs armaría para arrancar ya" con las tablas y SKUs.
- **feat: pipeline de ventas + proyección de compra** — se bajaron ene–jun 2026 del reporte Saftel (`benefits-report.php`) → `items/ventas-por-sku-2026.csv`. `gen-ventas-forecast.py` → `ventas-data.js` → [[Ventas-y-Proyeccion-LibreOpcion.html|dashboard Ventas & Proyección]]: navegable mes a mes + **proyección de compra 6 meses adelante** (jul–dic, ≈u$s 1,04M) + tabla agrupada por marca.
- **feat: dashboard linkeado desde la landing** — nav + tarjeta destacada en la sección Datos (igual que el cubo).
- **style: emojis planos** — los 3 HTML (Marca, Cubo, Ventas) pasan a **Noto Emoji** (plano monocromo, toma el color del texto) para verse igual en cualquier dispositivo.
- **docs:** se crearon [[arquitectura]], [[contexto]] y [[memoria]]; se actualizó el `CLAUDE.md` con los pipelines nuevos.

Archivos principales: `gen-combos-match.py`, `gen-ventas-forecast.py`, `combos-armables.md`, `ventas-data.js`, `Ventas-y-Proyeccion-LibreOpcion.html`, `Plan-Estrategico-LibreOpcion-Marca.html`.

## Ver también
- [[arquitectura]] · [[contexto]] · [[memoria]] · [[00 - Índice Gestión X]]
