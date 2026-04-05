---
jira_key: "COM-210"
aliases: ["COM-210"]
summary: "API - Feat - agregar filtro para buscar por nro de invoice y proforma (voucherNumber y proformaInvoice)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-10-01 18:07"
updated: "2025-12-10 13:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-210"
---

# COM-210: API - Feat - agregar filtro para buscar por nro de invoice y proforma (voucherNumber y proformaInvoice)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-01 18:07 |
| Actualizado | 2025-12-10 13:51 |
| Etiquetas | ninguna |
| Jira | [COM-210](https://bluinc.atlassian.net/browse/COM-210) |

## Relaciones

- **Padre:** [[COM-9 - Listar ordenes de compra|COM-9]] Listar ordenes de compra
- **has action item:** [[COM-209 - APP - MVP - Feat - agregar filtro para buscar por nro de invoice y proforma|COM-209]] APP - MVP - Feat - agregar filtro para buscar por nro de invoice y proforma (voucherNumber y proformaInvoice)
- **action item from:** [[COM-204 - API - MVP - Feat - Agregar campos número invoice y de proforma|COM-204]] API - MVP - Feat - Agregar campos número invoice y de proforma

## Descripcion

Refactorizaremos el recurso 

```
GET {API_URL}/v1/providerOrder?&proformaInvocie={proformaInvocie}&voucherNumber={voucherNumber}
```

Se deben agregar los filtros proformaInvocie y voucherNumber para buscar en los campos de la tabla `[NewBytes_DBF].[dbo].[PedProT].CSUFAC_TEMP` y `[NewBytes_DBF].[dbo].[PedProT].CSUPROF_TEMP` respectivamente



---

Borrador inicial de la historia

Relacionada con tarea 32 [link](https://docs.google.com/spreadsheets/d/18TUSaVG3bY_lMLunZ3kDCRlLnKpQV-_BPfrtbL4pHNA/edit?gid=723483997#gid=723483997) 

agregar filtros

`voucherNumber`

`proformaInvoice`

```
https://gamma.api.purchases.lio.red/v1/providerOrder?companyCode=4&proformaInvocie=5555
```

```
https://gamma.api.purchases.lio.red/v1/providerOrder?companyCode=4&voucherNumber=5555
```

 Avance con esta descripción separandolo del search general para no realentizar la busqueda, si ves que esta mal, a la vuelta lo corrijo segun la nueva descripcion de la tarea
