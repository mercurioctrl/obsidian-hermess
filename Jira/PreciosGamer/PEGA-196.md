---
jira_key: "PEGA-196"
summary: "API - Feat - Implementar envío de datos por parte del reseller"
status: "En curso"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-05-28 09:03"
updated: "2025-05-30 12:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-196"
---

# PEGA-196: API - Feat - Implementar envío de datos por parte del reseller

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-05-28 09:03 |
| Actualizado | 2025-05-30 12:25 |
| Etiquetas | ninguna |
| Jira | [PEGA-196](https://bluinc.atlassian.net/browse/PEGA-196) |

## Descripción

**Gestión vía Excel**

 Enviar y previsualizar un catálogo cargado por archivo.

```
POST /reseller/catalog/preview
```



payload: se sube el xlsx para validar que existan los campos y los tipos sean correctos. 

```none
curl --location --request POST 'http://localhost:8100/v1/reseller/catalog/preview' \
--header 'Authorization: Bearer 119|ctSSOE0lnRY8RQnRj5v3ee1h0pgLcJE8GF2Sjlo3cd0bda42' \
--form 'file=@"catalogo_template.xlsx"'
```

Response:

```json
{
   "message": "Vista previa del catálogo generada correctamente. Se encontraron los siguientes errores: Fila 7: El campo marca es obligatorio.. Fila 8: El campo marca es obligatorio.. Fila 9: El campo marca es obligatorio.. Fila 11: El campo marca es obligatorio.",
   "data": {
      "data": [
         {
            "description": "ASUS VIVOBOOK INTEL I5-1135G7 8GB 256GB 15.6 IN FHD IPS W11H BLACK F1500EA-WB5e1",
            "resellerTxt": "Katech",
            "brandTxt": "asus",
            "price": "1037650",
            "destinyUrl": "https://katech.com.ar/producto/asus-vivobook-intel-i5-1135g7-8gb-256gb-15-6-in-fhd-ips-w11h-black-f1500ea-wb51/?utm_source=hardgamers&utm_medium=search%20engine",
            "dataOriginUrl": "https://www.hardgamers.com.ar/product/1940642433",
            "dataOriginImgUrl": "https://katech.com.ar/wp-content/uploads/X2-99.jpg",
            "importerId": "3039",
            "originId": "1",
            "itemId": "614"
         },...
      ],
      "errors": [
         {
            "row": 7,
            "errors": {
               "brandTxt": [
                  "El campo marca es obligatorio."
               ]
            }
         },...
      ],
      "error_summary": [
         "Fila 7: El campo marca es obligatorio.",
         ...
      ],
      "total_rows": 10,
      "valid_rows": 6,
      "error_rows": 4
   }
}
```





Cargar el catálogo a la tabla Repository desde archivo Excel. 

```
POST /reseller/catalog/upload
```



#### **Gestión vía URL (feed XML)**

Registrar una URL para el catálogo.

```
POST /reseller/catalog/url
```



Validar la URL de catálogo proporcionada.

```
POST /reseller/catalog/url/validate
```



Sincronizar el catálogo automáticamente desde una URL válida.

```
POST /reseller/catalog/url/sync
```
