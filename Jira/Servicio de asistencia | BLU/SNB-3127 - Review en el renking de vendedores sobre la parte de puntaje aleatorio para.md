---
jira_key: "SNB-3127"
aliases: ["SNB-3127"]
summary: "Review en el renking de vendedores sobre la parte de puntaje aleatorio para productos nuevos"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-02 09:38"
updated: "2025-06-02 16:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3127"
---

# SNB-3127: Review en el renking de vendedores sobre la parte de puntaje aleatorio para productos nuevos

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-02 09:38 |
| Actualizado | 2025-06-02 16:07 |
| Etiquetas | ninguna |
| Jira | [SNB-3127](https://bluinc.atlassian.net/browse/SNB-3127) |

## Relaciones

*Sin relaciones*

## Descripcion

Eze, sabes que estuve viendo el cambio que hicimos en los ranking, para que cuando un producto no tiene ventas, aplique un rankeo mas aleatorio.

En principio me daba bastante raro, de hecho productos que si tenían ventas, entraban en el caso.

Yo por las dudas, para acomodar mejor el ranking porque había quedado raro para productos con ventas tuve la presunción de que podía haber un problema con esto

[link](https://github.com/LibreOpcion/sitio-api-rest-v4-laravel/commit/6870b2348240df16a571b4deaf50a20da74852d7) 
Es decir que podía ser que este agrupando por producto en lo, en lugar de por producto interno, lo que hacia que productos que si tenían ventas, para casos particulares no las tuviesen (entraba siempre).

Pero me quede con dudas de que sea asi, te dejo el caso para revisar por las dudas
