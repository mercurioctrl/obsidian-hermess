---
jira_key: "INV-235"
aliases: ["INV-235"]
summary: "APP - Feat - Ajuste manual de stock "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-11-10 09:23"
updated: "2025-12-05 04:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-235"
---

# INV-235: APP - Feat - Ajuste manual de stock 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-10 09:23 |
| Actualizado | 2025-12-05 04:16 |
| Etiquetas | ninguna |
| Jira | [INV-235](https://bluinc.atlassian.net/browse/INV-235) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **action item from:** [[INV-216 - API - MVP - Feat - Ajuste manual de stock (con permisos y registro)|INV-216]] API - MVP - Feat - Ajuste manual de stock (con permisos y registro)

## Descripcion

Actualmente el backend expone el recurso:

```
POST {API_URL}/itemsStocks/{itemId}/manualAdjustments
```

```
{
  "amount": 5,
  "reason": "Ajuste por conteo físico",
  "warehouseStockId": 2
}

```

La operación ajusta el valor del campo `nstock_d1` (stock oculto) del ítem y deja registro en el historial de stock.

---

### Objetivo

Desde el **listado de productos / stock**, permitir que un usuario con permisos pueda **ajustar manualmente el stock oculto (**`nstock_d1`**) de un ítem** mediante una acción contextual, sin agregar columnas nuevas en la grilla.

La operación ajusta el valor del campo `nstock_d1` (stock oculto) del ítem y deja registro en el historial de stock.

---

### Alcance funcional (Front)

- **Acción de ajuste desde el listado**

- En el listado de productos, al hacer **click derecho sobre una fila de ítem** o mediante un **acción contextual que no ocupe espacio adicional en la grilla** (por ejemplo, menú de tres puntos ya existente), se debe ofrecer la opción:

- **“Ajustar stock oculto”**.




- Esta acción abre un **modal de ajuste de stock** para el ítem seleccionado.




- **Modal de ajuste de stock oculto**

- El modal debe:

- Mostrar información mínima del ítem para no perder contexto (ej.: *ID del ítem + título*).


- Incluir un **input numérico** con el valor actual de `nstock_d1` como valor inicial.


- Explicar claramente que:

- El valor representa el **“stock oculto”**.


- El usuario está definiendo a qué cantidad quiere llevar ese stock oculto (no un delta).


- El cambio quedará **registrado en el historial de movimientos de stock**.




- Incluir un **textarea obligatorio** para la **justificación del ajuste** (`reason`).

- No debe permitirse enviar el formulario si la justificación está vacía.






- Botones:

- **Cancelar** (cierra el modal sin cambios).


- **Continuar** (dispara el flujo de confirmación).






- **Diálogo de confirmación previo al envío**

- Al presionar **Continuar** en el modal:

- Mostrar un **diálogo de confirmación** (confirm modal / alert) que resuma:

- Stock oculto actual (`nstock_d1` actual).


- Nuevo valor objetivo (`amount` ingresado).


- Justificación (`reason`).




- Preguntar explícitamente al usuario si desea confirmar el ajuste.




- Botones:

- **Confirmar** → ejecuta el llamado al endpoint.


- **Cancelar** → vuelve al modal de edición sin perder los datos cargados.






- **Llamado al endpoint y manejo de respuesta**

- Al confirmar:

- Llamar a `POST {API_URL}/itemsStocks/{itemId}/manualAdjustments` con:

- `amount`: valor numérico del input.


- `reason`: texto del textarea (justificación).


- `warehouseStockId`: el depósito correspondiente al registro seleccionado en la grilla (debe enviarse según el modelo actual del listado).






- Mientras se procesa el request:

- Deshabilitar botones de confirmar para evitar dobles envíos.




- En caso de **éxito**:

- Si la respuesta indica cambio (`updated = true`):

- Mostrar un mensaje de éxito (toast / alerta) indicando que el stock oculto fue ajustado.


- Actualizar en la grilla el valor visible asociado a `nstock_d1` (si se muestra) o refrescar la fila/listado.


- Cerrar modal y diálogo de confirmación.




- Si la respuesta indica **sin cambios** (`updated = false`):

- Mostrar mensaje tipo “Sin cambios: el valor ingresado es igual al stock actual”.


- Mantener consistencia visual en la grilla (no debería cambiar nada).






- En caso de **errores**:

- **403 Forbidden**: mostrar mensaje claro (“No tiene permisos para regularizar stock.”) y no volver a ofrecer la acción si podemos inferir el permiso desde el front.


- **404 Not Found**: informar que el ítem ya no existe o no se encontró.


- **422 Unprocessable Entity**: mostrar errores de validación, por ejemplo:

- “La cantidad debe ser un entero mayor o igual a 0”.


- Faltar justificación (si por algún motivo el backend también lo valida).




- **409 / 500**: mostrar mensaje genérico de error (“No se pudo completar el ajuste de stock. Intente nuevamente o contacte a sistemas.”).
