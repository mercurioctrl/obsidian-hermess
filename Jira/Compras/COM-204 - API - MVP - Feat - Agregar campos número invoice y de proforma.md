---
jira_key: "COM-204"
aliases: ["COM-204"]
summary: "API - MVP - Feat - Agregar campos número invoice y de proforma"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-09-30 15:54"
updated: "2025-12-09 07:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-204"
---

# COM-204: API - MVP - Feat - Agregar campos número invoice y de proforma

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-09-30 15:54 |
| Actualizado | 2025-12-09 07:26 |
| Etiquetas | ninguna |
| Jira | [COM-204](https://bluinc.atlassian.net/browse/COM-204) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **has action item:** [[COM-203 - APP - MVP - Feat - Agregar campos número invoice y de proforma|COM-203]] APP - MVP - Feat - Agregar campos número invoice y de proforma
- **has action item:** [[COM-210 - API - Feat - agregar filtro para buscar por nro de invoice y proforma|COM-210]] API - Feat - agregar filtro para buscar por nro de invoice y proforma (voucherNumber y proformaInvoice)

## Descripcion

Usaremos estos atributos en la tabla [NewBytes_DBF].[dbo].[pedprot] para poder tomar nota de estos parametros temporales, para hacer referencia a documentos que contienen informacion.

*(Mas adelante cuando se genere *`[NewBytes_DBF].[dbo].[FACPROT]`* quedaran fijos, pero no ahora )*

```
PATCH {API_URL}/v1/providerOrder/{providerOrdeId}/head
```

```
{
  "voucherNumber": "AA9330SDFDKFF" <-- SE AGREGA
  "proformaInvoice": "asd5a41s5d" <-- SE AGREGA
}
```

## Parametros en la tabla que afectaremos

```
Se agregan dos parametros en estas tablas (en la segunda solo se traslada)
[NewBytes_DBF].[dbo].[pedprot].CSUFAC_TEMP
[NewBytes_DBF].[dbo].[pedprot].CSUPROF_TEMP
```

Criterios de Aceptación

- El recurso `PATCH {API_URL}/v1/providerOrder/{providerOrderId}/head` debe permitir actualizar `voucherNumber` y `proformaInvoice`.


- Los datos deben persistirse en los campos correspondientes de la tabla `[NewBytes_DBF].[dbo].[PedProT]`: 


- `invoiceNumber`


- `proformaInvoice`




- La implementación no debe afectar ni alterar el comportamiento de otros campos de la orden de compra.


- Se debe permitir que `voucherNumber` y `proformaInvoice` sean nulos si no hay valores definidos.








Relacionada con tarea 7 [link](https://docs.google.com/spreadsheets/d/18TUSaVG3bY_lMLunZ3kDCRlLnKpQV-_BPfrtbL4pHNA/edit?gid=723483997#gid=723483997)
