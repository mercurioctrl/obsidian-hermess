---
jira_key: "SNB-3681"
aliases: ["SNB-3681"]
summary: "Facturacion Error 500 al generar facturas"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Pedidos Jira"
created: "2026-02-12 12:49"
updated: "2026-03-26 09:08"
labels: ["Facturación"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-3681"
---

# SNB-3681: Facturacion Error 500 al generar facturas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Pedidos Jira |
| Creado | 2026-02-12 12:49 |
| Actualizado | 2026-03-26 09:08 |
| Etiquetas | Facturación |
| Jira | [SNB-3681](https://bluinc.atlassian.net/browse/SNB-3681) |

## Relaciones

*Sin relaciones*

## Descripcion

No puedo realizar facturas desde el sistema.
Al intentar facturar, arroja el siguiente error:
Server error: POST http://ms-comprobantes.lio.red/v2/CreateVoucher
 resulted in a 500 Internal Server Error response:
"str_replace(): Argument #3 ($subject) must be of type array|string, null given"

Según me indicó Juan, ya se había generado un reporte anteriormente por este mismo inconveniente, pero el error volvió a presentarse.

Actualmente no puedo emitir ninguna factura, ya que el error se produce en todos los intentos.


Usuario: cgarcia
