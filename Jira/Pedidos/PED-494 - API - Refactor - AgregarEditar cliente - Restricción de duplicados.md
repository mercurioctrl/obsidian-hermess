---
jira_key: "PED-494"
aliases: ["PED-494"]
summary: "API - Refactor - Agregar/Editar cliente - Restricción de duplicados "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-01-17 17:06"
updated: "2024-02-01 19:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-494"
---

# PED-494: API - Refactor - Agregar/Editar cliente - Restricción de duplicados 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-17 17:06 |
| Actualizado | 2024-02-01 19:49 |
| Etiquetas | ninguna |
| Jira | [PED-494](https://bluinc.atlassian.net/browse/PED-494) |

## Relaciones

- **Padre:** [[PED-16]] Listar clientes
- **is blocked by:** [[PED-516]] API - Agregar/Editar cliente - Restricción de duplicados - Incidencias varias

## Descripcion

Implementaremos una nueva validación la cual no permita al usuario agregar o editar a un cliente con números/claves de identificación repetidos (CUIT/CUIL, DNI, etc.)

```
{{API_URL}}/v1/clients
```

[adjunto]
