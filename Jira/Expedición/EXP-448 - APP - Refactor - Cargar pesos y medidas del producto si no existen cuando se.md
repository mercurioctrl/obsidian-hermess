---
jira_key: "EXP-448"
aliases: ["EXP-448"]
summary: "APP - Refactor - Cargar pesos y medidas del producto si no existen cuando se serializan y no los tienen"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-09-24 12:42"
updated: "2024-09-27 10:27"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/EXP-448"
---

# EXP-448: APP - Refactor - Cargar pesos y medidas del producto si no existen cuando se serializan y no los tienen

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-24 12:42 |
| Actualizado | 2024-09-27 10:27 |
| Etiquetas | esperandoDependencia |
| Jira | [EXP-448](https://bluinc.atlassian.net/browse/EXP-448) |

## Relaciones

- **Padre:** [[EXP-11 - Feat - Serializar entrada de mercadería|EXP-11]] Feat - Serializar entrada de mercadería
- **action item from:** [[EXP-447 - API - Refactor - No dejar serializar un item que no tiene pesos,medidas y|EXP-447]] API - Refactor - No dejar serializar un item que no tiene pesos,medidas y cantidad por bulto
- **is blocked by:** [[EXP-449 - API - Refactor - Permitir editar pesos y medidas del item igual que eanskugtin|EXP-449]] API - Refactor - Permitir editar pesos y medidas del item igual que ean/sku/gtin
- **relates to:** [[EXP-450 - APP - Refactor - comentar paquetes por unidad|EXP-450]] APP - Refactor -  comentar paquetes por unidad

## Descripcion

Asi como lo hacemos lo mismo cuando no tiene Ean o Upc, agregaremos que para un prodcuto que no posee medidas, la obligacion de cargarlas mediante un formulario
