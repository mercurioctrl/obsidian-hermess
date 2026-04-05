---
jira_key: "POS-271"
aliases: ["POS-271"]
summary: "API - Refactor - Agregar el proveedor de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-03 13:50"
updated: "2023-10-03 17:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-271"
---

# POS-271: API - Refactor - Agregar el proveedor de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-03 13:50 |
| Actualizado | 2023-10-03 17:10 |
| Etiquetas | ninguna |
| Jira | [POS-271](https://bluinc.atlassian.net/browse/POS-271) |

## Relaciones

- **Padre:** [[POS-270 - Recuperos|POS-270]] Recuperos

## Descripcion

```
GET {API_URL}/v1/afterSaleProviders
```

Por alguna razón los parámetros

providerId
providerDescription 

llegan vacíos o en cero

Ahí tienen que llegar los proveedores de compra
