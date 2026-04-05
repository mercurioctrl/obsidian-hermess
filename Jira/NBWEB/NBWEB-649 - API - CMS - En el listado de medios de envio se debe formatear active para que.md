---
jira_key: "NBWEB-649"
aliases: ["NBWEB-649"]
summary: "API - CMS - En el listado de medios de envio se debe formatear \"active\" para que sea tipo Int"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Marbe Moreno"
created: "2024-03-18 13:27"
updated: "2024-04-16 12:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-649"
---

# NBWEB-649: API - CMS - En el listado de medios de envio se debe formatear "active" para que sea tipo Int

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Marbe Moreno |
| Creado | 2024-03-18 13:27 |
| Actualizado | 2024-04-16 12:12 |
| Etiquetas | ninguna |
| Jira | [NBWEB-649](https://bluinc.atlassian.net/browse/NBWEB-649) |

## Relaciones

*Sin relaciones*

## Descripcion

```json
{
    "id": "3030",
    "name": "Moto",
    "description": "Moto (Capital Federal)",
    "active": "1", //<------ Debe venir como numero no como string
    "extraDayMin": "0",
    "extraDayMax": "0",
    "kmPrice": "330",
    "minFee": "2500",
    "maxDistance": "80",
    "insuredLimit": null
}
```
