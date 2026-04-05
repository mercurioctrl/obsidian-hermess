---
jira_key: "COB-440"
aliases: ["COB-440"]
summary: "Refactor - Cuentas bancarias"
status: "Tareas por hacer"
type: "Historia"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2023-06-08 13:06"
updated: "2023-06-08 13:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-440"
---

# COB-440: Refactor - Cuentas bancarias

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-08 13:06 |
| Actualizado | 2023-06-08 13:25 |
| Etiquetas | ninguna |
| Jira | [COB-440](https://bluinc.atlassian.net/browse/COB-440) |

## Relaciones

- **Padre:** [[COB-16 - Cuentas bancarias|COB-16]] Cuentas bancarias
- **Subtarea:** [[COB-441 - API - Refactor - Cuentas bancarias|COB-441]] API - Refactor - Cuentas bancarias
- **Subtarea:** [[COB-442 - APP - Refactor - Cuentas bancarias|COB-442]] APP - Refactor - Cuentas bancarias

## Descripcion

Cambiaremos la forma en que se muestra la seccion

```
https://caja.saftel.com/banks
```

que actualmente funciona con el recurso [link](https://lioteam.atlassian.net/browse/COB-9) 

Lo que nos interesa mostrar ahora es lo mismo que muestra el modal para cada banco, pero para todos los bancos. Lo que buscamos es cambiar la perspectiva a una mas útil para el cajero, osea ver sus movimientos de banco.

[adjunto]
Para esto moveremos este esquema a la pestaña usando el recurso [link](https://lioteam.atlassian.net/browse/COB-218) 

```
{{API_URL}}/v1/currentBankAccount?&currency=1&agentId=12
```

Para esto la vista cuando entras a la pestaña ya debe filtrar para el usuario que esta mirando (Seba)
