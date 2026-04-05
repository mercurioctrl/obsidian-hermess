---
jira_key: "NBWEB-535"
aliases: ["NBWEB-535"]
summary: "API - Refactor - Editar Formas de Cobro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-04-24 07:56"
updated: "2023-05-08 07:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-535"
---

# NBWEB-535: API - Refactor - Editar Formas de Cobro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-24 07:56 |
| Actualizado | 2023-05-08 07:21 |
| Etiquetas | ninguna |
| Jira | [NBWEB-535](https://bluinc.atlassian.net/browse/NBWEB-535) |

## Relaciones

- **Padre:** [[NBWEB-533]] CMS - Medio de pago
- **blocks:** [[NBWEB-534]] APP - Refactor - Agregar FP_TOLERANCIA_DE_PAGO y DIF_COTIZACION_TOLERADA a la lista de medio formas de cobro para su edicion

## Descripcion

```
PATCH {API_URL}/v1/cms/paymentMethodTrade
```

Incluiremos los 2 parámetros nuevos a la edición de parámetros de medio de pago

- DIF_COTIZACION_TOLERADA


- FP_TOLERANCIA_DE_PAGO
