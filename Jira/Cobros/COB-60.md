---
jira_key: "COB-60"
summary: "API - Feat - Agregar saldo en cuenta a un cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-18 10:27"
updated: "2022-10-20 17:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-60"
---

# COB-60: API - Feat - Agregar saldo en cuenta a un cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-18 10:27 |
| Actualizado | 2022-10-20 17:08 |
| Etiquetas | ninguna |
| Jira | [COB-60](https://bluinc.atlassian.net/browse/COB-60) |

## Descripción

Esta historia se trata sobre como agregar un saldo en la cuenta corriente del cliente, o bien quitarlo.

Se hace mediante una inserción en la tabla `[NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]` para ese cliente.

```
POST {API_RUL}/v1/currentAccount
```

```
{
  clientId: 33123,
  trCode: 16, // estee es el tr code para este tipo de movimiento, puede ser 34 tambien si le estamos sacando plata de la cuenta
  amount: 3233,3,
  comment: "Este es un comentario cualquier opcional"
}
```
