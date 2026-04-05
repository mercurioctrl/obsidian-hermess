---
jira_key: "INV-41"
summary: "APP - Refactor - Mostrar modal con etiquetas de un producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-11-07 16:01"
updated: "2025-09-02 08:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-41"
---

# INV-41: APP - Refactor - Mostrar modal con etiquetas de un producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-07 16:01 |
| Actualizado | 2025-09-02 08:24 |
| Etiquetas | ninguna |
| Jira | [INV-41](https://bluinc.atlassian.net/browse/INV-41) |

## Descripción

Basandonos en el recurso 

```
GET {{API_URL}}/item/{itemId}
```

Mostraremos el contenido del objeto 

```
  "attributes": [
            {
                "name": "Marca",
                "value": "AMD",
                "id": 296653
            },
            {
                "name": "Caché",
                "value": "1 MB",
                "id": 296654
            }
....
```

Según las ideas propuestas en la charla de slack.

Se mostraran en un tabla que nos permita operar los atributos, cambiando su nombre, su valor o bien eliminándolo.

Para esto debemos usar el recurso de edicion del item enviando el objeto que deseamos editar

```
PATCH {{API_URL}}/item/{itemId}
```

```
"attributes": [
    {
        "name": "Marca",
        "value": "AMD",
        "id": 296653
    }
]
```
