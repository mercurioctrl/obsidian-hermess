---
jira_key: "PED-51"
aliases: ["PED-51"]
summary: "APP - Refactor - Agregar cliente -> Integrar búsqueda automatica según padrón de afip"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-29 08:59"
updated: "2023-09-12 11:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-51"
---

# PED-51: APP - Refactor - Agregar cliente -> Integrar búsqueda automatica según padrón de afip

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-29 08:59 |
| Actualizado | 2023-09-12 11:47 |
| Etiquetas | ninguna |
| Jira | [PED-51](https://bluinc.atlassian.net/browse/PED-51) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes
- **is blocked by:** [[PED-45]] API - Feat - Integración con Padrones de AFIP por documento de cliente

## Descripcion

Según lo trabajado en [link](https://lioteam.atlassian.net/browse/PED-45)  debemos hacer que nuestro formulario de edición/creación de cliente (usaremos el mismo) tenga una “tool” en el input donde se inscribe el cuit para completar automáticamente los datos del cliente desde el padrón de AFIP

La idea es que al escribir y accionar algo (o bien con una pausa y enviar la request) auto-complete los datos, al menos aquellos que nos entrega el padrón.

[adjunto]
