---
jira_key: "MKT-181"
aliases: ["MKT-181"]
summary: "API - Refactor - Crear recurso necesario para llevar el conteo del objetivo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-04 14:03"
updated: "2024-06-04 16:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/MKT-181"
---

# MKT-181: API - Refactor - Crear recurso necesario para llevar el conteo del objetivo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-04 14:03 |
| Actualizado | 2024-06-04 16:11 |
| Etiquetas | ninguna |
| Jira | [MKT-181](https://bluinc.atlassian.net/browse/MKT-181) |

## Relaciones

- **Padre:** [[MKT-180]] NB_ INCENTIVO CAPILARIDAD
- **blocks:** [[MKT-182]] APP - Refactor - Agregaremos dos widgets de objetivos para capilaridad, uno en general y otro para trust

## Descripcion

Generaremos un recurso que nos entregue informacion de “Cantidad de ventas” que cumplan con los siguiente criterios.

- Mínimo de compra: USD600 +iva (basado en pedclil o albclil)


- Periodo sin compra: 3 meses o NUEVO.


- Que el pedido este liquidado y en estado > 1



```
GET {API_URL} /v1/objectives/capillarityIncentive?itemFilter=trust (o similar)&agentId={}
```

```
[
  {
    "count":5, <-- cantidad de ventas que cumplen los criterios,
    "valueAmount": 5,
    "startDate": "01/06/2024"
    "endDate":"29/06/2024"
  }
]
```

El recurso funciona con y sin filtro por producto.

El filtro de item sirve solo para tener en cuenta items que tengan ese string
