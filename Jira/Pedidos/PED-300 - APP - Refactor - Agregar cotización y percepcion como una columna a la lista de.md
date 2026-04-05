---
jira_key: "PED-300"
aliases: ["PED-300"]
summary: "APP - Refactor - Agregar cotización y percepcion como una columna a la lista de pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-12-04 08:34"
updated: "2024-02-14 18:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-300"
---

# PED-300: APP - Refactor - Agregar cotización y percepcion como una columna a la lista de pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-04 08:34 |
| Actualizado | 2024-02-14 18:01 |
| Etiquetas | ninguna |
| Jira | [PED-300](https://bluinc.atlassian.net/browse/PED-300) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **relates to:** [[PED-561 - APP - Listar órdenes de compra - Color en percepciones|PED-561]] APP - Listar órdenes de compra - Color en percepciones

## Descripcion

Utilizando el parámetro `currency` y `perception` que llega en el recurso 

```
{API_URL}/v1/orders
```

Lo agregaremos en una columna antes de los totales finales.

[adjunto]
Estos datos deben usarse para mostrar los valores en pesos y dolares, en caso de que lleguen, caso contrario se usa la cotización del día.
