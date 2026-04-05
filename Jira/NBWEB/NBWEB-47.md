---
jira_key: "NBWEB-47"
summary: "Listar contenido del carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-21 14:45"
updated: "2024-11-06 02:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-47"
---

# NBWEB-47: Listar contenido del carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-21 14:45 |
| Actualizado | 2024-11-06 02:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-47](https://bluinc.atlassian.net/browse/NBWEB-47) |

## Descripción

**Se debe corregir el path de la imagen 04/04/2022

```
GET {{API_URL}}/v1/carrito/
```



Retorna:



```json
{
"Cart":{
"CartId":3334,
"CartName":"Nuevo Carrito Alfabis",
"Cotizacion":104.5,
"SubtotalDollar":4324.56,
"SubtotalDollarFinal":5232.72,
"SubtotalPesosAr":454078.8,
"SubtotalPesosArFinal":549434.38
},
"items":
[{
"Title":"FUENTE GAMER GIGABYTE 550W 80 PLUS",
"Id":"104964",
"Sku":"GP-P550B",
"Category":"FUENTES ",
"IdCategory":"38",
"IdBrand":"4",
"Brand":"GIGABYTE ",
"initialB":null,
"initialC":null,
"Stock":"Alto",
"AmountInCart":3,
"Price":{
"value":"53.56365",
"iva":10.5,
"finalPrice":59.187833250000004
},
"imagen_principal":"b65cd71de19e10c27d8c357cd99cded9.png"
},
{
"Title":"FUENTE GAMER GIGABYTE 550W 80 PLUS",
"Id":"104964",
"Sku":"GP-P550B",
"Category":"FUENTES ",
"IdCategory":"38",
"IdBrand":"4",
"Brand":"GIGABYTE ",
"initialB":null,
"initialC":null,
"AmountInCart":2,
"Stock":"Alto",
"Price":{
"value":"53.56365",
"iva":10.5,
"finalPrice":59.187833250000004
},
"imagen_principal":"b65cd71de19e10c27d8c357cd99cded9.png"
}]
}

```
