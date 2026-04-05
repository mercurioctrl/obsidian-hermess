---
jira_key: "EXP-284"
aliases: ["EXP-284"]
summary: "API - Refactor - Se agrega un estado especifico para cuando el producto fue entregado y posteriormente acreditado parcial o totalmente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-16 14:19"
updated: "2023-05-17 15:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-284"
---

# EXP-284: API - Refactor - Se agrega un estado especifico para cuando el producto fue entregado y posteriormente acreditado parcial o totalmente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-16 14:19 |
| Actualizado | 2023-05-17 15:05 |
| Etiquetas | ninguna |
| Jira | [EXP-284](https://bluinc.atlassian.net/browse/EXP-284) |

## Relaciones

- **Padre:** [[EXP-119]] Feat - Acreditar un pedido parcial o totalmente
- **blocks:** [[SNB-770]] ver en cobros pendientes

## Descripcion

Se agregaron a la tabla `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]` los estados

- 15 - Entregado. Acreditación completa


- 16 - Entregado. Acreditación parcial



Se debe refactorizar la feature [link](https://lioteam.atlassian.net/browse/EXP-125) 


```
POST {API_URL}/v1/ordersRefund/{pedido}
```

Para poder cambiar el estado, según sea el caso.

En el caso que sea exitosa mi acreditación y el resultado de 

```
SELECT SUM(ncanent - ACREDITADO)
  FROM [NewBytes_DBF].[dbo].[albclil]
  WHERE   ID_NROREMCLI_ENC = ?
```

sea 0 (cero) podemos decir entoncs que todo lo que se compro fue acreditado y entonces es una **Acreditacion Completa **del pedido y por lo tanto lo marcaremos como **15 - Entregado. Acreditación completa**.

En caso contrario, podríamos inferir que si acabo de hacer una devolución (o acreditacion) el estado que debo marcar es **16 - Entregado. Acreditación parcial**
