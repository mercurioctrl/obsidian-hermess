# Módulo People & Performance (RRHH)

Gestión de talento montada **dentro de la sección Personal** (`/staff`), no es sección nueva. Extiende [[Modulo Personal]] con rol/expectativas, competencias, objetivos, ausencias y evidencia por empleado desde [[Modulo GitHub|GitHub]] y Jira.

**Estado (2026-07-14):** Fase 1 completa + integraciones. Rama `feat/rrhh-ausencias-roles` (sin commitear al cierre de la sesión). Doc técnico del repo: `arquitectura/15-modulo-people-performance.md`.

**Fuentes funcionales** (en `documentos/` del repo): `Especificación Funcional y Técnica.docx` (spec People & Performance en 5 fases), `Planilla_Registro_de_Ausencias_Blu-1.xlsx`, Google Doc "Roles, responsabilidades y expectativas — Equipo Blu" (datos reales de los 7 colaboradores).

## Tabs de la ficha del empleado (`frontend/pages/staff/[id].vue`)

`Información · Rol & Expectativas · Competencias · Objetivos · Actividad · Proyectos · Ausencias · Pagos`

Los tabs **Actividad** (GitHub/Jira) hacen carga diferida (watch sobre `activeTab`), son llamadas en vivo. El resto se carga en `cargar()`.

## Base de datos

| Migración | Qué agrega |
|-----------|------------|
| `0081_add_rol_expectativas_to_empleados` | `area`, `reporta_a`, `proposito`, `responsabilidades` (JSON), `autonomia`, `expectativas` (JSON `[{titulo, items[]}]`), `foco_desarrollo` |
| `0082_create_ausencias_table` | `ausencias`: empleado_id, fecha, horario, motivo, lider_informado, observaciones, usuario_id |
| `0083_create_competencias_tables` | `competencias` (catálogo: nombre, categoria TECNICA/ORGANIZACIONAL) + `empleado_competencia` (pivot: nivel_esperado, nivel_actual 1-5, peso) |
| `0084_create_objetivos_table` | `objetivos` (OKRs): titulo, estado, progreso 0-100, prioridad, peso, trimestre, anio, fechas |
| `0086_add_jira_account_id_to_empleados` | `jira_account_id` |

> ⚠️ Prefijos de migración **duplicados** coexisten con los de GitHub (0081-0084) — Laravel trackea por nombre completo, no colisionan. Máximo real: **0086**, seguir en 0087. Ver [[Base de Datos]], [[Errores Comunes]].

## Endpoints (ver [[Backend - API]])

```
GET|PUT /api/empleados/{id}                     # rol & expectativas van acá
GET|POST /api/ausencias  · PUT|DELETE /api/ausencias/{id}    # ?empleado_id, ?desde, ?hasta
GET /api/competencias (+CRUD catálogo)
GET|PUT /api/empleados/{id}/competencias        # sync esperado/actual
GET|POST /api/empleados/{id}/objetivos · PUT|DELETE /api/objetivos/{id}
GET /api/empleados/{id}/jira-issues             # JQL en vivo por assignee. ?incluir_finalizadas
GET /api/jira/usuarios?q=                        # buscar usuario Jira (accountId)
GET /api/jira/sugerencias-empleados             # preview auto-vincular (exacto/unico/ambiguo/sin_match)
POST /api/jira/vincular-masivo                   # guarda solo lo confirmado
GET /api/github/desarrollador/{login}           # reusa integración existente (github_username)
```

## Seeders (idempotentes, a mano — NO en DatabaseSeeder)

```bash
php artisan db:seed --class=RolesExpectativasSeeder --force   # 7 colaboradores
php artisan db:seed --class=CompetenciasSeeder --force        # 8 técnicas + 10 organizacionales
```
`RolesExpectativasSeeder` matchea por nombre **case/acento-insensitive** (colación MySQL) → no duplica ("Belén"≈"Belen").

## Integraciones — evidencia, no métrica

Regla de la spec: la actividad GitHub/Jira es **evidencia consultable**, no puntaje automático. Vive en el tab Actividad, separada de Competencias/Objetivos.

- **GitHub**: mapeo `empleados.github_username` (ya existía). Sin backend nuevo.
- **Jira**: `empleados.jira_account_id`. Issues por JQL en vivo. **Auto-vincular masivo** (`/staff` → botón) busca por email y nombre, clasifica y **siempre pide confirmación** (los emails del ERP `@blu.inc` no coinciden con Jira → match por nombre).

## Permisos (ver [[Modulo Permisos]])

- Gating con `VER_SECCION_PERSONAL` (cubre `/staff/*`). Sueldos aparte con `VER_MONTOS_SALDOS`.
- **Fix**: el NavItem "Personal" estaba en el bloque solo-admin de `layouts/default.vue`; se cambió a `v-if="isAdmin || puedeVer('VER_SECCION_PERSONAL')"` (Usuarios/Configuración siguen solo-admin). Así un usuario RRHH ve solo Personal.
- ⚠️ Gating **solo frontend**; el Dashboard `/` no está gateado.

## Pendiente (roadmap de la spec)

- **Fase 2**: Feedback continuo → 1:1 → Evaluaciones (regla "ninguna evaluación sin evidencia", historial inmutable) → Plan de Desarrollo.
- **Fase 3**: Dashboards individual/líder/dirección, KPIs por rol, Matriz de talento, Alertas.
- **Fase 4**: integraciones avanzadas (evidencia auto desde GitHub/Jira/CI/ERP).
- **Fase 5**: IA (DeepSeek): recomendaciones, riesgo de rotación, planes de carrera, detección de líderes.

## Ver también

- [[Modulo Personal]] — base de empleados/pagos que este módulo extiende
- [[Modulo Calendario]] — vista mensual que consume ausencias/1:1/objetivos de este módulo
- [[Modulo GitHub]] — fuente de evidencia de actividad de devs
- [[Modulo Permisos]] — gating de la sección
- [[Base de Datos]] · [[Backend - API]] · [[Frontend]] · [[Errores Comunes]]
