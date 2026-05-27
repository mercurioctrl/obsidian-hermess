# gigaErp

Sistema interno de gestión para la marca **Gigabyte** (distribuidores IT en Argentina/Uruguay).

- **Directorio:** `/var/www/gigabyte/gigaErp/`
- **URL local:** `http://localhost:8824`
- **Credenciales seed:** `admin@gigabyte.com` / `admin123`
- **Operativos demo:** `maria.gomez@gigabyte.com` / `lucas.herrera@gigabyte.com` (pass: `demo1234`)
- **Última sincronización:** 2026-05-26

## Stack

| Capa | Tecnología |
|------|-----------|
| Frontend | Nuxt 3 SPA + Vue 3 + Tailwind CSS + Pinia |
| Backend | Laravel 11 + PHP 8.4 + Sanctum |
| DB | MySQL 8 (puerto host 3310) + Redis 7 |
| Proxy | Nginx → puerto **8824** |
| Deploy | Docker Compose (6 servicios) |

## Navegación (sidebar)

```
Principal:    Dashboard · Distribuidores · Proveedores
Operaciones:  Stock Bodega · Stock Distri · APIs Distri · Órdenes de Venta
Marketing:    Fondo · Calendario · Tareas
Admin:        Configuración
```

## Módulos implementados

- **Dashboard** — 6 KPIs + pixel bar chart 12 meses
- **Distribuidores** — CRUD + fondo de marketing + cuenta corriente (saldo, movimientos)
- **Proveedores** — CRUD completo
- **Tareas** — Kanban 4 columnas drag & drop + modal detalle
- **Fondo/Marketing** — Acciones + Campañas + adjuntos
- **Stock Bodega** — Stock dinámico por depósito + Depósitos + Subir Masivo (importación XLSX)
- **Stock Distri** (`/existencias`) — Tabla cruzada SKU × distribuidor
- **APIs Distri** (`/productos`) — Catálogo con 4 listas de precio, filtros, ficha
- **Órdenes de Venta** — Pipeline Orden → Invoice; selector con depósito → [[modulos/ordenes-venta]]
- **Invoice** — HTML preview compartible por token + PDF descargable → [[modulos/invoice-preview]]
- **Cuenta Corriente** — movimientos debe/haber por distribuidor, saldo acumulado corriente

## Notas del proyecto

### Cheatsheet y troubleshooting
- [[troubleshooting]] — catálogo de gotchas recurrentes con causa y fix
- [[stack]] — versiones exactas de dependencias

### Arquitectura
- [[arquitectura]] — estructura, patrones de controllers/resources, rutas, módulos, decisiones
- [[design-system]] — paleta, tipografía, layout, botones
- [[componentes-ui]] — Modal, DataTable, FormField, StatusBadge, StatsCard

### Módulos de negocio
- [[modulos/productos]] — catálogo, 4 listas de precio, SKU per-distribuidor
- [[modulos/ordenes-venta]] — pipeline BORRADOR → FACTURADA
- [[modulos/invoice-preview]] — preview HTML + PDF html2pdf

### Contexto y memoria
- [[contexto]] — reglas de negocio, decisiones, TODOs, nomenclatura UI
- [[memoria]] — memoria consolidada de Claude para este proyecto
- [[changelog]] — historial detallado por fecha

## Ver también

- [[../Gigabyte]] — carpeta padre
