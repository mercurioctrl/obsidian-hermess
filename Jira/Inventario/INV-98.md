---
jira_key: "INV-98"
summary: "API - Refactor - Agregar parametro companyCode al repositorio de marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-23 09:24"
updated: "2024-08-27 03:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-98"
---

# INV-98: API - Refactor - Agregar parametro companyCode al repositorio de marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-23 09:24 |
| Actualizado | 2024-08-27 03:27 |
| Etiquetas | ninguna |
| Jira | [INV-98](https://bluinc.atlassian.net/browse/INV-98) |

## Descripción

```
GET {{API_URL}}/v1/brands?companyCode={companyCode}
```

```
PATCH {{API_URL}}/v1/brands
```

```
{
companyCode: {companyCode}
}
```
