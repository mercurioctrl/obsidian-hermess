---
jira_key: "NBWEB-995"
aliases: ["NBWEB-995"]
summary: "API - Refactor - agregar sugerencia de transportista por zona, según codigo postal cotizado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-08-26 14:08"
updated: "2025-08-29 10:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-995"
---

# NBWEB-995: API - Refactor - agregar sugerencia de transportista por zona, según codigo postal cotizado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-08-26 14:08 |
| Actualizado | 2025-08-29 10:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-995](https://bluinc.atlassian.net/browse/NBWEB-995) |

## Relaciones

- **Padre:** [[NBWEB-423 - Logistica Envios|NBWEB-423]] Logistica Envios
- **has action item:** [[NBWEB-997 - API - Feat - Agregar parametro para destacar mejor opción|NBWEB-997]] API - Feat - Agregar parametro para destacar "mejor opción"

## Descripcion

Debido a que los transportistas externos presentan distintos tiempos de entrega según la zona, es necesario ajustar los endpoints de ms-envíos para brindar recomendaciones más precisas al cliente.

El objetivo es que, en la respuesta de cada cotización, se indique cuál transportista resulta más conveniente de acuerdo con nuestros tiempos logísticos y la eficiencia en la entrega (considerando cantidad de bultos y menor demora).

Para ello, se agregará un nuevo campo en la respuesta:

- suggested: true/false → Identifica si el transportista es el recomendado en esa zona.



De esta forma, el sistema podrá sugerir automáticamente la opción más eficiente y confiable para cada cliente.



Habilitar sugerencia de envio → variable de entorno

```
SHIPPING_SUGGESTION_ENABLED=false
```



```
GET /order/nb/0010-10342574/cp/1417
```



```
{
    "quote": [
        {
            "id": 4069,
            "costo": 3069,
            "descripcion": "A domicilio por Entregar",
            "precio": 0,
            "plazoEntrega": "entre el jueves 28 y el miércoles 03",
            "plazoEntregaNumero": 2,
            "total": 0,
            "suggested": true --> sugerencia
        },
        {
            "id": 4041,
            "costo": 8137.52,
            "descripcion": "A domicilio por OCA",
            "precio": 8137.52,
            "plazoEntrega": "entre el jueves 28 y el miércoles 03",
            "plazoEntregaNumero": 2,
            "total": 8137.52,
            "suggested": false 
        },
        {
            "id": 4065,
            "costo": 8629.39,
            "descripcion": "A domicilio por Andreani",
            "precio": 8629.39,
            "plazoEntrega": "entre mañana y el martes 02",
            "plazoEntregaNumero": 1,
            "total": 8629.39,
            "suggested": false
        },
        {
            "id": 3030,
            "costo": 9000,
            "descripcion": "Moto (Capital Federal)",
            "precio": 9000,
            "plazoEntrega": "entre mañana y el jueves 28",
            "plazoEntregaNumero": 1,
            "total": 9000,
            "suggested": false
        },
        {
            "id": 3031,
            "costo": 25000,
            "descripcion": "Camioneta",
            "precio": 25000,
            "plazoEntrega": "mañana",
            "plazoEntregaNumero": 1,
            "total": 25000,
            "suggested": false
        }
    ],
    "package": {
        "weightKg": 1.65,
        "sizeCm": "17.54x17.54x17.54",
        "amount": 1
    }
}
```



La idea seria mostrar algo similar a la siguiente imange.

Ejemplo, no debe ser exacto solo es para aclara la idea.

[adjunto]
