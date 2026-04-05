---
jira_key: "COB-439"
aliases: ["COB-439"]
summary: "API - Feat - Recurso para expirar cuentas corrientes"
status: "CodeReview"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-06-07 17:08"
updated: "2023-06-15 10:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-439"
---

# COB-439: API - Feat - Recurso para expirar cuentas corrientes

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-07 17:08 |
| Actualizado | 2023-06-15 10:52 |
| Etiquetas | ninguna |
| Jira | [COB-439](https://bluinc.atlassian.net/browse/COB-439) |

## Relaciones

- **Padre:** [[COB-20 - Cuentas Corrientes|COB-20]] Cuentas Corrientes
- **blocks:** [[SNB-822 - Lo que me parece q no anda es la fecha q le coloco q caduca una linea de credito|SNB-822]] Lo que me parece q no anda es la fecha q le coloco q caduca una linea de credito

## Descripcion

Crearemos un recurso que nos permita expirar las cuentas corrientes según la fecha

```
GET {API_RUL}/v1/balances/expire?token={tokeEnEl.Env}
```

Lo que hace es poner en cero todas las lineas de crédito

osea: `limitCheckBalanceAmount` y `limitBalanceAmount`

según la fecha correspondiente a cada caso sea anterior  al día actual

Ademas se debe retornar un objeto con los clientes que fueron afectados

Adicionalmente:

Agregaremos un envío de correo a la gerencia con la lista de clientes que perdieron la linea de crédito.
