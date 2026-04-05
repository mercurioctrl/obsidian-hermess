---
jira_key: "PED-896"
aliases: ["PED-896"]
summary: "API - Refactor - Al generar una orden para un cliente que no tiene vendedor, quien genera la orden pasa a poseerlo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-04 11:46"
updated: "2024-12-22 21:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-896"
---

# PED-896: API - Refactor - Al generar una orden para un cliente que no tiene vendedor, quien genera la orden pasa a poseerlo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-04 11:46 |
| Actualizado | 2024-12-22 21:11 |
| Etiquetas | ninguna |
| Jira | [PED-896](https://bluinc.atlassian.net/browse/PED-896) |

## Relaciones

- **Padre:** [[PED-34]] Generar / Editar ordenes

## Descripcion

Refactorizaremos el recurso

```
POST {API_URL}/v1/orders
```

De modo tal que si no tiene ID_VENDEDOR (y cccodage) el cliente, entonces se asigna el mismo en ese momento tanto en

```
  [NewBytes_DBF].[dbo].[clientes].ccodage
  [NewBytes_DBF].[dbo].[clientes].ID_VENDEDOR
```

Así como tambien en el pedido en si mismo (para que no pierda la comision)

```
[NewBytes_DBF].[dbo].[pedclit].ccodage
[NewBytes_DBF].[dbo].[pedclit].ID_VENDEDOR
```
