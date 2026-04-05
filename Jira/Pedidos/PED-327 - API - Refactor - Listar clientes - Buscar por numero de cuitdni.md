---
jira_key: "PED-327"
aliases: ["PED-327"]
summary: "API - Refactor - Listar clientes -> Buscar por numero de cuit/dni"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-13 13:18"
updated: "2024-01-26 04:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-327"
---

# PED-327: API - Refactor - Listar clientes -> Buscar por numero de cuit/dni

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-13 13:18 |
| Actualizado | 2024-01-26 04:36 |
| Etiquetas | ninguna |
| Jira | [PED-327](https://bluinc.atlassian.net/browse/PED-327) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **relates to:** [[PED-337 - Listar clientes - Buscar por número de CUITDNI - Incidencias varias|PED-337]] Listar clientes -> Buscar por número de CUIT/DNI - Incidencias varias

## Descripcion

Modificaremos el recurso 

```
GET /v1/clients?search={string}
```

para decir que si el parametro `search` contiene una cadena que al quitarle todos los guiones, son solo numeros, entonces tambien buscaremos el la columna de documento
