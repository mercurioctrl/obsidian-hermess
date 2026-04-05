---
jira_key: "PED-59"
summary: "API - Feat - Cotizar envío a una orden de compra "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-11 09:27"
updated: "2023-09-14 20:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-59"
---

# PED-59: API - Feat - Cotizar envío a una orden de compra 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-11 09:27 |
| Actualizado | 2023-09-14 20:51 |
| Etiquetas | ninguna |
| Jira | [PED-59](https://bluinc.atlassian.net/browse/PED-59) |

## Descripción

Crearemos el recurso

```
GET {{API_URL}}/order/addShipping/{branch}-{order}/cp/{cp destino}
```

Basado en la misma la misma idea que lo hacemos en [link](https://lioteam.atlassian.net/browse/NBWEB-256) 

Lo que se busca es obtener la cotización para los medios de envío de modo tal que el vendedor pueda escoger una de ellas y posteriormente confirmarlo agregándolo a la orden. 

```
[
    {
        "cost": 2342,
        "description": "Transporte Camioneta",
        "id": 4040,
        "price": "2342",
        "deliveryDeadline": "",
        "deliveryDeadlineNumber": 0,
        "total": 2342
    },
    {
        "cost": 541.55,
        "description": "Envio OCA a domicilio",
        "id": 4041,
        "price": "541.5500",
        "deliveryDeadline": "el viernes 17",
        "deliveryDeadlineNumber": 3,
        "total": 541.55
    },
    {
        "cost": 1545.81,
        "description": "Andreani a domicilio",
        "id": 4065,
        "price": 1545.81,
        "deliveryDeadline": "hoy",
        "deliveryDeadlineNumber": 0,
        "total": 1545.81
    },
    {
        "cost": 300,
        "description": "Moto (Capital Federal).",
        "price": 300,
        "deliveryDeadline": "hoy",
        "deliveryDeadlineNumber": 0,
        "total": 300
    }
]
```

Esto solo se puede hacer cuando el pedido se encuentra “pendiente”  osea `pedclit.cestado = "P"`
