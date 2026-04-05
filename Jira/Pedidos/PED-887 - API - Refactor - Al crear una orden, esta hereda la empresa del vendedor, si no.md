---
jira_key: "PED-887"
aliases: ["PED-887"]
summary: "API - Refactor - Al crear una orden, esta hereda la empresa del vendedor, si no esta disponible, hereda del cliente."
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-27 11:58"
updated: "2024-11-29 03:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-887"
---

# PED-887: API - Refactor - Al crear una orden, esta hereda la empresa del vendedor, si no esta disponible, hereda del cliente.

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-27 11:58 |
| Actualizado | 2024-11-29 03:23 |
| Etiquetas | ninguna |
| Jira | [PED-887](https://bluinc.atlassian.net/browse/PED-887) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes

## Descripcion

Haremos un refactor  para que al crear una orden esta quede marcada según la empresa a la que corresponde.

Para esto, usaremos la siguiente jerarquía.

Guardaremos en `[NewBytes_DBF].[dbo].[pedclit].companyCode` la empresa que se encuentra en `[NewBytes_DBF].[dbo].[agentes].[companyCode]` , en caso de no estar disponible o ser `null` lo tomaremos de `[NewBytes_DBF].[dbo].[clientes].CODEMP`

En caso de este ultimo, ser `null`, lo dejaremos `null`

```
POST {API_URL}/v1/orders
```

```
{
"clientId":26806,
"branch":"0002"
}
```
