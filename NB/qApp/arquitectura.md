# Arquitectura — qApp

Ver índice: [[qApp]] · relacionado: [[stack]] · [[contexto]]

## Objetivo

El QA selecciona un escenario, define sus parámetros, ejecuta el proceso y obtiene
un resultado reutilizable con evidencia (capturas, videos, trazas) y trazabilidad
(historial de ejecuciones, estados, resultados).

## Vista general

```
Servidor de QA (un solo host / VM — separación lógica en el código)
├── web    · Nuxt 4 + Vue 3 + TS   → UI: escenarios, parámetros, progreso, resultado, evidencias, historial
├── api    · NestJS + TS           → valida, encola, coordina ejecutores, expone resultados y SSE
│    ├── gestor de ejecuciones     → polling de la cola, límites de concurrencia por tipo
│    ├── Playwright Executor       → automatiza el sitio como usuario real, genera evidencias
│    └── API Executor              → pega a un endpoint y conserva status/headers/body
├── db     · SQL Server            → escenarios, ejecuciones, estados, resultados, rutas de evidencia
└── evidence (volumen local)       → capturas, videos, trazas — fuera de la base de datos
```

## Estructura del monorepo

- `apps/api` — NestJS. Módulos: `scenarios`, `executions` (cola + CRUD), `executor`
  (worker + ejecutores Playwright/HTTP), `events` (bus SSE), `evidence` (servido de
  archivos), `demo` (endpoint autocontenido), `database` (pool `mssql` + migrador).
- `apps/web` — Nuxt 4. Página única con formulario de lanzamiento, progreso en vivo
  por SSE, detalle de resultado + evidencias e historial.
- `packages/shared` — tipos y enums de estado compartidos front↔API (una sola fuente
  de verdad).
- `infra/db/migrations` — SQL crudo versionado e idempotente (esquema + seed).

## Flujo funcional

```
Usuario QA
  └─ selecciona escenario, ambiente, parámetros y modo (Playwright | HTTP)
       └─ la API valida y registra la ejecución en SQL Server (estado: pending)
            └─ el gestor toma la pendiente, respeta la concurrencia y la marca running
                 ├─ Playwright Executor → flujo visual, resultado y evidencias
                 └─ API Executor        → petición y respuesta configurada
            └─ la API registra resultado + rutas de evidencia (succeeded | failed)
       └─ el frontend recibe el estado por SSE y muestra resultado, evidencias e historial
```

## Modelo de datos

- **scenarios** — catálogo (`key`, `name`, `type` [playwright|http], `config` JSON).
- **executions** — cola persistida (`scenario_id`, `type`, `mode`, `environment`,
  `params`, `status`, `result`, `error`, timestamps).
- **evidence** — piezas de evidencia por ejecución (`type`, `path` relativo).
- **schema_migrations** — control de migraciones aplicadas.

Estados de una ejecución: `pending → running → succeeded | failed`.

## Decisiones de diseño (y por qué)

- **Cola persistida en la propia SQL Server** (sin Redis/RabbitMQ): pragmático para
  un host único. El ejecutor queda desacoplado por la cola, así que puede extraerse
  a otro proceso si hay que escalar.
- **SQL crudo con `mssql`** (sin ORM): control total y migraciones idempotentes.
- **Concurrencia configurable por tipo** (`PLAYWRIGHT_CONCURRENCY`,
  `HTTP_CONCURRENCY`): Playwright arranca en `1` pero se cambia por `.env`, sin tocar
  código.
- **Evidencias fuera de la base de datos**, en volumen local, servidas por la API bajo
  `/evidence/...` (con protección contra path traversal).
- **La conexión a la DB arranca en el constructor** del `DatabaseService` y `query`/
  `execute` esperan a que el pool esté listo → el orden de los hooks `onModuleInit`
  (p. ej. el migrador) deja de importar. Ver [[contexto]].
- **Despliegue único** con override `docker-compose.prod.yml` que apaga el contenedor
  de DB y apunta al SQL Server existente de QA.

## Ver también

- [[stack|Tecnologías y versiones]]
- [[contexto|Reglas, gotchas y próximos pasos]]
- [[changelog|Historial de cambios]]
