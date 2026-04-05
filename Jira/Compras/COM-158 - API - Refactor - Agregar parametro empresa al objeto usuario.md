---
jira_key: "COM-158"
aliases: ["COM-158"]
summary: "API - Refactor - Agregar parametro empresa al objeto usuario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-09 08:26"
updated: "2026-01-29 16:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-158"
---

# COM-158: API - Refactor - Agregar parametro empresa al objeto usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-09 08:26 |
| Actualizado | 2026-01-29 16:57 |
| Etiquetas | ninguna |
| Jira | [COM-158](https://bluinc.atlassian.net/browse/COM-158) |

## Relaciones

- **Padre:** [[COM-156]] Filtro Empresa
- **has action item:** [[COM-159]] APP - Refactor - Agregar filtro empresa global
- **action item from:** [[COM-281]] API - Refactor - Usuario autenticado → Homologado de respuesta en companyCode

## Descripcion

```
GET {API_URL}/v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "codeFP": 19227,
        "username": "catriel",
        "email": "hermess87@gmail.com",
        "codeAgent": 12,
        "showName": "catriel2",
        "usuIdentification": "Seba",
        "compras": true,
        "pm": true,
        "companyCode": 4 <-- Se agrega
    }
}
```
