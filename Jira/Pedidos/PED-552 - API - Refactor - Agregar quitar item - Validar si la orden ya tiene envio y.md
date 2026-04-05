---
jira_key: "PED-552"
aliases: ["PED-552"]
summary: "API - Refactor - Agregar / quitar item -> Validar si la orden ya tiene envio y avisar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-09 14:49"
updated: "2024-02-14 12:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-552"
---

# PED-552: API - Refactor - Agregar / quitar item -> Validar si la orden ya tiene envio y avisar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-09 14:49 |
| Actualizado | 2024-02-14 12:35 |
| Etiquetas | ninguna |
| Jira | [PED-552](https://bluinc.atlassian.net/browse/PED-552) |

## Relaciones

- **Padre:** [[PED-34]] Generar / Editar ordenes

## Descripcion

/v1/orders/addItem

```
PATCH /v1/orders/addItem
```

Lo que haremos antes de agregar/remover o editar un item es verificar si dentro de este pedido tenemos un envío.

En ese caso evitare hacer la acción y en cambio devolveré un mensaje (se puede usar el código **428 Precondition Required**).

El mensaje dira “No es posible editar una orden hasta remover el envio.”.
