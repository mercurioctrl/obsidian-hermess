---
jira_key: "NBWEB-138"
aliases: ["NBWEB-138"]
summary: "Vaciar Carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-25 16:08"
updated: "2022-06-26 10:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-138"
---

# NBWEB-138: Vaciar Carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-25 16:08 |
| Actualizado | 2022-06-26 10:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-138](https://bluinc.atlassian.net/browse/NBWEB-138) |

## Relaciones

- **Padre:** [[NBWEB-1 - API - Carrito de compras|NBWEB-1]] API - Carrito de compras

## Descripcion

Recurso especifico para vaciar el carrito

```
PATCH {{API_URL}}/v1/carrito/empty
```

Ruequest



```
{
carId:2355234
}
```
