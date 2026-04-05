---
jira_key: "COB-557"
aliases: ["COB-557"]
summary: "APP - Feat - Comentarios para las asignaciones de saldo en la linea de credito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-04-29 17:31"
updated: "2025-05-08 08:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-557"
---

# COB-557: APP - Feat - Comentarios para las asignaciones de saldo en la linea de credito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-29 17:31 |
| Actualizado | 2025-05-08 08:43 |
| Etiquetas | ninguna |
| Jira | [COB-557](https://bluinc.atlassian.net/browse/COB-557) |

## Relaciones

- **Padre:** [[COB-374 - Feat - Editar estado crediticio de la cuenta del cliente|COB-374]] Feat - Editar estado crediticio de la cuenta del cliente
- **has action item:** [[SNB-3010 - OBSERVACIONES EN FICHA DE LINEA DE CREDITO|SNB-3010]] OBSERVACIONES EN FICHA DE LINEA DE CREDITO

## Descripcion

Basándonos en el nuevo parámetro `comment` del recurso 

```
GET {{API_URL}}/v1/assignedCredit/{clientId}
```

usaremos este mismo para rellenar por defecto al cargar  la informacion crediticia.

[adjunto]
