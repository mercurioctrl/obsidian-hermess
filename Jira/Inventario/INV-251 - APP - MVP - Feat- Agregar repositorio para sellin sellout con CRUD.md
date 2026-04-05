---
jira_key: "INV-251"
aliases: ["INV-251"]
summary: "APP - MVP - Feat- Agregar repositorio para sellin sellout con CRUD "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-10-17 11:24"
updated: "2025-12-02 02:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-251"
---

# INV-251: APP - MVP - Feat- Agregar repositorio para sellin sellout con CRUD 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-17 11:24 |
| Actualizado | 2025-12-02 02:36 |
| Etiquetas | ninguna |
| Jira | [INV-251](https://bluinc.atlassian.net/browse/INV-251) |

## Relaciones

- **Padre:** [[INV-250 - Repositorio de Sell In Sell Out|INV-250]] Repositorio de Sell In Sell Out
- **action item from:** [[INV-249 - API - MVP - Feat- AgregarEditarEliminar repositorio para sellin sellout con CRUD|INV-249]] API - MVP - Feat- Agregar/Editar/Eliminar repositorio para sellin sellout con CRUD 

## Descripcion

Agregar a la aplicación de inventario una nueva pestaña para administrar los descuentos de tipo *sell-in / sell-out*:

- Listado con filtros usando el endpoint 

```
GET {API_URL}/sellDiscount?currentPage=1&itemsPerPage=500&companyCode=4&brandId=43&categoryId=3&between=05-11-2025_12-11-2025&search={itemId|string|sku}
```


- Acciones para **crear**, **editar/pausar** y **eliminar** descuentos.


- Un **mismo modal reutilizable** tanto para *alta* (POST) como para *edición* (PATCH).



La vista de frontend es únicamente la interfaz de administración; la lógica de costos y aplicación de descuentos se resuelve del lado del backend.

---

### Alcance funcional (Frontend)

#### 1. Nueva pestaña en Inventario

- Agregar una pestaña nueva dentro del módulo de Inventario llamada, por ejemplo, **“Sell-in / Sell-out”**.


- Al ingresar a esta pestaña se muestra:

- Filtros arriba.


- Tabla paginada con los descuentos.


- Botón principal para **“Nuevo descuento”**.





---

#### 2. Listado de descuentos (Grid)

Consumir:

```
GET {API_URL}/sellDiscount?currentPage=1&itemsPerPage=500&companyCode=4&brandId=&categoryId=&between=&search=
```

**Filtros visuales (mapeados a los parámetros del GET):**

- `companyCode` (select o valor fijo según cómo lo maneje la app hoy).


- `brandId` (combo opcional).


- `categoryId` (combo opcional).


- `between` (selector de rango de fechas dd-mm-YYYY_dd-mm-YYYY).


- `search` (input único que busque por itemId, sku o texto del título).


- Paginación: `currentPage` + `itemsPerPage` (usar el mismo patrón de la grilla actual de inventario).



**Columnas sugeridas en la tabla:**

- `itemId`


- `title`


- `sku`


- `stockWarehouseCode`


- `stockWarehouseId`


- `originalCost`


- `percentageDiscount`


- `amountDiscount`


- `maxStockQty`


- `endDate`


- `paused` (mostrar algo visual: chip/etiqueta “Activo” / “Pausado”)


- `createdAt`


- `updatedAt`


- Columna de **acciones** (editar, pausar/reactivar, eliminar).



> Importante: el listado **no debe mostrar** descuentos eliminados (DELETE soft en backend).


---

#### 3. Acciones desde la grilla

En la columna de acciones de cada fila:

- **Editar / Ver detalles**

- Abre el **modal de descuento** en modo edición.


- Carga los datos del registro seleccionado.


- Al guardar, dispara


```
PATCH {API_URL}/sellDiscount/{id}
```




- **Pausar / Reactivar**
Hay dos opciones posibles (a convenir en diseño), pero la historia debe contemplar al menos una:

- a) **Acción rápida** (toggle): botón o switch que mande un `PATCH` con `paused: true/false`, o


- b) Cambiar el flag dentro del mismo modal de edición (tildar o destildar la opción “Pausado”).



En ambos casos:

- Debe actualizar visualmente el estado en la grilla.


- El botón/etiqueta debe ser coherente con el estado actual (p. ej. si está activo, mostrar opción “Pausar”).




- **Eliminar**

- Botón “Eliminar” con **modal de confirmación**.


- En confirmación llamar a:

```
DELETE {API_URL}/sellDiscount/{id}
```


- Si la operación es exitosa:

- Mostrar mensaje de éxito.


- Refrescar la grilla.




- Si el `id` no existe o hay error, mostrar mensaje claro (404 u otro mensaje de error que devuelva el backend).





---

#### 4. Modal reutilizable (Crear / Editar)

El mismo modal se utiliza para:

- **Crear nuevo descuento** (POST).


- **Editar descuento existente** (PATCH).



**Apertura del modal:**

- Botón **“Nuevo descuento”** sobre la grilla:

- Abre modal vacío en modo “Alta”.


- Al confirmar, hace

```
POST /sellDiscount
```




- Acción “Editar” en cada fila:

- Abre el modal completado con los datos del descuento.


- Al confirmar, hace

```
PATCH /sellDiscount/{id}
```





**Campos del modal:**

Campos base (editable en alta, algunos pueden ser de solo lectura en edición, según diseño):

- `itemId`

- Input o selector (idealmente con búsqueda por sku/título).




- `stockWarehouseId`

- Selector de depósito.




- `originalCost`

- Mostrar **solo lectura** (lo resuelve backend, pero se puede mostrar si viene en la respuesta en modo edición).




- Tipo de descuento:

- Radio buttons o toggle:

- “Descuento porcentual” → habilita `percentageDiscount`.


- “Monto fijo” → habilita `amountDiscount`.






- `percentageDiscount` (input numérico, deshabilitado si está seleccionado monto fijo).


- `amountDiscount` (input numérico, deshabilitado si está seleccionado porcentaje).


- `maxStockQty` (input numérico opcional).


- `endDate` (selector de fecha/hora opcional).


- `paused` (checkbox o switch):

- “Descuento pausado” / “Descuento activo”.





**Reglas de validación en el frontend:**

- **Regla de exclusividad**:

- Debe haber **exactamente uno** de:

- `percentageDiscount` **o**


- `amountDiscount`.




- Si el usuario intenta guardar con **ambos con valor** o **los dos vacíos**, mostrar error claro antes de enviar la request.




- **Regla de fin de vigencia**:

- Debe estar presente **al menos uno** entre:

- `endDate`


- `maxStockQty`




- No permitir guardar si ambos están vacíos.




- **Valores no negativos**:

- No permitir valores negativos en:

- `percentageDiscount`


- `amountDiscount`


- `maxStockQty`






- Campos obligatorios en alta:

- `itemId`


- `stockWarehouseId`


- El tipo de descuento elegido con su valor correspondiente (según regla de exclusividad).




- En edición (PATCH):

- Permitir modificar parcialmente:

- `paused`


- `endDate`


- `maxStockQty`


- `percentageDiscount` / `amountDiscount` (manteniendo la exclusividad).







**Mensajes:**

- En éxito de POST:

- Mostrar mensaje tipo:

“Descuento sell-in/sell-out creado correctamente.”


- Cerrar modal y refrescar grilla.




- En éxito de PATCH:

- Mostrar mensaje tipo:

“Descuento sell-in/sell-out actualizado correctamente.”


- Cerrar modal y refrescar grilla.




- En errores de validación backend:

- Mostrar mensajes claros provenientes del backend (por ejemplo: exclusividad de porcentaje/monto, conflictos de fechas, etc.).





---

### Endpoints a consumir (resumen)

- `GET {API_URL}/sellDiscount?...` → Listado con filtros y paginación.


- `POST {API_URL}/sellDiscount` → Alta desde el modal.


- `PATCH {API_URL}/sellDiscount/{id}` → Edición / pausa / cambio de límites y tipo de descuento.


- `DELETE {API_URL}/sellDiscount/{id}` → Eliminación (soft delete) desde la acción de la grilla.



---
