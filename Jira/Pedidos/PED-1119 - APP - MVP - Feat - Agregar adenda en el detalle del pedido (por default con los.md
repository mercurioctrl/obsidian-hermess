---
jira_key: "PED-1119"
aliases: ["PED-1119"]
summary: "APP - MVP - Feat - Agregar adenda en el detalle del pedido (por default con los datos bancarios de Laset)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-09-29 09:55"
updated: "2025-10-20 10:49"
labels: ["MVPLaset", "esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1119"
---

# PED-1119: APP - MVP - Feat - Agregar adenda en el detalle del pedido (por default con los datos bancarios de Laset)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-09-29 09:55 |
| Actualizado | 2025-10-20 10:49 |
| Etiquetas | MVPLaset, esperandoDependencia |
| Jira | [PED-1119](https://bluinc.atlassian.net/browse/PED-1119) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **action item from:** [[PED-1120 - API - MVP - Feat - Agregar adenda en el detalle del pedido (por default con los|PED-1120]] API - MVP - Feat - Agregar adenda en el detalle del pedido (por default con los datos bancarios de Laset)

## Descripcion

Basándonos en lo realizado en [link](https://bluinc.atlassian.net/browse/PED-1120)  en el modal de **Orden** se debe **visualizar la adenda** asociada al `companyCode` **sin agrandar** innecesariamente el modal.
Opciones de UI (elegir la que resulte más limpia tras spike corto de diseño):

- **Dos columnas** en la fila del campo de comentario:

- Columna izquierda: **Comentario interno** (como hoy).


- Columna derecha: **Adenda (solo lectura por defecto)** con botón *Editar* (si permisos).




- **Adenda colapsable**: un **chip/badge “Adenda”** al lado del título “Cotización” o del campo Comentario que abre/cierra un **panel lateral o dropdown** con el contenido.


- **Aprovechar placeholder/tooltip**: si hay adenda, mostrar un **icono ℹ︎ “Adenda”** con **tooltip + botón “Ver completa”** (modal/side-panel).



> Nota educativa: incluir **copy** visible tipo “⚠︎ La adenda es visible para el cliente” para evitar que escriban información interna allí.


[adjunto]
## Reglas/Comportamiento

- Si **existe** adenda para `companyCode`, mostrarla (truncada a 3–5 líneas) con opción “Ver más”.


- Si **no existe**, mostrar estado vacío: “No hay adenda definida”.


- **No bloquear** el flujo: la UI no debe crecer en alto; usar truncado/colapso.
