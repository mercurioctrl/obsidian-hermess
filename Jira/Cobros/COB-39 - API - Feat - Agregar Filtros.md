---
jira_key: "COB-39"
aliases: ["COB-39"]
summary: "API - Feat - Agregar Filtros"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-01 06:58"
updated: "2022-10-04 15:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-39"
---

# COB-39: API - Feat - Agregar Filtros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-01 06:58 |
| Actualizado | 2022-10-04 15:33 |
| Etiquetas | ninguna |
| Jira | [COB-39](https://bluinc.atlassian.net/browse/COB-39) |

## Relaciones

- **Padre:** [[COB-3]] API - Feat - Listar movimiento por caja
- **blocks:** [[COB-40]] APP - Feat - Listar movimientos caja
- **blocks:** [[COB-56]] APP - Feat - Filtrar movimientos de caja

## Descripcion

Se debe contar con filtros por fecha en el siguiente estilo

```
GET {API_URL}/v1/box/{boxId}/{terminos de busqueda}?between=01-01-202_101-01-2022&currency=pesos
```

Los términos de búsqueda pueden incluir

- Descripción


- Usuario


- Agente


- Cliente


- Referencia


- nombre de usuario


- Leyenda


- fecha


- Caja


- remito



Tener en cuenta que puedo filtrar, sin necesariamente hacer match, en este estilo:

```
GET {API_URL}/v1/box/{boxId}/?between=01-01-202_101-01-2022&currency=pesos
```
