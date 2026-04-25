# NAEVO

E-commerce de suplementos de bienestar. Stack fullstack en Docker con backend headless y frontend SSR.

- **Repo local:** `/Users/hermess/www/naevo-web/naevo/`
- **Rama activa:** `feature/preview-switcher-tools`
- **URL local:** `http://localhost:8088`
- **Admin:** `admin@naevo.com`

## Stack

Nuxt 3 SSR + Laravel 11 + MySQL 8 + Redis 7 + Nginx, orquestados con Docker Compose (6 servicios). Pagos vía MercadoPago Bricks. Home 100% CMS-driven.

Ver [[stack|Stack y dependencias]] para el detalle.

## Notas del proyecto

- [[naevo/arquitectura|Arquitectura]] — estructura de carpetas, módulos, patrones de datos
- [[naevo/stack|Stack]] — versiones, dependencias, servicios externos
- [[naevo/modulos|Módulos]] — mapa de los 13 módulos del backend/frontend
- [[naevo/templates-preview|Templates & Preview Switcher]] — galería de 28 variantes de home + switcher comparativo para cliente
- [[naevo/changelog|Changelog]] — registro de cambios por fecha
- [[naevo/contexto|Contexto]] — reglas de negocio, decisiones, TODOs pendientes
- [[naevo/memoria|Memoria]] — memoria auto-guardada del proyecto (gotchas, patterns)

## Ver también

- [[Home]] — índice general de la bóveda
- Docs internas del repo: `naevo/docs/architecture.md`, `naevo/docs/schema.md`, `naevo/docs/modules/*.md`

---

_Última sincronización: 2026-04-19_
