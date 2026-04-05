---
jira_key: "ENV-9"
summary: "API - Refactor - se debe agregar campo dropshipping"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-05-29 11:26"
updated: "2024-05-31 13:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ENV-9"
---

# ENV-9: API - Refactor - se debe agregar campo dropshipping

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-05-29 11:26 |
| Actualizado | 2024-05-31 13:17 |
| Etiquetas | ninguna |
| Jira | [ENV-9](https://bluinc.atlassian.net/browse/ENV-9) |

## Descripción

La respuesta al cotizar por Carrito debe contener el campo `dropshipping: true o false`



```
{
    "tarifa": [
        {
            "id": 4041,
            "costo": 6327.27,
            "descripcion": "OCA a domicilio",
            "precio": 6327.27,
            "plazoEntrega": "entre el lunes 03 y el miércoles 05",
            "plazoEntregaNumero": 5,
            "total": 6327.27,
            "dropshipping": true
        },
        {
            "id": 4065,
            "costo": 7144.03,
            "descripcion": "Andreani a domicilio",
            "precio": 7144.03,
            "plazoEntrega": "entre mañana y el lunes 03",
            "plazoEntregaNumero": 1,
            "total": 7144.03,
            "dropshipping": true
        },
        {
            "id": 3031,
            "costo": 12357,
            "descripcion": "Camioneta",
            "precio": 12357,
            "plazoEntrega": "el viernes 31",
            "plazoEntregaNumero": 2,
            "total": 12357,
            "dropshipping": false
        },
        {
            "id": 3030,
            "costo": 3853,
            "descripcion": "Moto (Capital Federal)",
            "precio": 3853,
            "plazoEntrega": "el viernes 31",
            "plazoEntregaNumero": 2,
            "total": 3853,
            "dropshipping": false
        },
        {
            "id": 4069,
            "costo": 3330,
            "descripcion": "Entregar a domicilio",
            "precio": 4030,
            "plazoEntrega": "el lunes 03",
            "plazoEntregaNumero": 5,
            "total": 3330,
            "dropshipping": true
        }
    ],
    "package": {
        "weightKg": 0.5,
        "sizeCm": "21.2x21.2x21.2",
        "amount": 1
    }
}
```
