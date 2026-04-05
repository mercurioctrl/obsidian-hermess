---
jira_key: "PED-1181"
aliases: ["PED-1181"]
summary: "APP - Refactor - Mostrar kits en vista de pedido usando la nueva respuesta del endpoint"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-11 08:25"
updated: "2025-12-16 13:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1181"
---

# PED-1181: APP - Refactor - Mostrar kits en vista de pedido usando la nueva respuesta del endpoint

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-11 08:25 |
| Actualizado | 2025-12-16 13:41 |
| Etiquetas | ninguna |
| Jira | [PED-1181](https://bluinc.atlassian.net/browse/PED-1181) |

## Relaciones

- **Padre:** [[PED-1170 - Kits|PED-1170]] Kits
- **action item from:** [[PED-1180 - API - Refactor - Modelaremos el objeto de la orden para incluir relación con|PED-1180]] API - Refactor - Modelaremos el objeto de la orden para incluir relación con kits y su informacion complementaria sin ser disruptivos con el actual funcionamiento

## Descripcion

**Modale afectado de ejemplo**


[adjunto]
- Modal de detalle de pedido (ejemplo: “Pedido 0002-10426380”) en pedidos.


- Tabla donde hoy se listan los renglones del pedido (ID, Producto, Cant., Costo, Precio, IVA, Subtotales, etc.).



**Backend disponible**

- ```
GET {API_URL}/v1/orders/{branchNumber}-{orderNumber}
```


- Ahora devuelve:

- `items[]` con un nuevo campo `kitId` (nullable).


- `kits[]` con la información agregada de cada kit (id, title, sku, price, iva, etc.).





---

### Objetivo

Cuando una orden tenga items que pertenecen a un kit (`item.kitId` no nulo), la tabla **no debe mostrar esas líneas individuales como productos sueltos**, sino:

- Mostrar **una sola fila por kit**, tomando los datos desde `kits[]`.


- Permitir al operador **desplegar/plegar** el kit para ver qué items lo componen (sku, id, cantidad, nombre del producto).



---

### Comportamiento requerido

#### 1. Construcción de los renglones

A partir de la respuesta del endpoint:

- Armar un mapa:

- `itemsByKitId[kitId] = [items...]` con todos los `items` cuyo `item.kitId === kit.id`.




- Separar:

- **Items con kit**: `items` con `kitId` no nulo → no se muestran como filas “normales”.


- **Items sin kit**: `items` con `kitId === null` → se muestran igual que hoy.




- Para cada `kit` en `kits[]`:

- Crear una **fila de tipo “kit”** que represente al producto kit, usando:

- Columna **ID**: `kit.id`


- Columna **Producto**: `kit.title`


- Columna **Cant.**: `kit.amount` (si viene) o la suma de `itemsByKitId[kit.id].amount`.


- Columnas **Precio / IVA / Subtotal / Subtotal Final**: basadas en `kit.price` (mismo formato que hoy para items).




- Visualmente se debe ver como una línea de producto “normal”, pero con un icono o indicador de que es un kit (ej. flecha desplegable o ícono “+”).





#### 2. Interacción: desplegar / ver componentes del kit

- En la fila del kit agregar un accionable (botón/icono) del tipo:

- “Ver componentes” / ícono de desplegar (triángulo / caret).




- Al hacer clic:

- Se insertan **debajo de la fila del kit** las filas hijas correspondientes a `itemsByKitId[kit.id]`.


- Estas filas hijas muestran, al menos:

- **ID**: `item.id`


- **Producto**: `item.title`


- **SKU**: `item.sku`


- **Cant.**: `item.amount`


- Opcionalmente costo, precio, IVA, subtotales, etc., pero se pueden mostrar en estilo secundario (texto gris / indentado) para que se interpreten como detalle del kit.




- La fila de kit se mantiene visible arriba, actuando como cabecera.




- Al volver a hacer clic en el mismo icono:

- Se ocultan nuevamente las filas hijas de ese kit (colapsado).





#### 3. Totales y comportamiento sin kits

- **No cambiar la lógica actual de totales** (subtotales, IVA, percepción, etc.).
Solo cambia qué filas se visualizan inicialmente.


- Si la orden no tiene kits:

- `kits` vendrá vacío o no existirá.


- Todos los `items` tienen `kitId === null`.


- La tabla se comporta exactamente como hoy.







De no haber kit, no cambia nada, todo se muestra como siempre
