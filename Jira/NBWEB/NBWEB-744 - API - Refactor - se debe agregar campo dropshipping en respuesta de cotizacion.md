---
jira_key: "NBWEB-744"
aliases: ["NBWEB-744"]
summary: "API - Refactor - se debe agregar campo dropshipping en respuesta de cotizacion de carrito"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-05-29 11:22"
updated: "2024-05-31 17:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-744"
---

# NBWEB-744: API - Refactor - se debe agregar campo dropshipping en respuesta de cotizacion de carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-05-29 11:22 |
| Actualizado | 2024-05-31 17:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-744](https://bluinc.atlassian.net/browse/NBWEB-744) |

## Relaciones

- **blocks:** [[NBWEB-740]] APP - Mejora - No permitir seleccionar dropshipping en medio de pago que no esten habilitado

## Descripcion

Se debe agregar el campo dropshipping true/false dependiendo si el transportista esta habilitado para tal fin.

EJ:

```
{
    "cotizacion": [
        {
            "id": 4041,
            "description": "OCA a domicilio",
            "plazoEntrega": "entre el jueves 06 y el lunes 10",
            "plazoEntregaNumero": 6,
            "total": 3646.42,
            "dropshipping": true
        },
        {
            "id": 4065,
            "description": "Andreani a domicilio",
            "plazoEntrega": "entre el martes 04 y el jueves 06",
            "plazoEntregaNumero": 4,
            "total": 7144.03,
            "dropshipping": true
        },
        {
            "id": 3031,
            "description": "Camioneta",
            "plazoEntrega": "el miércoles 05",
            "plazoEntregaNumero": 5,
            "total": 12357,
            "dropshipping": false
        },
        {
            "id": 3030,
            "description": "Moto (Capital Federal)",
            "plazoEntrega": "el miércoles 05",
            "plazoEntregaNumero": 5,
            "total": 3853,
            "dropshipping": false
        },
        {
            "id": 4069,
            "description": "Entregar a domicilio",
            "plazoEntrega": "el jueves 06",
            "plazoEntregaNumero": 6,
            "total": 3330,
            "dropshipping": true
        }
    ],
    "datosBulto": {
        "weightKg": 0.5,
        "sizeCm": "21.2x21.2x21.2",
        "amount": 1
    }
}
```
