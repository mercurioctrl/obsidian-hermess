---
jira_key: "EXP-381"
aliases: ["EXP-381"]
summary: "API - Refactor - Al hacer la entrega de mercadería, se debe marcar entregado para libre opción"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-11 08:55"
updated: "2023-12-13 15:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-381"
---

# EXP-381: API - Refactor - Al hacer la entrega de mercadería, se debe marcar entregado para libre opción

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-11 08:55 |
| Actualizado | 2023-12-13 15:46 |
| Etiquetas | ninguna |
| Jira | [EXP-381](https://bluinc.atlassian.net/browse/EXP-381) |

## Relaciones

- **Padre:** [[EXP-258 - Feat - Autorizar Entrega mediante tarjeta de autorizacion|EXP-258]] Feat - Autorizar Entrega mediante tarjeta de autorizacion
- **is blocked by:** [[EXP-382 - API - Marcar mercadería entregada para LO - Incidencias varias|EXP-382]] API - Marcar mercadería entregada para LO - Incidencias varias

## Descripcion

Al ejecutar el recurso 

```
PATCH {API_URL}/v1/orders/{pedido}/hand
```

Sobre un pedido de Libre Opción

Se debe marcar como entregado tambien para libre opcion

`[LO].[dbo].[pedidosCabeceraVendedor].[entregado]`

`[LO].[dbo].[pedidosCabeceraPaquete]`.`[entregado]`

`[LO].[dbo].[pedidosCabecera].[despachado]`
