---
jira_key: "COB-297"
aliases: ["COB-297"]
summary: "APP - Feat - Listar provincias y el total de retenciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-01-06 09:56"
updated: "2023-01-31 13:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-297"
---

# COB-297: APP - Feat - Listar provincias y el total de retenciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-06 09:56 |
| Actualizado | 2023-01-31 13:51 |
| Etiquetas | ninguna |
| Jira | [COB-297](https://bluinc.atlassian.net/browse/COB-297) |

## Relaciones

- **Padre:** [[COB-294]] Feat - Listar provincias (Mas subtotales de retenciones)
- **is blocked by:** [[COB-296]] API - Feat - Listar provincias y el total de retenciones

## Descripcion

Basándonos en el listado de provincias y en la tabla que contiene las retenciones aplicadas, se debe confeccionar un listado para poder mostrar el acceso al detalle de cada uno.

El mismo estará en una pestaña nueva y mostrara las siguientes columnas

- id provincia


- nombre provincia


- retenciones acumuladas (el subtotal)



Debe estar ordenado de mayor a menor subtotal y tendra un filtro para ver solo *con saldo de retenciones /sin saldo de retenciones*

Usaremos el recurso [link](https://lioteam.atlassian.net/browse/COB-296)

```
GET {API_URL}/v1/retentionIibb
```

Adicionalmente al hacer click abriremos un modal para visualizar el detalle de los movimientos en la linea de lo que venimos haciendo [link](https://lioteam.atlassian.net/browse/COB-298)
