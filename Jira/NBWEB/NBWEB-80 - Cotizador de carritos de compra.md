---
jira_key: "NBWEB-80"
aliases: ["NBWEB-80"]
summary: "Cotizador de carritos de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-04-04 07:09"
updated: "2022-06-26 20:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-80"
---

# NBWEB-80: Cotizador de carritos de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-04 07:09 |
| Actualizado | 2022-06-26 20:17 |
| Etiquetas | ninguna |
| Jira | [NBWEB-80](https://bluinc.atlassian.net/browse/NBWEB-80) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios
- **is blocked by:** [[NBWEB-1]] API - Carrito de compras
- **relates to:** [[NBWEB-11]] API - Implementar Cotizadores de envio

## Descripcion

Se debe crear un recurso para poder cotizar un carrito completo, según los distintos métodos de envío.

```
GET {{API_URL}}/cart/nb/{cartId}/cp/{codigoPostalDestino}/cphost/{codigoPostalOrigen}
```

(Puede pasarse con y sin cp destino)

```
GET {{API_URL}}/cart/nb/{cartId}/cp/{codigoPostalDestino}
```

El mismo retorna un array de objetos del siguiente tipo:



```json
[
    {
        "costo": 439.01,
        "descripcion": "OCA a domicilio",
        "id": 4041,
        "precio": 0,
        "plazoEntrega": "entre el viernes 08 y el martes 12",
        "plazoEntregaNumero": 4,
        "total": 439.01
    },
    {
        "costo": 993.01,
        "descripcion": "Andreani a domicilio",
        "id": 4065,
        "precio": 993.01,
        "plazoEntrega": "entre mañana y el jueves 07",
        "plazoEntregaNumero": 1,
        "total": 993.01
    },
    {
        "costo": 300,
        "descripcion": "Moto (Capital Federal).",
        "id": 3030,
        "precio": 0,
        "plazoEntrega": "hoy",
        "plazoEntregaNumero": 0,
        "total": 300,
        "horaActual": "2022-04-04 07:07:36"
    }
]
```



SQL, algunos ejemplos:



```sql
SELECT 
familias.largoMaximo,
familias.anchoMaximo,
familias.altoMaximo,
familias.pesoMaximo,
FROM [NB_WEB].[dbo].[carritos]
LEFT JOIN [NB_WEB].[dbo].[contenidoCarritos]
ON carritos.id = contenidoCarritos.id_carrito
LEFT JOIN [NewBytes_DBF].dbo.[articulo] ON contenidoCarritos.codProducto = articulo.codigo
LEFT JOIN [NewBytes_DBF].dbo.familias ON articulo.ID_FAMILIA = familias.ID_FAMILIA
```
