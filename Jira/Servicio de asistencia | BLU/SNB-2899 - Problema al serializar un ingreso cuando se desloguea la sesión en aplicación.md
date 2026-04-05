---
jira_key: "SNB-2899"
aliases: ["SNB-2899"]
summary: "Problema al serializar un ingreso cuando se desloguea la sesión en aplicación de expedición"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-03-20 09:31"
updated: "2025-03-26 18:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2899"
---

# SNB-2899: Problema al serializar un ingreso cuando se desloguea la sesión en aplicación de expedición

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-20 09:31 |
| Actualizado | 2025-03-26 18:03 |
| Etiquetas | ninguna |
| Jira | [SNB-2899](https://bluinc.atlassian.net/browse/SNB-2899) |

## Relaciones

*Sin relaciones*

## Descripcion

Cuando se está serializando un ingreso de productos y la sesión se desloguea, a veces el foco de la ventana de login queda detrás del cuadro de serialización. En estos casos, no es posible ingresar el usuario ni la contraseña porque no se pueden seleccionar los campos de entrada, ni siquiera haciendo clic sobre ellos.

La única forma de resolverlo que yo vi, es utilizando herramientas el inspeccionador de elementos y eliminando manualmente elementos de la interfaz.

Adjunto una foto sacada por mi, del problema para referencia.

[adjunto]
