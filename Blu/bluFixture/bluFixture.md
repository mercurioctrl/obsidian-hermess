# bluFixture

Plataforma multiempresa de pronósticos para el **Mundial FIFA 2026**.

> **URL:** http://localhost:8830 · **Login:** admin@blufixture.com / admin1234

---

## Notas del proyecto

- [[arquitectura]] — Estructura, modelos, decisiones técnicas
- [[stack]] — Tecnologías, dependencias, Docker
- [[api]] — Referencia completa de endpoints
- [[contexto]] — Reglas de negocio, patrones, gotchas
- [[changelog]] — Historial de cambios por sesión

---

## Stack rápido

| Capa | Tecnología |
|------|-----------|
| Frontend | Nuxt 3 + Vue 3 + Tailwind + Pinia |
| Backend | Laravel 11 + PHP 8.3 + Sanctum |
| DB | MySQL 8 (puerto 3308) |
| Cache | Redis 7 |
| Proxy | Nginx (puerto 8830) |
| Deploy | Docker Compose |

## Roles

| Rol | Panel | Descripción |
|-----|-------|-------------|
| `super_admin` | `/admin` | Acceso total |
| `empresa_admin` | `/empresa` | Gestiona su empresa |
| `participante` | `/portal` | Portal de pronósticos |

---

*Última sincronización: 2026-06-08*
