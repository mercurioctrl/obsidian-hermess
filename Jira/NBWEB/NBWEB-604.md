---
jira_key: "NBWEB-604"
summary: "API - Feat - Incorporar tabla medios de pago a el update de cotizaciones "
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-05 12:00"
updated: "2023-12-11 18:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-604"
---

# NBWEB-604: API - Feat - Incorporar tabla medios de pago a el update de cotizaciones 

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-05 12:00 |
| Actualizado | 2023-12-11 18:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-604](https://bluinc.atlassian.net/browse/NBWEB-604) |

## Descripción

Modificaremos el recursi

```
PATCH {API_URL}/v1/cms/currencyQuote
```

Para que no solo se modifique la tabla de cotizaciones como sucede ahora, sino que tambien se modifique

`[NEW_BYTES].[dbo].[MC_FORMAS_PAGO]`

Vinculando cada medio de pago a las distintas columnas

PESOS
CHEQUE
RETENCION IIBB
RETENCION DE GANANCIAS
RETENCION IVA
RETENCION PATRONALES

Para esto sera necesario agregar una columna extra en `[NEW_BYTES].[dbo].[MC_FORMAS_PAGO]` que nos permita vincular a cual registro corresponde cada cotizacion
