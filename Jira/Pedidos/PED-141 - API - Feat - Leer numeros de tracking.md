---
jira_key: "PED-141"
aliases: ["PED-141"]
summary: "API - Feat - Leer numeros de tracking"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-12 12:22"
updated: "2023-10-17 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-141"
---

# PED-141: API - Feat - Leer numeros de tracking

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-12 12:22 |
| Actualizado | 2023-10-17 10:33 |
| Etiquetas | ninguna |
| Jira | [PED-141](https://bluinc.atlassian.net/browse/PED-141) |

## Relaciones

- **Padre:** [[PED-58 - Agregar Editar Envío en las ordenes de compra|PED-58]] Agregar / Editar Envío en las ordenes de compra
- **blocks:** [[PED-139 - APP - Refactor - Agregar controlador de tracking|PED-139]] APP - Refactor - Agregar controlador de tracking

## Descripcion

Basados en [link](https://lioteam.atlassian.net/browse/EXP-104) 

Esta historia sirve para mostrar todos los tracking numbers que un pedido tienen asociado, para luego mostrar las etiquetas para cada uno de ellos

```
GET {API_URL}/v1/orders/{pedido}/trackingNumbres
```

 

Esta basado en la tabla `[NewBytes_DBF].[dbo].[trackingNumber]` y se utiliza `order` y `branch` como claves
