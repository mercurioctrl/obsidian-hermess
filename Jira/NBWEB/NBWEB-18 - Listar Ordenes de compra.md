---
jira_key: "NBWEB-18"
aliases: ["NBWEB-18"]
summary: "Listar Ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-23 11:49"
updated: "2022-06-26 09:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-18"
---

# NBWEB-18: Listar Ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-23 11:49 |
| Actualizado | 2022-06-26 09:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-18](https://bluinc.atlassian.net/browse/NBWEB-18) |

## Relaciones

- **Padre:** [[NBWEB-2 - API - Mi cuenta|NBWEB-2]] API - Mi cuenta
- **relates to:** [[NBWEB-87 - Maquetar y conectar Mi cuenta - Ordenes de compra|NBWEB-87]] Maquetar y conectar Mi cuenta - Ordenes de compra

## Descripcion

Se trata del recurso para listar las ordenes de compra

```
GET {{API_URL}}/v1/miCuenta/ordenesDeCompra
```

El recurso de se obtiene de las tablas `[NewBytes_DBF].[dbo].[pedclit]` y `[NewBytes_DBF].[dbo].[pedclil]`

Y debe retornar un array de objetos

```json
{
  status: 2,
  branch: '0002',
  orderNumber: '25632323',
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
```
