---
jira_key: "NBWEB-20"
aliases: ["NBWEB-20"]
summary: "Mis comprobantes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-23 11:49"
updated: "2022-06-25 18:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-20"
---

# NBWEB-20: Mis comprobantes

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
| Jira | [NBWEB-20](https://bluinc.atlassian.net/browse/NBWEB-20) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta
- **blocks:** [[NBWEB-26]] Detalle Mis Comprobantes

## Descripcion

Se trata del recurso para listar los comprobantes fiscales o facturas 

```
GET {{API_URL}}/v1/miCuenta/comprobantes
```

El recurso de se obtiene de las tablas `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado]` y `[NewBytes_DBF].[dbo].[FP_FactWebCliDetalle]`

Y debe retornar un array de objetos

```json
[{
  cae: '61298741561088',
  branch: '0004',
  invoiceNumber: '25632323',
  invoiceType: 'A',
  invoiceDate: '23/04/2022'
  invoiceLabel: 'Factura',
  clientName: 'Marbe Moreno',
  clientId: 43243,
  voucherID: 463852,
  voucherUrl: 'https://comprobantes.lio.red/?F=463852&show=1',
  subtotal:
    {
    cotizacion:104.5,
    subtotal:4324.56,
    perceptionsIIBB: 45.55,
    subtotalIva:5232.72,
    subtotalFinal:5232.72,
    currency: 'DOL'
    }
}
]
```
