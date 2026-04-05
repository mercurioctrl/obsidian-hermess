---
jira_key: "COM-93"
aliases: ["COM-93"]
summary: "API - Refactor - Agregar datos adicionales de Items en respuesta de provider order add"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-05-15 17:00"
updated: "2024-05-22 04:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-93"
---

# COM-93: API - Refactor - Agregar datos adicionales de Items en respuesta de provider order add

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-05-15 17:00 |
| Actualizado | 2024-05-22 04:16 |
| Etiquetas | ninguna |
| Jira | [COM-93](https://bluinc.atlassian.net/browse/COM-93) |

## Relaciones

- **Padre:** [[COM-8 - Ordenes de compra|COM-8]] Ordenes de compra

## Descripcion

Success: 

```
{
    "state": "success",
    "response": "Item agregado correctamente",
    "code": 200,
    "item": {
        "id": 111770,
        "price": {
            "value": 0,
            "iva": 0
        },
        "amount": 1
    }
}
```

Fail:

```
{
    "state": "fail",
    "response": "No se ha podido agregar el item a la orden de compra",
    "code": 400,
    "item": null
}
```
