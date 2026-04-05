---
jira_key: "NBWEB-41"
aliases: ["NBWEB-41"]
summary: "Cambiar Carrito de compras"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 09:36"
updated: "2022-04-12 09:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-41"
---

# NBWEB-41: Cambiar Carrito de compras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 09:36 |
| Actualizado | 2022-04-12 09:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-41](https://bluinc.atlassian.net/browse/NBWEB-41) |

## Relaciones

- **Padre:** [[NBWEB-1 - API - Carrito de compras|NBWEB-1]] API - Carrito de compras

## Descripcion

```
PUT {{API_URL}}/v1/carrito/{id_carrito_por_el_que_cambiar}
```

Proceso, cambio las variables que determinan el carrito actual seleccionado y lo cambio en la bd para el usuario, dentro de la columna `[NB_WEB].[dbo].[usuarios_nb]`.`carritoActivo`
