---
jira_key: "COM-31"
aliases: ["COM-31"]
summary: "API - Feat - Listar ordenes de compra -> Agregar totales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-16 08:53"
updated: "2024-02-19 18:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-31"
---

# COM-31: API - Feat - Listar ordenes de compra -> Agregar totales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-16 08:53 |
| Actualizado | 2024-02-19 18:03 |
| Etiquetas | ninguna |
| Jira | [COM-31](https://bluinc.atlassian.net/browse/COM-31) |

## Relaciones

- **Padre:** [[COM-9]] Listar ordenes de compra
- **blocks:** [[COM-32]] APP - Feat - Listar ordenes de compra -> Agregar totales

## Descripcion

```
GET {API_URL}/v1/providerOrder
```

Agregaremos nuevos parámetros para referir a los totales

- Total


- Iva


- Total Final



Para esto sumaremos los items, multiplicados por la cantidad y a su vez haremos lo mismo considerando su iva

```
SELECT  ncanped, nprediv , ivaCompra
FROM Newbytes_DBF.dbo.pedprol 
LEFT JOIN Newbytes_DBF.dbo.articulo
ON Newbytes_DBF.dbo.pedprol.cref = Newbytes_DBF.dbo.articulo.cref
WHERE nnumped = ?
```

El objeto quedara similar a este

```
...
 {
    "status": "s",
    "date": "2016-05-30 10:24:35",
    "orderNumber": 7881,
    "providerId": "000046",
    "providerName": "",
    "currencyId": "PSO",
    "label": null,
    "total" : 100 <-- NUEVO
    "totalFinal": 121 <-- NUEVO
    "iva": 21  <-- NUEVO
  },
  ...
```
