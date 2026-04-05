---
jira_key: "PED-653"
aliases: ["PED-653"]
summary: "API - Feat - Hacer NC y Desvincular para refacturar un comprobante"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-03 13:14"
updated: "2024-04-30 13:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-653"
---

# PED-653: API - Feat - Hacer NC y Desvincular para refacturar un comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-03 13:14 |
| Actualizado | 2024-04-30 13:50 |
| Etiquetas | ninguna |
| Jira | [PED-653](https://bluinc.atlassian.net/browse/PED-653) |

## Relaciones

- **Padre:** [[PED-98]] Feat - Listar comprobantes
- **blocks:** [[PED-654]] APP - Feat - Hacer NC y Desvincular para refacturar un comprobante
- **blocks:** [[SNB-1704]] ERA FACTURA A y salio B 
- **blocks:** [[SNB-1695]] Por favor Re facturar
- **is blocked by:** [[PED-688]] API - Nota de crédito para refacturar - No se reconoce el método implementado
- **is blocked by:** [[PED-697]] API - Nota de crédito para refacturar - Registro de usuario

## Descripcion

Haremos un refactor tome un comprobante, y te permita "Hacer nota de crédito para refacturar"

```
POST {API_URL}/v1/creditToRebill
```

Osea que implica ese tipo de nota de creído especifica

1- Es solo fiscal, es decir que no toca saldo en la cuenta del cliente.
2- No toca Stock, es decir que no afecta para nada la cantidad de stock no producto
3- Libera el pedido de su factura para poder volver a facturarlo (Se debe marcar `albclit.lfacturado = false` y liberar `cnumalb` e `ID_NROREMENC_CLI`)

Recordar marcar en la cabecera de las facturas que usuario realiza la acción

Solo puede hacerse esto en comprobantes existentes, que no sean NOTA DE CREDITO, NI NOTA DE DEBITO. Solo facturas.
