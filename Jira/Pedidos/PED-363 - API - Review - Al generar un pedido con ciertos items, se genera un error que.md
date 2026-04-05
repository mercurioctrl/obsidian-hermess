---
jira_key: "PED-363"
aliases: ["PED-363"]
summary: "API - Review - Al generar un pedido con ciertos items, se genera un error que parece tener que ver con su \"cref\""
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-20 09:17"
updated: "2023-12-20 15:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-363"
---

# PED-363: API - Review - Al generar un pedido con ciertos items, se genera un error que parece tener que ver con su "cref"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-20 09:17 |
| Actualizado | 2023-12-20 15:06 |
| Etiquetas | ninguna |
| Jira | [PED-363](https://bluinc.atlassian.net/browse/PED-363) |

## Relaciones

- **Padre:** [[PED-4]] Pedidos

## Descripcion

Los que vi problemáticos son 

ATOMLUX ESTABILIZADOR R500@PLUS

y

FUENTE SFX 500W 20+4 SA



```
curl 'https://gamma.api.orders.lio.red/v1/makeSale' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDMwNzgxNTYsImF1ZCI6IjQyN2ZkOTI3ODU5NjdkOWY2MTg1NjMwYzJkYWFiYTJiMzhkNzdkY2IiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjF9LCJpYXQiOjE3MDMwNzQ1NTYsIm5iZiI6MTcwMzA3NDU1Nn0.XyuEcGRkJjcJQ0xxqRNJWIOo_sGBLqT0JpxIP2WlBYs' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"branch":"0002","order":"10332369"}' \
  --compressed
```

```
{
    "errors": {
        "status": 500,
        "title": "SQLSTATE[HY000]: General error: 20018 Invalid column name 'ESTAB_ATOM_A500P'. [20018] (severity 16) [ UPDATE\n        [NB_WEB].[dbo].[registro_stock]\n        SET sPosterior = (\n        SELECT\n            (nstock + nstock_lo + nstock_en_cola)\n        FROM\n            [NewBytes_DBF].[dbo].[stocks]\n        WHERE\n            (ID_ARTICULO = 169)\n        )\n        WHERE\n        id =\n        (\n        SELECT TOP(1) id\n        FROM [NB_WEB].[dbo].[registro_stock]\n        WHERE\n        codigo = 169\n        AND cref =  ESTAB_ATOM_A500P\n        AND remito = 'R-0002-00568882'\n        AND agente = 36\n        AND fichero = 'pedidos.nb'\n        AND cantidad = -2\n        ORDER BY fecha DESC\n        );] (SQL:  UPDATE\n        [NB_WEB].[dbo].[registro_stock]\n        SET sPosterior = (\n        SELECT\n            (nstock + nstock_lo + nstock_en_cola)\n        FROM\n            [NewBytes_DBF].[dbo].[stocks]\n        WHERE\n            (ID_ARTICULO = 169)\n        )\n        WHERE\n        id =\n        (\n        SELECT TOP(1) id\n        FROM [NB_WEB].[dbo].[registro_stock]\n        WHERE\n        codigo = 169\n        AND cref =  ESTAB_ATOM_A500P\n        AND remito = 'R-0002-00568882'\n        AND agente = 36\n        AND fichero = 'pedidos.nb'\n        AND cantidad = -2\n        ORDER BY fecha DESC\n        );)",
        "file": "\/var\/www\/app\/vendor\/laravel\/framework\/src\/Illuminate\/Database\/Connection.php",
        "line": 760
    }
}
```
