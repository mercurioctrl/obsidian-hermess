---
jira_key: "PED-390"
aliases: ["PED-390"]
summary: "APP - Feat - Listar clientes -> Conjunto de filtros ordenar por y sentido del orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-12-26 08:24"
updated: "2023-12-29 11:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-390"
---

# PED-390: APP - Feat - Listar clientes -> Conjunto de filtros ordenar por y sentido del orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-26 08:24 |
| Actualizado | 2023-12-29 11:30 |
| Etiquetas | ninguna |
| Jira | [PED-390](https://bluinc.atlassian.net/browse/PED-390) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes
- **is blocked by:** [[PED-389]] API - Refactor - Listar clientes -> Filtro ordenar por
- **is blocked by:** [[PED-405]] APP - Listar clientes -> Filtros - Incidencias varias

## Descripcion

Usaremos el recurso de [link](https://lioteam.atlassian.net/browse/PED-389) 

```
GET {API_URL}/v1/clients?order={parametro}&direction=desc
```

Agregando dos selectores, uno que desencadena la activacion del otro.

Si selecciono un parámetro para `order`, entonces activo el filtro con las opciones `direction`
