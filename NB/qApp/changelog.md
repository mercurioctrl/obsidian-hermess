# Changelog — qApp

Ver índice: [[qApp]]

## 2026-07-16

- **feat:** base ejecutable de la arquitectura de automatización QA (commit inicial
  `2c4d3af`). Monorepo dockerizado Nuxt 4 + NestJS + SQL Server.
  - API NestJS: escenarios, cola de ejecuciones persistida en SQL Server, gestor con
    concurrencia configurable por tipo, ejecutores Playwright y HTTP, SSE y servido
    de evidencias.
  - Front Nuxt 4: selección de escenario/parámetros, progreso en vivo, resultado,
    evidencias e historial.
  - SQL crudo (`mssql`) con migraciones versionadas e idempotentes (esquema + seed).
  - Demo autocontenido (endpoint `/demo/echo` + escenario Playwright que abre una URL
    real) para probar el circuito completo sin depender de Gamma ni de internet.
  - `docs/`: arquitectura y referencia de API.
- **Verificación end-to-end en Docker:** ejecución HTTP y ejecución Playwright ambas
  `succeeded`; evidencias generadas (screenshot, trace, video, log) y servidas por
  `/evidence/...`; guard de path traversal devuelve 404.
- **Fixes que surgieron al ejecutar** (ver [[contexto]]):
  - `corepack` no verificaba la firma de pnpm → se instala pnpm con `npm i -g`.
  - `ValidationPipe` exigía `class-validator` (no se usa) → removido.
  - El migrador corría antes de conectar el pool → la conexión arranca en el
    constructor y las queries la esperan.

Archivos principales: `apps/api/src/executor/`, `apps/api/src/database/`,
`apps/api/src/executions/`, `apps/web/app/pages/index.vue`,
`infra/db/migrations/`, `docker-compose.yml`.
