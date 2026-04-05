---
jira_key: "COM-123"
aliases: ["COM-123"]
summary: "API - Refactor - Cuando agregamos un item, si este no tiene taxposition, marcaremos la predeterminada de la categoria"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-06-29 21:02"
updated: "2024-07-05 08:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-123"
---

# COM-123: API - Refactor - Cuando agregamos un item, si este no tiene taxposition, marcaremos la predeterminada de la categoria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-29 21:02 |
| Actualizado | 2024-07-05 08:52 |
| Etiquetas | ninguna |
| Jira | [COM-123](https://bluinc.atlassian.net/browse/COM-123) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra

## Descripcion

```
PATCH /v1/providerOrder/{order}
```

```
{
    "state": "success",
    "response": "Item agregado correctamente",
    "code": 200,
    "item": {
        "id": 118850,
        "price": {
            "value": 0,
            "iva": 0
        },
        "amount": 1,
        "position": null, <---- traer la que es por defecto
        "taxPosition": null <---- traer la que es por defecto
    }
}
```
