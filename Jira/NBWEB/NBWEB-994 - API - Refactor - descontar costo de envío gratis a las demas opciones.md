---
jira_key: "NBWEB-994"
aliases: ["NBWEB-994"]
summary: "API - Refactor - descontar costo de envío gratis a las demas opciones"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-08-26 14:07"
updated: "2025-09-02 18:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-994"
---

# NBWEB-994: API - Refactor - descontar costo de envío gratis a las demas opciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-08-26 14:07 |
| Actualizado | 2025-09-02 18:54 |
| Etiquetas | ninguna |
| Jira | [NBWEB-994](https://bluinc.atlassian.net/browse/NBWEB-994) |

## Relaciones

- **Padre:** [[NBWEB-423 - Logistica Envios|NBWEB-423]] Logistica Envios

## Descripcion

Actualmente, al generar una cotización se ofrece automáticamente la condición de envío gratis. Sin embargo, esta opción no siempre resulta la más conveniente para el cliente según su zona de entrega.

Por este motivo, se implementará un ajuste en el cálculo:

- El costo del envío gratis se tomará como base absorbida por la empresa.


- A los demás transportistas se les descontará ese mismo valor, de manera que el cliente solo deba abonar la diferencia si desea elegir un transportista distinto al que tiene bonificación.



De esta forma, se mantiene el beneficio del envío bonificado y, al mismo tiempo, se le brinda al cliente la posibilidad de seleccionar un transportista alternativo sin perder el descuento equivalente.



Habilitar bonus de envio → variable de entorno true/false

```
SHIPPING_BONUS_ENABLED=false
```



Ejemplo de response segun endpoints de ms-envios.

```
GET /order/nb/0002-10426466/cp/7400
```



```json
{
    "quote": [
        {
            "id": 4069,
            "costo": 3069,
            "descripcion": "A domicilio por Entregar",
            "precio": 0,
            "plazoEntrega": "entre el jueves 28 y el miércoles 03",
            "plazoEntregaNumero": 2,
            "total": 0
        },
        {
            "id": 4041,
            "costo": 8137.52,
            "descripcion": "A domicilio por OCA",
            "precio": 5068.52, --> aplica la resta del costo del transportista gratis
            "plazoEntrega": "entre el jueves 28 y el miércoles 03",
            "plazoEntregaNumero": 2,
            "total": 5068.52 --> aplica la resta del costo del transportista gratis
        },
        {
            "id": 4065,
            "costo": 8629.39,
            "descripcion": "A domicilio por Andreani",
            "precio": 5560.38, --> aplica la resta del costo del transportista gratis
            "plazoEntrega": "entre mañana y el martes 02",
            "plazoEntregaNumero": 1,
            "total": 5560.38 --> aplica la resta del costo del transportista gratis
        },
        {
            "id": 3030,
            "costo": 9000,
            "descripcion": "Moto (Capital Federal)",
            "precio": 5931, --> aplica la resta del costo del transportista gratis
            "plazoEntrega": "entre mañana y el jueves 28",
            "plazoEntregaNumero": 1,
            "total": 5931 --> aplica la resta del costo del transportista gratis
        },
        {
            "id": 3031,
            "costo": 25000,
            "descripcion": "Camioneta",
            "precio": 21931, --> aplica la resta del costo del transportista gratis
            "plazoEntrega": "mañana",
            "plazoEntregaNumero": 1,
            "total": 21931 --> aplica la resta del costo del transportista gratis
        }
    ],
    "package": {
        "weightKg": 1.65,
        "sizeCm": "17.54x17.54x17.54",
        "amount": 1
    }
}
```
