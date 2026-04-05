---
jira_key: "COM-151"
aliases: ["COM-151"]
summary: "API - Review - Problemas al generar un registro cuando hago el INGRESO"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-12-09 07:22"
updated: "2024-12-20 05:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-151"
---

# COM-151: API - Review - Problemas al generar un registro cuando hago el INGRESO

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-09 07:22 |
| Actualizado | 2024-12-20 05:15 |
| Etiquetas | ninguna |
| Jira | [COM-151](https://bluinc.atlassian.net/browse/COM-151) |

## Relaciones

- **Padre:** [[COM-109]] Generar INGRESO o pedido (a partir de una orden de compra)

## Descripcion

Esto pasa solo en produ aparentemente, tal vez sea un tipo diferente en una tabla

```
POST {API_URL}/v1/makeProviderOrderInbound
```

```
curl 'https://api.purchases.lio.red/v1/makeProviderOrderInbound' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzM3NDMyMzYsImF1ZCI6ImM5ZjZiZGNjMDZmZmQwOTYwMTJlZDhjNzE4YzdiMjFiZTc0NjFlYTgiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImNvbXByYXMiOiIxIiwicG0iOiIxIn0sImlhdCI6MTczMzczOTYzNiwibmJmIjoxNzMzNzM5NjM2fQ.VGzpEFiIoi_OtFq1MT-tD9pAVms31lezG16yo4NSpeY' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://compras.saftel.com' \
  -H 'Referer: https://compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"orderNumber":11401,"providerId":"002009","providerName":"CORESA GROUP SRL","observation":"","status":"P","voucherPurchaseId":"","buyerName":"Carou Agustin","buyerId":67,"currencyQuote":1,"distributeTaxes":[],"items":[{"id":119798,"title":"SENSOR SMART MACROLED PARA DETECCION DE HUMO, 30 M2, 2 PILAS AAA CON ALARMA SONORA","sku":"SSH-30M2-2AAA","price":{"value":35.14,"iva":21,"finalPrice":42.519400000000005},"warranty":"3 meses","amount":20,"position":null,"taxPosition":null,"amountEntered":null,"partialIncome":0}]}'
```

```
{
    "errors": {
        "status": 500,
        "title": "SQLSTATE[22001]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Los datos de cadena o binarios se truncar\u00edan. (SQL: INSERT INTO newbytes_dbf.dbo.albprol (\n                                      nnumalb,\n                                      cref,\n                                      cdetalle,\n                                      nprediv,\n                                      ncanent,\n                                      nservicio,\n                                      ndto,\n                                      cserie,\n                                      nivaserv,\n                                      nlinea,\n                                      ntipocomp,\n                                      nmontoimp,\n                                      ntipoimp,\n                                      id_articulo)\n                        VALUES (:nnumalb,\n                                :cref,\n                                :cdetalle,\n                                :nprediv,\n                                :ncanent,\n                                :nservicio,\n                                :ndto,\n                                :cserie,\n                                :nivaserv,\n                                (SELECT IIF(MAX(nlinea) IS NULL, 1, MAX(nlinea) + 1) FROM newbytes_dbf.dbo.albprol WHERE nnumalb = :nnumalb2),\n                                :ntipocomp,\n                                :nmontoimp,\n                                :ntipoimp,\n                                :ID_Articulo))",
        "file": "\/var\/www\/app\/vendor\/laravel\/framework\/src\/Illuminate\/Database\/Connection.php",
        "line": 760
    }
}
```
