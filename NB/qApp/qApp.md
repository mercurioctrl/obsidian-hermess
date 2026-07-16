# qApp — Automatización QA

Base de conocimiento del proyecto **qApp** (repo `New-Bytes/qApp`).

Herramienta interna de QA para generar datos de prueba de negocio (pedidos creados,
pagados, despachados, facturados, con postventa) de forma reproducible, con
evidencia y trazabilidad.

## Stack

- **Front:** Nuxt 4 + Vue 3 + TypeScript
- **API:** NestJS + TypeScript
- **DB:** SQL Server (cola persistida + datos), SQL crudo con `mssql`
- **Ejecutores:** Playwright (navegador) y cliente HTTP
- **Infra:** Docker Compose, evidencias en volumen local, actualizaciones por SSE

## Repositorio

`git@github.com:New-Bytes/qApp.git`

## Notas

_(Las decisiones de arquitectura, contexto y bitácora del proyecto se guardan en esta carpeta.)_
