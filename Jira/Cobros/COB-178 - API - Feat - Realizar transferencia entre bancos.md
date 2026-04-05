---
jira_key: "COB-178"
aliases: ["COB-178"]
summary: "API - Feat - Realizar transferencia entre bancos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-10-19 08:55"
updated: "2022-10-27 08:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-178"
---

# COB-178: API - Feat - Realizar transferencia entre bancos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-19 08:55 |
| Actualizado | 2022-10-27 08:38 |
| Etiquetas | ninguna |
| Jira | [COB-178](https://bluinc.atlassian.net/browse/COB-178) |

## Relaciones

- **Padre:** [[COB-16]] Cuentas bancarias
- **Subtarea:** [[COB-192]] API - Research - Buscar si existen tablas de movimientos de banco
- **Subtarea:** [[COB-248]] API - Refactor - Alterar saldo proveedor, en caso de que el concepto sea un "pago de factura" o "pago proveedor"
- **Subtarea:** [[COB-249]] APP - Refactor - Agregar al modal de salida un selector de proveedor si el id del concepto es 3 o 35

## Descripcion

```
POST {API_URL}/v1/bankTransfer
```

```
[
{
  ammount: 250.33,
  paymentMethodId:2,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5,
  originBankId: 1,
  tergetBankId: 2
},
{
  ammount: 250.33,
  paymentMethodId:2,
  reference: "Este es un texto de referencia.",
  currencyQuote: 140.5,
  originBankId: 1,
  tergetBankId: 2
}
}
```

Esto solo es un movimiento entre bancos, por lo tanto impacta en saldos de bancos
