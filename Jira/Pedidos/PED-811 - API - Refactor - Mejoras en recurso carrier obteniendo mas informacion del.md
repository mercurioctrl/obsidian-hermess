---
jira_key: "PED-811"
aliases: ["PED-811"]
summary: "API - Refactor - Mejoras en recurso carrier obteniendo mas informacion del transportista asignado "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-08-29 16:28"
updated: "2024-09-02 23:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-811"
---

# PED-811: API - Refactor - Mejoras en recurso carrier obteniendo mas informacion del transportista asignado 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-08-29 16:28 |
| Actualizado | 2024-09-02 23:29 |
| Etiquetas | ninguna |
| Jira | [PED-811](https://bluinc.atlassian.net/browse/PED-811) |

## Relaciones

- **Padre:** [[PED-58 - Agregar Editar Envío en las ordenes de compra|PED-58]] Agregar / Editar Envío en las ordenes de compra

## Descripcion

Actualmente URL/v1/carrier/{id} → id del medio de envio.

se remplaza por:

URL/v1/carrier/{branch}-{order}

teniendo mas información del transportista seleccionado.

```
[
    {
        "id": 3030,
        "description": "Moto (Capital Federal)",
        "pricePes": 5199.99723,
        "priceUsd": 5.60949,
        "quoteOrder": 927
    }
]
```
