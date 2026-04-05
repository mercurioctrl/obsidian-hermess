---
jira_key: "LIO-496"
aliases: ["LIO-496"]
summary: "API - Refactor - Obtener productos para un usuario determinado dentro de su cuenta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-30 07:47"
updated: "2026-02-10 08:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-496"
---

# LIO-496: API - Refactor - Obtener productos para un usuario determinado dentro de su cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-30 07:47 |
| Actualizado | 2026-02-10 08:52 |
| Etiquetas | ninguna |
| Jira | [LIO-496](https://bluinc.atlassian.net/browse/LIO-496) |

## Relaciones

- **Padre:** [[LIO-98]] Inventario resellers
- **has action item:** [[LIO-535]] APP - Refactor - Se debe migrar a V4 el recurso para navegar el inventario

## Descripcion

Crearemos el recurso base para poder navegar el inventario de cada reseller desde la siguiente pantalla.

[adjunto]
Este recurso es el punta pie inicial del nuevo alcance del catalogo que permitirá tanto tener productos propios, usados, como importados de otros distribuidores (hoy charlaremos esto).

**Importante: **Este recurso esta basado exclusivamente desde la perspectiva de `CS.dbo.productos` y no desde su postprocesado para el catalogo `SEARCH_ENGINE_LO.dbo.items`

El recurso solo muestra los productos con `activo=1` que tiene el vendedor logueado

```
GET {{API_URL}}/v4/inventories/products?search=&offset=2&brandId=3337&categoryId=226&order=description&orderDirection=desc
```

```
{
    "metadata": {
        "total": 1323,
        "offset": 2,
        "limit": 30,
        "order": "asc"
    },
    "items": [
        {
            "id": 742715,
            "internalId": 120162,
            "description": "DASHCAM TRANSCEND DRIVEPRO 250 GPS QHD 2K 60FPS +SD64GB",
            "image": "e5b0bee9cc696a64a2a5b7503ca3c313.png",
            "brandId": 3337,
            "brandName": "TRANSCEND",
            "categoryId": 226,
            "categoryName": "Iluminaci\u00f3n",
            "freeShipping": true,
            "instantFlash": false,
            "ratingStar": null,
            "resellerCost": 94.41,
            "utility": 2.00000000,
            "iva": 21.00,
            "internalTax": 0,
            "discount": 0.00,
            "priceUsd": 116.520822,
            "price": 171868,
            "gtin": null,
            "sku": "TS-DP250B-64G",
            "hide":0,
            "stock_cliente":0
        },
        {
            "id": 518547,
            "internalId": 108947,
            "description": "TECLADO GAMER DUCKY MECHA MINI V2 RGB KAILH BOX RED SWITCH ISO ES",
            "image": "a1b4b622fc087e260d6afa9147796c72.jpeg",
            "brandImage": "75d04b2fa7c96419c72f7d11993e6bf7.png",
            "brandId": 5687,
            "brandName": "DUCKY",
            "categoryId": 3,
            "categoryName": "Teclados",
            "freeShipping": true,
            "bestSeller": null,
            "instantFlash": false,
            "ratingStar": null,
            "resellerCost": 138.89,
            "utility": 2.00000000,
            "iva": 10.50,
            "internalTax": 0,
            "discount": 0.00,
            "priceUsd": 156.54,
            "price": 230900,
            "sellerId": 447,
            "sellerName": "Gears Store",
            "gtin": null,
            "sku": "DKME2061ST-KESALAATR",
            "hide":0,
            "stock_cliente":0
        },
       ..
    ]
}
```

## Los atributos `order` y `orderDirection` dentro del queryString

Estos atributos sirven para ordenar el listado por cualquiera de los atributos que lo permitan, osea puede ser `brandName`, `description`, `id`, `utility`, etc. Cualquiera que lo permita, para esto crearemos un metodo inteligente que tome `order` para saber cual es el parametro por el cual vamos a ordenar, y `orderDirection` para indicar si es ascendente o descendente. Por defecto es Ascendente.


## Criterios de Aceptación – API v4 Inventories Products

- **Respuesta exitosa**

- **200 OK**

- Request válida.


- Respuesta respeta el contrato `metadata + items[]`.


- Fuente: **CS.dbo.productos**.


- `items` puede ser vacío.






- **Paginación y filtros**

- `offset`, `limit`, `search`, `brandId`, `categoryId` se aplican correctamente.


- Filtros opcionales no afectan el resultado si no están presentes.




- **Ordenamiento**

- `order` define el campo.


- `orderDirection` (`asc` | `desc`), default **asc**.


- Existe un orden por defecto estable si no se envía `order` que es por nombre.




- **Errores de request**

- **400 Bad Request**

- `order` no permitido.


- `orderDirection` inválido.


- Parámetros mal formados (tipos incorrectos, valores inválidos).






- **Sin resultados**

- **200 OK**

- `items: []`


- `metadata.total = 0`


- No se devuelve 404 por búsquedas vacías.






- **Errores internos**

- **500 Internal Server Error**

- Fallos de base de datos o errores no controlados.


- El mensaje no expone detalles sensibles.






- **Seguridad y performance**

- Regla de los 2 segundos


- Orden y filtros solo sobre campos habilitados.
