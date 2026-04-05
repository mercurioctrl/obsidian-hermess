---
jira_key: "EXP-344"
aliases: ["EXP-344"]
summary: "API - Feat - Mis comprobantes -> Facturar operacion"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-07-17 06:54"
updated: "2023-11-06 10:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-344"
---

# EXP-344: API - Feat - Mis comprobantes -> Facturar operacion

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-17 06:54 |
| Actualizado | 2023-11-06 10:17 |
| Etiquetas | ninguna |
| Jira | [EXP-344](https://bluinc.atlassian.net/browse/EXP-344) |

## Relaciones

- **Padre:** [[EXP-202 - Feat - Pestaña comprobantes|EXP-202]] Feat - Pestaña comprobantes

## Descripcion

Al igual que se hizo en su momento en expedición, debe poderse realizar una factura  a partir de un pedido

```
POST {API_URL}/v1/makeVoucher
```

```
{
"voucherTypeId":1,
"clientId":53386,
"pedido":"X000200568377",
"iibbPerception":"0.00"
}
```

Devuelve 

```
{
    "msg": "Factura emitida correctamente",
    "success": true,
    "CAE": "73458064779943",
    "voucherId": "518317",
    "token": "4ea38286523bfefa58151869f9d07f",
    "cfactura": "B000400039728"
}
```
