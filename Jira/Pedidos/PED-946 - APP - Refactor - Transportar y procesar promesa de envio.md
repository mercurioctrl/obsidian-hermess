---
jira_key: "PED-946"
aliases: ["PED-946"]
summary: "APP - Refactor - Transportar y procesar \"promesa de envio\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-02-11 08:45"
updated: "2025-02-18 23:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-946"
---

# PED-946: APP - Refactor - Transportar y procesar "promesa de envio"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-11 08:45 |
| Actualizado | 2025-02-18 23:41 |
| Etiquetas | ninguna |
| Jira | [PED-946](https://bluinc.atlassian.net/browse/PED-946) |

## Relaciones

- **Padre:** [[PED-58]] Agregar / Editar Envío en las ordenes de compra
- **has action item:** [[PED-947]] API - Refactor - Transportar y procesar "promesa de envio"

## Descripcion

Con fines estadísticos es necesario poder guardar la promesa de envío que se le hace al usuario en el sitio.

Para eso es necesario llevarla desde el chekcout hasta el momento de poder procesarlo, tal como hacemos con las dimensiones del paquete 

Usaremos el parámetro que proviene de 

```
GET /v1/orders/nb/{branch}-{order}/cp/{cp}
```

```
{
    "quote": [
        {
            "id": 4069,
            "costo": 2524,
            "descripcion": "A domicilio por Entregar",
            "precio": 3054,
            "plazoEntrega": "entre ma\u00f1ana y el jueves 13",
            "plazoEntregaNumero": 1,
            "total": 3054
        },
        {
            "id": 4041,
            "costo": 6801.86,
            "descripcion": "A domicilio por OCA",
            "precio": 6801.86,
            "plazoEntrega": "entre el jueves 13 y el martes 18",
            "plazoEntregaNumero": 2,
            "total": 6801.86
        },
        {
```

Y finalmente lo enviaremos en el recurso

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
