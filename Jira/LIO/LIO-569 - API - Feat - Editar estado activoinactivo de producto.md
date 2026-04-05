---
jira_key: "LIO-569"
aliases: ["LIO-569"]
summary: "API - Feat - Editar estado activo/inactivo de producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-09 08:41"
updated: "2026-03-12 09:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-569"
---

# LIO-569: API - Feat - Editar estado activo/inactivo de producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-09 08:41 |
| Actualizado | 2026-03-12 09:55 |
| Etiquetas | ninguna |
| Jira | [LIO-569](https://bluinc.atlassian.net/browse/LIO-569) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-571]] APP - Feat - Editar estado activo/inactivo de producto

## Descripcion

Como vendedor, quiero poder activar o desactivar un producto de mi catálogo desde la API, para controllar qué productos aparecen publicados en el sitio sin tener que eliminarlos.

## Endpoint existente a extender

```
PATCH /v4/inventories/products/{productId}/list
```

Este endpoint ya admite la actualización de `price` y `utility`. Se debe agregar soporte para el parámetro `active`.

---

## Request de ejemplo

```
PATCH /v4/inventories/products/464661/list
​
{
  "active": false
}
```

## Response esperada

La respuesta debe incluir el producto actualizado con el campo `active` reflejando el nuevo estado.

```
{
    "message": "Registro actualizado",
    "status": 200,
    "success": true,
    "product": {
        "id": 464661,
        "internalId": 104935,
        "description": "ACCESORIOS BASE AURICULARES TRUST GXT 265 CINTAR RGB",
        "image": "9aa21a53281c1ba04ba5addcad773562.png",
        "brandImage": "377405e3c9d10637e7cf9c87f6253a04.png",
        "brandId": 5690,
        "brandName": "TRUST",
        "categoryId": 265,
        "categoryName": null,
        "freeShipping": true,
        "instantFlash": false,
        "ratingStar": null,
        "resellerCost": 22194.600000000002,
        "utility": 30.07780241,
        "iva": 21,
        "internalTax": 0,
        "discount": 0,
        "priceUsd": 24.600704,
        "price": 34932,
        "gtin": null,
        "sku": "23647",
        "hide": 0,
        "stock_cliente": 0,
        "stock": 63,
        "inStock": true,
        "sellerId": 22,
        "sellerName": "BsAsPC",
        "ranking": 51,
        "rankingPrevio": 64,
        "active": false
    }
}
```

---

## Tabla afectada

```
UPDATE [CS].[dbo].[productos]
SET activo_vendedor = 0,   -- o 1
    actualizacion = GETDATE()
WHERE vendedorID = ?
  AND id = ?
```

---

## Criterios de aceptación

- `PATCH` con `{ "active": true }` actualiza `activo_vendedor = 1` en `CS.dbo.productos`


- `PATCH` con `{ "active": false }` actualiza `activo_vendedor = 0`


- Valor inválido (ej: `"active": "si"`) retorna error 400 con mensaje claro


- El endpoint solo permite modificar productos que pertenezcan al vendedor autenticado (ya garantizado por `findById()`)


- La respuesta incluye el campo `active` con el valor actualizado


- El campo `actualizacion` se actualiza en la misma query (ya manejado por `parametrizeUpdate()`)


- Se pueden combinar `active` con `price` en el mismo request, pero ejecutan cada uno su logica como hasta ahora



---

## Notas técnicas

- El patrón `parametrizeUpdate()` ya maneja múltiples parámetros en un mismo PATCH; solo se agrega un nuevo `if (isset($params['active']))` al bloque existente.


- No se requiere migración de base de datos; la columna `activo_vendedor` ya existe en `CS.dbo.productos`.
