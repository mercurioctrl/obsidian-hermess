---
jira_key: "COB-512"
aliases: ["COB-512"]
summary: "API - Feat - Leer salidas pendientes"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-07-05 09:41"
updated: "2024-07-08 18:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-512"
---

# COB-512: API - Feat - Leer salidas pendientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-05 09:41 |
| Actualizado | 2024-07-08 18:27 |
| Etiquetas | ninguna |
| Jira | [COB-512](https://bluinc.atlassian.net/browse/COB-512) |

## Relaciones

- **Padre:** [[COB-19 - Cola de salidas|COB-19]] Cola de salidas
- **blocks:** [[COB-513 - APP - Feat - Pestaña Salidas pendientes|COB-513]] APP - Feat - Pestaña Salidas pendientes
- **relates to:** [[COB-521 - API - Leer salidas pendientes - Sugerencia de mejora en la búsqueda de la|COB-521]] API - Leer salidas pendientes - Sugerencia de mejora en la búsqueda de la referencia

## Descripcion

Crearemos un recurso para leer la cola de salidas pendientes en el cual tendremos algunos filtros como ser

- pending: true/false → para filtrar las salidas que aun estan pendientes y las que ya se procesaron. Si el parametro no viene filtrar todas.


- description: Para buscar en las descripciones por string


- agentId: Para filtrar por quien lo creo



```
GET {API_URL}/v1/pendingCashOut?pending=true&description={striing}&agentId={agentId}
```

```
pagination: {
    "total": 19,
    "current": 1,
    "pageSize": 5
},
data:[
  {
    "date": "01-02-24 12:45"
    "agentName": "Soledad Passerini",
    "agentId": "66",
    "amount": 20,
    "paymentMethodId": 2,
    "outputConceptId": 37,
    "reference": "Esto es una observacion",
    "currencyQuote": 927,
    "type": bankTransfers
  },
{
    "date": "01-02-24 12:45"
    "agentName": "Soledad Passerini",
    "agentId": "66",
    "amount": 50,
    "paymentMethodId": 2,
    "outputConceptId": 37,
    "reference": "Esto es una observacion",
    "currencyQuote": 927,
    "type": cashOut
  }
 ...   
]
```
