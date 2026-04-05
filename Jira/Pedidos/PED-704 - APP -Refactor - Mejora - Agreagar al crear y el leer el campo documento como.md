---
jira_key: "PED-704"
aliases: ["PED-704"]
summary: "APP -Refactor - Mejora - Agreagar al crear y el leer el campo documento como opcional y tambien el banco destino de la transferencia"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2024-04-29 12:20"
updated: "2024-04-30 21:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-704"
---

# PED-704: APP -Refactor - Mejora - Agreagar al crear y el leer el campo documento como opcional y tambien el banco destino de la transferencia

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2024-04-29 12:20 |
| Actualizado | 2024-04-30 21:01 |
| Etiquetas | ninguna |
| Jira | [PED-704](https://bluinc.atlassian.net/browse/PED-704) |

## Relaciones

- **Padre:** [[PED-584]] Comprobantes de pago
- **is blocked by:** [[PED-705]] API - Refactor - agregar campo destino bancario para recurso de comprobante
- **relates to:** [[PED-707]] APP - Modal de Comprobante - Oportunidad de mejora en legibilidad del texto

## Descripcion

Al crear agregar el campo document
al leer, mostrar banco destino y documento


```
[
    {
        "id": 2405228,
        "nameOwner": "Gprueba1145",
        "document": null,---> NUEVO DATO
        "operationNumber": "10332765",
        "fileImg": "https://static.nb.com.ar/img/731da603219cb848041e35bb9b43806f.png",
        "cbu": "1033276510332765103327",
        "internalOperationNumber": 10332,
        "creationDate": "2024-04-28 23:45:41",
        "updateDate": "2024-04-28 23:46:11",
        "noperacion": null,
        "statusIdOrder": null,
        "destinationBankId": 15           -----> NUEVO DATO
        "destinationBankName": "mercadopago"  -----> NUEVO DATO
    }
]
```
