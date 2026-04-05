---
jira_key: "NBWEB-612"
aliases: ["NBWEB-612"]
summary: "API - Refactor - Mis datos - Restricción de duplicados"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2024-01-17 18:13"
updated: "2024-01-17 18:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-612"
---

# NBWEB-612: API - Refactor - Mis datos - Restricción de duplicados

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-17 18:13 |
| Actualizado | 2024-01-17 18:21 |
| Etiquetas | ninguna |
| Jira | [NBWEB-612](https://bluinc.atlassian.net/browse/NBWEB-612) |

## Relaciones

- **Padre:** [[NBWEB-2 - API - Mi cuenta|NBWEB-2]] API - Mi cuenta

## Descripcion

Implementaremos una nueva validación la cual no permita al usuario agregar o editar a un cliente con números/claves de identificación repetidos (CUIT/CUIL, DNI, etc.)

```
{{API_URL}}/v1/client
```

[adjunto]
