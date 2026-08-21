# inventario

Sistema de inventario de NB. Monorepo con frontend SPA y backend API REST.

**Última sincronización: 2026-08-21

> **Estado (2026-08-04):** sesión de fixes de grilla + **performance de Stock**. Backend mergeado a Development: **#309** (NC en modal seriales), **#310** (delta ignora NC no-toca-stock), **#312/#315** (globalAlter resuelve depósito / warehouseStockId opcional). Performance con PRs **abiertos**: **#319** (cache materializado de seriales `serial_counts`, grilla 500 filas ~19s→~9s; SP+Agent job cada 5 min ya en prod) y **#320** (connection pool por thread + MARS). Front: **#406** (globalAlter precarga Cantidad, mergeado), **#408** (rename "NC Pos."→"Cambios", abierto), **#411** (Ctrl de precios de Stock igual a Precios, abierto). Además **correcciones de datos en prod**: albprol/stock faltantes de la OC 13309 y restauración de costo+precios de la OC 13373. Ver [[changelog#2026-08-04 — Fixes de grilla/datos, performance de Stock, y correcciones de OC en prod|changelog]], [[performance-indices#2026-08-04 — Cache materializado de seriales + connection pool|performance]] y [[contexto#Correcciones de datos en producción (2026-08-04)|contexto]].

## Sub-proyectos

| Proyecto | Tecnología | Directorio |
|----------|-----------|------------|
| inventario-web-app | Nuxt.js 2 / Vue 2 | `inventario-web-app/app/` |
| ms-metadata | FastAPI (Python) | `ms-metadata/` |

## Notas

- [[arquitectura]] — Arquitectura del sistema y decisiones de diseño
- [[modulo-precios]] — Sección Precios: edición bidireccional + competencia (BluPartPicker)
- [[modulo-regularizacion]] — Regularización de stock: delta documental, restauración albprol/albclil, Acción 1 (Control), cc11 no serializa
- [[modulo-seriales]] — Modal de seriales por artículo: estado, documentos (factura/NC/pedido), Cambio RMA, compra, export
- [[performance-indices]] — Índices P1–P3 (DMV real), por qué el refactor con IN se revirtió, fix N+1 selldiscount
- [[regularizacion-buckets]] — clasificación de deltas cc4: auto-cerrables (lógica) vs a recontar (físico) vs revisar/granel
- [[competencia-partpicker-cache]] — Cache de competencia (backend 30min SWR + cache local en Precios)
- [[stack]] — Tecnologías, versiones y dependencias
- [[changelog]] — Historial de cambios recientes
- [[contexto]] — Entorno local, variables de entorno y gotchas
- [[memoria]] — Memoria de sesiones de Claude Code

## Ver también

- [[NB]] — Proyecto padre en NB
- [[Compras]] · [[pedidos]] · [[expedicion]] · [[sincroAfip]]
- [[BluPartPicker]] — API de precios de competencia que consume la sección Precios
