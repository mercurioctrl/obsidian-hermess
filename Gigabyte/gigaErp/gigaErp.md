# gigaErp

Sistema interno de gestión para la marca **Gigabyte** (hardware IT).
Distribuye productos a mayoristas (Elit, New Bytes, INVID, Air) en Argentina.

**Stack:** Laravel 11 + PHP 8.4 · Nuxt 3 SPA · MySQL 8 · Redis 7 · Nginx · Docker
**Puerto:** 8824 · **Login dev:** admin@gigabyte.com / admin123

*Última sincronización: 2026-05-26*

---

## Notas de este proyecto

- [[arquitectura]] — estructura, patrones, permisos, flujo de estados de órdenes
- [[stack]] — tecnologías, dependencias, servicios
- [[design-system]] — paleta, tipografía, layout, botones, cards
- [[componentes-ui]] — Modal, DataTable, FormField, StatusBadge, StatsCard
- [[contexto]] — reglas de negocio, distribuidores, usuarios, TODOs
- [[troubleshooting]] — gotchas recurrentes (sanctum, nginx, optimize:clear, html2canvas)
- [[changelog]] — historial de trabajo por fecha
- [[memoria]] — patrones, gotchas, workflow — leer antes de cada sesión

## Módulos

- [[modulos/ordenes-venta]] — pipeline BORRADOR → APROBADA → FACTURADA, permisos, ítems, depósito
- [[modulos/invoice-preview]] — preview HTML estilo Blu + html2pdf.js + shareable token
- [[modulos/productos]] — 4 listas de precio, SKU per-distribuidor, importaciones XLSX

## Estado actual (2026-05-26)

| Módulo | Estado |
|--------|--------|
| Dashboard | ✅ KPIs + pixel bar chart |
| Distribuidores | ✅ listado con saldo cc + cuenta corriente |
| Cuenta corriente | ✅ movimientos, saldo acumulado |
| Stock Bodega | ✅ tabs + buscador + filtro + importaciones XLSX |
| Stock Distri | ✅ tabla cruzada SKU × distribuidor |
| APIs Distri | ✅ catálogo con filtros y stock |
| Órdenes de Venta | ✅ BORRADOR → APROBADA → FACTURADA + validación stock |
| Gestión usuarios | ✅ CRUD + permisos configurables desde UI |
| Fondo Marketing | ✅ lectura (ingreso pendiente desde UI) |
| Tareas / Kanban | ✅ drag & drop + modal detalle |
