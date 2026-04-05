---
jira_key: "PED-754"
aliases: ["PED-754"]
summary: "API - Feat - Ranking de aceleradores"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-26 09:52"
updated: "2024-07-08 01:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-754"
---

# PED-754: API - Feat - Ranking de aceleradores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-26 09:52 |
| Actualizado | 2024-07-08 01:49 |
| Etiquetas | ninguna |
| Jira | [PED-754](https://bluinc.atlassian.net/browse/PED-754) |

## Relaciones

- **Padre:** [[PED-753]] Incentivos Clientes
- **relates to:** [[PED-756]] API - Ranking de aceleradores - Sugerencia de mejora en las descripciones

## Descripcion

Crearemos un recurso “interno” en el sistema de pedidos para poder ver el ranking completo por un parámetro que filtra por grupo.

Es igual al que se usa en la web ([link](https://lioteam.atlassian.net/browse/NBWEB-754) ), pero no tiene el sesgo, osea que se muestran todos los clientes del grupo (salvo el grupo c que como son mucho solo mostraremos los primero 50)

```
GET {{API_URL}}/v1/clientsObjectives/acelerateRanking?clientGroup
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
