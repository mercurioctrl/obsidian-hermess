---
jira_key: "INV-136"
aliases: ["INV-136"]
summary: "API - Refactor - Al editar y crear un producto tambien alterar los parametros viejos en string"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-18 14:18"
updated: "2024-09-24 23:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-136"
---

# INV-136: API - Refactor - Al editar y crear un producto tambien alterar los parametros viejos en string

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-18 14:18 |
| Actualizado | 2024-09-24 23:08 |
| Etiquetas | ninguna |
| Jira | [INV-136](https://bluinc.atlassian.net/browse/INV-136) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **is blocked by:** [[INV-142 - Refactor Validar sku|INV-142]] Refactor: Validar sku

## Descripcion

Cuando agregas un item, no se crea ccdofam (solo id_Categoria)
Cuando agregas un item no se agrega el nombre de la marca (cpredef4)
