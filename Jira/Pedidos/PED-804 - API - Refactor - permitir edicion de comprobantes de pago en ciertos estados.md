---
jira_key: "PED-804"
aliases: ["PED-804"]
summary: "API - Refactor - permitir edicion de comprobantes de pago en ciertos  estados con medio de pago diferido"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-08-23 13:37"
updated: "2024-08-25 23:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-804"
---

# PED-804: API - Refactor - permitir edicion de comprobantes de pago en ciertos  estados con medio de pago diferido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-08-23 13:37 |
| Actualizado | 2024-08-25 23:50 |
| Etiquetas | ninguna |
| Jira | [PED-804](https://bluinc.atlassian.net/browse/PED-804) |

## Relaciones

- **Padre:** [[PED-5 - Comprobantes|PED-5]] Comprobantes
- **blocks:** [[SNB-2233 - SUBIR COMPROBANTE DE PAGO|SNB-2233]] SUBIR   COMPROBANTE DE PAGO

## Descripcion

pago diferido && status === null, 1,2,3,4,10,11,12,14, se puede editar cargar comprobante (editado) 
o
pago diferido && status != 16,15,13,9
