---
jira_key: "LIO-338"
aliases: ["LIO-338"]
summary: "API - Feat - Agregar repositorio de medios de pago disponibles en el sitio

"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-07 08:40"
updated: "2025-05-20 00:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-338"
---

# LIO-338: API - Feat - Agregar repositorio de medios de pago disponibles en el sitio



| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-07 08:40 |
| Actualizado | 2025-05-20 00:46 |
| Etiquetas | ninguna |
| Jira | [LIO-338](https://bluinc.atlassian.net/browse/LIO-338) |

## Relaciones

- **Padre:** [[LIO-8 - Proceso pago sencillo y competitiva a nivel financiamiento|LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento
- **has action item:** [[LIO-339 - APP - Refactor - Calcular cuotas para el catalogo en base a los intereses del|LIO-339]] APP - Refactor - Calcular cuotas para el catalogo en base a los intereses del repositorio nuevo de medios de pago

## Descripcion

Agregarmos un repositorio para listar los medios de pago disponibles en el sitio de manera general.

Para esto usaremos la tabla `[LO].[dbo].[mediosPago]`

```
GET {API_V4}/v4/paymentMethods
```

```
[
    {
        "id": "5049",
        "activo": "0",
        "destacado_home": "0",
        "cuotas": "1",
        "interesBruto": ".0000",
        "interes": ".00",
        "nombre": "A convenir con el vendedor",
        "descripcion": "A convenir con el vendedor",
        "interes1": null,
        "interes3": null,
        "interes6": null,
        "interes9": null,
        "interes12": null
    },
    {
        "id": "4004",
        "activo": "1",
        "destacado_home": "1",
        "cuotas": "1",
        "interesBruto": ".0000",
        "interes": ".00",
        "nombre": "Efectivo",
        "descripcion": "Efectivo",
        "interes1": null,
        "interes3": null,
        "interes6": null,
        "interes9": null,
        "interes12": null
    },
    {
        "id": "5060",
        "activo": "1",
        "destacado_home": "1",
        "cuotas": "1",
        "interesBruto": "7.8700",
        "interes": "6.50",
        "nombre": "Tarjeta cr\u00e9dito 1 pago",
        "descripcion": "Tarjeta de cr\u00e9dito en un pago",
        "interes1": null,
        "interes3": null,
        "interes6": null,
        "interes9": null,
        "interes12": null
    },
    {
        "id": "5076",
        "activo": "1",
        "destacado_home": "0",
        "cuotas": "1",
        "interesBruto": ".0000",
        "interes": ".00",
        "nombre": "Tarjeta de Credito \/ Debito",
        "descripcion": "Tarjeta de Credito \/ Debito",
        "interes1": ".00",
        "interes3": "15.00",
        "interes6": "24.00",
        "interes9": null,
        "interes12": null
    },
    {
        "id": "5062",
        "activo": "1",
        "destacado_home": "1",
        "cuotas": "1",
        "interesBruto": ".0000",
        "interes": ".00",
        "nombre": "Tarjeta d\u00e9bito 1 pago",
        "descripcion": "Tarjeta de d\u00e9bito en un pago",
        "interes1": null,
        "interes3": null,
        "interes6": null,
        "interes9": null,
        "interes12": null
    },
    {
        "id": "4005",
        "activo": "1",
        "destacado_home": "1",
        "cuotas": "1",
        "interesBruto": ".0000",
        "interes": ".00",
        "nombre": "Transferencia",
        "descripcion": "Transferencia bancaria",
        "interes1": null,
        "interes3": null,
        "interes6": null,
        "interes9": null,
        "interes12": null
    }
]
```

**🔹 Criterios de Aceptación:**

- Solo se listan medios con `"activo": "1"` y` eliminado =0`
