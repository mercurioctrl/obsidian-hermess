---
jira_key: "COB-381"
aliases: ["COB-381"]
summary: "API - Feat - Mover saldo entre cuentas de clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-23 08:38"
updated: "2023-03-30 10:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-381"
---

# COB-381: API - Feat - Mover saldo entre cuentas de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-23 08:38 |
| Actualizado | 2023-03-30 10:37 |
| Etiquetas | ninguna |
| Jira | [COB-381](https://bluinc.atlassian.net/browse/COB-381) |

## Relaciones

- **Padre:** [[COB-380 - Feat - Mover saldo entre cuentas de cliente|COB-380]] Feat - Mover saldo entre cuentas de cliente
- **blocks:** [[COB-384 - APP - Feat - Mover saldo entre cuentas de clientes|COB-384]] APP - Feat - Mover saldo entre cuentas de clientes

## Descripcion

Este recurso se trata sobre mover saldos de clientes entre cuenta.

Requiere un permiso especial en la tabla `NB_WEB.dbo.permisos_agente.moveBalance` (si no existe, se agrega) y ademas envía un correo a [gerencia@nb.com.ar](mailto:gerencia@nb.com.ar) con la siguiente leyenda.

Obviamente solo puede hacerse a partir del saldo excedente, sin considerar créditos. Solo saldo. En caso de que el monto que se desee mover, sea mayor a “este saldo” se debe informar al respecto.

###### “Se movieron {amount} desde la cuenta origen ({clientId}) - {Nombre de cliente} a la cuenta de destino  ({clientId}) - {Nombre de cliente}”

```
POST {API_URL}/v1/moveBalanceCustomer
```

```
{
  amount: 1000,
  originClientId :12,
  destinyClientId :12,
  comment: "un comentario cualquiera"
}
```
