---
jira_key: "POS-77"
aliases: ["POS-77"]
summary: "API - Refactor - Agregar al recurso la descripción de la falla"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-23 14:41"
updated: "2022-10-18 14:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-77"
---

# POS-77: API - Refactor - Agregar al recurso la descripción de la falla

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-23 14:41 |
| Actualizado | 2022-10-18 14:18 |
| Etiquetas | ninguna |
| Jira | [POS-77](https://bluinc.atlassian.net/browse/POS-77) |

## Relaciones

- **Padre:** [[POS-56 - API - Feat - Ver detalle ingreso|POS-56]] API - Feat - Ver detalle ingreso

## Descripcion

Segun el objeto 

```
[{
    "serial": "",
    "quantity": 1,
    "productDescription": "TECLADO CORSAIR K65 LUX RGB ENGLISH",
    "productId": 101081,
    "invoiceNumber": "534576578656",
    "failType": 3,
    "contactNumber": "3241234312",
    "clientId": 25433,
    "userId": 7463,
    "userName": "master",
    "clientName": "GOLDIN DAVID L. Y LOPEZ ALCOBA PABLO A. SH",
    "dateAdmission": "23-08-2022 14:38",
    "id": 3,
    "description": "No da imagen",
    "productUrl": "https:\/\/www.nb.com.ar\/fromPostventa_-_101081"
}]
```

Parece que se esta utilizando `   "description": "No da imagen",` que era un parametro originalmente pensado para mostrar la descripcion larga realizada por el cliente para el “tipo de falla”.



En el ejemplo hice un preingreso de postventa, con una larga descripcion, pero al consultar

```
curl 'https://gamma.api.aftersale.lio.red/v1/preAfterSales/33' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjEyNzkzMDIsImF1ZCI6Ijk0ZGViZWJhNjM4NDQyZDRhNjViMjVlOWQ5MzM3ZjNhNDZkZjMxNWUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjI1NDMzIiwicG9zdHZlbnRhIjoiMSIsInBvc3R2ZW50YV9jcmVkaXRvcyI6IjEiLCJhZ2VudElkIjoiMTIiLCJwb3N0dmVudGFfc29sdWNpb24iOiIwIiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIn0sImlhdCI6MTY2MTE5MjkwMiwibmJmIjoxNjYxMTkyOTAyfQ.Nxxzer48_tJMq7748eDIHMEw3w-aK1AMX62Kbzlm6x0' \
  -H 'Connection: keep-alive' \
  -H 'Origin: http://gamma.postventa.saftel.com' \
  -H 'Referer: http://gamma.postventa.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

Obtengo el tipo de falla en el lugar de la descripción.



Deberían estar ambos.
