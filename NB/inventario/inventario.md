# inventario

Sistema de inventario de NB. Monorepo con frontend SPA y backend API REST.

**Última sincronización:** 2026-06-29

> **Estado:** toda la tanda (modal de **seriales**, cache de competencia, **índices P1–P3** en prod —grilla de Stock −67%—, word-break global, fix N+1 en selldiscount, mejoras de grilla) **commiteada y pusheada a `regularizacion-stock`** (back `7f67d7b..bf2c8d1`, front `653c025..481be0f`). Lista para PR a Development/Gamma. Ver [[changelog]], [[modulo-seriales]] y [[performance-indices]].

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
