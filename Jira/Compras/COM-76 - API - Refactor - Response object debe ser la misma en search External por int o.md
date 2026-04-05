---
jira_key: "COM-76"
aliases: ["COM-76"]
summary: "API - Refactor - Response object debe ser la misma en search External por int o string"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-03-22 16:52"
updated: "2024-04-21 20:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-76"
---

# COM-76: API - Refactor - Response object debe ser la misma en search External por int o string

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-03-22 16:52 |
| Actualizado | 2024-04-21 20:31 |
| Etiquetas | ninguna |
| Jira | [COM-76](https://bluinc.atlassian.net/browse/COM-76) |

## Relaciones

- **Padre:** [[COM-1 - Bases y repositorios|COM-1]] Bases y repositorios

## Descripcion

Sea que se haga una busqueda externa por Texto o por Posicion. 

la estructura de respuesta siempre debe ser la misma. 

```
{
    "search": "8528.49.30.000K",
    "response": [
        {
            "position": "8528.49.30.000K",
            "description": "Policromaticos, con dispositivos de seleccion de barrido (<underscanning>) y de retardo de sincronismo horizontal y vertical (<H/V delay> o <pulse cross>)",
            "tax": [
                {
                    "description": "AEC",
                    "value": 16
                },
                {
                    "description": "DII",
                    "value": 0
                },
                {
                    "description": "TE",
                    "value": 3
                },
                {
                    "description": "DIE",
                    "value": 0
                }
            ]
        }
    ],
    "count": 1
}
```
