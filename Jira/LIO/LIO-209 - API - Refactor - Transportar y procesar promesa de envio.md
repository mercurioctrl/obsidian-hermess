---
jira_key: "LIO-209"
aliases: ["LIO-209"]
summary: "API - Refactor - Transportar y procesar \"promesa de envio\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-06 14:44"
updated: "2025-02-18 04:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-209"
---

# LIO-209: API - Refactor - Transportar y procesar "promesa de envio"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-06 14:44 |
| Actualizado | 2025-02-18 04:12 |
| Etiquetas | ninguna |
| Jira | [LIO-209](https://bluinc.atlassian.net/browse/LIO-209) |

## Relaciones

- **Padre:** [[LIO-16]] Mejorar tiempos de entrega
- **action item from:** [[LIO-208]] APP - Refactor - Transportar y procesar "promesa de envio"

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
