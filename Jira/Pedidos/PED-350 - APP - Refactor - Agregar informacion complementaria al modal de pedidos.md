---
jira_key: "PED-350"
aliases: ["PED-350"]
summary: "APP - Refactor - Agregar informacion complementaria al modal de pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-12-18 09:21"
updated: "2023-12-19 11:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-350"
---

# PED-350: APP - Refactor - Agregar informacion complementaria al modal de pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-18 09:21 |
| Actualizado | 2023-12-19 11:41 |
| Etiquetas | ninguna |
| Jira | [PED-350](https://bluinc.atlassian.net/browse/PED-350) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **is blocked by:** [[PED-349]] API -  Refactor - Ver detalle de una orden de compra -> Agregar tracking number

## Descripcion

[adjunto]
Agregaremos el trecking Number y adicionalmente un accionable para abrir el modal de trackingNumbers para poder cubrir los casos donde hay mas de uno.

```
{API_URL}/v1/orders/{pedido}/trackingNumbers
```



**Adicionalmente**

Haremos que la factura sea clickeable
