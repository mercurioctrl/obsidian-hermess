# qApp — Automatización QA

Base de conocimiento del proyecto **qApp** (repo `New-Bytes/qApp`).

Herramienta interna de QA para **generar datos de prueba de negocio** (pedidos
creados, pagados, despachados, facturados, con postventa) de forma reproducible,
con evidencia y trazabilidad. El QA elige un escenario, define parámetros, ejecuta
y obtiene un resultado reutilizable.

## Stack

- **Front:** Nuxt 4 + Vue 3 + TypeScript
- **API:** NestJS + TypeScript
- **DB:** SQL Server (cola persistida + datos), SQL crudo con `mssql`
- **Ejecutores:** Playwright (navegador) y cliente HTTP
- **Infra:** Docker Compose, evidencias en volumen local, actualizaciones por SSE

Detalle en [[stack|Stack]].

## Notas del proyecto

- [[arquitectura|Arquitectura]] — componentes, flujo funcional, modelo de datos y decisiones de diseño.
- [[stack|Stack]] — tecnologías, versiones y dependencias clave.
- [[changelog|Changelog]] — historial de lo trabajado.
- [[contexto|Contexto]] — reglas de negocio, decisiones, gotchas y próximos pasos.

## Repositorio

`git@github.com:New-Bytes/qApp.git` · ubicación local: `/var/www/guille/newbytes-qa-automation`

---
*Última sincronización: 2026-07-17*
