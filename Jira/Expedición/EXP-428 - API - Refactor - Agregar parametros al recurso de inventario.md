---
jira_key: "EXP-428"
aliases: ["EXP-428"]
summary: "API - Refactor - Agregar parametros al recurso de inventario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-05 17:57"
updated: "2024-08-15 03:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-428"
---

# EXP-428: API - Refactor - Agregar parametros al recurso de inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-05 17:57 |
| Actualizado | 2024-08-15 03:28 |
| Etiquetas | ninguna |
| Jira | [EXP-428](https://bluinc.atlassian.net/browse/EXP-428) |

## Relaciones

- **Padre:** [[EXP-17 - Feat - Listar productos (Control de stock)|EXP-17]] Feat - Listar productos (Control de stock)
- **blocks:** [[EXP-429 - APP - Refactor - Items alertados en el inventario|EXP-429]] APP - Refactor - Items alertados en el inventario

## Descripcion

Agregaremos dos parámetros nuevos al recurso de conteo de inventario, adicionalmente “ordenaremos” primero (parecido como hicimos en las pestañas de despacho) para que aparezcan listados en primer lugar aquellos con `alert=true`

```
GET {API_URL}/v1/items
```

```
{
    "response": [
        {
            "title": "MOTHER GIGABYTE (AM4) B450M GAMING",
            "sku": "B450M GAMING",
            "id": 104809,
            "category": "MOTHER GIGABYTE",
            "categoryId": 37,
            "brandId": 4,
            "brand": "GIGABYTE                                          ",
            "imagenMarca": "https:\/\/static.nb.com.ar\/img\/f2aae2c829b051430eb6a039ad6bc7ae.jpg",
            "imagenPrincipal": "010d80727f5667da41a82268c09d6833.png",
            "counted": null,
            "countedDate": null,
            "createDate": "2024-08-05 16:18:18.490",
            "countable": "1",
            "weightAverage": 0,
            "lengthAverage": 0,
            "widthAverage": 0,
            "highAverage": 0,
            "countedApproved": true/false, <--- NUEVO
            "alert": true/false <--- NUEVO
        },
        {
            "title": "MOTHER GIGABYTE (AM4) B450M S2H",
            "sku": "B450M S2H 1.0",
            "id": 103326,
            "category": "MOTHER GIGABYTE",
            "categoryId": 37,
            "brandId": 4,
            "brand": "GIGABYTE                                          ",
            "imagenMarca": "https:\/\/static.nb.com.ar\/img\/f2aae2c829b051430eb6a039ad6bc7ae.jpg",
            "imagenPrincipal": "233625fe793f2b155d1f5f1029681a3b.png",
            "counted": null,
            "countedDate": null,
            "createDate": "2024-08-05 16:18:18.490",
            "countable": "1",
            "weightAverage": 0,
            "lengthAverage": 0,
            "widthAverage": 0,
            "highAverage": 0,
            "countedApproved": true/false, <--- NUEVO
            "alert": true/false <--- NUEVO            
        },
        
....        
```
