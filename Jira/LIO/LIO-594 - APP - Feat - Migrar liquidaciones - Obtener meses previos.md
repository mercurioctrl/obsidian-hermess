---
jira_key: "LIO-594"
aliases: ["LIO-594"]
summary: "APP - Feat - Migrar liquidaciones -> Obtener meses previos "
status: "Ready for QA"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-03-31 15:58"
updated: "2026-04-01 17:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-594"
---

# LIO-594: APP - Feat - Migrar liquidaciones -> Obtener meses previos 

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-31 15:58 |
| Actualizado | 2026-04-01 17:17 |
| Etiquetas | ninguna |
| Jira | [LIO-594](https://bluinc.atlassian.net/browse/LIO-594) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **action item from:** [[LIO-560 - API - Feat - Migrar liquidaciones - Obtener meses previos|LIO-560]] API - Feat - Migrar liquidaciones -> Obtener meses previos 

## Descripcion

[adjunto]
Se debe conectar al nuevo recurso de api4 

## Recurso a migrar

| Campo | Valor |
| --- | --- |
| **Verbo** | `GET` |
| **Path** | `/liquidaciones/meses-previos` |
| **Autenticación** | Bearer JWT (token del vendedor en el header `Authorization`) |
| **Body / Payload** | Ninguno. Es un GET sin cuerpo. |
| **Query params** | Ninguno. |
