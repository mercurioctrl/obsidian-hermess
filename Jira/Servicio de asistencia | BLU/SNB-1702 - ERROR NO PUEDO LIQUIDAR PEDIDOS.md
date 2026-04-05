---
jira_key: "SNB-1702"
aliases: ["SNB-1702"]
summary: "ERROR NO PUEDO LIQUIDAR PEDIDOS"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Pedidos Jira"
created: "2024-04-03 10:49"
updated: "2024-04-03 13:31"
labels: ["blitz_test", "bugfix"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-1702"
---

# SNB-1702: ERROR NO PUEDO LIQUIDAR PEDIDOS

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Pedidos Jira |
| Creado | 2024-04-03 10:49 |
| Actualizado | 2024-04-03 13:31 |
| Etiquetas | blitz_test, bugfix |
| Jira | [SNB-1702](https://bluinc.atlassian.net/browse/SNB-1702) |

## Relaciones

*Sin relaciones*

## Descripcion

clientes que pagan por banco y retiran en el local. probe con clientes diferentes y pasa lo mismo:
al hacer boton derecho, calcular y liquidar, salta el error:
Ha ocurrido un error
include(/var/www/app/vendor/composer/../../app/Http/Controllers/Liquidate/LiquidateController.php): Failed to open stream: No such file or directory

al apretar realizar para la liquidacion, salta este otro error y no permite liquidarlos:
Ha ocurrido un error
include(/var/www/app/vendor/composer/../../app/Http/Controllers/Liquidate/LiquidateController.php): Failed to open stream: No such file or directory
Usuario: pat
