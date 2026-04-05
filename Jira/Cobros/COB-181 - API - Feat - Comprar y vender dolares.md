---
jira_key: "COB-181"
aliases: ["COB-181"]
summary: "API - Feat - Comprar y vender dolares"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-10-19 13:43"
updated: "2022-10-27 08:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-181"
---

# COB-181: API - Feat - Comprar y vender dolares

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-19 13:43 |
| Actualizado | 2022-10-27 08:37 |
| Etiquetas | ninguna |
| Jira | [COB-181](https://bluinc.atlassian.net/browse/COB-181) |

## Relaciones

- **Padre:** [[COB-175 - API - Feat - Compra venta de dolares|COB-175]] API - Feat - Compra venta de dolares
- **is blocked by:** [[COB-180 - API - Research - Compra venta dolares|COB-180]] API - Research - Compra / venta dolares

## Descripcion

Este recurso es consumido por un modal [link](https://lioteam.atlassian.net/browse/COB-174) que sirve justamente para hacer intercambio de divisas de pesos a dolares y alreves.

Para esto solo puede hacerlo siempre y cuando el saldo de la moneda que se usa para pagar el cambio, sea suficiente para hacerlo y obviamente descuenta el saldo a esa caja.



```
POST {API_RL}/V1/exchange
```

Payload

```
{
type: //pude ser compra o venta,
currencyQuote: //es la cotizacion de la divisa
dollarAmount : //este es el monto en dolares
pesoAmount : //este es el monto en dolares
}
```
