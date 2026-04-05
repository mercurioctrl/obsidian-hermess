---
jira_key: "COB-489"
aliases: ["COB-489"]
summary: "API - Feat - Ver comprobante de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-03-01 08:32"
updated: "2024-03-19 11:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-489"
---

# COB-489: API - Feat - Ver comprobante de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-01 08:32 |
| Actualizado | 2024-03-19 11:57 |
| Etiquetas | ninguna |
| Jira | [COB-489](https://bluinc.atlassian.net/browse/COB-489) |

## Relaciones

- **Padre:** [[COB-487 - Feat - Cobrables - Comprobantes de pago|COB-487]] Feat - Cobrables -> Comprobantes de pago
- **blocks:** [[COB-490 - APP - Feat - Agregar accionable para ver comprobante pago de mp|COB-490]] APP - Feat - Agregar accionable para ver comprobante / pago de mp
- **blocks:** [[COB-491 - APP - Feat - Mostrar Modal de comprobante de pago|COB-491]] APP - Feat - Mostrar Modal de comprobante de pago
- **relates to:** [[PED-585 - API - Feat - Agregar comprobantes de pago|PED-585]] API - Feat - Agregar comprobantes de pago
- **relates to:** [[COB-498 - API - Refactor - Ver comprobante de pago - Apuntar a NB|COB-498]] API - Refactor - Ver comprobante de pago - Apuntar a NB

## Descripcion

```
GET {API_URL}/v1/paymentVoucher/{branch-order}
```

Agregaremos un recurso igual al que usamos en el sistema de pedidos para visualizar los comprobantes de pago, pero esa vez utilizaremos branch y order para encontrar el comprobante.

```
{
    "id": 71000,
    "nameOwner": "Alfredo Maximiliano Britez",
    "document": "33597728",
    "operationNumber": "32985994198",
    "fileImg": "https:\/\/static.nb.com.ar\/img\/75b677d64492baebfb2c6f44c7dd9088.jpg",
    "cbu": "0070035130004028616862",
    "internalOperationNumber": 73343381612,
    "creationDate": "2024-02-29 17:02:44",
    "updateDate": null,
    "noperacion": "",
    "statusIdOrder": 4
}
```
