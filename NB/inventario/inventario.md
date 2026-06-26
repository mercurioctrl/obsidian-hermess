# inventario

Sistema de inventario de NB. Monorepo con frontend SPA y backend API REST.

**Última sincronización:** 2026-06-26

> **Estado:** regularización de stock + documental (scripts en `ms-metadata`, sin commit). Hecho en prod (agente Catriel): **170 items** de stock realineados a seriales (gap serial↔columnas) y **88 líneas de `albclil.ACREDITADO`** corregidas (772 u de crédito fantasma) cruzando la NC real de `FP_FactWebCli` (NTIPODOCU=2). Caveat: el enlace NC es incompleto → solo `ACREDITADO>ncanent` es corregible con confianza. Ver [[modulo-regularizacion]], [[changelog]] y [[memoria]].

## Sub-proyectos

| Proyecto | Tecnología | Directorio |
|----------|-----------|------------|
| inventario-web-app | Nuxt.js 2 / Vue 2 | `inventario-web-app/app/` |
| ms-metadata | FastAPI (Python) | `ms-metadata/` |

## Notas

- [[arquitectura]] — Arquitectura del sistema y decisiones de diseño
- [[modulo-precios]] — Sección Precios: edición bidireccional + competencia (BluPartPicker)
- [[modulo-regularizacion]] — Regularización de stock: delta documental, restauración albprol/albclil, Acción 1 (Control), cc11 no serializa
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
