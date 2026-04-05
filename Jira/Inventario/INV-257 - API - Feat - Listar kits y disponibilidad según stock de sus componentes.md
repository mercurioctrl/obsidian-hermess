---
jira_key: "INV-257"
aliases: ["INV-257"]
summary: "API - Feat - Listar kits y disponibilidad según stock de sus componentes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-20 08:58"
updated: "2025-12-05 05:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-257"
---

# INV-257: API - Feat - Listar kits y disponibilidad según stock de sus componentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-20 08:58 |
| Actualizado | 2025-12-05 05:45 |
| Etiquetas | ninguna |
| Jira | [INV-257](https://bluinc.atlassian.net/browse/INV-257) |

## Relaciones

- **Padre:** [[INV-253 - Crear y modificar Kits|INV-253]] Crear y modificar Kits
- **has action item:** [[INV-271 - APP - Feat - Pestaña “Kits”, listado y acción “Marcar como kit”|INV-271]] APP - Feat - Pestaña “Kits”, listado y acción “Marcar como kit”

## Descripcion

Exponer un recurso que:

- Liste todos los productos que están marcados como **kit** en
`[NewBytes_DBF].[dbo].[articulo].kit = 1`.


- Para cada kit, calcule si **tiene stock suficiente de todas sus piezas** en
`[NewBytes_DBF].[dbo].[stocks].nstock` (por depósito / `stockWarehouseId`).


- Devuelva:

- La ficha del producto (similar al listado estándar).


- Un parámetro booleano que indique si el kit está **disponible** (tiene stock en todas las piezas para al menos 1 kit).


- La cantidad de kits que se pueden armar (opcional pero muy útil, la calculamos igual).





> Regla de negocio alineada al documento de kits: un kit se puede vender solo mientras haya stock de todas sus piezas; si falta una, el kit no está disponible. Productos compuestos (kits) — P…


---

### Endpoint

```
GET {API_URL}/itemsKits

```

### Parámetros de query (sugeridos)

- `companyCode` *(opcional)*: filtra por compañía.


- `stockWarehouseId` *(recomendado/obligatorio)*: depósito desde el cual se evalúa stock de componentes.


- `onlyAvailable` *(opcional, bool, default=false)*:

- `true` → devolver solo kits cuya disponibilidad sea `true`.


- `false` → devolver todos los kits con su flag de disponibilidad.





Ejemplos:

```
GET {API_URL}/itemsKits?stockWarehouseId=2&onlyAvailable=true
GET {API_URL}/itemsKits?stockWarehouseId=2&companyCode=4

```

---

### Respuesta esperada

Formato general:

```
{
  "list": [
    {
      "title": "DISCO SSD PATRIOT P400 2TB M.2 2280 GEN4 PS001656",
      "sku": "P400LP2KGM28H",
      "id": 121111,
      "category": "DISCOS SSD",
      "categoryId": 56,
      "brand": "ARGENPLAS",
      "brandId": 1276,
      "mainImage": "http://static.nb.com.ar/img/c25217056e206716326a42d6c23cabc8.png",
      "stock": 47.0,
      "warranty": "14 meses",
      "companyCode": 4,
      "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
      "iva": 0.0,
      "notSerializable": 0,
      "distributorDescription": "Air",
      "distributorId": 4,
      "stockWarehouseId": 2,
      "stockWarehouseDescription": "SAFcom",

      "kitStockSatisfied": true,
      "kitBuildableQty": 47.0
    }
  ],
  "total": 1
}

```

**Nuevos campos específicos de kit**

- `kitStockSatisfied` (bool)

- `true` → todas las piezas del kit tienen stock suficiente para armar **al menos 1 kit** en el depósito indicado.


- `false` → alguna pieza no tiene stock suficiente.




- `kitBuildableQty` (numérico)

- Cantidad máxima de kits que se pueden armar con el stock actual de componentes, calculado como:

- `MIN( FLOOR( nstock_componente / quantityNeeded ) )` sobre todos los componentes del kit activos (`softDelete = 0`) en ese depósito.







**Campo **`stock`

- Puede mapearse directamente a `kitBuildableQty` (es decir, el “stock virtual” del kit).


- Si ya tenés una convención de `stock` para el resto de productos, definimos que, para kits, `stock = kitBuildableQty` para mantener coherencia.



---

### Lógica de negocio

- **Identificar kits**

- Seleccionar artículos con:

```
FROM [NewBytes_DBF].[dbo].[articulo] A
WHERE A.kit = 1

```




- **Relacionar componentes**

- Usar `[NewBytes_DBF].[dbo].[articulo_kits]`:

- `itemId` → id del kit.


- `itemIdInKit` → id del componente.


- `quantityNeeded`→ cantidad de ese componente por 1 kit.


- `softDelete = 0`→ solo componentes activos.






- **Traer stock de componentes**

- Desde `[NewBytes_DBF].[dbo].[stocks]`:

- `stocks.id_articulo = itemIdInKit`


- `stocks.id_deposito = @stockWarehouseId` (parámetro del endpoint).


- `stocks.nstock` = stock disponible de ese componente en ese depósito.






- **Calcular stock virtual de kit**

Para cada kit:

- Por cada componente:

- `kits_posibles_por_componente = FLOOR( nstock / quantityNeeded )`




- Stock de kit:

- `kitBuildableQty = MIN( kits_posibles_por_componente )` (entre todos los componentes del kit).




- Disponibilidad:

- `kitStockSatisfied = (kitBuildableQty >= 1)`






- **Filtros**

- Si `onlyAvailable = true`, filtrar por `kitBuildableQty >= 1`.


- Si se pasa `companyCode`, filtrar por compañía del artículo/stock.





---

### Criterios de aceptación

- **Listado básico de kits**

- Dado que existen artículos con `kit = 1`, al llamar:

```
GET /itemsKits?stockWarehouseId=2

```

se devuelve un `200` con:

- `list` conteniendo solo productos kit.


- Campos básicos (title, sku, id, category, brand, etc.).


- `kitBuildableQty` calculado.


- `kitStockSatisfied` coherente con `kitBuildableQty >= 1`.






- **Filtro de disponibilidad**

- Dado un kit cuyos componentes tienen stock suficiente para al menos 1 kit:

- Aparece en `GET /itemsKits?stockWarehouseId=2&onlyAvailable=true`


- `kitStockSatisfied = true`.




- Dado un kit con alguna pieza sin stock:

- No aparece si `onlyAvailable=true`.


- Sí aparece si `onlyAvailable=false`, con `kitStockSatisfied = false` y `kitBuildableQty = 0`.






- **Consistencia de stock**

- Para un kit con:

- Componente A: `nstock = 10`, `quantityNeeded = 2` → 5 kits posibles.


- Componente B: `nstock = 3`, `quantityNeeded = 1` → 3 kits posibles.




- El endpoint debe devolver:

- `kitBuildableQty = 3`


- `stock = 3`


- `kitStockSatisfied = true`.






- **Errores de parámetros**

- Si se llama sin `stockWarehouseId` y el endpoint lo requiere:

- Devolver `400` con mensaje claro.




- Si `stockWarehouseId` no existe:

- Devolver `400` o `404` según convención del backend.







[adjunto]
