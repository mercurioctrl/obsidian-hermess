---
jira_key: "PEGA-105"
aliases: ["PEGA-105"]
summary: "API - Review - Detalle ultimo precios igual a precio actual"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-09-03 08:59"
updated: "2024-09-11 03:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-105"
---

# PEGA-105: API - Review - Detalle ultimo precios igual a precio actual

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-03 08:59 |
| Actualizado | 2024-09-11 03:58 |
| Etiquetas | ninguna |
| Jira | [PEGA-105](https://bluinc.atlassian.net/browse/PEGA-105) |

## Relaciones

- **Padre:** [[PEGA-2 - Catalogos y Buscador|PEGA-2]] Catalogos y Buscador

## Descripcion

`lastPrice` y `currentPrice` parecen venir casi siempre iguales, cuando solo deben venir iguales en los casos donde no exista un precio anterior diferente

```
{
    "response": [
        {
            "id": 189,
            "resellerId": 1068,
            "resellerDescription": "Gaming city",
            "brandId": 11643,
            "brandDescription": "Aerocool",
            "description": "ADAPTADOR AEROCOOL MIRAGE INTEL LGA1700",
            "lastPrice": 3704, <<<-----
            "currentPrice": 3704, <<<-----
            "percentage": 0,
            "destinyUrl": "https:\/\/www.tienda.gamingcity.com.ar\/MLA-1391369531-adaptador-aerocool-mirage-intel-lga1700-_JM?utm_source=hardgamers&utm_medium=search%20engine",
            "defaultImgUrl": "https:\/\/http2.mlstatic.com\/D_NQ_NP_647117-MLA72112628691_102023-V.webp"
        },
```
