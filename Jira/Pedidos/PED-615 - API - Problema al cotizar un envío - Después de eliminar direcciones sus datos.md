---
jira_key: "PED-615"
aliases: ["PED-615"]
summary: "API - Problema al cotizar un envío - Después de eliminar direcciones sus datos siguen apareciendo"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-03-14 19:43"
updated: "2024-03-18 17:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-615"
---

# PED-615: API - Problema al cotizar un envío - Después de eliminar direcciones sus datos siguen apareciendo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-14 19:43 |
| Actualizado | 2024-03-18 17:17 |
| Etiquetas | ninguna |
| Jira | [PED-615](https://bluinc.atlassian.net/browse/PED-615) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **blocks:** [[PED-592]] APP - Refactor -  Problema al cotizar un envio
- **blocks:** [[PED-611]] API - Refactor - condigo postal a mostrar en diferentes casos

## Descripcion

Al eliminar las direcciones del cliente siguen apareciendo datos de dirección en el listado de ordenes

[adjunto]

Dato extra:
Al eliminar las direcciones del cliente `[NB_WEB].[dbo].[dircli]`no se eliminan en `[NewBytes_DBF].[dbo].[dircli]` por lo que al traer el listado de ordenes aparecen los datos de dirección.

[adjunto]
