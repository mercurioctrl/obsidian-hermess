---
jira_key: "COB-64"
aliases: ["COB-64"]
summary: "API - Feat - Filtros listar clientes"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-25 11:22"
updated: "2022-10-31 12:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-64"
---

# COB-64: API - Feat - Filtros listar clientes

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-25 11:22 |
| Actualizado | 2022-10-31 12:03 |
| Etiquetas | ninguna |
| Jira | [COB-64](https://bluinc.atlassian.net/browse/COB-64) |

## Relaciones

- **Padre:** [[COB-53 - API - Feat - Listar clientes|COB-53]] API - Feat - Listar clientes

## Descripcion

```
GET {API_RUL}/v1/clients/{terminosDeBusqueda}?order=clientName&sort=desc
```

En principio vamos a filtrar en base al string sobre los campos

- `clientName`


- `clientBusinessName`


- `clientTaxNumber`


- `clientId`



Ademas como algo a parte vamos a agregar un selector para el orden para los siguientes parametros



- `clientName`


- `clientBusinessName`


- `clientId`


- `limitCheckBalanceAmount`


- `usedCheckBalanceAmount`


- `limitBalanceAmount`


- `usedBalanceAmount`
