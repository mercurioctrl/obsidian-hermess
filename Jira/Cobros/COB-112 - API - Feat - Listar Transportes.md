---
jira_key: "COB-112"
aliases: ["COB-112"]
summary: "API - Feat - Listar Transportes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-09-22 15:33"
updated: "2022-10-25 09:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-112"
---

# COB-112: API - Feat - Listar Transportes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-09-22 15:33 |
| Actualizado | 2022-10-25 09:02 |
| Etiquetas | ninguna |
| Jira | [COB-112](https://bluinc.atlassian.net/browse/COB-112) |

## Relaciones

- **Padre:** [[COB-41]] APP - Feat -  Listar cobrables

## Descripcion

```
GET {{API_URL}}/v1/tradableDispatchMethod
```

Recurso para listar todos los dispatch  de la tabla `NewBytes_DBF.dbo.transpor`.

```
[
    {
        "id": 1,
        "description": "Retiro de cliente en Local"
    },
    {
        "id": 7,
        "description": "Cargas Terrestes y Aereas"
    },
    {
        "id": 8,
        "description": "Cruz del Sur"
    }...
] 
```
