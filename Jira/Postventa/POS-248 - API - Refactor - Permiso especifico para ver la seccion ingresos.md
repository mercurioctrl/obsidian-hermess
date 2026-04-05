---
jira_key: "POS-248"
aliases: ["POS-248"]
summary: "API - Refactor - Permiso especifico para ver la seccion ingresos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-20 10:10"
updated: "2023-06-05 15:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-248"
---

# POS-248: API - Refactor - Permiso especifico para ver la seccion ingresos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-20 10:10 |
| Actualizado | 2023-06-05 15:02 |
| Etiquetas | ninguna |
| Jira | [POS-248](https://bluinc.atlassian.net/browse/POS-248) |

## Relaciones

- **Padre:** [[POS-4 - API - Feat - Listar ingresos de postventa|POS-4]] API - Feat - Listar ingresos de postventa
- **blocks:** [[SNB-642 - usuarios autorizados para ingreso de mercaderia|SNB-642]] usuarios autorizados para ingreso de mercaderia
- **blocks:** [[POS-249 - APP - Refactor - Ocultar ingresos segun permiso especifico|POS-249]] APP - Refactor - Ocultar ingresos segun permiso especifico

## Descripcion

Agregaremos un permiso especifico para ingresar seriales nuevos (ingreso de mercadería).

Por el momento solo lo aplicaremos a la carga de seriales.

Para esto agregaremos una columna en `exp_upload_serials` en la tabla`[NB_WEB].[dbo].[permisos_agente]`
