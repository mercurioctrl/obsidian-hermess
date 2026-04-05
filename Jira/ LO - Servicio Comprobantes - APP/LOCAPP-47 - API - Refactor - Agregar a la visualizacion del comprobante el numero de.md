---
jira_key: "LOCAPP-47"
aliases: ["LOCAPP-47"]
summary: "API - Refactor - Agregar a la visualizacion del comprobante el numero de despacho"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-05-22 16:28"
updated: "2024-05-27 20:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-47"
---

# LOCAPP-47: API - Refactor - Agregar a la visualizacion del comprobante el numero de despacho

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-05-22 16:28 |
| Actualizado | 2024-05-27 20:51 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-47](https://bluinc.atlassian.net/browse/LOCAPP-47) |

## Relaciones

- **Padre:** [[LOCAPP-45]] Numeros de despacho visibles

## Descripcion

```
{API_URL}/v2/F/535655/ec01278247d925d078bcf377a8ca06
```

```
...

},
"cliente": {
"numeroDocumentoCliente": "20225037109",
"tipoResponsableCliente": "Responsable Inscripto",
"condicionCliente": "DEPOSITO EN BANCO",
"nombreCliente": "BURKE GABRIEL GUSTAVO",
"domicilioCliente": "LOPE DE VEGA AV. 86",
"observaciones": null,
"addressFinal": null,
"postalCodeFinal": null,
"provinceNameFinal": null,
"localityNameFinal": null
},
"detalle": [
{
"cantidad": 1,
"sku": "WD10EZEX",
"producto": "Disco Hdd 1tb Wd Blue Sata",
"garantia": "12 meses",
"despacho": "22073IC04096301T",
"iva": "10,50",
"precio": "55,84",
"subtotal": "55,84"
},
{
"cantidad": 2,
"sku": "NT01SA500-240-S3X",
"producto": "Disco Ssd Netac Sa500 2.5 Sata3 240 Gb",
"garantia": "12 Meses",
"despacho": "22001IC04182105X", <--- ESTE ES EL DATO NUEVO QUE VAMOS A REMPLAZAR
"iva": "10,50",
"precio": "24,04",
"subtotal": "48,08",

}
],
"totales": {
"moneda": "DOL",
"cotizacion": "909,00",
"perIngresosBrutos": "3,12",
"importeTotal": "117,95",
"netoNoGravado": "103,92",

...
```
