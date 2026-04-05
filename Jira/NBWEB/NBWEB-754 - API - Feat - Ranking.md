---
jira_key: "NBWEB-754"
aliases: ["NBWEB-754"]
summary: "API - Feat - Ranking "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-24 14:27"
updated: "2024-06-26 18:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-754"
---

# NBWEB-754: API - Feat - Ranking 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-24 14:27 |
| Actualizado | 2024-06-26 18:55 |
| Etiquetas | ninguna |
| Jira | [NBWEB-754](https://bluinc.atlassian.net/browse/NBWEB-754) |

## Relaciones

- **Padre:** [[NBWEB-610 - API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro|NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta
- **blocks:** [[NBWEB-755 - APP - Feat - Ranking|NBWEB-755]] APP - Feat - Ranking 
- **blocks:** [[MKT-183 - NB_ Incentivo Resellers 25 años|MKT-183]] NB_ Incentivo Resellers 25 años

## Descripcion

Para la acción [link](https://lioteam.atlassian.net/browse/MKT-183?focusedCommentId=18108&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-18108)  crearemos un repositorio dentro de mi cuenta para poder mostrar la tabla a la “tabla de posiciones” del grupo al que pertenece el cliente.

La idea es que el cliente logueado pueda conocer su posición y la de los 2 competidores que están inmediatamente arriba e inmediatamente abajo.

Es importante advertir que hay 3 grupos distintos de categoría de clientes **Grupo A (4 GANADORES)**, **Grupo B (4 GANADORES)**, **Grupo C (2 GANADORES)** ver documento [link](https://docs.google.com/spreadsheets/d/1UH6KLY0hBH_WxXXgIs0-lgeYLP2bSM4DagdHzcPuoFg/edit?gid=0#gid=0) . El grupo C es para todos los clientes que no forman parte del grupo A o el grupo B (por un tema de practicidad solo mostraremos y contaremos los primeros 50)

Para esto crearemos un recurso del siguiente tipo

```
GET {{API_URL}}/v1/miCuenta/ranking
```

```
[
  count: 59 <-- Indica la cantidad de clientes del ranking
  ranking: [
      {
        description: "DAMARFU SA", <-- razon social
        amount: 31324, <-- puntaje redondeado
        position: 6,
        clientId: 4343,
        self: false
      },
{
        description: "COMPUFAN SRL", <-- razon social
        amount: 30332, <-- puntaje redondeado
        position: 7,
        clientId: 23434,
        self: false
      },
{
        description: "GRUPOS INTEGRADOS S.A.", <-- razon social
        amount: 26356, <-- puntaje redondeado
        position: 8,
        clientId: 3243,
        self: true <-- Esto indica la cuenta desde donde se esta accediendo al ranking
      },      
{
        description: "GHERTNER MATIAS / SEBASTIAN", <-- razon social
        amount: 22156, <-- puntaje redondeado
        position: 9,
        clientId: 4343,
        self: false
      },
{
        description: "GRUPO MEXX S.R.L", <-- razon social
        amount: 21135, <-- puntaje redondeado
        position: 10,
        clientId: 4343,
        self: false
      },                  
  ]
]
```

## ¿como se calculan los puntos?

Para poder calcular los puntos, simplemente multiplicaremos el monto en dolares por el indice de aceleración guardado en `[NewBytes_DBF].[dbo].[pedclil].acelerator`

Diremos entonces que el puntaje para cada cliente esta definido por la suma de todos los pedidos del cliente en el intervalo de fechas de la acción (`1/07/24 a las 00hs hasta el 15/11/24 a las 18 hs`) 

```
SUM ([NewBytes_DBF].[dbo].[pedclil].acelerator * [NewBytes_DBF].[dbo].[pedclil].npreunit * [NewBytes_DBF].[dbo].[pedclil].ncanped)
```

Partimos de la idea que solo contabilizamos aquellos que tienen un valor en `[NewBytes_DBF].[dbo].[pedclil].acelerator` y están liquidados.
