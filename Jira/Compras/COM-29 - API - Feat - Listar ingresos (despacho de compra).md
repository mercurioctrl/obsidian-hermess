---
jira_key: "COM-29"
aliases: ["COM-29"]
summary: "API - Feat - Listar ingresos (despacho de compra)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-15 15:21"
updated: "2024-02-22 15:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-29"
---

# COM-29: API - Feat - Listar ingresos (despacho de compra)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-15 15:21 |
| Actualizado | 2024-02-22 15:42 |
| Etiquetas | ninguna |
| Jira | [COM-29](https://bluinc.atlassian.net/browse/COM-29) |

## Relaciones

- **Padre:** [[COM-12 - Listar ingresos (despachos de compra)|COM-12]] Listar ingresos (despachos de compra)
- **blocks:** [[COM-13 - APP - Feat - Listar ingresos (despachos de compra)|COM-13]] APP - Feat - Listar ingresos (despachos de compra)
- **is blocked by:** [[COM-41 - API - Feat - Listar ingresos (despacho de compra) - Filtro por serializado no|COM-41]] API - Feat - Listar ingresos (despacho de compra) - Filtro por serializado no coincidente 
- **blocks:** [[COM-57 - API - Listar ingresos - Referencia a tabla distinta|COM-57]] API - Listar ingresos -> Referencia a tabla distinta

## Descripcion

Basandonos en el mismo recurso que hemos construido para expedicion, crearemos uno muy parecido basado en la siguiente respuest y filtros

```
GET {API_URL}/v1/providerOrderInbound?search={nombre proveedor, providerOrder, id proveedor}&fullSerialized=0&providerId=000002&brandId=223&sku=as&itemId=intel
```

```
{
    "response": [
        {
            "id": 9219,
            "providerOrder": "00011101",
            "providerId": "000401",
            "providerName": "SERVICE & ENTERTAINMENT S A",
            "distpatchName": "SERVICE Y ENTERTAIMENT SA",
            "userId": "14",
            "updated": null,
            "dispatchDate": "04\/01\/2024",
            "numPed": "11101",
            "fullSerialized": 1
        },
        {
            "id": 9218,
            "providerOrder": "00011100",
            "providerId": "000401",
            "providerName": "SERVICE & ENTERTAINMENT S A",
            "distpatchName": "SERVICE Y ENTERTAIMENT SA",
            "userId": "14",
            "updated": null,
            "dispatchDate": "28\/12\/2023",
            "numPed": "11100",
            "fullSerialized": 0
        },
        {
            "id": 9217,
            "providerOrder": "00011099",
            "providerId": "001564",
            "providerName": "FABRICA AUSTRAL DE PRODUCTOS ELECTRICOS SA",
            "distpatchName": "FABRICA AUSTRAL DE PRODUCTOS ELECTRICOS SA",
            "userId": "14",
            "updated": null,
            "dispatchDate": "27\/12\/2023",
            "numPed": "11099",
            "fullSerialized": 1
        },
        {
            "id": 9216,
            "providerOrder": "00011098",
            "providerId": "001564",
            "providerName": "FABRICA AUSTRAL DE PRODUCTOS ELECTRICOS SA",
            "distpatchName": "FABRICA AUSTRAL DE PRODUCTOS ELECTRICOS SA",
            "userId": "14",
            "updated": null,
            "dispatchDate": "27\/12\/2023",
            "numPed": "11098",
            "fullSerialized": 1
        }
]
```

```
SELECT   CONVERT(VARCHAR, dfecalb, 20) AS fecha, albprot.ccoddiv , albprot.label, FP_Proveedores.cnompro
                    FROM NewBytes_DBF.dbo.albprot
                    LEFT JOIN NewBytes_DBF.dbo.FP_Proveedores ON albprot.ccodpro = FP_Proveedores.ccodpro
                    WHERE nnumalb <> 0
```
