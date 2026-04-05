---
jira_key: "PED-793"
aliases: ["PED-793"]
summary: "API - Feat - Filtrar clientes por empresa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-12 11:55"
updated: "2024-08-15 03:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-793"
---

# PED-793: API - Feat - Filtrar clientes por empresa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-12 11:55 |
| Actualizado | 2024-08-15 03:44 |
| Etiquetas | ninguna |
| Jira | [PED-793](https://bluinc.atlassian.net/browse/PED-793) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **is blocked by:** [[PED-24 - API - Repository - Empresas|PED-24]] API - Repository - Empresas 
- **blocks:** [[PED-794 - APP - Feat - Filtrar clientes por empresa|PED-794]] APP - Feat - Filtrar clientes por empresa

## Descripcion

Agregaremos el parámetro `companyCode` para poder filtrar los clientes por empresa 

```
GET {API_URL}/v1/clients?companyCode=4
```



Se filtra según el parámetro `[NewBytes_DBF].[dbo].[clientes].CODEMP`

Si no se envía el filtro o esta null, entonces muestro todo.
