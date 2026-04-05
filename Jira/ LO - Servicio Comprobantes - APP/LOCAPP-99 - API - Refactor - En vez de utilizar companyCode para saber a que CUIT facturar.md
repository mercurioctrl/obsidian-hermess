---
jira_key: "LOCAPP-99"
aliases: ["LOCAPP-99"]
summary: "API - Refactor - En vez de utilizar companyCode para saber a que CUIT facturar es voucherCompanyCode"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-26 10:09"
updated: "2026-02-11 13:38"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-99"
---

# LOCAPP-99: API - Refactor - En vez de utilizar companyCode para saber a que CUIT facturar es voucherCompanyCode

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-26 10:09 |
| Actualizado | 2026-02-11 13:38 |
| Etiquetas | esperandoDependencia |
| Jira | [LOCAPP-99](https://bluinc.atlassian.net/browse/LOCAPP-99) |

## Relaciones

- **Padre:** [[LOCAPP-23 - Generar un comprobante|LOCAPP-23]] Generar un comprobante
- **action item from:** [[PED-1283 - API - Refactor - Agregar nuevo parámetro voucherCompanyCode|PED-1283]] API - Refactor - Agregar nuevo parámetro voucherCompanyCode

## Descripcion

Según lo definido previamente en [[[PED-1283]]](https://bluinc.atlassian.net/browse/PED-1283), se actualizará la lógica de generación y gestión de comprobantes para que utilice el atributo `voucherCompanyCode` en lugar de `companyCode`.

Este cambio permite separar explícitamente la empresa de pertenencia del cliente de la empresa utilizada para facturación, evitando inconsistencias en los casos en los que un usuario pertenece a una empresa pero, por requerimientos específicos, debe facturar a través de otra.
