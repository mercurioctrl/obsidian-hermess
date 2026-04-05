---
jira_key: "PED-956"
aliases: ["PED-956"]
summary: "API - Refactor - Cambios en el recurso de \"Tasa de reactivación de clientes\""
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-24 14:07"
updated: "2025-02-24 18:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-956"
---

# PED-956: API - Refactor - Cambios en el recurso de "Tasa de reactivación de clientes"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-24 14:07 |
| Actualizado | 2025-02-24 18:39 |
| Etiquetas | ninguna |
| Jira | [PED-956](https://bluinc.atlassian.net/browse/PED-956) |

## Relaciones

- **Padre:** [[PED-242 - Pestaña Estadisticas|PED-242]] Pestaña Estadisticas
- **has action item:** [[PED-957 - APP - Refactor - Modificacion en el indicador tasa de reactivacion de clientes|PED-957]] APP - Refactor - Modificacion en el indicador  "tasa de reactivacion de clientes"

## Descripcion

Para facilitar su lectura y utilizar un  dato un poco mas útil y fácil de explicar haremos un pequeño cambio para transformar la “tasa de reactivacion de clientes” por “tasa de clientes activos”.

Para esto utilizaremos una formula casi idéntica de la que venimos usando pero agregando a la base la cantidad total de clientes en lugar de solo los clientes que no compraron. Ademas, lo convertiremos en un porcentual (esto es lo que aparentemente se esta intentando desde el front pero lo vamos a corregir).

Antes haciamos 

```
Tasa de ractivacion de clientes = Clientes CON compras en los ultimos 3 meses / Clientes SIN compras en los ultimos 3 meses
```

Ahora haremos el siguiente concepto con las mismas querys (no es necasrio  cambiar nada)

```
Clientes activos (%) = (Clientes CON compras en los ultimos 3 meses / (Clientes CON compras en los ultimos 3 meses + Clientes SIN compras en los ultimos 3 meses))* 100
```
