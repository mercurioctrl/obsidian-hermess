# gigaErp

ERP interno para la marca **Gigabyte** (hardware IT). Gestiona distribuidores, stock, órdenes de venta, cuenta corriente y documentos comerciales.

**Stack:** Laravel 11 + Nuxt 3 SPA + MySQL 8 + Docker · Puerto `8824`
**Rama activa:** **`Development`** (integración/deploy; con D mayúscula, `main` quedó atrás)
**Último commit:** `57afd7e` · **Última sincronización:** 2026-08-14
**Último trabajo:** **Deploy del release de colaboración** (6 commits, migs `0061–0091`) desplegado en caliente por Claude. Entra un bloque grande de trabajo del dev: **Tareas 2.0** (subtareas, comentarios con menciones, adjuntos S3, enlaces, seguidores, relaciones, historial de estados), **Solicitudes** (piden convertirse en Tarea, aprobación por email firmado), **Minutas**, **Notificaciones** in-app + email + **push FCM**, y la **fusión Proyectos→Campañas**. Ver [[modulos/tareas]], [[modulos/solicitudes]], [[modulos/minutas]], [[modulos/notificaciones]], [[modulos/campanas]] y [[changelog#2026-08-14 — Deploy release colaboración (Tareas 2.0, Solicitudes, Minutas, Notificaciones+Push, Campañas)|changelog]]. Detalle del deploy (nueva dep PHP `kreait/laravel-firebase`, vendor vía `composer:2`) en [[memoria#Deploy de dependencia PHP nueva sin rebuild|memoria]] y [[troubleshooting]].

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

- [[modulos/clientes]] — clientes distribuidor/reseller, sección Contactos, importación por bloques
- [[modulos/ordenes-venta]] — pipeline Orden → Aprobación → Invoice → Nota de crédito
- [[modulos/invoice-preview]] — preview Blu-style + html2pdf client-side
- [[modulos/productos]] — sync partpicker + carga masiva de catálogo GIGABYTE, 4 listas de precio
- [[modulos/resellers]] — resellers live desde partpicker, sin importar a DB
- [[modulos/addons]] — lanzadores a apps externas (url + token) que abren en pestaña nueva
- [[modulos/contenido]] — repositorio de material de marca en S3 (bucket privado + URLs firmadas), vista pública con branding
- [[modulos/ploteos]] — branding físico de resellers (ploteos/vinilos) con mapa geolocalizado (Leaflet + Nominatim) e importación por Excel
- [[modulos/envios]] — campañas de mailing (proxy a `envios.to-aor.us`, solo lectura) con filtro Real/Test prefiltrado en Real
- [[modulos/google-ads]] — reportes de Google Ads (API REST + GAQL, nativo Laravel) navegables entre fechas; cuentas Gigabyte AR/UY/CL bajo MCC; métricas de negocio (compras/monto goal-aware)
- [[modulos/meta-ads]] — reportes de Meta Ads (Facebook/Instagram, Graph API) espejo de Google Ads; System User token; action_type canónico anti-duplicación; suma Alcance/Frecuencia/ROAS nativos
- [[modulos/tareas]] — **Tareas 2.0**: Kanban + subtareas, comentarios con menciones, adjuntos S3, enlaces, seguidores, relaciones, historial de estados, número correlativo (migs 0064–0091)
- [[modulos/solicitudes]] — cola de pedidos que se convierten en Tarea; aprobar/rechazar desde el ERP o por **email con link firmado** sin login (mig 0077)
- [[modulos/minutas]] — actas de reunión con puntos tipo checklist (reordenar/toggle) (migs 0087–0089)
- [[modulos/notificaciones]] — centro in-app + email + **push FCM** (kreait/laravel-firebase); motor `TareaNotificador`; scheduler de deadlines 09:00 ART (migs 0079–0080)
- [[modulos/campanas]] — fusión Proyectos→**Campañas**: campaña comercial opcional sobre un proyecto, con tipos configurables y líneas de cliente + presupuesto (migs 0061–0065, 0090)

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
Principal:    Dashboard · Distribuidores · Contactos · Proveedores
Operaciones:  Stock Bodega · Stock Distri · APIs Distri · Resellers · Órdenes de Venta · Notas de Crédito
Marketing:    Fondos · Campañas · Mapa de Ploteos · Calendario · Tareas · Solicitudes · Addons · Minutas · Envíos · Google Ads · Meta Ads
Admin:        Configuración (solo admin)
```
> Cambios 2026-08: "Proyectos" → **Campañas** (`/marketing/campanas`, key legacy `VER_SECCION_PROYECTOS`) · nuevas **Solicitudes** y **Minutas** · **Contenido** pasó a `oculto` (accesible por URL/permiso, no en sidebar). Ver [[modulos/campanas]], [[modulos/solicitudes]], [[modulos/minutas]].

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
| Migraciones | 0001–0091 (release colaboración 0061–0091, ver [[changelog#2026-08-14 — Deploy release colaboración (Tareas 2.0, Solicitudes, Minutas, Notificaciones+Push, Campañas)|changelog]]) |

### Usuarios demo

| Email | Rol | Permisos |
|-------|-----|----------|
| `admin@gigabyte.com` / `admin123` | ADMIN | todos |
| `carolina.lagos@gigabyte.com` / `demo1234` | OPERATIVO | aprobaciones + VER_MONTOS |
| `martin.fierro@gigabyte.com` / `demo1234` | OPERATIVO | VER_MONTOS |
| `julia.mendez@gigabyte.com` / `demo1234` | OPERATIVO | — |

---

## Ver también

- [[changelog]] — últimos: [[modulos/envios|Envíos]] (proxy campañas de mailing, filtro Real/Test) — 2026-07-28 · [[modulos/ploteos|Ploteos]] con mapa + estados de proyecto configurables — 2026-07-27 · Clientes distribuidor/reseller + Contactos — 2026-07-23
- [[arquitectura]] — SincronizarApiController, ResellersController, ImportacionCatalogoController
- [[contexto]] — reglas de negocio y TODOs pendientes
