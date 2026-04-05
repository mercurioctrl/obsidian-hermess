---
jira_key: "COB-367"
aliases: ["COB-367"]
summary: "API - Feat - Pagar al cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-17 13:03"
updated: "2023-04-11 09:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-367"
---

# COB-367: API - Feat - Pagar al cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-17 13:03 |
| Actualizado | 2023-04-11 09:34 |
| Etiquetas | ninguna |
| Jira | [COB-367](https://bluinc.atlassian.net/browse/COB-367) |

## Relaciones

- **Padre:** [[COB-366 - Feat - Pagar al cliente con su saldo en cuenta|COB-366]] Feat - Pagar al cliente con su saldo en cuenta

## Descripcion

Se trata de un recurso para poder pagarle al cliente con su saldo.

En principio debemos validar que “el saldo”  sea menor o igual al monto que deseamos pagarle.

Y luego que tengamos esa cantidad de dinero en la caja.

De ser así, registramos el débito de la cc del cliente y hacemos lo mismo en la caja que esta realizando el pago.

```
POST {API_URL}/v1/payCustomer
```

```
{
  amount: 1000,
  paymenthMethod: 1,
  clientId :12,
  comment: "un comentario cualquiera"
}
```

Para esto usaremos el TR_CODIGO = 34
