---
jira_key: "LIO-208"
aliases: ["LIO-208"]
summary: "APP - Refactor - Transportar y procesar \"promesa de envio\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-06 14:44"
updated: "2025-02-14 10:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-208"
---

# LIO-208: APP - Refactor - Transportar y procesar "promesa de envio"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-06 14:44 |
| Actualizado | 2025-02-14 10:18 |
| Etiquetas | ninguna |
| Jira | [LIO-208](https://bluinc.atlassian.net/browse/LIO-208) |

## Relaciones

- **Padre:** [[LIO-16]] Mejorar tiempos de entrega
- **has action item:** [[LIO-209]] API - Refactor - Transportar y procesar "promesa de envio"

## Descripcion

Para poder guardar con fines estadísticos (todo lo relacionado a la historia [link](https://lioteam.atlassian.net/browse/STASK-8) )

Tomaremos el parámetro al momento que procesamos la orden el sitio de libre opción mediante el recurso

```
POST {API_URL}/pedidos/checkout/confirmar
```

**Carga util:**

```
{
"id":658342,
"quotes":
    {
      "deliveryTimeRange": "entre el lunes 10 y el viernes 14",
      "deliveryDays": 4,
    },
"bulk":{
  "weightKg":7,
  "sizeCm":"33.62x33.62x33.62",
  "amount":1
  }
}
```

Según el refactor de Front en [link](https://lioteam.atlassian.net/browse/LIO-208)
