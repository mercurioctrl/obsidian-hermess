---
jira_key: "PED-153"
aliases: ["PED-153"]
summary: "API - Refactor - Listar ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-18 23:05"
updated: "2023-10-19 18:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-153"
---

# PED-153: API - Refactor - Listar ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-18 23:05 |
| Actualizado | 2023-10-19 18:00 |
| Etiquetas | ninguna |
| Jira | [PED-153](https://bluinc.atlassian.net/browse/PED-153) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra

## Descripcion

Agregaremos el parramtetro `satusDescription`

El mismo tendrá si `status = p` la leyenda 'Pendiente' y si `satus=s` la leyenda 'Remitido. 

En caso de estar liquidado devolveremos específicamente la leyenda obtenida en `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]`
