---
jira_key: "PED-566"
aliases: ["PED-566"]
summary: "API - Feat - Bonificar envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-22 10:27"
updated: "2024-02-28 13:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-566"
---

# PED-566: API - Feat - Bonificar envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-22 10:27 |
| Actualizado | 2024-02-28 13:41 |
| Etiquetas | ninguna |
| Jira | [PED-566](https://bluinc.atlassian.net/browse/PED-566) |

## Relaciones

- **Padre:** [[PED-58 - Agregar Editar Envío en las ordenes de compra|PED-58]] Agregar / Editar Envío en las ordenes de compra
- **blocks:** [[PED-571 - APP - Feat - Bonificar Envio|PED-571]] APP - Feat - Bonificar Envio
- **is blocked by:** [[PED-573 - API - Bonificar envío - Agregar creador al registro|PED-573]] API - Bonificar envío - Agregar creador al registro

## Descripcion

```
POST {{API_URL}}/order/{branch}-{order}/discountShipping
```

Crearemos un recurso para bonificar envío, ligado a un permiso especifico “`discountShipping`".

Es decir que quien tenga el permiso puede ejecutar esto para cualquier pedido.

Lo que hace es poner el precio de envío en cero (No así el costo del mismo, que permanece para saber cuanto cuesta)

Adicionalmente estaria bueno guardar en una tabla anexa quien hizo la bonificacion, cuando y cual era el precio de la misma, y el numero de orden bonificado.
