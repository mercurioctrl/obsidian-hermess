# Changelog

Historial de cambios del proyecto Compras, basado en los commits de ambos repositorios.

## 2026-03-11

- feat: Despachos temporales y serialización de datos (API)
- Merge de rama `laset-compras-temp-despacho`

## 2026-03-05

- fix: Arreglo en generación de proforma (API)

## 2026-03-04

- feat: Agregar campo `finalPrice` en órdenes (API)
- fix: COM-285 — Revisión de funcionalidad que no andaba correctamente (API)

## 2026-03-03

- fix: Hotfix para query incompleta en stock de warehouse inbound (API)
- fix: Hotfix para inserción con datos incorrectos en tabla de stocks (API)
- fix: Completar columnas faltantes en INSERT de stocks y castear `companyCode` en `ListCategoriesDto` (API)

## 2026-02-24

- refactor: COM-284 — Ajustar visibilidad del selector de depósito cuando la orden está pendiente y no hay `amountEntered` (Frontend)

## 2026-02-02

- refactor: COM-283 — Cambiar "IVA" por "Impuestos" en el listado de órdenes (Frontend)
- refactor: COM-279 — Filtro de `companyCode` en proveedores dentro de crear orden + selector de empresa (Frontend)
- mejora: COM-280 — Agregar logo de empresa para identificación rápida (Frontend)
- refactor: COM-277 — Selector de empresa en alta/edición de proveedores (Frontend)
- refactor: COM-281 — Usuario autenticado homologado (API)
- fix: Cálculo de `taxAmount` en órdenes de proveedor (API)
- refactor: COM-278 — Modificar proveedor incorporando `companyCode` (API)

## 2026-01-29 — 2026-01-30

- fix: Arreglo `companyCode` en autenticación (API)
- fix: Corregir cálculo de `totalFinal` en listado de órdenes (API)
- feat: `companyCode` en patch de proveedor (API)
- refactor: COM-277 — Alta/Edición de proveedores con selector de empresa (Frontend)
- refactor: Logo de empresa al lado del proveedor, mejora de navegación y anchos de tabla (Frontend)
- fix: COM-271 — No agregar productos sin cantidad al hacer ingreso parcial (Frontend)

## 2026-01-26 — 2026-01-27

- fix: Resolución de conflictos gamma → dev (Frontend)
- refactor: COM-201 — Atributo `warehousesId` asociado a órdenes (Frontend)
- refactor: COM-222 — Cambiar posición del buscador en modal de orden de compra (Frontend)
- fix: COM-198 — Eliminar país del detalle de orden mostraba NaN (Frontend)

---

Ver también: [[arquitectura|Arquitectura]] · [[stack|Stack]] · [[Jira/Compras/_COM - Indice|Tickets Jira]]
