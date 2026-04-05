---
jira_key: "PED-705"
aliases: ["PED-705"]
summary: "API - Refactor - agregar campo destino bancario para recurso de comprobante"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-04-29 12:44"
updated: "2024-05-07 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-705"
---

# PED-705: API - Refactor - agregar campo destino bancario para recurso de comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-04-29 12:44 |
| Actualizado | 2024-05-07 17:11 |
| Etiquetas | ninguna |
| Jira | [PED-705](https://bluinc.atlassian.net/browse/PED-705) |

## Relaciones

- **blocks:** [[PED-704]] APP -Refactor - Mejora - Agreagar al crear y el leer el campo documento como opcional y tambien el banco destino de la transferencia
- **is blocked by:** [[PED-706]] API - Listado de ordenes -> Destino bancario - No coincidente con el liquidado

## Descripcion

Se debe retornar el banco asignado en liquidacion en el recurso de GET /orders  

```
[
        {
            "date": "2024-04-27 17:11:46",
            ....
            "liquidateDestinationBankName": "BBVA BANCO FRANCES S.A." --> nuevo campo 
        },
]
```
