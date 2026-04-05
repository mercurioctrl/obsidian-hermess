---
jira_key: "NBWEB-762"
aliases: ["NBWEB-762"]
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

## Relaciones

- **Padre:** [[NBWEB-682 - Productos|NBWEB-682]] Productos
- **blocks:** [[NBWEB-763 - APP - Refactor - Modificaremos la ficha del producto para mostrar el acelerador|NBWEB-763]] APP - Refactor - Modificaremos la ficha del producto para mostrar el acelerador que tiene el item (si tiene)
- **relates to:** [[NBWEB-764 - API - Obtener acelerador para un item determinado - Articulo sin acelerador|NBWEB-764]] API - Obtener acelerador para un item determinado - Articulo sin acelerador 
- **blocks:** [[NBWEB-767 - API - Review - Obtener acelerador para un item determinado parece no asimilar|NBWEB-767]] API - Review - Obtener acelerador para un item determinado parece no asimilar las fechas de inicio y fin para mostrarse

## Descripcion

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
