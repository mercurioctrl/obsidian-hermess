# Contexto — gigaErp

## Negocio

Sistema interno de gestión para la marca **Gigabyte** (hardware IT).
Usuarios: equipo de marketing/administración de Gigabyte.
Moneda: USD exclusivamente.

## Usuarios

| Email | Pass | Rol | Permisos extra |
|-------|------|-----|----------------|
| \`admin@gigabyte.com\` | \`admin123\` | ADMIN | todos |
| \`maria.gomez@gigabyte.com\` | \`demo1234\` | OPERATIVO | VER_MONTOS |
| \`lucas.herrera@gigabyte.com\` | \`demo1234\` | OPERATIVO | — |

## Distribuidores (Clientes con tipo='distribuidor')

| Nombre | Ciudad | Fondo 2026 | Productos cargados |
|--------|--------|------------|-------------------|
| Elit | Buenos Aires | \$50,000 | — |
| New Bytes | Córdoba | \$40,000 | 206 productos |
| INVID | Mendoza | \$35,000 | 41 productos |
| Air | Rosario | \$30,000 | — |

> Los distribuidores son **Clientes** con \`tipo='distribuidor'\`. No son una entidad separada.
> Elit y Air son clientes de marketing sin catálogo de productos cargado aún.

## Proveedores

| Nombre | Tipo |
|--------|------|
| Blu Studio | Estudio de Marketing |
| Imprenta Gráfica Sur | Imprenta |
| Logística Rápida SA | Logística |
| Tech Events SRL | Organización de Eventos |
| Media Digital Pro | Agencia Digital |

## Catálogo de productos — dos códigos

Cada producto tiene dos códigos separados:

| Campo | Descripción | Ejemplo INVID | Ejemplo NB |
|-------|-------------|---------------|------------|
| \`codigo_distribuidor\` | Código interno del distribuidor | \`0416990\` | \`GP-P550SS\` |
| \`sku\` | Modelo oficial del fabricante (Gigabyte) | \`GP-P550SS\` | \`GP-P550SS\` |

- **INVID**: códigos numéricos propios → SKU buscado en gigabyte.com manualmente
- **New Bytes**: ya usa el SKU real como código → \`sku = codigo_distribuidor\`
- Cuando coincide el SKU entre distribuidores, aparecen en la **misma fila** en Existencias
- SKU es único **por distribuidor** (constraint 0025), no globalmente

## Branding / UI

- **Logo sidebar**: \`aorus_logo_black.svg\` → \`class="h-8 w-auto"\` en \`layouts/default.vue\`
- **Topbar**: texto "Brand ERP" (\`text-sm text-[#9B9B93]\`)
- Logos en \`frontend/public/logos/\`: \`aorus_logo_black.svg\`, \`gigabyte_logo_clean.svg\`

## Reglas de negocio

### Fondo de marketing
- Cada distribuidor tiene fondo asignado por año (puede haber múltiples aportes)
- Acciones de marketing consumen el fondo (\`monto_usd\`)
- Disponible = asignado − consumido (puede ser negativo)

### Tareas / Kanban
- 4 columnas: POR_HACER → EN_CURSO → READY_FOR_QA → LISTO
- Drag & drop HTML5 nativo
- Click en card → modal detalle estilo Jira

### Stock de productos
- Campo \`stock\` directo en tabla \`productos\` — usado por el módulo Productos/Existencias
- Tabla \`stock_deposito\` (modelo \`StockDeposito\`) — usada por \`/mercaderia/stock\`
- Vista \`/mercaderia/stock\` ahora muestra una columna por depósito activo (dinámico)

### Existencias (vista cruzada)
- Agrupa productos por SKU real
- Un producto sin SKU **no aparece** en Existencias
- Todos los distribuidores aparecen como columnas aunque no tengan productos
- \`null\` en una celda = ese distribuidor no vende ese producto
- \`0\` = lo vende pero está sin stock

### Órdenes de Venta
- Entidad nueva: \`OrdenVenta\` (cabecera) + \`ItemOrdenVenta\` (líneas)
- Estados: \`EstadoOrdenVenta\` enum
- Endpoint \`GET /api/ordenes-venta\` paginado
- Listas de precio 1–4 disponibles en productos para uso en órdenes

### Dashboard
- Ingresos = ventas con estado PAGADA
- Gastos = AccionMarketing.monto_usd (gasto de marketing)
- No hay conversión ARS/USD — el sistema opera solo en USD

## Datos demo cargados

| Seeder | Entidad | Cantidad |
|--------|---------|----------|
| DemoSeeder | Productos legacy (stock por depósito) | 12 |
| DemoSeeder | Ventas | 13 (8 PAGADA · 4 PENDIENTE · 1 CANCELADA) |
| DemoSeeder | Tareas | 22 |
| DemoSeeder | Acciones de marketing | 15 |
| ProductoInvidSeeder | Productos Gigabyte INVID | 41 |
| ProductoNewBytesSeeder | Productos Gigabyte New Bytes | 206 |

## Decisiones tomadas

- Distribuidores y clientes son la misma entidad (tabla \`clientes\`, campo \`tipo\`)
- Drag & drop HTML5 nativo en Kanban — sin dependencias externas
- Modal Jira para detalle de tarea — evita página separada
- Export Excel/PDF como stubs 501 — libs ya instaladas para después
- Sistema opera solo en USD — no hay conversión ni cotización
- \`codigo_distribuidor\` separado de \`sku\` para poder manejar distribuidores con codificación propia
- SKUs reales de INVID fueron buscados en gigabyte.com en sesión 2026-05-20
- SKU único por distribuidor (no global) — un mismo SKU puede tenerlo INVID y NB

## TODOs pendientes

- [ ] Agregar SKUs reales a productos de Elit y Air cuando se cargue su catálogo
- [ ] Agregar precio/stock a productos de Elit y Air
- [ ] Export Excel (\`maatwebsite/excel\` instalado, stubs 501)
- [ ] Export PDF ventas (\`barryvdh/laravel-dompdf\` instalado, stubs 501)
- [ ] Asignación de fondo desde panel cliente (hoy solo lectura)
- [ ] Permisos granulares en sidebar (hoy todos ven todo)
- [x] Módulo Productos con filtros, stock, último ingreso
- [x] Módulo Existencias (tabla cruzada SKU × distribuidor)
- [x] Seeders completos registrados para fresh install
- [x] Módulo Órdenes de Venta (cabecera + líneas + estados)
- [x] Stock con columnas dinámicas por depósito en \`/mercaderia/stock\`

## Bugs corregidos (historial)

- \`config:cache\` ya estaba en entrypoint — el síntoma SQLite reaparece si se corre \`optimize:clear\` manual (patrón recurrente: siempre correr \`config:cache\` después)
- \`apiResource('acciones')\` → \`{accione}\` → fix \`.parameters()\`
- \`apiResource('proveedores')\` → \`{proveedore}\` → fix \`.parameters()\`
- \`pages/marketing/[id].vue\` asignaba \`accion.value = a\` sin desenvolver \`{ data: {} }\`
- \`AccionMarketingResource\` no retornaba \`tareas\` en \`toArray\`
- \`->keyBy('estado')\` falla con enum cast → fix: \`->keyBy(fn(\$v) => \$v->estado->value)\`
- Migración 0022 intentaba popular stock antes de que existieran los productos → movido a seeders

## Puerto confirmado

- **gigaErp: 8824** (no 8823 — ese lo usa minisaas-nginx)
- minisaas: 8823 | gigaErp: 8824 | DB: 3310

## Ver también

- [[gigaErp]] · [[arquitectura]] · [[changelog]] · [[memoria]]