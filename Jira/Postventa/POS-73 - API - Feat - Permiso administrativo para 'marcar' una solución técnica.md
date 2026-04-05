---
jira_key: "POS-73"
aliases: ["POS-73"]
summary: "API - Feat - Permiso administrativo para 'marcar' una solución técnica "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-18 09:33"
updated: "2022-10-27 17:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-73"
---

# POS-73: API - Feat - Permiso administrativo para 'marcar' una solución técnica 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-18 09:33 |
| Actualizado | 2022-10-27 17:36 |
| Etiquetas | ninguna |
| Jira | [POS-73](https://bluinc.atlassian.net/browse/POS-73) |

## Relaciones

- **Padre:** [[POS-40]] API - Feat - Definir solucion tecnica

## Descripcion

Utilizando la tabla `[NB_WEB].[dbo].[permisos_agente]` validaremos la acción [link](https://lioteam.atlassian.net/browse/POS-40)  con una columna llamada `postventa_solucion.`

En caso de no estar validada la petición, devolver un `401` y un mensaje de referencia.
