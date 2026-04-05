---
jira_key: "LIO-139"
aliases: ["LIO-139"]
summary: "API - Refactor - Cambiar el objeto en el recurso de cotización nativo (evaluar migración a v4) para tener informacion del paquete disponible al front "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-11-25 12:10"
updated: "2024-11-29 04:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-139"
---

# LIO-139: API - Refactor - Cambiar el objeto en el recurso de cotización nativo (evaluar migración a v4) para tener informacion del paquete disponible al front 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-25 12:10 |
| Actualizado | 2024-11-29 04:44 |
| Etiquetas | ninguna |
| Jira | [LIO-139](https://bluinc.atlassian.net/browse/LIO-139) |

## Relaciones

- **Padre:** [[LIO-133 - Ms Envios Libre Opcion|LIO-133]] Ms Envios Libre Opcion
- **has action item:** [[LIO-138 - APP - Refactor - Se deben transportar los objetos con informacion del paquete|LIO-138]] APP - Refactor - Se deben transportar los objetos con informacion del paquete (pesos, medidas y bultos) dentro del checkout para poder enviarlo en el payload al procesar la compra

## Descripcion

Modificaremos

```
GET {API_LEGACY}/envios/checkout/cotizacion

  {
  cotization: [
    {
        "id": 4041,
        "costo": 6298.02,
        "descripcion": "A domicilio por OCA",
        "precio": 0,
        "plazoEntrega": "entre el miércoles 27 y el lunes 02",
        "plazoEntregaNumero": 2,
        "total": 6298.02
    },
    {
        "id": 4065,
        "costo": 7112.3,
        "descripcion": "A domicilio por Andreani",
        "precio": 7112.3,
        "plazoEntrega": "entre mañana y el viernes 29",
        "plazoEntregaNumero": 1,
        "total": 7112.3
    },
    {
        "id": 3030,
        "costo": 7000,
        "descripcion": "Moto (Capital Federal)",
        "precio": 7000,
        "plazoEntrega": "hoy",
        "plazoEntregaNumero": 0,
        "total": 7000
    },
    {
        "id": 4069,
        "costo": 2524,
        "descripcion": "A domicilio por Entregar",
        "precio": 3054,
        "plazoEntrega": "entre mañana y el miércoles 27",
        "plazoEntregaNumero": 1,
        "total": 3054
    }
],
    "bulk": {
        "weightKg": 0.5,
        "sizeCm": "16.82x16.82x16.82",
        "amount": 1
    }
}
```
