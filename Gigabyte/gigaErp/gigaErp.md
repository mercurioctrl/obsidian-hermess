# gigaErp

ERP interno para la marca **Gigabyte** (hardware IT). Gestiona distribuidores, stock, órdenes de venta, cuenta corriente y documentos comerciales.

**Stack:** Laravel 11 + Nuxt 3 SPA + MySQL 8 + Docker · Puerto `8824`
**Último commit:** `320a645` · **Última sincronización:** 2026-06-17
**En desarrollo (working tree):** guía interactiva / tour de onboarding por sección — ver [[changelog#2026-06-17 — Guía interactiva]]

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
- [[modulos/productos]] — sync partpicker + carga masiva de catálogo GIGABYTE, 4 listas de precio
- [[modulos/resellers]] — resellers live desde partpicker, sin importar a DB

---

## Estado actual (2026-06-11) — commit `d08b3a4`

### Módulos implementados

| Módulo | Estado | Notas |
|--------|--------|-------|
| Dashboard | ✅ | 6 KPIs + pixel chart + tareas + calendario + OV + deudores + productos por distri |
| Distribuidores / Cuenta corriente | ✅ | Movimientos, saldo, línea de crédito con historial |
| Notas de crédito | ✅ | Desde CC (libre) y desde orden FACTURADA (parciales/totales) |
| Órdenes de Venta | ✅ | BORRADOR → APROBADA → FACTURADA, permisos granulares |
| Invoice (PDF + preview) | ✅ | html2pdf.js, preview pública por token |
| Stock Bodega | ✅ | Depósitos (+ flag Stock Ilimitado, mig 0041), importaciones XLSX, columnas por depósito, filtro Todos/Con/Sin stock |
| Catálogo (carga masiva) | ✅ | Carga base GIGABYTE (item_no, bu_code, chipset, carton...), upsert por item_no, pestaña editar |
| Stock Distri | ✅ | Tabla cruzada SKU × distribuidor, filtro marca default GIGABYTE |
| APIs Distri | ✅ | Sync real desde partpicker (Air/Ceven/Invid/Stylus), vincular-skus, filtro GIGABYTE |
| Resellers | ✅ | Live desde partpicker, 37 tiendas PreciosGamer, filtro GIGABYTE |
| Fondos de Marketing | ✅ | Asignación por distribuidor y año |
| Tareas (Kanban) | ✅ | 4 columnas, drag & drop, modal detalle |
| Calendario | ✅ | Eventos y fechas comerciales |
| Configuración | ✅ | Datos empresa + CRUD usuarios con permisos |
| Buscador global | ✅ | Topbar ⌘K — busca clientes, productos, OV, proveedores, tareas |
| Guía interactiva | ✅ | Tour paso a paso por sección (botón Ayuda + auto-inicio 1ª vez), motor propio — *working tree* |

### Sidebar

```
Principal:    Dashboard · Distribuidores · Proveedores
Operaciones:  Stock Bodega · Stock Distri · APIs Distri · Resellers · Órdenes de Venta
Marketing:    Fondos · Calendario · Tareas
Admin:        Configuración (solo admin)
```

> Inventario (Stock Bodega) tiene 4 pestañas: **Stock · Catálogo · Depósitos · Subir Masivo**.

### Distribuidores en DB

| id | Nombre | Origen |
|----|--------|--------|
| 1 | Elit | seeder demo |
| 2 | New Bytes | seeder demo + sync partpicker |
| 3 | Invid | seeder demo + sync partpicker |
| 4 | Air | seeder demo + sync partpicker |
| 5 | Ceven | creado al primer sync |
| 6 | Stylus | creado al primer sync |

> El catálogo GIGABYTE se carga **sin distribuidor** (`distribuidor_id=null`, `marca=GIGABYTE`).

### Volumen en DB (post-sync partpicker)

| Entidad | Cantidad |
|---------|---------|
| Órdenes de venta | 22 |
| Ventas / Invoices | 34 |
| Productos (demo+seeders) | ~259 base |
| Productos (post-sync) | +miles (Air ~8k, Invid ~1.2k, Ceven ~466, Stylus ~908) |
| Migraciones | 0001–0041 |

### Usuarios demo

| Email | Rol | Permisos |
|-------|-----|----------|
| `admin@gigabyte.com` / `admin123` | ADMIN | todos |
| `carolina.lagos@gigabyte.com` / `demo1234` | OPERATIVO | aprobaciones + VER_MONTOS |
| `martin.fierro@gigabyte.com` / `demo1234` | OPERATIVO | VER_MONTOS |
| `julia.mendez@gigabyte.com` / `demo1234` | OPERATIVO | — |

---

## Ver también

- [[changelog]] — últimos: depósito stock ilimitado + reglas catálogo/stock propio (2026-06-16) · carga masiva catálogo GIGABYTE (d08b3a4)
- [[arquitectura]] — SincronizarApiController, ResellersController, ImportacionCatalogoController
- [[contexto]] — reglas de negocio y TODOs pendientes
