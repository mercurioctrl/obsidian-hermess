# gigaErp

ERP interno para la marca **Gigabyte** (hardware IT). Gestiona distribuidores, stock, órdenes de venta, cuenta corriente y documentos comerciales.

**Stack:** Laravel 11 + Nuxt 3 SPA + MySQL 8 + Docker · Puerto `8824`
**Último commit:** `db6bf60` · **Última sincronización:** 2026-05-27

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

## Estado actual (2026-05-27) — commit `db6bf60`

### Módulos implementados

| Módulo | Estado | Notas |
|--------|--------|-------|
| Dashboard | ✅ | 6 KPIs + pixel chart + tareas + calendario + OV + deudores + productos por distri |
| Distribuidores / Cuenta corriente | ✅ | Movimientos, saldo, línea de crédito con historial |
| Notas de crédito | ✅ | Desde CC (libre) y desde orden FACTURADA (parciales/totales) |
| Órdenes de Venta | ✅ | BORRADOR → APROBADA → FACTURADA, permisos granulares |
| Invoice (PDF + preview) | ✅ | html2pdf.js, preview pública por token |
| Stock Bodega | ✅ | Depósitos, importaciones XLSX, filtros en card |
| Stock Distri / APIs Distri | ✅ | Catálogo por distribuidor, 4 listas de precio |
| Fondos de Marketing | ✅ | Asignación por distribuidor y año |
| Tareas (Kanban) | ✅ | 4 columnas, drag & drop, modal detalle |
| Calendario | ✅ | Eventos y fechas comerciales |
| Configuración | ✅ | Datos empresa + CRUD usuarios con permisos |

### Dashboard — widgets actuales

```
Row 1-2: 6 KPI cards (Distribuidores, Ingresos, Gastos, Resultado, Cobrado, Deuda)
Row 3:   Pixel bar chart 12 meses (Ingresos vs Gastos)
Row 4:   Tareas por estado  |  Próximos 14 días (calendario)
Row 5:   Últimas 8 OV       |  Cuentas corrientes / top deudores
Row 6:   Resultado período  |  Ventas por estado + Top clientes
Row 7:   Productos por distribuidor (full width)
```

### Endpoint `/api/dashboard` — campos

```json
{ kpis, ventas_por_estado, top_clientes, ultimos_12_meses,
  proximos_eventos, tareas_stats, ultimas_ordenes,
  productos_por_distri, cuentas_corrientes }
```

### Volumen en DB

| Entidad | Cantidad |
|---------|---------|
| Órdenes de venta | 22 (OV-0001 a OV-0022) |
| Ventas / Invoices | 34 (VTA-0001 a VTA-0034) |
| Movimientos cc | ~62 |
| Productos | 259 (12 demo + 41 Invid + 206 New Bytes) |
| Migraciones | 0001–0033 |

### Usuarios demo

| Email | Rol | Permisos |
|-------|-----|----------|
| `admin@gigabyte.com` / `admin123` | ADMIN | todos |
| `carolina.lagos@gigabyte.com` / `demo1234` | OPERATIVO | aprobaciones + VER_MONTOS |
| `martin.fierro@gigabyte.com` / `demo1234` | OPERATIVO | VER_MONTOS |
| `julia.mendez@gigabyte.com` / `demo1234` | OPERATIVO | — |

### Distribuidores

| Nombre | Ciudad | SKUs | Saldo cc | Línea de crédito |
|--------|--------|------|----------|-----------------|
| New Bytes | Córdoba | 206 | a cobrar | $20,000 |
| Invid | Mendoza | 41 | a cobrar | $40,000 |
| Elit | Buenos Aires | — | a cobrar | $30,000 |
| Air | Rosario | — | a cobrar | $12,000 |

---

## Ver también

- [[changelog]] — último cambio: dashboard expandido (db6bf60)
- [[arquitectura]] — estructura completa del código
- [[contexto]] — reglas de negocio y TODOs pendientes
