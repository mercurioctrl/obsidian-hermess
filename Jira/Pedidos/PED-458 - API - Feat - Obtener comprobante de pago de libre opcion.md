---
jira_key: "PED-458"
aliases: ["PED-458"]
summary: "API - Feat - Obtener comprobante de pago de libre opcion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-08 12:25"
updated: "2024-01-16 11:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-458"
---

# PED-458: API - Feat - Obtener comprobante de pago de libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-08 12:25 |
| Actualizado | 2024-01-16 11:24 |
| Etiquetas | ninguna |
| Jira | [PED-458](https://bluinc.atlassian.net/browse/PED-458) |

## Relaciones

- **Padre:** [[PED-329]] Listado de ordenes
- **blocks:** [[PED-485]] APP - Feat - Mostrar modal con info de comprobante de pago

## Descripcion

Crearemos un recurso para poder obtener informacion del comprobante de pago bancario del cliente de libre opción. El mismo contendrá, ademas de la informacion que se muestra mas abajo, la imagen del mismo.

```
GET {API_URL}/v1/paymentVoucher/{idLo}
```

```
SELECT TOP (1) A.[id]
    , [titular] AS nameOwner
    , [documento] AS document
    , [nroOperacion] AS operationNumber
    , [archivo] AS fileImg
    , cbu
    , operacionInterna AS internalOperationNumber
    , CONVERT(VARCHAR, A.fechaCreacion, 120) AS creationDate
    , [fechaActualizacion] AS updateDate
    , cop.[noperacion]
    , ID_STATUS AS statusIdOrder
FROM [LO].[dbo].[pedidosCabeceraComprobantePago] A
LEFT JOIN LO.dbo.pedidosCabeceraVendedor C
    ON C.pedidoCabeceraID = A.pedidoCabeceraID
LEFT JOIN NewBytes_DBF.dbo.pedclit D
    ON D.cnumped = C.pedclitID
LEFT JOIN NewBytes_DBF.dbo.albclit E
    ON E.cnumped = D.cnumped
LEFT JOIN [NEW_BYTES].[dbo].[MS_VENTAS_REMITOS] F
    ON F.REMITO_FP = E.cnumalb
LEFT JOIN LO.dbo.[pedidosDetallePaqueteComprobantePagoOperaciones] cop
    ON C.id = cop.[pedidoCabeceraPaqueteID]
WHERE A.pedidoCabeceraID = ?
```
