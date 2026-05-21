
# gigaErp.md
# gigaErp

Sistema interno de gestión para la marca **Gigabyte** (distribuidores IT en Argentina/Uruguay).

- **Directorio:** `/var/www/gigabyte/gigaErp/`
- **URL local:** `http://10.10.10.7:8824`
- **Credenciales seed:** `admin@gigabyte.com` / `admin123`
- **Operativos demo:** `maria.gomez@gigabyte.com` / `lucas.herrera@gigabyte.com` (pass: `demo1234`)
- **Repositorio:** `git@github.com:BluIncStudio/gigaErp.git` — rama `main`
- **Última sincronización:** 2026-05-20

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
- **Mercadería** — Ventas + Stock por depósito + Depósitos
- **Productos** — Catálogo con grid/lista, filtros distribuidor/stock, SKU, código dist., foto, precios
- **Existencias** — Tabla cruzada SKU × distribuidor (quién tiene qué y cuánto)
- **Calendario** — Eventos y fechas comerciales
- **Configuración** — Etiquetas, tipos, estados (solo admin)

## Catálogo cargado (2026-05-20)

| Distribuidor | Productos | SKU real |
|-------------|-----------|---------|
| INVID | 41 | ✅ buscados en gigabyte.com |
| New Bytes | 206 | ✅ igual al código |
| Elit | — | pendiente |
| Air | — | pendiente |

## Branding

- Logo sidebar: `aorus_logo_black.svg` (h-8 / 2rem)
- Topbar: "Brand ERP"

## Puertos de la máquina

| Proyecto | Puerto |
|---------|--------|
| gigaErp | **8824** |
| minisaas | 8823 |
| bluMiniErp | 8088 |
| DB gigaErp | 3310 |

## Notas del proyecto

- [[arquitectura]] — Decisiones de diseño, patterns backend/frontend, endpoints Productos y Existencias
- [[stack]] — Tecnologías, versiones, comandos de deploy
- [[changelog]] — Historial de construcción sesión a sesión
- [[contexto]] — Reglas de negocio, distribuidores, catálogo, TODOs
- [[memoria]] — Convenciones críticas, troubleshooting, debugging checklist
