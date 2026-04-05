---
jira_key: "LIO-182"
aliases: ["LIO-182"]
summary: "API - Feat - Agregar interés de cuotas diferenciado para un mismo medio de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-27 15:39"
updated: "2025-01-31 17:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-182"
---

# LIO-182: API - Feat - Agregar interés de cuotas diferenciado para un mismo medio de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-27 15:39 |
| Actualizado | 2025-01-31 17:45 |
| Etiquetas | ninguna |
| Jira | [LIO-182](https://bluinc.atlassian.net/browse/LIO-182) |

## Relaciones

- **Padre:** [[LIO-8 - Proceso pago sencillo y competitiva a nivel financiamiento|LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento
- **has action item:** [[LIO-197 - APP - Feat - Agregar en el checkOut interes segun cuotas diferenciadas|LIO-197]] APP - Feat - Agregar en el checkOut interes segun cuotas diferenciadas

## Descripcion

Lo que necesitamos para poder tener la flexibilidad total y poder integarar plataformas que funcionan de diferentes maneras (en este caso mercadopago) es que no solo tengamos un interes “base” del medio de pago, sino ademas uno extra para cada cantidad de cuotas

Para esto refactorizaremos la tabla `[LO].[dbo].[mediosPago]` para agregar los intereses de pago para los siguientes casos

`[LO].[dbo].[mediosPago].interes1`

`[LO].[dbo].[mediosPago].interes3`

`[LO].[dbo].[mediosPago].interes6`

`[LO].[dbo].[mediosPago].interes9`

`[LO].[dbo].[mediosPago].interes12`

Estos parámetros pueden tomar valores decimales, pueden ser `cero` (0) o `NULL`

```
GET {{API_LEGACY}}/pedidos/checkout/{pedido}
```

```
{
...
  "mediosPago": [
        ...
            "descripcion": "Mercado Pago",
            "interes": 7.5,
            "soloSucursal": false,
            "cuotas": 1,
            "total": 0
        },
        {
            "id": 5062,
            "key": 5062,
            "activo": true,
            "nombre": "Tarjeta débito 1 pago",
            "descripcion": "Tarjeta de crédito o débito",
            "interes": 0,
            "interes1": 0, <-- Se agrega
            "interes3": 20,  <-- Se agrega
            "interes6": 30,  <-- Se agrega
            "interes9": 40,  <-- Se agrega
            "interes12": 50,  <-- Se agrega                                                            
            "soloSucursal": false,
            "cuotas": 1,
            "total": 0
        },
        ...
    ],
...    
}
```
