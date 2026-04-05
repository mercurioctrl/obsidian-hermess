---
jira_key: "NBWEB-762"
summary: "API - Feat - Obtener acelerador para un item determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-02 09:58"
updated: "2024-07-08 11:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-762"
---

# NBWEB-762: API - Feat - Obtener acelerador para un item determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-02 09:58 |
| Actualizado | 2024-07-08 11:58 |
| Etiquetas | ninguna |
| Jira | [NBWEB-762](https://bluinc.atlassian.net/browse/NBWEB-762) |

## Descripción

Agregaremos un recurso para consultar si el item que estoy viendo tiene un acelerador

```
GET {API_URL}/v1/item/{itemId}/acelerator
```

```
[
  {
    "id": 1,
    "txtMatch": " ",
    "acelerator": 1.0,
    "startDate": "2024-07-01T00:00:00",
    "endDate": "2024-07-31T00:00:00"
  }
]
```

este recurso es de libre acceso, osea que no tenes que estar logueado para ver cuanto acelera un producto
