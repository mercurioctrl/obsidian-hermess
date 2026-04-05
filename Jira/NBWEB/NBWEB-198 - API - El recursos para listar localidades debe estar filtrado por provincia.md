---
jira_key: "NBWEB-198"
aliases: ["NBWEB-198"]
summary: "API - El recursos para listar localidades debe estar filtrado por provincia siempre "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-22 21:50"
updated: "2022-06-26 21:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-198"
---

# NBWEB-198: API - El recursos para listar localidades debe estar filtrado por provincia siempre 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-22 21:50 |
| Actualizado | 2022-06-26 21:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-198](https://bluinc.atlassian.net/browse/NBWEB-198) |

## Relaciones

- **Padre:** [[NBWEB-130 - API - Registro y alta de cliente|NBWEB-130]] API - Registro y alta de cliente

## Descripcion

Mala mia, este recurso debe estar siempre filtrado de la siguiente manera



```
GET {{API_URL}}/v1/places/{provincesId}
```
