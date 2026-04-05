---
jira_key: "LIO-232"
aliases: ["LIO-232"]
summary: "API - Feat - Listar movimientos en billetera"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-24 08:10"
updated: "2025-03-12 10:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-232"
---

# LIO-232: API - Feat - Listar movimientos en billetera

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-24 08:10 |
| Actualizado | 2025-03-12 10:18 |
| Etiquetas | ninguna |
| Jira | [LIO-232](https://bluinc.atlassian.net/browse/LIO-232) |

## Relaciones

- **Padre:** [[LIO-231 - Billetera|LIO-231]] Billetera
- **has action item:** [[LIO-271 - APP - Feat - Visualización de la Billetera del Usuario|LIO-271]] APP - Feat - Visualización de la Billetera del Usuario

## Descripcion

La idea es poder mostrar una lista con los movimientos de cuenta corriente de un determinado usuario de libre opción, en función de su consecuente cliente dentro de NB.

```
GET {API_V4}/wallet/transactions
```

```
{
  "transactions": [
    {
      "transactionId": "12345",
      "amount": 100.50,
      "currency": "ARS",
      "concept": "Compra #43243 Monitor Samguns F3454",
      "date": "2024-02-24T15:30:00Z",
      "transactionType": "income"
    },
    {
      "transactionId": "12346",
      "amount": -50.00,
      "currency": "ARS",
      "concept": "Devolucion al usuario",
      "date": "2024-02-23T10:00:00Z",
      "transactionType": "expense"
    },
    {
      "transactionId": "12347",
      "amount": 25.00,
      "currency": "ARS",
      "concept": "Airdrop",
      "date": "2024-02-22T08:45:00Z",
      "transactionType": "income"
    }
  ],
  "pagination": {
    "limit": 50,
    "offset": 0,
    "total": 120
  }
}
```

Este recurso es similar conceptualmente a https://api.orders.lio.red/v1/currentAccount/{clientId} solo que en este caso solo mostraremos los movimientos generados en libreOpcion para evitar conflictos y tener mayor control para las cuentas mixtas

Para poder identificar estos movimientos de manera exacta crearemos un parámetro nuevo en la tabla `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` llamado `HMAC`



El valor del campo `transactionType`, corresponde al simbolo del respectivo TR_CODIGO del movimiento que puede ser negativo o positivo. `“+" = income` `“-" = expense`. los tr_codigo hacen referencia a la tabla. `NEW_BYTES.[dbo].GL_TRANSACCIONES`
