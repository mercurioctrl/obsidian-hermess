# gigaErp

Sistema interno de gestión para la marca **Gigabyte** (distribuidores IT en Argentina/Uruguay).

- **Directorio:** `/var/www/gigabyte/gigaErp/`
- **URL local:** `http://10.10.10.7:8824`
- **Credenciales seed:** `admin@gigabyte.com` / `admin123`
- **Operativos demo:** `maria.gomez@gigabyte.com` / `lucas.herrera@gigabyte.com` (pass: `demo1234`)
- **Repositorio:** `git@github.com:BluIncStudio/gigaErp.git` — rama `main`
- **Última sincronización:** 2026-05-23

## Stack

| Capa | Tecnología |
|------|-----------|
| Frontend | Nuxt 3 SPA + Vue 3 + Tailwind CSS + Pinia |
| Backend | Laravel 11 + PHP 8.4 + Sanctum |
| DB | MySQL 8 (puerto 3310) + Redis 7 |
| Proxy | Nginx → puerto **8824** |
| Deploy | Docker Compose |

## Módulos implementados

- **Dashboard** — 6 KPIs + pixel bar chart 12 meses + resultado del período + ventas por estado
- **Distribuidores** — CRUD + fondo de marketing por año + detalle (ex-Clientes)
- **Proveedores** — CRUD completo
- **Tareas** — Kanban 4 columnas con drag & drop + modal detalle estilo Jira
- **Marketing** — Acciones + Campañas + adjuntos
- **Mercadería** — Ventas + Stock dinámico por depósito + Depósitos
- **Productos** — Catálogo con grid/lista, filtros distribuidor/stock, SKU, código dist., foto, precios
- **Existencias** — Tabla cruzada SKU × distribuidor con stock por fuente
- **Órdenes de Venta** — Listado + Crear/Editar con picker de productos por depósito + Generar Invoice PDF

## Notas del proyecto

- [[arquitectura]] — Decisiones de diseño, endpoints, relaciones, patrones backend/frontend
- [[stack]] — Tecnologías, dependencias, versiones
- [[changelog]] — Historial de cambios por fecha
- [[contexto]] — Reglas de negocio, decisiones de sesión, TODOs
- [[memoria]] — Memoria consolidada de Claude para este proyecto

## Ver también

[[Gigabyte/Gigabyte|Gigabyte]]
