---
jira_key: "PED-928"
aliases: ["PED-928"]
summary: "API - Refactor - Agregar el parámetro \"perfil\" al repositorio de clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-10 08:10"
updated: "2025-01-27 17:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-928"
---

# PED-928: API - Refactor - Agregar el parámetro "perfil" al repositorio de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-10 08:10 |
| Actualizado | 2025-01-27 17:33 |
| Etiquetas | ninguna |
| Jira | [PED-928](https://bluinc.atlassian.net/browse/PED-928) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes
- **has action item:** [[PED-930]] APP - Feat - Agregar filtro de perfil en la lista de clientes

## Descripcion

Crearemos un filtro de perfil para que puedan filtrar los clientes por tipo de perfil (el tipo de perfil es que tipo de lista de precio les toca) y combinado con otros filtros

```
GET {API_URL}/v1/clients?profile=1
```

Basándonos en el parámetro `[NewBytes_DBF].[dbo].[clientes].perfil`
