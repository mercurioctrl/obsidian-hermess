---
jira_key: "PED-52"
aliases: ["PED-52"]
summary: "API - Feat - Eliminar direccion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2023-08-29 11:04"
updated: "2024-03-01 15:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-52"
---

# PED-52: API - Feat - Eliminar direccion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2023-08-29 11:04 |
| Actualizado | 2024-03-01 15:29 |
| Etiquetas | ninguna |
| Jira | [PED-52](https://bluinc.atlassian.net/browse/PED-52) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **blocks:** [[PED-578 - API - Feat - Eliminar direccion - Evitar que se eliminen direcciones vinculadas|PED-578]] API - Feat - Eliminar direccion -> Evitar que se eliminen direcciones vinculadas a pedidos pendietes de ser despachadas

## Descripcion

```
{{API_URL}}/v1/shippingAddress/{clientId}/{idDirCli}
```



Elimina logicamente la direccion del cliente
