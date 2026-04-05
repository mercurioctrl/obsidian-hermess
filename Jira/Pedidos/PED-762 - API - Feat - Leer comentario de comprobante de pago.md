---
jira_key: "PED-762"
aliases: ["PED-762"]
summary: "API - Feat - Leer comentario de comprobante de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-02 10:22"
updated: "2024-07-26 19:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-762"
---

# PED-762: API - Feat - Leer comentario de comprobante de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-02 10:22 |
| Actualizado | 2024-07-26 19:55 |
| Etiquetas | ninguna |
| Jira | [PED-762](https://bluinc.atlassian.net/browse/PED-762) |

## Relaciones

- **Padre:** [[PED-761 - Comprobantes de pago|PED-761]] Comprobantes de pago
- **blocks:** [[SNB-2150 - AGREGAR NOTAS EN LA SECCION DEL COMPROBANTE|SNB-2150]] AGREGAR NOTAS EN LA SECCION DEL COMPROBANTE
- **blocks:** [[PED-764 - APP - Refactor - Agregar comentario al modal de comprobante de pago|PED-764]] APP - Refactor - Agregar comentario al modal de comprobante de pago

## Descripcion

Agregaremos una nueva tabla similar a las otras tablas de comentarios, pero para los comprobantes de pago llamada `[NB_WEB].[dbo].[comentariosPedidosComprobantePago]`


```
GET {API_URL}/v1/paymentVoucherComments/{branch-order}
```

```
{
"order":"10360675",
"branch":"0002",
"comment":"test test test"
}
```

```
SELECT TOP (1000) [pedido]
      ,[comentario]
      ,[id]
      ,[sucursal]
  FROM [NB_WEB].[dbo].[comentariosPedidosComprobantePago]
```
