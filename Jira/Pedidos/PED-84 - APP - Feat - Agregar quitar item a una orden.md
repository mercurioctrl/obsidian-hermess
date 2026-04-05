---
jira_key: "PED-84"
aliases: ["PED-84"]
summary: "APP - Feat - Agregar / quitar item a una orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-09-21 09:34"
updated: "2023-10-02 13:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-84"
---

# PED-84: APP - Feat - Agregar / quitar item a una orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-21 09:34 |
| Actualizado | 2023-10-02 13:33 |
| Etiquetas | ninguna |
| Jira | [PED-84](https://bluinc.atlassian.net/browse/PED-84) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **is blocked by:** [[PED-39 - API - Feat - Agregarquitar item a una orden|PED-39]] API - Feat - Agregar/quitar item a una orden
- **blocks:** [[PED-110 - APP - Feat - Editar precio de un pedido y cantidad (Solo muestro esto cuando el|PED-110]] APP - Feat - Editar precio de un pedido y cantidad (Solo muestro esto cuando el pedido esta pendiente)

## Descripcion

Usaremos el recurso

```
PATCH {API_URL}/v1/order/addItem
```

```
[
    {
        "order": "0002",
        "branch": "10328550",
        "amount": "9.000", <-- esta es la cantidad que quiero que el pedido tenga
        "itemId": 12434,
    }
]
```

Para en conjunto con el componente de productos para sumar y restar unidades.

Si se pudo agregar la cantidad, se debe poner el casillero en verde, en caso contrario debe poerse en rojo. Y mientras se hace la peticion debe ponerse en amarillo.

(Ver beta.pedidos.saftel.com)
