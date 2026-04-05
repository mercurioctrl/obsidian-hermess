---
jira_key: "COB-359"
aliases: ["COB-359"]
summary: "API - Refactor - Si es efectivo, tiene que dejarte ponerte la plata en la cuenta del cliente (Solo cuando la esta agregando a la caja digamos)"
status: "CodeReview"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-10 16:41"
updated: "2023-03-13 09:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-359"
---

# COB-359: API - Refactor - Si es efectivo, tiene que dejarte ponerte la plata en la cuenta del cliente (Solo cuando la esta agregando a la caja digamos)

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-10 16:41 |
| Actualizado | 2023-03-13 09:58 |
| Etiquetas | ninguna |
| Jira | [COB-359](https://bluinc.atlassian.net/browse/COB-359) |

## Relaciones

- **Padre:** [[COB-33 - Cobrar|COB-33]] Cobrar

## Descripcion

Actualmente al intentarlo da 

```
App\Repository\Box\BoxTradeRepository::searchOrder(): Argument #1 ($numOrder) must be of type string, null given, called in /var/www/app/src/Service/Box/Trade/ExecuteTrade.php on line 467
```

[adjunto]
Es importante que esto aplique solo a a EFECTIVO dolar/pesos ya que el unico mecanismo de control de esto, es que la plata esta en la caja fisicamente.
