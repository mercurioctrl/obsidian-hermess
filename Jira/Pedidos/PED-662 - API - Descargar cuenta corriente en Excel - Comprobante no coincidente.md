---
jira_key: "PED-662"
aliases: ["PED-662"]
summary: "API - Descargar cuenta corriente en Excel - Comprobante no coincidente"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-10 20:30"
updated: "2024-04-23 23:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-662"
---

# PED-662: API - Descargar cuenta corriente en Excel - Comprobante no coincidente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-10 20:30 |
| Actualizado | 2024-04-23 23:41 |
| Etiquetas | ninguna |
| Jira | [PED-662](https://bluinc.atlassian.net/browse/PED-662) |

## Relaciones

- **Padre:** [[PED-15]] Clientes
- **blocks:** [[PED-651]] Descargar excel cta corriente

## Descripcion

Creo que el número de comprobante podría no ser el correcto. Además, según tengo entendido, el pedido debería estructurarse con el formato número de sucursal-remito.

[adjunto]
```
{
  "date": "2024-04-09",
  "albNumber": "00569076", <---------------------- ***
  "total": -331.424857,
  "currencyQuote": 882.5,
  "agent": "Seba",
  "agentDescription": "Web Sistema",
  "branch": "0002",
  "comment": "Gprueba1921",
  "currentBalance": -570.759017,
  "currencyQuoteDay": 882.5,
  "currencyQuoteDayCheck": 882.5,
  "subTotal": -331.424857,
  "totalPesos": -292482.43630249996,
  "id": 762981,
  "notFiscalId": null,
  "voucherId": null, <---------------------------- ***
  "token": null,
  "availableBalance": -570.759017,
  "dollarQuote": null,
  "availableBalancePesos": -503694.8325025,
  "trCode": 24,
  "trName": "Remitos - Ventas",
  "order": "10332640" <--------------------------- ***
}
```

---

Actualización 19/04/24

- El comprobante no se visualiza cuando este no es fiscal. Quiero pensar que se deberían considerar todos los comprobantes, si no es el caso ignora este punto


- En el pedido aparece el número de orden en lugar del número de pedido


- Sugiero como mejora reemplazar los espacios vacíos por el valor cero, así como en el modal de clientes



[adjunto]
[adjunto]
