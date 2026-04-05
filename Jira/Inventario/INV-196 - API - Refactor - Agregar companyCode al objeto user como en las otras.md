---
jira_key: "INV-196"
aliases: ["INV-196"]
summary: "API - Refactor - Agregar companyCode al objeto user como en las otras aplicaciones"
status: "Finalizada"
type: "Subtarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-04 15:39"
updated: "2025-09-03 19:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-196"
---

# INV-196: API - Refactor - Agregar companyCode al objeto user como en las otras aplicaciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-04 15:39 |
| Actualizado | 2025-09-03 19:26 |
| Etiquetas | ninguna |
| Jira | [INV-196](https://bluinc.atlassian.net/browse/INV-196) |

## Relaciones

- **Padre:** [[INV-24]] Feat - Bases y login
- **has action item:** [[INV-195]] APP - INV- agregar el selector de empresa general (en la parte superior derecha como PED o EXP)

## Descripcion

```
POST {API_URL}/auth/user
```

```
{"user":
{
"id":7463,
"username":"catriel",
"email":"hermess87@gmail.com"
"companyCode": 4
}
}
```

Si no tienen ninguna, viene en null
