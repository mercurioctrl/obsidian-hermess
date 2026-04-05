---
jira_key: "COB-511"
aliases: ["COB-511"]
summary: "API - Feat - Crear Salida pendiente"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-07-05 09:40"
updated: "2024-07-08 17:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-511"
---

# COB-511: API - Feat - Crear Salida pendiente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-05 09:40 |
| Actualizado | 2024-07-08 17:51 |
| Etiquetas | ninguna |
| Jira | [COB-511](https://bluinc.atlassian.net/browse/COB-511) |

## Relaciones

- **Padre:** [[COB-19]] Cola de salidas
- **blocks:** [[COB-514]] APP - Feat - Crear salida pendiente
- **is blocked by:** [[COB-520]] API - Crear Salida pendiente - Error de tipo de dato

## Descripcion

Crearemos un recurso que nos permite crear un a petición de salida  en la cola par que después sea tomada por otra persona con el permiso suficiente para realizar la salida bancaria o de caja

```
POST {API_URL}/v1/pendingCashOut
```

```
[
  {
    "amount": 50,
    "paymentMethodId": 2,
    "outputConceptId": 37,
    "reference": "Esto es una observacion",
    "currencyQuote": 927,
    "type": cashOut/bankTransfers
  }
]

```



Para esto crearemos una nueva tabla ya que este concepto hasta que no existió.
