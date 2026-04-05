---
jira_key: "NBWEB-19"
summary: "Mis pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-23 11:49"
updated: "2022-06-25 18:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-19"
---

# NBWEB-19: Mis pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-23 11:49 |
| Actualizado | 2022-06-25 18:49 |
| Etiquetas | ninguna |
| Jira | [NBWEB-19](https://bluinc.atlassian.net/browse/NBWEB-19) |

## Descripción

Se trata del recurso para listar los pedidos (ordenes de compra ya procesadas por un vendedor)

```
GET {{API_URL}}/v1/miCuenta/pedidos
```

El recurso de se obtiene de las tablas `[NewBytes_DBF].[dbo].[albclit]` y `[NewBytes_DBF].[dbo].[albclil]`

Y debe retornar un array de objetos



```json
[{
  status: 2,
  branch: '0002',
  albNumber: '00032323',
  clientName: 'Marbe Moreno',
  clientId: 43243,
  subtotal:
    {
    cotizacion:104.5,
    subtotalDollar:4324.56,
    subtotalDollarFinal:5232.72,
    subtotalPesosAr:454078.8,
    subtotalPesosArFinal:549434.38
    }
}
]
```

Todos los esquemas de tablas son similares a pedclit, y ya fueron explicados previamente
