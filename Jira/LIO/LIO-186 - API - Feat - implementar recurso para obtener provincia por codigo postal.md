---
jira_key: "LIO-186"
aliases: ["LIO-186"]
summary: "API - Feat - implementar recurso para obtener provincia por codigo postal"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-01-28 12:33"
updated: "2025-04-24 11:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-186"
---

# LIO-186: API - Feat - implementar recurso para obtener provincia por codigo postal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-01-28 12:33 |
| Actualizado | 2025-04-24 11:27 |
| Etiquetas | ninguna |
| Jira | [LIO-186](https://bluinc.atlassian.net/browse/LIO-186) |

## Relaciones

- **relates to:** [[LIO-334 - API - Obtener provincia por código postal - Provincia no coincidente|LIO-334]] API - Obtener provincia por código postal - Provincia no coincidente

## Descripcion

Se debe implementar recurso 

```
GET /v4/users/postalCode?cp=7600
```

params:

```
?cp=7600
```

response:

```
{
   "province": "Buenos Aires",
   "postalCode": 7600
}
```
