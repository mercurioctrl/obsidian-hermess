---
jira_key: "INV-17"
summary: "API - Feat - Obtener todas las imágenes para un producto desde los repositorios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-09 14:27"
updated: "2022-06-13 14:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-17"
---

# INV-17: API - Feat - Obtener todas las imágenes para un producto desde los repositorios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-09 14:27 |
| Actualizado | 2022-06-13 14:17 |
| Etiquetas | ninguna |
| Jira | [INV-17](https://bluinc.atlassian.net/browse/INV-17) |

## Descripción

```
GET {{API_URL}}/v1/getImages/barcode/{ean,upc, codigo de barras}
```

```
GET {{API_URL}}/v1/getImages/description/{sku, titulo de descripcion}
```



```
{"barcode": [
      "http://http2.mlstatic.com/D_941718-MLA48352452977_112021-F.jpg"
    ],
"Meli":   [
      "http://http2.mlstatic.com/D_941718-MLA48352452977_112021-F.jpg",
      "http://http2.mlstatic.com/D_664949-MLA48352452981_112021-F.jpg",
      "http://http2.mlstatic.com/D_703081-MLA48352452979_112021-F.jpg",
      "http://http2.mlstatic.com/D_766255-MLA48352452980_112021-F.jpg",
      "http://http2.mlstatic.com/D_874363-MLA48352452978_112021-F.jpg"
    ],
    "Newegg":   [
        "https://c1.neweggimages.com/ProductImage/14-986-003-V20.jpg",
        "https://c1.neweggimages.com/ProductImage/14-986-003-V17.jpg",
        "https://c1.neweggimages.com/ProductImage/14-986-003-V16.jpg",
        "https://c1.neweggimages.com/ProductImage/14-986-003-V18.jpg",
        "https://c1.neweggimages.com/ProductImage/14-986-003-V19.jpg",
        "https://c1.neweggimages.com/ProductImage/14-986-003-V15.jpg",
        "https://c1.neweggimages.com/ProductImage/14-986-003-V21.jpg",
        "https://c1.neweggimages.com/ProductImage/14-986-003-V22.jpg",
        "https://c1.neweggimages.com/ProductImage/14-986-003-Z01.jpg"
      ]
    }
    }
```
