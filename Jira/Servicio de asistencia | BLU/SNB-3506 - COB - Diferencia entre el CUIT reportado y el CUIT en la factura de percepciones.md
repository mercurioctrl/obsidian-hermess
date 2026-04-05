---
jira_key: "SNB-3506"
aliases: ["SNB-3506"]
summary: "COB - Diferencia entre el CUIT reportado y el CUIT en la factura de percepciones "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-04 09:30"
updated: "2025-11-05 14:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3506"
---

# SNB-3506: COB - Diferencia entre el CUIT reportado y el CUIT en la factura de percepciones 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-04 09:30 |
| Actualizado | 2025-11-05 14:16 |
| Etiquetas | ninguna |
| Jira | [SNB-3506](https://bluinc.atlassian.net/browse/SNB-3506) |

## Relaciones

*Sin relaciones*

## Descripcion

Al sacar el reporte de percepciones ARBA de la siguiente manera

```
curl 'https://api.cashbox.lio.red/v1/perceptioniibb?currentPage=1&itemsPerPage=15&type=ARBA&between=01-10-2025_01-11-2025&download=1' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjIyNTk1MzksImF1ZCI6IjQ3NDRhOTgzOTQxNTY2YjEzNjQzNWI1MTVkN2YyOWE4Y2ExZmJkNTEiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImNvYnJvIjoiMSIsImNvYnJvQWRtaW4iOiIxIiwiYWdlbnRJZCI6IjEyIiwiYm94IjoiU2ViYSIsIm1hbmFnZW1lbnQiOiIxIiwiZWRpdF9jcmVkaXQiOiIxIiwiY29icm9BZGp1c3RUbyI6IjEifSwiaWF0IjoxNzYyMTczMTM5LCJuYmYiOjE3NjIxNzMxMzl9._Gyg-k4mQbJUvKQ1VOAO815vc-5dn6Wbn1broLKEidY' \
  -H 'Referer: https://caja.saftel.com/perceptioniibb?currentPage=1&itemsPerPage=15&type=ARBA&between=01-10-2025_01-11-2025' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua: "Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0'
  
```

Veo que hay 2 o 3 casos que no me coinciden los cuit, por ejemplo el de 

| VENTILACION TEVA SA |  |
| --- | --- |

En este caso se puede observar que en el informe el cuit es 30-52044177-7 pero al revisar el cliente y la factura vemos el correcto: 30-52044177-4

Esto surge porque al presentar el informe nos envian ciertos cuits como problematicos

```
Lote: AR-30709246638-2025100-D7-LOTE1_67EA9A6DF8365131E7E02D1954AC3A2A.zip

   Línea     24: 30-52044177-706/10/2025FA000400164536000061770,0000000617,64A

 

                  Numero de CUIT invalido

 

   Línea    116: 20-20561735-521/10/2025FA000400165263000076574,4000001531,47A

 

                  Numero de CUIT invalido

 

   Línea    176: 20-29805119-930/10/2025FA000400165760000078942,2000003157,75A

 

                  Numero de CUIT invalido

 

   Línea    184: 20-25748687-731/10/2025FA000400165836000104923,3000004196,82A

                  Numero de CUIT invalido
```



[adjunto]
