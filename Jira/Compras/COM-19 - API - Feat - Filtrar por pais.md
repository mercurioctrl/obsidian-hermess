---
jira_key: "COM-19"
aliases: ["COM-19"]
summary: "API - Feat - Filtrar por pais"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-13 16:46"
updated: "2024-02-14 09:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-19"
---

# COM-19: API - Feat - Filtrar por pais

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-13 16:46 |
| Actualizado | 2024-02-14 09:47 |
| Etiquetas | ninguna |
| Jira | [COM-19](https://bluinc.atlassian.net/browse/COM-19) |

## Relaciones

- **Padre:** [[COM-6]] Listar proveedores
- **is blocked by:** [[COM-16]] API - Feat - Repositorios Paises
- **blocks:** [[COM-20]] APP - Feat - Filtrar por pais

## Descripcion

```
GET {{API_URL}}/v1/providers?countryId={countryId}
```

Agregaremos le filtro de pais
