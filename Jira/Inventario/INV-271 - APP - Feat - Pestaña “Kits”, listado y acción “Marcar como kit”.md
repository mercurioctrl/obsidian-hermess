---
jira_key: "INV-271"
aliases: ["INV-271"]
summary: "APP - Feat - Pestaña “Kits”, listado y acción “Marcar como kit”"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-04 05:00"
updated: "2025-12-26 12:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-271"
---

# INV-271: APP - Feat - Pestaña “Kits”, listado y acción “Marcar como kit”

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-04 05:00 |
| Actualizado | 2025-12-26 12:41 |
| Etiquetas | ninguna |
| Jira | [INV-271](https://bluinc.atlassian.net/browse/INV-271) |

## Relaciones

- **Padre:** [[INV-253 - Crear y modificar Kits|INV-253]] Crear y modificar Kits
- **action item from:** [[INV-254 - API - Feat - Cear un nuevo kit|INV-254]] API - Feat - Cear un nuevo kit
- **action item from:** [[INV-257 - API - Feat - Listar kits y disponibilidad según stock de sus componentes|INV-257]] API - Feat - Listar kits y disponibilidad según stock de sus componentes
- **relates to:** [[INV-308 - APP - Refactor - Marcar articulo como kit - Considerar companyCode al buscar en|INV-308]] APP - Refactor - Marcar articulo como kit -> Considerar companyCode al buscar en items

## Descripcion

En el módulo de **Inventario / Lista de productos** necesitamos una nueva pestaña específica para **Kits**, donde:

- Se liste la información de los kits usando `GET /itemsKits`.


- Se vea su **disponibilidad** según stock de componentes.


- Se pueda **marcar un artículo como kit** usando `POST /itemsKits`.



### Objetivo

Agregar una pestaña **“Kits”** junto a la lista de productos, que:

- Consuma 

```
GET {API_URL}/itemsKits
```

 para mostrar el listado de productos marcados como kit, con sus campos específicos:

- `kitStockSatisfied` (bool)


- `kitBuildableQty` (cantidad de kits armables)


- `stock` mapeado a `kitBuildableQty`




- Permita, desde la misma pestaña, ejecutar el endpoint 

```
POST {API_URL}/itemsKits
```

 para marcar un artículo existente como kit, enviando el `itemId`.



---

### Alcance funcional (Front)

#### 1) Nueva pestaña “Kits”

- En la pantalla donde hoy se listan los productos, agregar una pestaña adicional:

- **Productos | Kits | (otras…)**




- Al seleccionar **“Kits”**, se carga una vista específica de kits.



#### 2) Listado de kits (GET /itemsKits)

- El frontend debe consumir:

```
GET {API_URL}/itemsKits?stockWarehouseId={id}&onlyAvailable={bool?}&companyCode={code?}
```


- En la UI, la pestaña **Kits** debe incluir:

- Un selector obligatorio de **depósito** (`stockWarehouseId`).


- Filtros opcionales:

- **Solo disponibles** (`onlyAvailable = true/false`).


- **Compañía** (`companyCode`, si aplica al flujo).






- Al confirmar los filtros, llamar a `GET /itemsKits` y mostrar la grilla con, como mínimo:

- `title`, `sku`, `id`, `brand`, `category`, `companyName`, `stockWarehouseDescription`


- `kitBuildableQty` (mostrado como stock de kit).


- `kitStockSatisfied` (badge/indicador visual: disponible / no disponible).





> Nota: Para mantener coherencia, en la grilla de kits el campo “Stock” debe usar el valor de `kitBuildableQty`.


#### 3) Indicadores de disponibilidad

- Para cada fila:

- Si `kitStockSatisfied = true` → mostrar indicador de **kit disponible** (por ejemplo, badge verde “Disponible”).


- Si `kitStockSatisfied = false` → indicador de **no disponible** (badge rojo “Sin stock de componentes” o similar).




- Mostrar `kitBuildableQty` como “Kits posibles” (por ejemplo: `3`, `0`, etc.).



#### 4) Acción “Marcar artículo como kit” (POST /itemsKits)

- Dentro de la pestaña **Kits**, agregar un mecanismo para marcar un artículo existente como kit, por ejemplo:

- Botón “**Marcar artículo como kit**” que abre un modal.


- En el modal, un campo para ingresar `itemId` (o búsqueda básica de producto, si se quiere).




- Al confirmar:

- Llamar:

```
POST {API_URL}/itemsKits
```

```
{
  "itemId": 12345
}
```


- Mostrar estado de carga mientras se hace la petición.


- Si la respuesta devuelve `success = true`:

- Mostrar mensaje de éxito (“El artículo fue marcado como kit”).


- Refrescar el listado llamando nuevamente a `GET /itemsKits` para ver el nuevo kit.




- Manejar errores:

- **404** → mensaje claro: el artículo no existe.


- **409** → mensaje: el artículo ya está marcado como kit.


- Otros errores → mensaje genérico (“No se pudo marcar el artículo como kit. Intentá de nuevo.”).







---

### Criterios de aceptación (Front)

- **Pestaña “Kits” visible**

- Dado que el usuario ingresa al módulo de lista de productos,
cuando se renderiza la navegación de pestañas,
entonces se visualiza una pestaña adicional llamada **“Kits”**.




- **Selector de depósito obligatorio**

- Dado que el usuario está en la pestaña **Kits**,
cuando intenta cargar el listado sin elegir depósito (`stockWarehouseId`),
entonces la interfaz debe impedir la búsqueda o mostrar un mensaje indicando que el depósito es obligatorio.




- **Listado de kits con campos de negocio**

- Dado que existen artículos con `kit = 1` y se llama a
`GET /itemsKits?stockWarehouseId=2`,
cuando la respuesta incluye `list` y `total`,
entonces la grilla muestra:

- Solo productos kit.


- Los campos básicos (title, sku, id, brand, etc.).


- `kitBuildableQty` en una columna de “Stock” o “Kits posibles”.


- Un indicador que refleja `kitStockSatisfied` (Disponible / No disponible).






- **Filtro “Solo disponibles”**

- Dado kits con y sin stock de componentes,
cuando el usuario marca el filtro “Solo disponibles” (onlyAvailable=true),
entonces el listado sólo muestra kits con `kitStockSatisfied = true` y `kitBuildableQty >= 1`.




- **Consistencia stock–kitBuildableQty**

- Dado un kit con componentes que permiten armar 3 kits como máximo,
cuando se carga el listado,
entonces se muestra `kitBuildableQty = 3`, `stock = 3` y `kitStockSatisfied = true`.




- **Acción “Marcar artículo como kit” exitosa**

- Dado un `itemId` existente que aún no es kit,
cuando el usuario lo ingresa en el modal y confirma,
entonces el frontend llama a `POST /itemsKits` con ese `itemId`,
y al recibir `success = true`:

- Se muestra un mensaje de éxito.


- El ítem aparece luego en el listado de `GET /itemsKits` tras refrescar.






- **Errores 404 / 409**

- Dado que se ingresa un `itemId` inexistente,
cuando el backend devuelve **404**,
entonces se muestra un mensaje indicando que el artículo no existe.


- Dado que se ingresa un `itemId` que ya es kit,
cuando el backend devuelve **409**,
entonces se muestra un mensaje indicando que el artículo ya está marcado como kit.




- **Errores generales**

- Dado que ocurre un error de red o 5xx al llamar a `POST /itemsKits` o `GET /itemsKits`,
cuando el frontend recibe el error,
entonces se muestra un mensaje genérico de error sin romper la vista ni dejarla en estado inconsistente.
