---
jira_key: "LIO-593"
aliases: ["LIO-593"]
summary: "APP - Feat - Migrar liquidaciones de usuarios vendedores"
status: "Ready for QA"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-03-31 15:56"
updated: "2026-04-01 11:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-593"
---

# LIO-593: APP - Feat - Migrar liquidaciones de usuarios vendedores

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-31 15:56 |
| Actualizado | 2026-04-01 11:40 |
| Etiquetas | ninguna |
| Jira | [LIO-593](https://bluinc.atlassian.net/browse/LIO-593) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **action item from:** [[LIO-559 - API - Feat - Migrar liquidaciones de usuarios vendedores|LIO-559]] API - Feat - Migrar liquidaciones de usuarios vendedores

## Descripcion

[adjunto]
Se debe conectar por migracion el nuevo recurso de v4

## Recurso a migrar

| Campo | Valor |
| --- | --- |
| **Verbo** | `GET` |
| **Path** | `/liquidaciones/resumen-actual` |
| **Autenticación** | Bearer JWT (token del vendedor en el header `Authorization`) |
| **Body / Payload** | Ninguno. Es un GET sin cuerpo. |
| **Query params** | Ninguno. |
