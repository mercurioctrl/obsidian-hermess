---
jira_key: "PED-94"
aliases: ["PED-94"]
summary: "API - Refactor - Agregar/quitar item a una orden -> Parametro opcional de precio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-27 10:13"
updated: "2023-10-02 15:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-94"
---

# PED-94: API - Refactor - Agregar/quitar item a una orden -> Parametro opcional de precio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-27 10:13 |
| Actualizado | 2023-10-02 15:21 |
| Etiquetas | ninguna |
| Jira | [PED-94](https://bluinc.atlassian.net/browse/PED-94) |

## Relaciones

- **Padre:** [[PED-34]] Generar / Editar ordenes
- **blocks:** [[PED-110]] APP - Feat - Editar precio de un pedido y cantidad (Solo muestro esto cuando el pedido esta pendiente)

## Descripcion

Haremos un refactor del recurso para poder, en algunos casos editar el precio del item que estamos seleccionado.

El parámetro `selectedPrice`, no es obligatorio, puede no venir. En el caso de que así sea, entonces e marca el precio default para ese cliente como venimos haciendo.

En caso de que **venga una letra**, verificamos cual es el precio que corresponde a esa letra y marcamos en en pedclil el precio correcto.

En caso de que venga un numero (precio a mano) verificamos un permiso que pondremos en `[NB_WEB].[dbo].[permisos_agente].ordenModificarPrecio` y si es 1, entonces utilizamos el numero que nos vimos para marcar pedclil para ese item, como sin iva.

```
PATCH {API_URL}/v1/order/addItem
```

Ejemplo 1

```
[
    {
        "order": "0002",
        "branch": "10328550",
        "amount": "9.000",
        "itemId": 12434,
        "selectedPrice": "B" <-- este parametro es opcional, puede ser una letra o un valor
    }
]
```

Ejemplo 2

```
[
    {
        "order": "0002",
        "branch": "10328550",
        "amount": "9.000",
        "itemId": 12434,
        "selectedPrice": 120.34 <-- este parametro es opcional, puede ser una letra o un valor
    }
]
```
