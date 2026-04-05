---
jira_key: "COB-45"
aliases: ["COB-45"]
summary: "API - Feat - Filtros"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-04 12:24"
updated: "2022-10-25 09:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-45"
---

# COB-45: API - Feat - Filtros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-04 12:24 |
| Actualizado | 2022-10-25 09:02 |
| Etiquetas | ninguna |
| Jira | [COB-45](https://bluinc.atlassian.net/browse/COB-45) |

## Relaciones

- **Padre:** [[COB-8]] API - Feat - Listar pases
- **blocks:** [[COB-77]] APP - Feat - Listar pases

## Descripcion

Se debe contar con filtros por fecha en el siguiente estilo

```
GET {API_URL}/v1/passes/{terminos de busqueda}?between=01-01-202_101-01-2022&status=abierto&origin=dario&destiny=catriel&currency=pesos
```

Los términos de búsqueda pueden incluir

- Nombre del agente


- Nombre de usuario


- Descripcion


- Comentario


- origen


- destino


- moneda



Tener en cuenta que puedo filtrar, sin necesariamente hacer match, en este estilo:

```
GET {API_URL}/v1/passes/?between=01-01-202_101-01-2022&status=abierto&origin=dario&destiny=catriel&currency=pesos
```
