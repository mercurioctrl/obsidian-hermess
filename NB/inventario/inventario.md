# inventario

Sistema de inventario de NB. Monorepo con frontend SPA y backend API REST.

**Última sincronización: 2026-09-15

> **Estado (2026-09-15):** sesión de lectura (sin cambios de código): se documentó el flujo de
> **transferencias entre depósitos** en [[modulo-transferencias-stock]]. Mergeado desde la sync anterior:
> **portal público de certificados eléctricos** (INV-370, back #341 / front #460 — rutas `/public/...` sin
> auth, página `certificados-electricos.vue` con layout `public` y cliente axios aparte vía `METADATA_HOST`),
> **fix del filtro con/sin stock** que duplicaba items entre ambos filtros (#340: WHERE → HAVING sobre los
> SUM, y el count contaba una fila por almacén: empresa 4 5983 → 4391), **fallback de `ultimaVenta` vía
> `albclil`** cuando `articulo.ULTIMA_VENTA` es NULL (SNB-4143, #344) y **videos de YouTube en productos**
> (SNB-3866/3867: limpiar video persiste `videoId=null`, soporte de Shorts). Ver [[changelog#2026-09-15 — Sync: portal público de certificados, fix filtro con/sin stock, videos de YouTube|changelog]].
>
> **Estado anterior (2026-08-26):** feature **APA/Soportes** completa (4 fases, [[modulo-apa]]) y **depósito
> en Precios** (filtro + preselección del predeterminado, PRs #333/#334).

## Sub-proyectos

| Proyecto | Tecnología | Directorio |
|----------|-----------|------------|
| inventario-web-app | Nuxt.js 2 / Vue 2 | `inventario-web-app/app/` |
| ms-metadata | FastAPI (Python) | `ms-metadata/` |

## Notas

- [[arquitectura]] — Arquitectura del sistema y decisiones de diseño
- [[modulo-precios]] — Sección Precios: edición bidireccional + competencia (BluPartPicker)
- [[modulo-apa]] — APA/Soportes (AMD Price Adjustment): baja temporal del costo, cron, columna en Precios
- [[modulo-regularizacion]] — Regularización de stock: delta documental, restauración albprol/albclil, Acción 1 (Control), cc11 no serializa
- [[modulo-transferencias-stock]] — Movimientos de stock: transferencia entre depósitos, mover entre columnas, ajuste manual
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
