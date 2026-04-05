---
jira_key: "PED-957"
aliases: ["PED-957"]
summary: "APP - Refactor - Modificacion en el indicador  \"tasa de reactivacion de clientes\""
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-24 14:13"
updated: "2025-02-26 14:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-957"
---

# PED-957: APP - Refactor - Modificacion en el indicador  "tasa de reactivacion de clientes"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-24 14:13 |
| Actualizado | 2025-02-26 14:19 |
| Etiquetas | ninguna |
| Jira | [PED-957](https://bluinc.atlassian.net/browse/PED-957) |

## Relaciones

- **Padre:** [[PED-242 - Pestaña Estadisticas|PED-242]] Pestaña Estadisticas
- **action item from:** [[PED-956 - API - Refactor - Cambios en el recurso de Tasa de reactivación de clientes|PED-956]] API - Refactor - Cambios en el recurso de "Tasa de reactivación de clientes"

## Descripcion

Intentaremos hacer mas simple el indicador modificando el concepto de dato.

Para esto es necesario hacer dos pasos:

1 -  No se debe multiplicar en en el Front por 100 como se hace con los porcentajes, dado que esto es un arreglo que estaba mal en el back y ahora se arregla en la tarea[link](https://lioteam.atlassian.net/browse/PED-956) 

2 - Cambiaremos el nombre del indicador de “Tasa de reactivación de clientes”  a “**Clientes activos (%)**”.

Adicionalmente cambiaremos la informacion del indicador y pondermos algo como esto:

```
Calcula el porcentaje de clientes que han realizado una compra en los últimos 3 meses respecto al total de clientes, que es la suma de los que han comprado y los que no.

Formula:
Clientes activos (%) = (Clientes CON compras en los ultimos 3 meses / (Clientes CON compras en los ultimos 3 meses + Clientes SIN compras en los ultimos 3 meses))* 100
```
