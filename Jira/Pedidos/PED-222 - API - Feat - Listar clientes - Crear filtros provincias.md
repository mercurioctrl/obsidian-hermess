---
jira_key: "PED-222"
aliases: ["PED-222"]
summary: "API - Feat - Listar clientes -> Crear filtros provincias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-11-03 09:54"
updated: "2023-11-08 08:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-222"
---

# PED-222: API - Feat - Listar clientes -> Crear filtros provincias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-03 09:54 |
| Actualizado | 2023-11-08 08:44 |
| Etiquetas | ninguna |
| Jira | [PED-222](https://bluinc.atlassian.net/browse/PED-222) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes

## Descripcion

Basándose en el repositorio [link](https://lioteam.atlassian.net/browse/PED-21)  se debe poder filtrar el listado de clientes ([link](https://lioteam.atlassian.net/browse/PED-17) ) de la siguiente forma según su provincia

```
GET {API_URL}/v1/clients?provinceId={id de la provincia}
```
