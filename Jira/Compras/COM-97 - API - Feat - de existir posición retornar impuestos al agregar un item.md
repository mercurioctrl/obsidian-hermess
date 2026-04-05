---
jira_key: "COM-97"
aliases: ["COM-97"]
summary: "API - Feat - de existir posición retornar impuestos  al agregar un item"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-05-16 10:23"
updated: "2024-05-22 04:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-97"
---

# COM-97: API - Feat - de existir posición retornar impuestos  al agregar un item

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-05-16 10:23 |
| Actualizado | 2024-05-22 04:22 |
| Etiquetas | ninguna |
| Jira | [COM-97](https://bluinc.atlassian.net/browse/COM-97) |

## Relaciones

- **Padre:** [[COM-8]] Ordenes de compra

## Descripcion

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
        "amount": 1,
        "position": "4823.69.00.200M"
    },
    "tax": {  -----> se debe ver esto en caso de enviar "position"
        "aec": 16,
        "iibb": 2.5,
        "iva": 21,
        "ivaAd": 20,
        "ganancias": 6,
        "te": 3,
        "dii": 0,
        "die": 16
    }
}
```

En caso de no enviar position, tax sera null.

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
    },
    "tax": null
}
```
