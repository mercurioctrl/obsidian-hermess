---
jira_key: "NBWEB-985"
aliases: ["NBWEB-985"]
summary: "APP- Refactor - Agregar percepciones ARBA a los subtotales del carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-20 22:19"
updated: "2025-07-29 10:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-985"
---

# NBWEB-985: APP- Refactor - Agregar percepciones ARBA a los subtotales del carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-20 22:19 |
| Actualizado | 2025-07-29 10:59 |
| Etiquetas | ninguna |
| Jira | [NBWEB-985](https://bluinc.atlassian.net/browse/NBWEB-985) |

## Relaciones

- **Padre:** [[NBWEB-983 - Percepciones|NBWEB-983]] Percepciones

## Descripcion

Con el objetivo de mostrar las percepciones en el carrito (repasando el ticket que nos habían mandado), solo restaria agregar las de ARBA. Para esto Agregaremmos la suma de ambos monto de las percepciones (hoy solo se considera CABA) en el repositorio

```
GET {API_URL}/v1/carrito/subtotales
```

```
{
    "cartId": "8301768",
    "cartName": "Nuevo carrito",
    "cotizacion": 1300,
    "subTotalDollar": 233.08894999999998,
    "subTotalDollarFinal": 284.368519,
    "subTotalPesosAr": 303015.63499999995,
    "subTotalPesosArFinal": 369679.0747,
    "perceptions": 2.3308895 <--- SUMAREMOS AMBAS EN ESTE PARAMETRO
}
```

[adjunto]
