# inventario

Sistema de inventario de NB. Monorepo con frontend SPA y backend API REST.

**Última sincronización:** 2026-07-08

> **Estado:** ambos repos en `development`/`Development`, actualizados por pull — entró **historial de costos/precios** (front PR #390, back PR #289/#290; columna **PCAM**, dockerización del back). En rama de feature sin PR: **ajuste manual crea la fila de stock** cuando no existe (`manualAdjustments`, en vez de 404). Trabajo local sobre `development`; DB local en `10.10.10.47,1433` (usuario `cmercurio`). Ver [[changelog]], [[modulo-regularizacion#Ajuste manual de nstock_d1 (manualAdjustments)]] y [[modulo-precios]].

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
