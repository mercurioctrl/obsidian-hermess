# gigaErp

Sistema interno de gestión para la marca **Gigabyte** (distribuidores IT en Argentina/Uruguay).

- **Directorio:** `/var/www/gigabyte/gigaErp/`
- **URL local:** `http://10.10.10.7:8824`
- **Credenciales seed:** `admin@gigabyte.com` / `admin123`
- **Operativos demo:** `maria.gomez@gigabyte.com` / `lucas.herrera@gigabyte.com` (pass: `demo1234`)
- **Repositorio:** `git@github.com:BluIncStudio/gigaErp.git` — rama `main`
- **Última sincronización:** 2026-05-14

## Stack

| Capa | Tecnología |
|------|-----------|
| Frontend | Nuxt 3 SPA + Vue 3 + Tailwind CSS + Pinia |
| Backend | Laravel 11 + PHP 8.4 + Sanctum |
| DB | MySQL 8 (puerto 3310) + Redis 7 |
| Proxy | Nginx → puerto **8824** |
| Deploy | Docker Compose |

## Módulos implementados

- **Dashboard** — 6 KPIs (clientes, ingresos, gastos, resultado, cobrado, deuda) + pixel bar chart 12 meses + resultado del período + ventas por estado
- **Clientes** — CRUD + fondo de marketing por año + detalle
- **Proveedores** — CRUD completo (5 proveedores en demo)
- **Tareas** — Kanban 4 columnas con **drag & drop** + modal detalle estilo Jira
- **Marketing** — Acciones + Campañas + adjuntos
- **Mercadería** — Ventas + Stock por depósito + Depósitos
- **Calendario** — Eventos y fechas comerciales
- **Configuración** — Etiquetas, tipos, estados (solo admin)

## Branding

- Logo sidebar: `aorus_logo_black.svg` (h-8 / 2rem)
- Topbar: "Brand ERP"

## Datos de demo

DemoSeeder cargado (2026-05-14) — 3 meses de operación simulados:
12 productos · 13 ventas · 22 tareas · 15 acciones de marketing · 4 campañas · 12 eventos

## Puertos de la máquina

| Proyecto | Puerto |
|---------|--------|
| gigaErp | **8824** |
| minisaas | 8823 |
| bluMiniErp | 8088 |
| DB gigaErp | 3310 |

## Notas del proyecto

- [[arquitectura]] — Decisiones de diseño, patterns backend/frontend, bug apiResource pluralización, pixel bar chart SVG
- [[stack]] — Tecnologías, versiones, comandos de deploy
- [[changelog]] — Historial de construcción sesión a sesión
- [[contexto]] — Reglas de negocio, branding, datos demo, TODOs
- [[memoria]] — Convenciones críticas, endpoints, troubleshooting, debugging checklist
