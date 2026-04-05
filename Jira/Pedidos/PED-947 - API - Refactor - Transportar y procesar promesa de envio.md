---
jira_key: "PED-947"
aliases: ["PED-947"]
summary: "API - Refactor - Transportar y procesar \"promesa de envio\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-11 08:45"
updated: "2025-02-18 23:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-947"
---

# PED-947: API - Refactor - Transportar y procesar "promesa de envio"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-11 08:45 |
| Actualizado | 2025-02-18 23:41 |
| Etiquetas | ninguna |
| Jira | [PED-947](https://bluinc.atlassian.net/browse/PED-947) |

## Relaciones

- **Padre:** [[PED-58]] Agregar / Editar Envío en las ordenes de compra
- **action item from:** [[PED-946]] APP - Refactor - Transportar y procesar "promesa de envio"

## Descripcion

Para poder guardar con fines estadísticos (todo lo relacionado a la historia [link](https://lioteam.atlassian.net/browse/STASK-8) )

Tomaremos el parámetro al momento que procesamos la orden el sitio de libre opción mediante el recurso

```
POST {API_URL}/v1/orders/{branch}-{order}/addShipping
```

**Carga util:**

```
{
    "shippingMethodId": 4069,
    "shippingName": "A domicilio por Entregar",
    "shippingPrice": 3054,
    "shippingCost": 2524,
    "customerAddressId": 18063,
    "weightKg": 1,
    "sizeCm": "13.58x13.58x13.58",
    "amount": 1,
    "quotes":
        {
          "deliveryTimeRange": "entre el lunes 10 y el viernes 14",
          "deliveryDays": 4,
        }
}
```

Según el refactor de Front en [link](https://lioteam.atlassian.net/browse/PED-946)
