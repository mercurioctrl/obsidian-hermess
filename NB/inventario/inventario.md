# inventario

Sistema de inventario de NB. Monorepo con frontend SPA y backend API REST.

**Última sincronización:** 2026-07-13

> **Estado:** **utilidades negativas** en Precios y en el *ctrl precios* de Stock (`MAY1=10 + MAY2=-9` ⇒ MAY = 1%; `LO1=5 + LO2=-10` ⇒ LO = -5%, bajo costo a propósito). La **utilidad mínima** dejó de bloquear: ahora es un modal de confirmación + `force=true`. Ramas `feature/utilidad-negativa` en ambos repos (front `03f23d7`, back `aa13999`), **pusheadas, PRs sin abrir**. Antes (2026-07-08): pull de `development`/`Development` con historial de costos/precios, y ajuste manual que crea la fila de stock inexistente (rama sin PR). Ver [[changelog]], [[modulo-precios#Utilidades negativas (2026-07-13)]] y [[contexto#Reglas de negocio relevantes]].

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
