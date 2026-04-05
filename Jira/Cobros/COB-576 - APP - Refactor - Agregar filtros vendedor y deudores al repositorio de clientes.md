---
jira_key: "COB-576"
aliases: ["COB-576"]
summary: "APP - Refactor - Agregar filtros \"vendedor\" y \"deudores\" al repositorio de clientes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-08-20 08:12"
updated: "2025-08-22 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-576"
---

# COB-576: APP - Refactor - Agregar filtros "vendedor" y "deudores" al repositorio de clientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-20 08:12 |
| Actualizado | 2025-08-22 10:48 |
| Etiquetas | ninguna |
| Jira | [COB-576](https://bluinc.atlassian.net/browse/COB-576) |

## Relaciones

- **Padre:** [[COB-573]] Clientes
- **action item from:** [[COB-574]] API - Refactor - Agregar filtros "vendedor" y "deudores" al repositorio de clientes
- **action item from:** [[COB-575]] API - Feat - Repositorio vendedores

## Descripcion

Usando el repositorio [link](https://bluinc.atlassian.net/browse/COB-575)  agregaremos los filtros nuevos  `sellerId` y `balanceState` según la historia [link](https://bluinc.atlassian.net/browse/COB-574) 

[adjunto]
La idea es agregar el filtro vendedor por un lado, como ya hemos realizado en otros casos como el sistema de pedidos.

Y otro filtro que es `balanceState` o Estado de cuenta y cuyos valores son 

- *debt* = Deudores


- *credit* = Con saldo a favor


- *none* = Saldo neutro


- *null* = Todos
