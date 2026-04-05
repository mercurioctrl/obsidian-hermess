---
jira_key: "PED-803"
aliases: ["PED-803"]
summary: "APP - Refactor - permitir edicion de comprobantes de pago en ciertos  estados con medio de pago diferido"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2024-08-23 12:58"
updated: "2024-08-25 23:44"
labels: ["blitz_test", "bugfix"]
jira_url: "https://bluinc.atlassian.net/browse/PED-803"
---

# PED-803: APP - Refactor - permitir edicion de comprobantes de pago en ciertos  estados con medio de pago diferido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2024-08-23 12:58 |
| Actualizado | 2024-08-25 23:44 |
| Etiquetas | blitz_test, bugfix |
| Jira | [PED-803](https://bluinc.atlassian.net/browse/PED-803) |

## Relaciones

- **causes:** [[SNB-2233]] SUBIR   COMPROBANTE DE PAGO

## Descripcion

pago diferido && status  === null, 1,2,3,4,10,11,12,14, se puede editar cargar comprobante (editado) 
o
pago diferido &&  status != 16,15,13,9
