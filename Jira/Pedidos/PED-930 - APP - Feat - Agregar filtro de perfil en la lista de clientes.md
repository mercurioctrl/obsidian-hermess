---
jira_key: "PED-930"
aliases: ["PED-930"]
summary: "APP - Feat - Agregar filtro de perfil en la lista de clientes"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-10 08:24"
updated: "2025-01-20 11:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-930"
---

# PED-930: APP - Feat - Agregar filtro de perfil en la lista de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-10 08:24 |
| Actualizado | 2025-01-20 11:21 |
| Etiquetas | ninguna |
| Jira | [PED-930](https://bluinc.atlassian.net/browse/PED-930) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **action item from:** [[PED-928 - API - Refactor - Agregar el parámetro perfil al repositorio de clientes|PED-928]] API - Refactor - Agregar el parámetro "perfil" al repositorio de clientes
- **action item from:** [[PED-929 - API - Feat - Agregar tabla complementaria de perfiles y repositorio de perfiles|PED-929]] API - Feat - Agregar tabla complementaria de perfiles y repositorio de perfiles

## Descripcion

Crearemos un filtro de perfil para que puedan filtrar los clientes por tipo de perfil (el tipo de perfil es que tipo de lista de precio les toca) y combinado con otros filtros

```
GET {API_URL}/v1/clients?profile=1
```

[adjunto]
Para eso utilizaremos  [link](https://lioteam.atlassian.net/browse/PED-928)  y [link](https://lioteam.atlassian.net/browse/PED-929)
