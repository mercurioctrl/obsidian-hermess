---
jira_key: "COM-52"
aliases: ["COM-52"]
summary: "API - Feat - Ver ingreso"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-20 09:07"
updated: "2024-02-23 18:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-52"
---

# COM-52: API - Feat - Ver ingreso

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-20 09:07 |
| Actualizado | 2024-02-23 18:31 |
| Etiquetas | ninguna |
| Jira | [COM-52](https://bluinc.atlassian.net/browse/COM-52) |

## Relaciones

- **Padre:** [[COM-51 - Ver ingreso|COM-51]] Ver ingreso
- **blocks:** [[COM-53 - APP - Feat - Ver ingreso|COM-53]] APP - Feat - Ver ingreso

## Descripcion

Crearemos el recurso encargado de listar el detalle de un orden de compra

```
GET {API_URL}/v1/providerOrderInbound/3213

```

```
{
            "providerOrderInbound": "00011101",
            "providerId": "000401",
            "providerName": "SERVICE & ENTERTAINMENT S A",
            "distpatchName": "SERVICE Y ENTERTAIMENT SA",
            "userId": "14",
            "updated": null,
            "dispatchDate": "04\/01\/2024",
            "numPed": "11101",
            "fullSerialized": 1
    "items": [
        {
            "title": "MOTHER ASROCK (LGA1700) H610M-HDV",
            "sku": "MB-H610M-HDV",
            "id": 117720,
            "price": {
                "value": 124.3928,
                "iva": 10.5,
                "finalPrice": 137.45404399999998
            },
            "warranty": "36 meses",
            "amount": 1
        },
        {
            "title": "DISCO SSD PATRIOT BURST ELITE SOLID 120 GB SATA3 PE000775",
            "sku": "PBE120GS25SSDR",
            "id": 109489,
            "price": {
                "value": 22.12688,
                "iva": 10.5,
                "finalPrice": 24.4502024,
            },
            "warranty": "12 meses",
            "amount": 1
        }
    ]
}
```

Consulta orientadora (cualquier cosa me preguntas)

```
SELECT *
  FROM [NewBytes_DBF].[dbo].[albprot]
  LEFT JOIN NewBytes_DBF.dbo.albprol ON albprol.nnumalb = albprot.nnumalb
```
