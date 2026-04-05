---
jira_key: "PED-1062"
aliases: ["PED-1062"]
summary: "API PED refactor separacion entre descuento items descuento lo"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-07-23 17:25"
updated: "2025-08-05 19:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1062"
---

# PED-1062: API PED refactor separacion entre descuento items descuento lo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-07-23 17:25 |
| Actualizado | 2025-08-05 19:12 |
| Etiquetas | ninguna |
| Jira | [PED-1062](https://bluinc.atlassian.net/browse/PED-1062) |

## Relaciones

*Sin relaciones*

## Descripcion

En el endpoint implementado en Pedidos.

```
GET /v1/aboutMarketPlace/0002-10420338
```

Se debe agrergar los siguentes campos.

```json
discountLo,discount
```

los cuales pertenecen a la tabal LO.dbo.pedidosCabeceraDetalle.



Response Ej.: 

```json
{
    "success": true,
    "msg": "Pedido encontrado",
    "data": {
        "document": "38851923",
        "idLo": 741372,
        ...
        "items": [
            {
            ...
                "priceLo": 1014887, 
                "discountLo": 2000, → debe mostrar el valor nominal correspondiente al porcentaje.
                "discount": 101488.7, → debe mostrar el valor nominal correspondiente al porcentaje.
            }
        ]
    }
}


```
