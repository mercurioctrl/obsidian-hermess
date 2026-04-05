---
jira_key: "COB-442"
aliases: ["COB-442"]
summary: "APP - Refactor - Cuentas bancarias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-06-08 13:20"
updated: "2023-07-06 07:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-442"
---

# COB-442: APP - Refactor - Cuentas bancarias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-08 13:20 |
| Actualizado | 2023-07-06 07:02 |
| Etiquetas | ninguna |
| Jira | [COB-442](https://bluinc.atlassian.net/browse/COB-442) |

## Relaciones

- **Padre:** [[COB-440]] Refactor - Cuentas bancarias

## Descripcion

Utilizaremos el refactor de [link](https://lioteam.atlassian.net/browse/COB-441)  para diseñar dentro de la pestaña

```
https://caja.saftel.com/banks
```

que actualmente funciona con el recurso [link](https://lioteam.atlassian.net/browse/COB-9)

Lo que nos interesa mostrar ahora es lo mismo que muestra el modal para cada banco, pero para todos los bancos. Lo que buscamos es cambiar la perspectiva a una mas útil para el cajero, osea ver sus movimientos de banco.

[adjunto]
Para esto moveremos este esquema a la pestaña usando el recurso [link](https://lioteam.atlassian.net/browse/COB-218)

```
{{API_URL}}/v1/currentBankAccount?&currency=1&agentId=12&bankId=1,2,3
```

Para esto la vista cuando entras a la pestaña ya debe filtrar para el usuario que esta mirando (Seba es el 12 en este caso)

Siempre cuando clickeo las pestañas debo ver la del usuario en pesos para todos los bancos

Adicionalmente agregaremos el filtro para banco y agregaremos columnas para mostrar el id del banco - nombre del banco
