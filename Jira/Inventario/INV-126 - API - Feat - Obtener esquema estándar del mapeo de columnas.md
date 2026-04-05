---
jira_key: "INV-126"
aliases: ["INV-126"]
summary: "API - Feat - Obtener esquema estándar del mapeo de columnas "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-12 07:02"
updated: "2024-09-18 04:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-126"
---

# INV-126: API - Feat - Obtener esquema estándar del mapeo de columnas 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-12 07:02 |
| Actualizado | 2024-09-18 04:14 |
| Etiquetas | ninguna |
| Jira | [INV-126](https://bluinc.atlassian.net/browse/INV-126) |

## Relaciones

- **Padre:** [[INV-125]] Importación de catálogos
- **blocks:** [[INV-128]] APP - Feat - Formulario de carga masiva de productos a través de un archivo 

## Descripcion

Este recurso trabaja para devolver un esquema base o un ejemplo de cómo se espera que sea el mapeo de columnas

```
GET {API_URL}/import/mapping
```

```
"mapping": {
    "A": "mainImage",
    "B": "sku",
    "C": "title",
    "D": "brand",
    "E": "category",
    "F": "price",
    "G": "stock",
    "H": "iva",
    "I": "officialSiteUrl"
}
```

Estaría bueno que lo datos provengan de una tabla especifica para que si deseamos hacer un cambio o agregar un parámetro, sea posible
