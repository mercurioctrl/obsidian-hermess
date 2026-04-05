---
jira_key: "EXP-362"
aliases: ["EXP-362"]
summary: "Refactor - Parece no tener el voucherId, al menos en algunos casos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-08-25 15:14"
updated: "2023-09-04 16:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-362"
---

# EXP-362: Refactor - Parece no tener el voucherId, al menos en algunos casos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-25 15:14 |
| Actualizado | 2023-09-04 16:58 |
| Etiquetas | ninguna |
| Jira | [EXP-362](https://bluinc.atlassian.net/browse/EXP-362) |

## Relaciones

- **Padre:** [[EXP-202]] Feat - Pestaña comprobantes
- **blocks:** [[SNB-1141]] facturacion 

## Descripcion

Por alguna razón, estoy viendo casos donde en la pestaña comprobantes de Expedición

[adjunto]
Al hacer clic en la factura para verla, envio un faltante en el payload, lo que resulta en un racurso como este

[https://ms-comprobantes.lio.red/v2/F/undefined/bd54e08567cc4d03b4ee4a7c69f7c7](https://ms-comprobantes.lio.red/v2/F/undefined/bd54e08567cc4d03b4ee4a7c69f7c7)

Cuando en realidad debería ser

[https://ms-comprobantes.lio.red/v2/F/512979/bd54e08567cc4d03b4ee4a7c69f7c7](https://ms-comprobantes.lio.red/v2/F/512979/bd54e08567cc4d03b4ee4a7c69f7c7)
