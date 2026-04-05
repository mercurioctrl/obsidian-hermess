---
jira_key: "PED-233"
aliases: ["PED-233"]
summary: "API - Feat - Facturar orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-06 10:17"
updated: "2023-11-06 13:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-233"
---

# PED-233: API - Feat - Facturar orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-06 10:17 |
| Actualizado | 2023-11-06 13:30 |
| Etiquetas | ninguna |
| Jira | [PED-233](https://bluinc.atlassian.net/browse/PED-233) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **blocks:** [[PED-234 - APP - Feat - Facturar orden|PED-234]] APP - Feat - Facturar orden

## Descripcion

Al igual que se hizo en su momento en expedición, debe poderse realizar una factura  a partir de un pedido (Solo puede hacerse esto si esta liquidado)

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
