# Módulo Minutas

Actas de reunión con **puntos** tipo checklist. Sección `VER_SECCION_MINUTAS` (`/minutas`). Migs `0087` (minutas), `0088` (minuta_puntos), `0089` (descripción).

## Modelo

- `Minuta`: cabecera del acta (título, descripción, fecha…).
- `MinutaPunto`: puntos/ítems de la minuta, ordenables y con toggle de completado.

## Rutas

- `apiResource minutas` (param `minuta`).
- `POST /minutas/{m}/puntos` · `POST /minutas/{m}/puntos/reordenar`
- `PUT /minuta-puntos/{p}` · `PATCH /minuta-puntos/{p}/toggle` · `DELETE /minuta-puntos/{p}`

Frontend: `pages/minutas/index.vue` + componente `MinutaPuntos.vue` (mismo patrón de checklist reordenable que las subtareas de [[modulos/tareas]]).

## Ver también

- [[modulos/tareas]] — mismo patrón de puntos/checklist
- [[changelog#2026-08-14 — Deploy release colaboración (Tareas 2.0, Solicitudes, Minutas, Notificaciones+Push, Campañas)|changelog]]
