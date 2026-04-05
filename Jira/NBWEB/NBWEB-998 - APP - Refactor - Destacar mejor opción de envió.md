---
jira_key: "NBWEB-998"
aliases: ["NBWEB-998"]
summary: "APP - Refactor - Destacar mejor opción de envió"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-08-27 11:31"
updated: "2025-08-28 10:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-998"
---

# NBWEB-998: APP - Refactor - Destacar mejor opción de envió

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-27 11:31 |
| Actualizado | 2025-08-28 10:39 |
| Etiquetas | ninguna |
| Jira | [NBWEB-998](https://bluinc.atlassian.net/browse/NBWEB-998) |

## Relaciones

- **Padre:** [[NBWEB-423]] Logistica Envios
- **action item from:** [[NBWEB-997]] API - Feat - Agregar parametro para destacar "mejor opción"

## Descripcion

Agregaremos un destacado al envió sugerido que diga algo así como “**Estadisticamente, el mas rapido a tu zona!**” o “**El más rápido según nuestros datos 🚀**

o alguna sugerencia similar que quede bien!

[adjunto]



```
GET {API_URL}/v1/carrito/calcularEnvioPara/1804/19339
```

```
{
    "cotizacion": [
        {
            "id": 4069,
            "description": "A domicilio por Entregar",
            "plazoEntrega": "entre ma\u00f1ana y el mi\u00e9rcoles 03",
            "plazoEntregaNumero": 1,
            "total": 0,
            "dropshipping": true,
            "suggested": true <---- ESTA ES LA SUGERENCIA
        },
        {
            "id": 4041,
            "description": "A domicilio por OCA",
            "plazoEntrega": "entre ma\u00f1ana y el mi\u00e9rcoles 03",
            "plazoEntregaNumero": 1,
            "total": 2508.52,
            "dropshipping": true,
            "suggested": false
        },
        {
            "id": 4065,
            "description": "A domicilio por Andreani",
            "plazoEntrega": "entre hoy y el martes 02",
            "plazoEntregaNumero": 0,
            "total": 3251.3,
            "dropshipping": true,
            "suggested": false
        },
        {
            "id": 3030,
            "description": "Moto (Capital Federal)",
            "plazoEntrega": "entre el viernes 29 y el lunes 01",
            "plazoEntregaNumero": 2,
            "total": 10182.2,
            "dropshipping": false,
            "suggested": false
        }
    ],
    "datosBulto": {
        "weightKg": 2.5,
        "sizeCm": "20.2x20.2x20.2",
        "amount": 1
    }
}
```
