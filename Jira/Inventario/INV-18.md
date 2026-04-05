---
jira_key: "INV-18"
summary: "API - Feat - Obtener todos los atributos para un producto desde los repositorios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-09 14:28"
updated: "2022-06-13 14:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-18"
---

# INV-18: API - Feat - Obtener todos los atributos para un producto desde los repositorios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-09 14:28 |
| Actualizado | 2022-06-13 14:17 |
| Etiquetas | ninguna |
| Jira | [INV-18](https://bluinc.atlassian.net/browse/INV-18) |

## Descripción

```
GET {{API_URL}}/v1/getAttributes/barcode/{ean,upc, codigo de barras}
```

```
GET {{API_URL}}/v1/getAttributes/description/{sku, titulo de descripcion}
```

```
{
"barcode":  [
      {
        "name": "Marca del repuesto",
        "value": "Razer"
      },
      {
        "name": "Código universal de producto",
        "value": "810056142155"
      },
      {
        "name": "Condición del ítem",
        "value": "Nuevo"
      }
    ],
"Meli":    [
      {
        "name": "Marca del repuesto",
        "value": "Razer"
      },
      {
        "name": "Código universal de producto",
        "value": "810056142155"
      },
      {
        "name": "Condición del ítem",
        "value": "Nuevo"
      },
      {
        "name": "Modelo del repuesto",
        "value": "RC21-01720100-R3M1"
      }
    ],
    "Newegg":   [
      {
        "name": "Código universal de producto",
        "value": "810056142155"
      },
      {
        "name": "Condición del ítem",
        "value": "Nuevo"
      },
      {
        "name": "Modelo del repuesto",
        "value": "RC21-01720100-R3M1"
      }
    ]
    }
```
