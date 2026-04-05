---
jira_key: "PED-1178"
aliases: ["PED-1178"]
summary: "API - Refactor - Generar pedido -> Evitar creación y duplicación de pedidos ante errores en el proceso"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-10 08:26"
updated: "2025-12-17 11:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1178"
---

# PED-1178: API - Refactor - Generar pedido -> Evitar creación y duplicación de pedidos ante errores en el proceso

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-10 08:26 |
| Actualizado | 2025-12-17 11:21 |
| Etiquetas | ninguna |
| Jira | [PED-1178](https://bluinc.atlassian.net/browse/PED-1178) |

## Relaciones

- **Padre:** [[PED-4 - Pedidos|PED-4]] Pedidos
- **relates to:** [[PED-90 - API - Feat- Generar pedido (albclit) desde una orden de compra (pedclit)|PED-90]] API - Feat- Generar pedido (albclit) desde una orden de compra (pedclit)

## Descripcion

Al generar un pedido, si ocurre un error durante el proceso, en algunos casos se crean dos pedidos para la misma orden. Para evitar este comportamiento, se realizará un refactor que garantice que, ante cualquier error en el proceso, el pedido no sea creado ni la orden duplicada.

Algunas propuestas:

- Envolver la creación de la orden en una transacción de base de datos y ejecutar un rollback ante cualquier error.


- Separar la lógica de validación y persistencia, creando la orden únicamente al final del proceso.


- Definir claramente el orden de ejecución de las sentencias, asegurando que todas las validaciones y operaciones previas se completen correctamente antes de insertar o confirmar la creación de la orden.





```
POST {{API_URL}}/v1/makeSale
```

[adjunto]
