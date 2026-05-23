# gigaErp

Sistema interno de gestión para la marca **Gigabyte** (distribuidores IT en Argentina/Uruguay).

- **Directorio:** `/Users/hermess/www/gigaErp/`
- **URL local:** `http://localhost:8824`
- **Credenciales seed:** `admin@gigabyte.com` / `admin123`
- **Operativos demo:** `maria.gomez@gigabyte.com` / `lucas.herrera@gigabyte.com` (pass: `demo1234`)
- **Repositorio:** `git@github.com:BluIncStudio/gigaErp.git` — rama `main`
- **Última sincronización:** 2026-05-23

## Stack

| Capa | Tecnología |
|------|-----------|
| Frontend | Nuxt 3 SPA + Vue 3 + Tailwind CSS + Pinia |
| Backend | Laravel 11 + PHP 8.4 + Sanctum |
| DB | MySQL 8 (puerto host 3310) + Redis 7 |
| Proxy | Nginx → puerto **8824** |
| Deploy | Docker Compose |

## Módulos implementados

- **Dashboard** — 6 KPIs + pixel bar chart 12 meses + resultado del período + ventas por estado
- **Distribuidores** — CRUD + fondo de marketing por año + detalle (ex-Clientes)
- **Proveedores** — CRUD completo
- **Tareas** — Kanban 4 columnas con drag & drop + modal detalle estilo Jira
- **Marketing** — Acciones + Campañas + adjuntos
- **Mercadería** — Ventas + Stock dinámico por depósito + Depósitos
- **Productos** — Catálogo con grid/lista, filtros, ficha con 4 listas de precio editables → [[modulos/productos]]
- **Existencias** — Tabla cruzada SKU × distribuidor con stock por fuente
- **Órdenes de Venta** — Pipeline Orden → Invoice; selector con 4 listas + depósito → [[modulos/ordenes-venta]]
- **Invoice Preview** — HTML preview estilo Blu con descarga PDF cliente-side, compartible por token → [[modulos/invoice-preview]]

## Notas del proyecto

### Cheatsheet y troubleshooting
- [[troubleshooting]] — catálogo de gotchas recurrentes con causa y fix
- [[stack]] — versiones exactas de dependencias

### Arquitectura
- [[arquitectura]] — estructura, patrones de controllers/resources, rutas, frontend
- [[design-system]] — paleta, tipografía, layout, botones
- [[componentes-ui]] — Modal, DataTable, FormField, StatusBadge, StatsCard

### Módulos de negocio
- [[modulos/productos]] — catálogo, 4 listas de precio, SKU per-distribuidor
- [[modulos/ordenes-venta]] — pipeline BORRADOR → FACTURADA
- [[modulos/invoice-preview]] — preview HTML + PDF html2pdf

### Contexto y memoria
- [[contexto]] — reglas de negocio, decisiones, TODOs
- [[memoria]] — memoria consolidada de Claude para este proyecto
- [[changelog]] — historial por fecha

## Ver también

- [[../Gigabyte]] — carpeta padre (Gigabyte)
