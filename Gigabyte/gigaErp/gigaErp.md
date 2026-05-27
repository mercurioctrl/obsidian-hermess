# gigaErp

ERP interno para la marca **Gigabyte** (hardware IT). Gestiona distribuidores, stock, órdenes de venta, cuenta corriente y documentos comerciales.

**Stack:** Laravel 11 + Nuxt 3 SPA + MySQL 8 + Docker · Puerto `8824`
**Última sincronización:** 2026-05-27

---

## Notas del proyecto

- [[arquitectura]] — modelos, rutas, patrones frontend/backend, deploy
- [[contexto]] — reglas de negocio, usuarios, distribuidores, TODOs
- [[changelog]] — historial de cambios por fecha
- [[memoria]] — gotchas, workflow, patrones recurrentes
- [[stack]] — dependencias y versiones
- [[design-system]] — paleta, tipografía, layout, botones
- [[componentes-ui]] — Modal, DataTable, FormField, StatusBadge
- [[troubleshooting]] — errores conocidos y fixes

### Módulos

- [[modulos/ordenes-venta]] — pipeline Orden → Aprobación → Invoice → Nota de crédito
- [[modulos/invoice-preview]] — preview Blu-style + html2pdf client-side
- [[modulos/productos]] — 4 listas de precio + SKU per-distribuidor

---

## Estado actual (2026-05-27)

### Módulos implementados

| Módulo | Estado | Notas |
|--------|--------|-------|
| Distribuidores / Cuenta corriente | ✅ | Movimientos, saldo, línea de crédito con historial |
| Notas de crédito | ✅ | Desde CC (texto libre) y desde orden FACTURADA (parciales) |
| Órdenes de Venta | ✅ | BORRADOR → APROBADA → FACTURADA, permisos |
| Invoice (PDF + preview) | ✅ | html2pdf.js, preview pública por token |
| Stock Bodega | ✅ | Depósitos, importaciones XLSX, filtros |
| Stock Distri / APIs Distri | ✅ | Catálogo por distribuidor |
| Fondos de Marketing | ✅ | Asignación por distribuidor y año |
| Tareas (Kanban) | ✅ | 4 columnas, drag & drop, modal detalle |
| Configuración | ✅ | Datos empresa + CRUD usuarios con permisos |

### Migraciones

`0001–0033` — la última agrega `notas_credito` + `notas_credito_items` + FK `nota_credito_id` en `movimientos_cuenta`.

### Usuarios demo

| Email | Rol | Permisos |
|-------|-----|----------|
| `admin@gigabyte.com` / `admin123` | ADMIN | todos |
| `carolina.lagos@gigabyte.com` / `demo1234` | OPERATIVO | aprobaciones + VER_MONTOS |
| `martin.fierro@gigabyte.com` / `demo1234` | OPERATIVO | VER_MONTOS |
| `julia.mendez@gigabyte.com` / `demo1234` | OPERATIVO | — |
