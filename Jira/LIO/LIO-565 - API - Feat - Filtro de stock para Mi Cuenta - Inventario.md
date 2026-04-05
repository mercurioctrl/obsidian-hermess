---
jira_key: "LIO-565"
aliases: ["LIO-565"]
summary: "API - Feat - Filtro de stock para Mi Cuenta -> Inventario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-05 09:19"
updated: "2026-03-09 10:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-565"
---

# LIO-565: API - Feat - Filtro de stock para Mi Cuenta -> Inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-05 09:19 |
| Actualizado | 2026-03-09 10:25 |
| Etiquetas | ninguna |
| Jira | [LIO-565](https://bluinc.atlassian.net/browse/LIO-565) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-567]] APP - Feat - Filtro de stock para Mi Cuenta -> Inventario

## Descripcion

# Historia: Agregar filtro de stock en `GET /v4/inventories/products`

[adjunto]


## Descripción

Al consumir el endpoint `GET /v4/inventories/products`, quiero poder filtrar los productos según su estado de stock (con stock / sin stock), de la misma forma en que el campo `estados.stock` funciona en `GET /v4/item/{id}`.

---

## Contexto técnico

El endpoint `GET /v4/item/{id}` expone el estado de stock de un producto como:

```
"estados": {
  "stock": true  // true si stock > 0, false si stock = 0
}
```

El stock efectivo de un producto se calcula de forma diferente según su origen:

- Si el producto tiene `id_interno` (producto del catálogo NewBytes) → el stock viene de `[NewBytes_DBF].[dbo].[stocks]`


- Si el producto **no** tiene `id_interno` (producto de cliente/reseller) → el stock viene de `[CS].[dbo].[productos].stock_cliente`



---

## Criterios de aceptación

- El endpoint acepta un nuevo query param opcional: `inStock` (boolean: `true` / `false`)


- Si `inStock=true` → retorna solo productos con stock efectivo > 0


- Si `inStock=false` → retorna solo productos con stock efectivo <= 0


- Si `inStock` no se envía → comportamiento actual sin cambios (no filtra por stock)


- El filtro aplica tanto a los resultados paginados como al conteo total (`metadata.total`)


- Se añade el campo `inStock` (boolean) al DTO de respuesta por ítem



---

## Ejemplo de uso

```
GET /v4/inventories/products?offset=0&limit=30&inStock=true
GET /v4/inventories/products?offset=0&limit=30&inStock=false
```

### Respuesta por ítem (campos nuevos)

```
{
  "id": 123,
  "description": "Producto X",
  "stock_cliente": 5,
  "stock": 5,
  "inStock": true,
  ...
}
```

---

## Archivos a modificar

| Archivo | Cambio |
| --- | --- |
| `app/Service/Inventory/Products/InventoryProductsService.php` | En `extractFilters()`: leer y validar el parámetro `inStock` |
| `app/Repository/Inventory/Products/ProductsRepository.php` | Agregar JOIN a `stocks`, campo calculado en SELECT, método helper `applyStockFilter()` y uso en `listProducts()` y `countProducts()` |
| `app/Dto/Inventory/InventoryProductDto.php` | Agregar propiedades `int $stock` y `bool $inStock` |

---

## Implementación guiada

### 1. `InventoryProductsService.php` — `extractFilters()`

Agregar dentro del método `extractFilters()`, junto a los otros filtros existentes (`brandId`, `categoryId`):

```
if (isset($params['inStock'])) {
    $filters['inStock'] = filter_var($params['inStock'], FILTER_VALIDATE_BOOLEAN, FILTER_NULL_ON_FAILURE);
}
```

> `filter_var` con `FILTER_NULL_ON_FAILURE` devuelve `true`, `false`, o `null` si el valor no es reconocible. Si es `null`, el repositorio lo ignora y no filtra.


---

### 2. `ProductsRepository.php`

#### Paso A — agregar JOIN a `stocks` en ambas queries

El query ya tiene el join a `[articulo]` como alias `[A]`. Agregar debajo:

```
LEFT JOIN [NewBytes_DBF].[dbo].[stocks] [S] ON [A].ID_ARTICULO = [S].ID_ARTICULO
```

#### Paso B — agregar el campo calculado en el SELECT de `listProducts()`

```
CASE
    WHEN [P].id_interno IS NOT NULL
        THEN ISNULL([S].nstock, 0) + ISNULL([S].nstock_lo, 0) + ISNULL([S].nstock_virtual, 0)
             - ISNULL([S].nstock_reserva_pedidos, 0) - ISNULL([S].nstock_lo_reserva_pedidos, 0)
             - ISNULL([S].nstock_seguridad, 0)
    ELSE [P].stock_cliente
END AS stock_calculado
```

#### Paso C — método privado helper `applyStockFilter()`

Agregar este método privado. Es reutilizado por `listProducts()` y `countProducts()` para evitar duplicar la lógica:

```
private function applyStockFilter(?bool $inStock, array &$whereConditions): void
{
    if ($inStock === null) {
        return;
    }
​
    $stockExpr = "
        CASE
            WHEN [P].id_interno IS NOT NULL
                THEN ISNULL([S].nstock, 0) + ISNULL([S].nstock_lo, 0) + ISNULL([S].nstock_virtual, 0)
                     - ISNULL([S].nstock_reserva_pedidos, 0) - ISNULL([S].nstock_lo_reserva_pedidos, 0)
                     - ISNULL([S].nstock_seguridad, 0)
            ELSE [P].stock_cliente
        END
    ";
​
    $whereConditions[] = $inStock
        ? "({$stockExpr}) > 0"
        : "({$stockExpr}) <= 0";
}
```

> No recibe `$params` por referencia porque no agrega parámetros bindeados — la condición compara solo con literales seguros (0).


#### Paso D — invocar el helper en `listProducts()` y `countProducts()`

En ambos métodos, junto al resto de los filtros:

```
$inStock = $filters['inStock'] ?? null;
$this->applyStockFilter($inStock, $whereConditions);
```

---

### 3. `InventoryProductDto.php`

```
// Propiedades nuevas
public int $stock;
public bool $inStock;
​
// En el constructor, junto a stock_cliente:
$this->stock_cliente = (int) ($data->stock_cliente ?? 0);
$this->stock         = (int) ($data->stock_calculado ?? $this->stock_cliente);
$this->inStock       = $this->stock > 0;
```

---

## SQL resultante (ejemplos completos)

### Con `inStock=true`

```
SELECT [P].id, [P].titulo, [P].stock_cliente,
       CASE
           WHEN [P].id_interno IS NOT NULL
               THEN ISNULL([S].nstock,0) + ISNULL([S].nstock_lo,0) + ISNULL([S].nstock_virtual,0)
                    - ISNULL([S].nstock_reserva_pedidos,0) - ISNULL([S].nstock_lo_reserva_pedidos,0)
                    - ISNULL([S].nstock_seguridad,0)
           ELSE [P].stock_cliente
       END AS stock_calculado, ...
FROM [CS].[dbo].[productos] [P]
LEFT JOIN [NewBytes_DBF].[dbo].[articulo] [A] ON [A].ID_ARTICULO = [P].id_interno
LEFT JOIN [NewBytes_DBF].[dbo].[stocks]   [S] ON [A].ID_ARTICULO = [S].ID_ARTICULO
...
WHERE [P].vendedorID = 42
  AND [P].activo = 1
  AND (
        CASE WHEN [P].id_interno IS NOT NULL
            THEN ISNULL([S].nstock,0) + ISNULL([S].nstock_lo,0) + ISNULL([S].nstock_virtual,0)
                 - ISNULL([S].nstock_reserva_pedidos,0) - ISNULL([S].nstock_lo_reserva_pedidos,0)
                 - ISNULL([S].nstock_seguridad,0)
            ELSE [P].stock_cliente
        END
      ) > 0
ORDER BY [P].titulo ASC
OFFSET 0 ROWS FETCH NEXT 30 ROWS ONLY
```

### Con `inStock=false`

Igual que el anterior pero con `... ) <= 0` al final de la condición de stock.

### Sin `inStock` (comportamiento actual, sin cambios)

Sin la condición de stock en el WHERE.
