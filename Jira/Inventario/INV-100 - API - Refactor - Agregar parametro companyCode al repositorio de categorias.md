---
jira_key: "INV-100"
aliases: ["INV-100"]
summary: "API - Refactor - Agregar parametro companyCode al repositorio de categorias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-26 09:11"
updated: "2024-08-27 03:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-100"
---

# INV-100: API - Refactor - Agregar parametro companyCode al repositorio de categorias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-26 09:11 |
| Actualizado | 2024-08-27 03:30 |
| Etiquetas | ninguna |
| Jira | [INV-100](https://bluinc.atlassian.net/browse/INV-100) |

## Relaciones

- **Padre:** [[INV-69 - Categorias|INV-69]] Categorias
- **blocks:** [[INV-101 - APP - Refactor - Agregar parametro companyCode al repositorio de categorias|INV-101]] APP - Refactor - Agregar parametro companyCode al repositorio de categorias

## Descripcion

```
GET {{API_URL}}/v1/categories?companyCode={companyCode}
```

```
PATCH {{API_URL}}/v1/categories
```

```
{
companyCode: {companyCode}
}
```
