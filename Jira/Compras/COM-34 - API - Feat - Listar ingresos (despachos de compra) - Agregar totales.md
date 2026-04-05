---
jira_key: "COM-34"
aliases: ["COM-34"]
summary: "API - Feat -  Listar ingresos (despachos de compra) - > Agregar totales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-16 10:30"
updated: "2024-02-22 16:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-34"
---

# COM-34: API - Feat -  Listar ingresos (despachos de compra) - > Agregar totales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-16 10:30 |
| Actualizado | 2024-02-22 16:12 |
| Etiquetas | ninguna |
| Jira | [COM-34](https://bluinc.atlassian.net/browse/COM-34) |

## Relaciones

- **Padre:** [[COM-12]] Listar ingresos (despachos de compra)
- **blocks:** [[COM-57]] API - Listar ingresos -> Referencia a tabla distinta

## Descripcion

```
GET {API_URL}/v1/providerOrderInbound
```

Agregaremos nuevos parámetros para referir a los totales

- Total


- Iva


- Total Final



Para esto sumaremos los items, multiplicados por la cantidad y a su vez haremos lo mismo considerando su iva

```
SELECT   ncanent, nprediv, ivaCompra
FROM Newbytes_DBF.dbo.albprol 
LEFT JOIN Newbytes_DBF.dbo.articulo
ON Newbytes_DBF.dbo.albprol.cref = Newbytes_DBF.dbo.articulo.cref
WHERE nnumalb =  ?
```

El objeto quedara similar a este

```
...
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
    "total" : 100 <-- NUEVO
    "totalFinal": 121 <-- NUEVO
    "iva": 21  <-- NUEVO
  },
  ...
```
