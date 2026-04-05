---
jira_key: "COB-86"
aliases: ["COB-86"]
summary: "API - Refactor - Se debe agregar un parametro llamado docuemtReference"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-01 13:58"
updated: "2022-10-04 15:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-86"
---

# COB-86: API - Refactor - Se debe agregar un parametro llamado docuemtReference

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-01 13:58 |
| Actualizado | 2022-10-04 15:33 |
| Etiquetas | ninguna |
| Jira | [COB-86](https://bluinc.atlassian.net/browse/COB-86) |

## Relaciones

- **Padre:** [[COB-3]] API - Feat - Listar movimiento por caja
- **blocks:** [[COB-85]] APP - Refactor - Agregar una columna para agrear un documento

## Descripcion

El parámetro se agrega al objeto de la lista y puede estar o no.

Sirve para mostrar números de los documentos a los que se hace referencia para poder identificarlos.

Si la linea muestra el movimiento de un cheque, muestra el numero de cheque.

Si la linea muestra una compra, muestra el numero de pedido.

Consultame si tenes dudas y buscamos de donde sacar los datos, pero seguro estan por las tablas de la familia que venimos usando.
