---
jira_key: "EXP-449"
aliases: ["EXP-449"]
summary: "API - Refactor - Permitir editar pesos y medidas del item igual que ean/sku/gtin"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-24 14:16"
updated: "2024-10-01 16:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-449"
---

# EXP-449: API - Refactor - Permitir editar pesos y medidas del item igual que ean/sku/gtin

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-24 14:16 |
| Actualizado | 2024-10-01 16:10 |
| Etiquetas | ninguna |
| Jira | [EXP-449](https://bluinc.atlassian.net/browse/EXP-449) |

## Relaciones

- **Padre:** [[EXP-11 - Feat - Serializar entrada de mercadería|EXP-11]] Feat - Serializar entrada de mercadería
- **blocks:** [[EXP-448 - APP - Refactor - Cargar pesos y medidas del producto si no existen cuando se|EXP-448]] APP - Refactor - Cargar pesos y medidas del producto si no existen cuando se serializan y no los tienen

## Descripcion

```
PATCH {API_URL}/items/{productId}
```

```
{
    "gtin": "12345678999999",  <-- puede ser cualquiera de los codigos (gtin,ean,isbn,upc)
    "ean":"0012345678905a",  <-- puede ser cualquiera de los codigos (gtin,ean,isbn,upc)
    "isbn": "9788481300185",  <-- puede ser cualquiera de los codigos (gtin,ean,isbn,upc)
    "upc":"012345678905",  <-- puede ser cualquiera de los codigos (gtin,ean,isbn,upc)
    "weightAverage": 10, <-- Olbigatorio, no puede ser cero
    "lengthAverage": 10,  <-- Olbigatorio, no puede ser cero
    "widthAverage": 10,  <-- Olbigatorio, no puede ser cero
    "highAverage": 10,  <-- Olbigatorio, no puede ser cero
    
    "packagePerUnit": 10,  <-- Olbigatorio, no puede ser cero
}

```
