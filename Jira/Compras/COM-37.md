---
jira_key: "COM-37"
summary: "API - Refactor - Listar proveedores -> Agregar búsqueda general"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-02-16 14:07"
updated: "2024-02-20 11:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-37"
---

# COM-37: API - Refactor - Listar proveedores -> Agregar búsqueda general

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-16 14:07 |
| Actualizado | 2024-02-20 11:30 |
| Etiquetas | ninguna |
| Jira | [COM-37](https://bluinc.atlassian.net/browse/COM-37) |

## Descripción

Basándonos en el recurso

```
GET {{API_URL}}/v1/providers?name={name, id o businessName}&countryId={countryId}&provicenId={provicenId}&localitieId={localitieId}
```

Vamos a cambiar el parámetro de búsqueda de `name` por `search`. De esta manera, mantendremos la misma línea en las búsquedas generales.
