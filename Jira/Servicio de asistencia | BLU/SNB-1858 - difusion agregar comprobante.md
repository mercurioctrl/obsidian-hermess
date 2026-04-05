---
jira_key: "SNB-1858"
aliases: ["SNB-1858"]
summary: "difusion agregar comprobante"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Pedidos Jira"
created: "2024-04-30 15:02"
updated: "2024-04-30 17:02"
labels: ["blitz_test", "bugfix"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-1858"
---

# SNB-1858: difusion agregar comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Pedidos Jira |
| Creado | 2024-04-30 15:02 |
| Actualizado | 2024-04-30 17:02 |
| Etiquetas | blitz_test, bugfix |
| Jira | [SNB-1858](https://bluinc.atlassian.net/browse/SNB-1858) |

## Relaciones

*Sin relaciones*

## Descripcion

El banco destino del comprobante de pago debe ser igual al banco destino de la liquidación; caso contrario, se debe desliquidar y liquidar nuevamente asignándole el banco destino correcto.


eso pusieron el el grupo de difusion
mas de una vez no sabemos anticipadamente a que banco depositan...y debemos pasar la factura para que pasen el pagoi.
tambien a veces es una sumatoria de depopsitos/ transferencias de diferentes cuentas... como setria en ese caso? que va a diferenmtes bancos el dinero?
Usuario: andi
