---
jira_key: "PED-1049"
aliases: ["PED-1049"]
summary: "API - Refactor - Completar datos del cliente de la forma mas completa posible, según la informacion provista por mercadolibre"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-15 08:29"
updated: "2025-07-22 22:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1049"
---

# PED-1049: API - Refactor - Completar datos del cliente de la forma mas completa posible, según la informacion provista por mercadolibre

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-15 08:29 |
| Actualizado | 2025-07-22 22:13 |
| Etiquetas | ninguna |
| Jira | [PED-1049](https://bluinc.atlassian.net/browse/PED-1049) |

## Relaciones

- **Padre:** [[PED-915]] MercadoLibre

## Descripcion

```
POST {{API_URL}}/v1/syncUp/mercadolibreOrders
```

Para esto guardaremos los siguientes datos, tratando de mapear con nuestra estructura de clientes a modo de tener la mayor informacion posible, hasta donde lo permite mercadolibre

| Campo en tu API | Origen en ML (`additional_info`) | Lógica / Transformación |
| --- | --- | --- |
| `cdnicif` | `DOC_NUMBER` | Valor bruto de `value` (ej. `"33457962"`). |
| `ndocidenti` | `DOC_TYPE` | DNI,CUIT, hay que mapear con nuestra tablita `[NewBytes_DBF].[dbo].[FP_DocumentosAFIP]`el parametro `Id_TipoDocumentoInterno` |
| `cnomcli` | `FIRST_NAME` + `LAST_NAME` |  |
| `cnomcom` | `FIRST_NAME` + `LAST_NAME` |  |
| `niva` | `INVOICE_TYPE` | El tipo de comprobante (ej. `"Factura A"` o `"Factura B"`)  sirve para deducir niva para llegar a `[NewBytes_DBF].[dbo].[FP_CategoriasIVA]` |
| `niva` | `TAX_TYPE` | sirve para deducir niva para llegar a `[NewBytes_DBF].[dbo].[FP_CategoriasIVA]` |
| `niva` | `TAXPAYER_TYPE_ID` | sirve para deducir niva para llegar a `[NewBytes_DBF].[dbo].[FP_CategoriasIVA]` |
| `cptlcli` | `ZIP_CODE` | Valor directo (ej. `"1407"`). |
| `cdircli` | `STREET_NAME` + `STREET_NUMBER` | Unión de ambos campos, dejando un espacio (“Av. B RIVADAVIA” + “8830”). |
| `ID_PROVINCIA` | `STATE_NAME` | Lookup en tu tabla de provincias (ej. “Capital Federal” → 1, “Buenos Aires” → 2, …). |
| `ID_CIUDAD` | `CITY_NAME` | Lookup en tu tabla de localidades (ej. “Velez Sarsfield” → 20891, …). |
| `ID_PAIS` | `COUNTRY_ID` | Este siempe es ARG |
