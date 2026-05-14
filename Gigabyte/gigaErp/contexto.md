# Contexto — gigaErp

## Negocio

Sistema interno de gestión para la marca **Gigabyte** (hardware IT).
Usuarios: equipo de marketing/administración de Gigabyte.
Moneda: USD exclusivamente.

## Usuarios

| Email | Pass | Rol | Permisos extra |
|-------|------|-----|----------------|
| `admin@gigabyte.com` | `admin123` | ADMIN | todos |
| `maria.gomez@gigabyte.com` | `demo1234` | OPERATIVO | VER_MONTOS |
| `lucas.herrera@gigabyte.com` | `demo1234` | OPERATIVO | — |

## Distribuidores

| Nombre | Ciudad | Fondo 2026 | Contacto |
|--------|--------|------------|---------|
| Elit | Buenos Aires | $50,000 | Martín Sosa |
| New Bytes | Córdoba | $40,000 | Carla Méndez |
| Invid | Mendoza | $35,000 | Pablo Ríos |
| Air | Rosario | $30,000 | Valentina Cruz |

## Proveedores

| Nombre | Tipo |
|--------|------|
| Blu Studio | Estudio de Marketing |
| Imprenta Gráfica Sur | Imprenta |
| Logística Rápida SA | Logística |
| Tech Events SRL | Organización de Eventos |
| Media Digital Pro | Agencia Digital |

## Branding / UI

- **Logo sidebar**: `aorus_logo_black.svg` → `class="h-8 w-auto"` en `layouts/default.vue`
- **Topbar**: texto "Brand ERP" (`text-sm text-[#9B9B93]`)
- Logos en `frontend/public/logos/`: `aorus_logo_black.svg`, `gigabyte_logo_clean.svg`

## Reglas de negocio

### Fondo de marketing
- Cada distribuidor tiene fondo asignado por año (puede haber múltiples aportes)
- Acciones de marketing consumen el fondo (`monto_usd`)
- Disponible = asignado − consumido (puede ser negativo)

### Tareas / Kanban
- 4 columnas: POR_HACER → EN_CURSO → READY_FOR_QA → LISTO
- Drag & drop HTML5 nativo
- Click en card → modal detalle estilo Jira

### Stock
- Administrado por depósito (Argentina / Uruguay), no global
- Ajuste setea cantidad absoluta (no incremental)

### Dashboard
- Ingresos = ventas con estado PAGADA
- Gastos = AccionMarketing.monto_usd (gasto de marketing)
- No hay conversión ARS/USD — el sistema opera solo en USD

## Datos de demo cargados (2026-05-14)

DemoSeeder — simula 3 meses de operación (Feb–May 2026):

| Entidad | Cantidad |
|---------|----------|
| Productos | 12 (Notebooks, Monitores, Componentes, Periféricos) |
| Ventas | 13 (8 PAGADA · 4 PENDIENTE · 1 CANCELADA) |
| Tareas | 22 (11 LISTO · 5 EN_CURSO · 2 READY_FOR_QA · 4 POR_HACER) |
| Acciones de marketing | 15 (7 Finalizadas · 4 En curso · 1 Planificada · 1 Pausada · 1 Cancelada) |
| Campañas | 4 (una por distribuidor) |
| Eventos calendario | 12 |

## Decisiones tomadas

- Distribuidores y clientes son la misma entidad (tabla `clientes`)
- Drag & drop HTML5 nativo en Kanban — sin dependencias externas
- Modal Jira para detalle de tarea — evita página separada
- Export Excel/PDF como stubs 501 — libs ya instaladas para después
- Sistema opera solo en USD — no hay conversión ni cotización

## TODOs pendientes

- [ ] Export Excel (`maatwebsite/excel` instalado, stubs 501)
- [ ] Export PDF ventas (`barryvdh/laravel-dompdf` instalado, stubs 501)
- [ ] Página detalle + formulario nueva venta con items dinámicos
- [ ] Asignación de fondo desde panel cliente (hoy solo lectura)
- [ ] Permisos granulares en sidebar (hoy todos ven todo)
- [x] Repositorio: `git@github.com:BluIncStudio/gigaErp.git` — rama `main`
- [ ] Backups de DB

## Bugs corregidos

- `config:cache` ya estaba en entrypoint — el síntoma SQLite reaparece si se corre `optimize:clear` manual
- `apiResource('acciones')` → `{accione}` → fix `.parameters()`
- `apiResource('proveedores')` → `{proveedore}` → fix `.parameters()`
- `pages/marketing/[id].vue` asignaba `accion.value = a` sin desenvolver `{ data: {} }`
- `AccionMarketingResource` no retornaba `tareas` en `toArray`
- `->keyBy('estado')` falla con enum cast → fix: `->keyBy(fn($v) => $v->estado->value)`

## Puerto confirmado

- **gigaErp: 8824** (no 8823 — ese lo usa minisaas-nginx)
- minisaas: 8823 | gigaErp: 8824 | DB: 3310

## Ver también

- [[gigaErp]] · [[arquitectura]] · [[changelog]] · [[memoria]]
