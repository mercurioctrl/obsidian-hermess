---
jira_key: "NBWEB-413"
aliases: ["NBWEB-413"]
summary: "API - Refactor - Mi cuenta - Mis comprobantes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-19 08:09"
updated: "2022-07-21 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-413"
---

# NBWEB-413: API - Refactor - Mi cuenta - Mis comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-19 08:09 |
| Actualizado | 2022-07-21 10:41 |
| Etiquetas | ninguna |
| Jira | [NBWEB-413](https://bluinc.atlassian.net/browse/NBWEB-413) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta
- **is caused by:** [[NBWEB-414]] DB - Refactor - Se debe agregar un token que cambie periodicamente y se guarde para el usuarios

## Descripcion

Para el recurso 

```
GET {{API_URL}}/v1/miCuenta/comprobantes
```

Que retorna

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

Se debe modificar el parámetro `voucherUrl`

` voucherUrl: 'https://comprobantes.lio.red/?F=463852&show=1&token=49f0bad299687c62334182178bfd75d8'`

¿de donde sale el token entonces?

En la tabla `NB_WEB.dbo.usuarios_nb.softToken`
