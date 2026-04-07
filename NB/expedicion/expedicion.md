# Expedición

Sistema de expedición y logística de warehouse para NB (distribuidor mayorista).
Monorepo con API REST (PHP/Slim 4) y Frontend (Nuxt 2/Vue 2).

**Última sincronización:** 2026-04-05

---

## Notas del proyecto

| Nota | Descripción |
|------|-------------|
| [[NB/expedicion/contexto|Contexto]] | Qué es, dominios de negocio, autenticación, entornos |
| [[NB/expedicion/arquitectura|Arquitectura]] | Diagramas, capas backend, flujo frontend, Docker, CI/CD |
| [[NB/expedicion/stack|Stack]] | Tecnologías, versiones, dependencias, servicios externos |
| [[NB/expedicion/documentacion|Documentación]] | Setup local, variables de entorno, comandos, endpoints |
| [[NB/expedicion/changelog|Changelog]] | Historial de cambios (API + Frontend) |
| [[NB/expedicion/memoria|Memoria]] | Problemas resueltos, decisiones, gotchas |

---

## Tareas

- [[NB/expedicion/tareas/API - Feat - Permisos por agente para saltear validaciones de serials|API - Feat - Permisos por agente para saltear validaciones de serials]]
- [[NB/expedicion/tareas/API - Feat - Incluir permisos de bypass en objeto user|API - Feat - Incluir permisos de bypass en objeto user]]
- [[NB/expedicion/tareas/APP - Refactor - Separar campos obligatorios y opcionales en modal de medidas|APP - Refactor - Separar campos obligatorios y opcionales en modal de medidas]]

---

## Sub-proyectos

- **api-rest-expedicion/** — API REST PHP 8.3 / Slim 4 / SQL Server / Docker
- **expedicion-web-app-v1/** — Frontend Nuxt 2 / Vue 2 / Ant Design Vue / PM2

## Links rápidos

- API local: `http://localhost:8084/v1`
- Frontend local: `http://localhost:4149`
- Repo API: `New-Bytes/api-rest-expedicion` (GitHub)
- Repo Frontend: `New-Bytes/expedicion-web-app-v1` (GitHub)
- Jira Tareas: prefijo `EXP-`
