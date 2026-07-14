# Módulo GitHub (integración solo lectura)

Integración con GitHub (**solo lectura**, auth por **Personal Access Token**) para evaluar el rendimiento de los programadores. Dos vistas: un **dashboard de rendimiento** por desarrollador y una **vista detallada por dev** (`/github/{login}`) con commits día a día. Entregado en **PR #9** (rama `feat/integracion-github`), 2026-07-11.

> Doc técnica de referencia en el repo: `arquitectura/14-integracion-github.md`.

## ⚠️ Arquitectura: persistencia + sync incremental (NO live)

Pegarle a la API de GitHub en cada carga es lento y agota el rate limit. Por eso los datos **se persisten en la DB** y las vistas leen de ahí (instantáneo, ~0.15s):

- **Sync incremental** (`GithubService::sync()` → `syncRepo()`, comando `github:sync`, scheduler **hourly** en `routes/console.php`): trae solo los PRs con `updated_at` posterior a `github_repos.last_synced_at`. Por cada PR hace upsert del detalle (`guardarPr`: commits/additions/deletions/base/fechas), reemplaza sus reviews y trae sus commits individuales (`guardarCommits`).
- El **dashboard** (`rendimiento()`) y el **detalle** (`detalleDesarrollador()`) NO llaman a la API: leen 100% de la DB.
- Sync **manual** por el botón "Sincronizar" (`POST /github/sync`) sirve solo para incremental; el **backfill inicial** de muchos repos va por scheduler/CLI (el POST tiene timeout de 60s de Nginx).

## Tablas (ver [[Base de Datos]])

- `github_repos` (0079): repos a trackear (`owner`, `name`, `full_name` unique, `activo`, `default_branch`, `last_synced_at` — 0082).
- `github_pull_requests` (0083): PRs (author, base_ref, state, merged, commits, additions, deletions, fechas `gh_*`).
- `github_pr_reviews` (0084): reviews por PR (reviewer, state, submitted_at).
- `github_commits` (0085): commits individuales — `sha` (unique por repo), `author_login`, `author_name`, `committed_at` (fecha real de autoría), `message`. Sin +/− por commit.
- Config en `configuracion`: `github_token` (0078, enmascarado en `GET /config`), `github_org` (0078), `github_rama_destino` (0081, default `development`).
- `empleados.github_username` (0080): mapea login de GitHub → empleado (case-insensitive).

## Dashboard `/github`

Ranking de desarrolladores por período: **commits** (contados por PR), **+/− líneas** (nivel PR), **PRs abiertos / mergeados / a rama destino**, **reviews**. Gráfico `PixelBarChart` de commits por dev. Repos trackeados en sección **colapsable** (122 repos de BluIncStudio / New-Bytes / LibreOpción). Bots excluidos (`login` termina en `[bot]`). Cada fila del ranking navega a la vista detallada.

## Vista detallada por dev `/github/{login}` (2026-07-11)

Página dedicada (`pages/github/[login].vue`) con:
- **Tiles:** Commits (en el período), Líneas +/−, **PRs aceptados** (mergeados en el período), **PRs pendientes** (abiertos ahora + cuántos "hoy"), Reviews.
- **Commits día a día:** `PixelBarChart` con la serie diaria (`por_dia`), contando cada commit por su **fecha real de autoría** (`github_commits.committed_at`, filtrado por `author_login`).
- **Listas:** PRs pendientes (backlog abierto, de cualquier fecha), PRs aceptados (mergeados en el período) y reviews — con link a GitHub.
- Selector de período propio con presets (Hoy / 7 días / 30 días / 3 meses).

## Commits: backfill y límites

- El sync trae los commits de cada PR (`/pulls/{n}/commits`, dedup por `(repo, sha)`).
- Los PRs sincronizados **antes** de crear `github_commits` no los tienen → `php artisan github:backfill-commits` (idempotente, maneja rate limit cortando y retomando; también corre hourly).
- ⚠️ Un commit hecho con un email git **no vinculado** a la cuenta de GitHub llega con `author.login = null` → no se atribuye a ningún dev (limitación de GitHub). Solo se traen commits dentro de PRs (pushes directos sin PR no se capturan).
- Las **líneas +/−** son a nivel PR (GitHub no da additions/deletions por commit sin una llamada por SHA).

## Backend

- `GithubService` (patrón `Http::withToken` + `abort`): `test()`, `listarReposDisponibles()` (org + user repos), `sync()`/`syncRepo()`/`guardarPr()`/`guardarCommits()`, `backfillCommits()`, `rendimiento()`, `detalleDesarrollador()`. Detección de rate limit → `abort(429, 'GITHUB_RATE_LIMIT:...')`.
- `GithubController` + rutas (`auth:sanctum`): `GET /github/test`, `/repos-disponibles`, `GET|POST /github/repos`, `PATCH|DELETE /github/repos/{repo}`, `POST /github/sync`, `GET /github/rendimiento`, `GET /github/desarrollador/{login}`. Ver [[Backend - API]].
- Comandos: `github:sync`, `github:backfill-commits` (ambos hourly).
- Permiso `VER_SECCION_GITHUB` (solo frontend). Ver [[Modulo Permisos]].

## Gotchas operativos (ver [[Errores Comunes]])

- **⚠️ Opcache (FPM):** tras `docker cp` de código PHP, si el endpoint HTTP sirve la versión vieja → `docker restart minisaas-backend`. `optimize:clear` NO limpia el opcache de FPM (el CLI/artisan corre fresco, por eso confunde).
- **Rate limit** 5000/h con PAT: el sync y el backfill cortan al llegar al límite y retoman en la corrida hourly; los repos se ordenan por menos-sincronizado primero para que cada corrida avance.
- **Token scope:** classic con `repo` + `read:org` (sin `read:org` no aparecen los repos de las orgs, solo los personales).

## Roadmap

- Vincular repos a **proyectos** (`ProyectoGithubRepo`, análogo a los tableros Jira).
- Releases / CI (Actions). Vincular repos/PRs al [[Modulo Tareas|kanban de Tareas]].

## Ver también

- [[Modulo People Performance]] — reusa `/github/desarrollador/{login}` como evidencia por empleado (tab Actividad)
- [[Backend - API]] — rutas del módulo
- [[Base de Datos]] — tablas `github_*`
- [[Frontend]] — páginas `/github` y `/github/[login]`
- [[Modulo Permisos]] — `VER_SECCION_GITHUB`
- [[Errores Comunes]] — opcache, rate limit
- [[changelog]] · [[memoria]]
