---
jira_key: "EXP-394"
aliases: ["EXP-394"]
summary: "APP - Seleccionar y enviar para imprimir números de serie específicos en un payload - Actualizar payload"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-01-31 01:45"
updated: "2024-02-07 13:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-394"
---

# EXP-394: APP - Seleccionar y enviar para imprimir números de serie específicos en un payload - Actualizar payload

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-31 01:45 |
| Actualizado | 2024-02-07 13:42 |
| Etiquetas | ninguna |
| Jira | [EXP-394](https://bluinc.atlassian.net/browse/EXP-394) |

## Relaciones

- **Padre:** [[EXP-5]] Ingreso de mercaderia
- **blocks:** [[EXP-393]] APP - Feat - Seleccionar y enviar para imprimir números de serie especificos en un payload

## Descripcion

Al momento de intentar imprimir los seriales seleccionados me aparece un error de parte del back

[adjunto]
Dato extra:
Esto puede ser debido a que la API está esperando que los seriales estén contenidos en el parámetro `serials`

```
"serials": ["9LX2612Q30305","9LX2730Q30399"]
```
