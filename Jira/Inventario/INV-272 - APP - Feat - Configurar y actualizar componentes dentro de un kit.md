---
jira_key: "INV-272"
aliases: ["INV-272"]
summary: "APP - Feat - Configurar y actualizar componentes dentro de un kit"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-12-04 05:08"
updated: "2025-12-09 16:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-272"
---

# INV-272: APP - Feat - Configurar y actualizar componentes dentro de un kit

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-04 05:08 |
| Actualizado | 2025-12-09 16:02 |
| Etiquetas | ninguna |
| Jira | [INV-272](https://bluinc.atlassian.net/browse/INV-272) |

## Relaciones

- **Padre:** [[INV-253 - Crear y modificar Kits|INV-253]] Crear y modificar Kits
- **action item from:** [[INV-256 - API - Feat - Eliminar un componente de un kit (soft delete) y recalcular su|INV-256]] API - Feat - Eliminar un componente de un kit (soft delete) y recalcular su costo
- **action item from:** [[INV-255 - API - Feat - Configurar o actualizar componentes de un kit y recalcular su costo|INV-255]] API - Feat - Configurar o actualizar componentes de un kit y recalcular su costo

## Descripcion

**Contexto**
En la pestaña **“Kits”** del módulo de inventario, necesitamos poder **configurar qué productos componen cada kit**, con sus cantidades y estado (pausado o no).
La configuración se hará a nivel de cada kit desde el listado, usando los recursos de backend:

```
PATCH {API_URL}/itemsKits/{itemId}
```

 para **agregar/actualizar** un componente.

```
DELETE {API_URL}/itemsKits/{itemId}/{itemIdInKit}
```

 para **eliminar (soft delete)** un componente.

El backend se encarga de recalcular el costo promedio del kit (`ncosteprom`) cada vez que cambiamos componentes.

---

### Objetivo

Permitir que desde el listado de kits el usuario pueda:

- Abrir una vista / modal de **“Componentes del kit”** para un kit específico.


- Ver el listado de componentes actuales del kit (cada `itemIdInKit` con su `quantityNeeded` y estado `paused`).


- **Agregar o editar** componentes del kit usando `PATCH /itemsKits/{itemId}`.


- **Eliminar** componentes del kit usando `DELETE /itemsKits/{itemId}/{itemIdInKit}`.


- Ver feedback visual de que el costo del kit se actualizó (por ejemplo, mostrando el costo actualizado del kit si viene en el response o en un refresh del kit).



---

### Alcance funcional (Front)

#### 1) Acceso a la configuración de componentes

- En la pestaña **Kits**, sobre cada fila de kit del listado, agregar una forma de acceder a la configuración:

- Ejemplo:

- Opción en menú de **click derecho**: “Configurar componentes del kit”.


- O un botón/ícono de acción en la fila (tres puntitos, engranaje, etc.).






- Al accionar esa opción:

- Abrir un **modal** o pantalla lateral llamada, por ejemplo, **“Componentes del kit {sku / título}”**.





#### 2) Vista / modal de “Componentes del kit”

Dentro del modal (o vista) se debe mostrar:

- Datos resumen del kit: `title`, `sku`, `id` y, si está disponible, su costo actual.


- Una **grilla/lista de componentes** con columnas mínimas:

- `itemIdInKit`


- Descripción / título del componente


- `quantityNeeded`


- `paused` (ej. con un switch o badge “Pausado/Activo”)




- Un botón **“Agregar componente”** para crear una nueva relación.


- Acciones por fila:

- **Editar** (abrir formulario con los datos actuales).


- **Eliminar** (soft delete) → confirmación antes de llamar al DELETE.





> Nota: El origen exacto de los datos de componentes puede venir de un endpoint específico de detalle del kit o de la misma respuesta de backend que ya tengas definida. En esta historia asumimos que el frontend tiene una forma de obtener la lista actual de componentes para ese kit (GET de detalle).


#### 3) Alta / edición de componentes (PATCH /itemsKits/{itemId})

- Al hacer clic en **“Agregar componente”**:

- Abrir un sub-formulario dentro del modal con:

- Campo para seleccionar / ingresar `itemIdInKit`.


- Campo numérico para `quantityNeeded` (> 0).


- Toggle/checkbox para `paused` (true/false).






- Al guardar:

- Enviar:

```
PATCH {API_URL}/itemsKits/{itemId}
```

```
{
  "itemIdInKit": 42343,
  "quantityNeeded": 2,
  "paused": false
}
```


- Mostrar estado de carga.


- Si la respuesta es `success = true`:

- Mostrar mensaje de éxito (“Se guardó el componente del kit y se actualizó el costo”).


- Refrescar el listado de componentes.


- Opcional: refrescar el kit en el listado principal para ver el nuevo costo/stock si aplica.




- Manejo de errores típicos:

- **404** → mostrar mensaje claro:

- Si `itemId` no existe o no es kit → informar que el kit no es válido.


- Si `itemIdInKit` no existe → informar que el componente no existe.




- **400** (por `quantityNeeded <= 0` o `itemId = itemIdInKit`) → mostrar mensaje específico según la causa (cantidad debe ser mayor a 0 / el kit no puede incluirse a sí mismo).


- **409** (si se usa para la regla de auto-contenencia) → mensaje indicando que el kit no puede incluirse a sí mismo.


- Otros 5xx o red → mensaje genérico de error.






- Para **editar** un componente existente:

- Reutilizar el mismo formulario cargando valores actuales de `itemIdInKit`, `quantityNeeded`, `paused`.


- Enviar el mismo PATCH (el backend decide si hace INSERT o UPDATE).





#### 4) Eliminar componente (DELETE /itemsKits/{itemId}/{itemIdInKit})

- En cada fila de la grilla de componentes, incluir una acción **“Eliminar”**.


- Al hacer clic:

- Mostrar un **diálogo de confirmación** (“¿Seguro que querés eliminar este componente del kit?”).


- Si se confirma, llamar:

```
DELETE {API_URL}/itemsKits/{itemId}/{itemIdInKit}
```


- Mostrar estado de carga.


- Si la respuesta es `success = true`:

- Quitar el componente de la grilla (o marcarlo como eliminado al recargar).


- Mostrar mensaje de éxito (“Se eliminó el componente del kit y se actualizó el costo”).


- Refrescar datos del kit si corresponde (costo/stock).




- Si el componente no existe o ya está soft deleted → mostrar mensaje coherente con el 404 (“El componente que intentás eliminar ya no existe en este kit”).


- Otros errores → mensaje genérico sin romper la vista.





#### 5) Costo actualizado del kit (feedback visual)

- Aunque el cálculo lo hace el backend, el front debería:

- Después de cualquier PATCH o DELETE exitoso, **refrescar**:

- La lista de componentes.


- Y, si es posible, los datos del kit (incluyendo costo) en la cabecera del modal o en el listado principal.






- Opcional pero deseable:

- Mostrar el costo antes y después de la operación, si la API lo provee (no es obligatorio en esta historia, solo refrescar).





---

### Criterios de aceptación (Front)

- **Acceso desde el listado de kits**

- Dado que el usuario está en la pestaña **Kits** y ve un kit en la grilla,
cuando hace click derecho o usa el botón de acción sobre ese kit,
entonces aparece la opción **“Configurar componentes del kit”** y, al seleccionarla, se abre el modal/vista correspondiente.




- **Visualización de componentes**

- Dado un kit con componentes configurados,
cuando se abre la pantalla de **Componentes del kit**,
entonces se muestra la lista de componentes con `itemIdInKit`, descripción, `quantityNeeded` y estado `paused`.




- **Alta/edición de componente (PATCH OK)**

- Dado un kit válido (`itemId` es kit) y un componente válido (`itemIdInKit` existe y no es kit),
cuando el usuario completa `quantityNeeded > 0` y guarda,
entonces el front envía `PATCH /itemsKits/{itemId}` con el payload correcto y,
al recibir `success = true`, se muestra mensaje de éxito y se refresca la lista de componentes.




- **Manejo de errores de validación (PATCH)**

- Dado que el usuario intenta guardar un componente con `quantityNeeded <= 0` o `itemId = itemIdInKit`,
cuando el backend responde con 400/409,
entonces el front muestra un mensaje entendible y mantiene el formulario visible para corrección.




- **Eliminación de componente (DELETE OK)**

- Dado un componente existente en el kit,
cuando el usuario confirma la operación de eliminar,
entonces el front llama `DELETE /itemsKits/{itemId}/{itemIdInKit}` y,
al recibir `success = true`, quita el componente de la grilla (o lo oculta tras recargar) y muestra mensaje de éxito.




- **Manejo de errores en DELETE**

- Dado que un componente ya fue eliminado o no existe en el kit,
cuando el backend responde 404 al DELETE,
entonces el front muestra un mensaje informando que el componente no se encuentra y no rompe la pantalla.




- **Actualización de costo del kit (feedback)**

- Dado que se ejecutó un PATCH o DELETE exitoso sobre los componentes de un kit,
cuando la operación termina,
entonces el front refresca los datos del kit (en el modal y/o en el listado principal) para reflejar el costo actualizado.
