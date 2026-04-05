---
jira_key: "LIO-452"
aliases: ["LIO-452"]
summary: "API - Refactor - Se debe sumar a el analisis de integridad los nuevos parametros de uso de dinero en wallet"
status: "Finalizada"
type: "Subtarea"
priority: "Low"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-12 16:06"
updated: "2025-12-05 05:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-452"
---

# LIO-452: API - Refactor - Se debe sumar a el analisis de integridad los nuevos parametros de uso de dinero en wallet

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Low |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-12 16:06 |
| Actualizado | 2025-12-05 05:51 |
| Etiquetas | ninguna |
| Jira | [LIO-452](https://bluinc.atlassian.net/browse/LIO-452) |

## Relaciones

- **Padre:** [[LIO-373]] Seguridad del checkout y protección de transacciones
- **action item from:** [[LIO-386]] API - Feat - Evaluar integridad de una compra respecto a su envio, pago y descuentos

## Descripcion

Sumaremos al análisis que ya se hace en [link](https://bluinc.atlassian.net/browse/LIO-386) 

los parametros agregados en 

- `[pedidosDetalle].walletUsedHere`


- `[pedidosCabeceraVendedor].walletUsedHere`


- `[pedidosCabeceraVendedor].walletAvailable`







Nota: Para que este recurso sea correcto se agrego a la tabla 

`LO.dbo.checkout_snapshot_data`  el campo `walletUsedHere` el cual se le asigna su valor cuando se utiliza PATCH pedidos/checkout desdes v3-legacy LO.
