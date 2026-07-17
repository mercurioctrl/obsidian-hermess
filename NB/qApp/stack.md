# Stack — qApp

Ver índice: [[qApp]] · relacionado: [[arquitectura]]

## Monorepo

- **pnpm workspaces** (`pnpm@9.12.0`) — `apps/*` + `packages/*`.
- **TypeScript** `^5.5.4` en todo el repo.

## Frontend — `apps/web`

- **Nuxt** `^4.0.0` (srcDir `app/`, SSR activado).
- **Vue** `^3.5.13`.
- `runtimeConfig.public.apiBase` → URL de la API accesible desde el navegador
  (`NUXT_PUBLIC_API_BASE`).
- SSE nativo (`EventSource`) para progreso en vivo.

## Backend — `apps/api`

- **NestJS** `^10.4.4` (`@nestjs/common`, `@nestjs/core`, `@nestjs/platform-express`).
- **mssql** `^11.0.1` — driver de SQL Server, **SQL crudo** (sin ORM).
- **playwright** `1.49.0` (pin exacto para matchear la imagen de Docker).
- **rxjs** `^7.8.1` — usado por el bus SSE.
- Módulos internos: `scenarios`, `executions`, `executor`, `events`, `evidence`,
  `demo`, `database`, `health`.

## Base de datos

- **SQL Server 2022** (`mcr.microsoft.com/mssql/server:2022-latest`) en dev.
- Migraciones SQL crudo, versionadas e idempotentes, aplicadas al arrancar por un
  migrador propio (tabla `schema_migrations`).

## Infraestructura

- **Docker Compose** — servicios `db`, `api`, `web`.
- Imagen de la API basada en `mcr.microsoft.com/playwright:v1.49.0-noble`
  (trae los navegadores instalados; Node 22).
- Imagen de web basada en `node:20-slim`.
- **pnpm se instala con `npm i -g pnpm@9.12.0`** en los Dockerfiles (evita el fallo
  de verificación de firma de `corepack`). Ver [[contexto]].
- Evidencias en volumen local; en prod, carpeta real del host (`/var/qa-evidence`).

## Variables de entorno clave (`.env`)

- `DB_*` — conexión a SQL Server.
- `PLAYWRIGHT_CONCURRENCY` (1) / `HTTP_CONCURRENCY` (5) — límites por ejecutor.
- `QUEUE_POLL_INTERVAL_MS` — cada cuánto el gestor revisa la cola.
- `EVIDENCE_DIR` — carpeta de evidencias.
- `GAMMA_BASE_URL` / `GAMMA_USER` / `GAMMA_PASSWORD` — ambiente real (vacíos en el demo).
- `NUXT_PUBLIC_API_BASE`, `WEB_PORT`, `API_PORT`.

## Ver también

- [[arquitectura|Arquitectura]]
- [[contexto|Contexto y gotchas]]
