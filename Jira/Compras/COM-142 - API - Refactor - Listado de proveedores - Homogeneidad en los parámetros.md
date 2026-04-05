---
jira_key: "COM-142"
aliases: ["COM-142"]
summary: "API - Refactor - Listado de proveedores - Homogeneidad en los parámetros"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-09-06 11:21"
updated: "2024-09-13 02:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-142"
---

# COM-142: API - Refactor - Listado de proveedores - Homogeneidad en los parámetros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-09-06 11:21 |
| Actualizado | 2024-09-13 02:20 |
| Etiquetas | ninguna |
| Jira | [COM-142](https://bluinc.atlassian.net/browse/COM-142) |

## Relaciones

- **Padre:** [[COM-5]] Proveedores
- **relates to:** [[COM-140]] APP - Refactor - Agregar el proveedor primario al crear una orden de compra

## Descripcion

Debido a que en la interfaz se produce una discrepancia entre los identificadores del proveedor

[adjunto]


Vamos a llevar a cabo una refactorización en las órdenes de proveedor y me gustaría proponer dos posibles mejoras:

- Mantener el nombre del parámetro `providerId`, pero cambiar su valor por el id del proveedor.


- Cambiar el nombre del parámetro de `providerId` a `providerCode` y mantener su valor actual.



Dejo estas dos sugerencias para tu consideración y dejo a tu consideración cuál de ellas sería más adecuada para identificar al proveedor en las órdenes.


```
{{API_URL}}/v1/providerOrder
```

```
{
	"response": [
		{
			"status": "P",
			"date": "2024-09-05 17:06:31",
			"orderNumber": 11211,
			"providerId": "001150", <------------------------ CAMBIAR
			"providerName": "LASET S.A.",
			"currencyId": "DOL",
			"label": "",
			"currencyAmount": 927,
			"warehouse": "SAF",
			"warehouseDescription": "SAFcom",
			"total": 0,
			"totalFinal": 0,
			"iva": 21
		}
...
```




```
{{API_URL}/v1/providers?search=laset
```

```
{
	"response": [
		{
			"id": 13175, <--------------------------------- REFERENCIA
			"providerCode": "001150", <-------------------- REFERENCIA
			"name": "LASET S.A.",
			"businessName": "LASET S.A.",
			"address": "MISIONES 1371",
			"countryId": 5,
			"prefixFlag": "US",
			"countryDescription": "Estados Unidos De AMERICA",
			"countryFlagId": 78,
			"provinceId": 19,
			"locateId": 13666,
			"ccoddiv": "DOL",
			"locateDescription": "MEDINA"
		}
...
```
