---
jira_key: "COM-96"
summary: "API - Refactor - Reestructurar objecto al agregar un item en provider order"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-05-15 17:03"
updated: "2024-05-22 04:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-96"
---

# COM-96: API - Refactor - Reestructurar objecto al agregar un item en provider order

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-05-15 17:03 |
| Actualizado | 2024-05-22 04:48 |
| Etiquetas | ninguna |
| Jira | [COM-96](https://bluinc.atlassian.net/browse/COM-96) |

## Descripción

Nueva estructura de object al agregar un Item. 

En caso de enviar “position“: null este se quitara del item seleccionado.



```
{
    "id": 111770,
    "price": {
        "value": 0,
        "iva": 0
    },
    "amount": 1,
    "position": "4823.69.00.200M",
    "taxPosition": {
        "aec": 16,
        "iibb": 2.5,
        "iva": 21,
        "ivaAd": 22,
        "ganancias": 6,
        "te": 3,
        "dii": 0,
        "die": 16
    }
}
```
