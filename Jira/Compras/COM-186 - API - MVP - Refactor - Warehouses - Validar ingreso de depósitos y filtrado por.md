---
jira_key: "COM-186"
aliases: ["COM-186"]
summary: "API - MVP - Refactor - Warehouses -> Validar ingreso de depósitos y filtrado por identificador"
status: "Finalizada"
type: "Tarea"
priority: "Lowest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-05-09 11:23"
updated: "2025-09-30 10:16"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/COM-186"
---

# COM-186: API - MVP - Refactor - Warehouses -> Validar ingreso de depósitos y filtrado por identificador

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-05-09 11:23 |
| Actualizado | 2025-09-30 10:16 |
| Etiquetas | MVPLaset |
| Jira | [COM-186](https://bluinc.atlassian.net/browse/COM-186) |

## Relaciones

- **Padre:** [[COM-178 - Depositos|COM-178]] Depositos

## Descripcion

Vamos a refactorizar para:

- Validar que no se agreguen códigos (`CODE`) repetidos al ingresar depósitos.


- Investigar si es viable usar el ID del depósito como parámetro principal de filtrado.



```
{{API_URL}}/v1/warehouses
```

[adjunto]
