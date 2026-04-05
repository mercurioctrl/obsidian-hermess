---
jira_key: "PED-1037"
aliases: ["PED-1037"]
summary: "API - Feat- Crear un comprobante manual para un cliente determinado"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-03 17:19"
updated: "2025-07-08 17:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1037"
---

# PED-1037: API - Feat- Crear un comprobante manual para un cliente determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-03 17:19 |
| Actualizado | 2025-07-08 17:53 |
| Etiquetas | ninguna |
| Jira | [PED-1037](https://bluinc.atlassian.net/browse/PED-1037) |

## Relaciones

- **Padre:** [[PED-1036]] Generar comprobantes manuales
- **blocks:** [[PED-1038]] APP - Feat- Crear un comprobante manual para un cliente determinado

## Descripcion

Haciendo uso del recurso del micro servicio de comprobantes (`{{API_URL}}/v2/CreateVoucher`)

Crearemos un nuevo recurso en nuestra API de pedidos como el siguiente

```
POST {{API_URL}}/v2/CreatemManualVoucher
```

```
{
"voucherType": "CREDITO" | "DEBITO" | "FACTURA",
  "clientId": 81406 ,
  "trade":[
    {
        "internalId": 119765,
        "units": 1,
        "ivaTax":21,
        "price": 265.936,
        "description": "MONITOR GAMER GIGABYTE 32 GS32QC CURVO",
        "internalTax": 10.51
    }
],
"impactCurrentAccount": true <-- Este parametro se agrega
}
```



Se debe realizar la siguiente acciones

1 - Validar que el usuario logueado tiene permisos para realizar la acción con `[NB_WEB].[dbo].[permisos_agente].CreatemManualVoucher`

2- Crear el comprobante fiscal según las especificaciones recibidas en el objeto

3 - Si puedo crearse el comprobante fiscal evaluaremos `impactCurrentAccount` para que en caso de que sea `true`impactar sobre la cuenta corriente del cliente en `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` (Como cuando hacemos una NC)
