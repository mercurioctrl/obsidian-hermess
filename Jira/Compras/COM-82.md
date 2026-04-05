---
jira_key: "COM-82"
summary: "API - Feat - Repositorio de productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-04-04 06:53"
updated: "2025-02-19 00:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-82"
---

# COM-82: API - Feat - Repositorio de productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-04 06:53 |
| Actualizado | 2025-02-19 00:44 |
| Etiquetas | ninguna |
| Jira | [COM-82](https://bluinc.atlassian.net/browse/COM-82) |

## Descripción

Crearemos un repositorio de productos, necesario para buscar y agregarlos a una orden ademas de listarlo con otros fines.

```
GET {API_URL}/v1/items?stock=1&search=amd
```

```
{
    "response": [
        {
            "title": "MINI PC GIGABYTE BRIX BSRE-1505 (AMD Ryzen 1505G)",
            "sku": "GB-BSRE-1505",
            "id": 116741,
            "category": "COMPUTADORAS",
            "categoryId": 31,
            "brand": "GIGABYTE",
            "brandId": 4,
            "mainImage": "https:\/\/static.nb.com.ar\/img\/cc931534c55dd0fe2ee6a3fa0aa4378f.jpeg",
            "availableStock": 4,
        },
...
```

El atributo search de la query en la url busca por

- Sku


- Descripcion


- Marca


- Categoria


- item Id
