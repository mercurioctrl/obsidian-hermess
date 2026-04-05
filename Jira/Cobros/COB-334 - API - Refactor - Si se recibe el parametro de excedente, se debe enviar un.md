---
jira_key: "COB-334"
aliases: ["COB-334"]
summary: "API - Refactor - Si se recibe el parametro de excedente, se debe enviar un correo a los administradores"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-02-23 17:26"
updated: "2023-02-24 12:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-334"
---

# COB-334: API - Refactor - Si se recibe el parametro de excedente, se debe enviar un correo a los administradores

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-23 17:26 |
| Actualizado | 2023-02-24 12:20 |
| Etiquetas | ninguna |
| Jira | [COB-334](https://bluinc.atlassian.net/browse/COB-334) |

## Relaciones

- **Padre:** [[COB-115]] Feat - Realizar un cobro

## Descripcion

Al ejecutar [link](https://lioteam.atlassian.net/browse/COB-126)  debemos procesar un nuevo parametro.

Según [link](https://lioteam.atlassian.net/browse/COB-320)  si se genera un excedente mayor a un valor determinado se recibirá el parámetro `surplusFlag:true` al hacer un cobro.

Si es así, entonces enviaremos un correo a los administradores con el siguiente texto:

```
Se realizo un cobro en el pedido XXXX que tiene un excedente mayor a XXXX.
El total del pedido fue XXX
El total del excedente fue xxxx y quedo acreditado en la cuenta del cliente como saldo a favor.
```
