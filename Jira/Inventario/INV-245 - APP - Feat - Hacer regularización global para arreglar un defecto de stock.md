---
jira_key: "INV-245"
aliases: ["INV-245"]
summary: "APP - Feat - Hacer regularización global para arreglar un defecto de stock (globalRegularization)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-11-12 17:24"
updated: "2025-12-05 04:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-245"
---

# INV-245: APP - Feat - Hacer regularización global para arreglar un defecto de stock (globalRegularization)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-12 17:24 |
| Actualizado | 2025-12-05 04:57 |
| Etiquetas | ninguna |
| Jira | [INV-245](https://bluinc.atlassian.net/browse/INV-245) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios
- **action item from:** [[INV-243]] API - Feat - Hacer regularización global para arreglar un defecto de stock (globalRegularization)

## Descripcion

Se debe permitir ejecutar la acción de **regularización global de stock** desde el frontend, sobre un ítem y depósito específicos, utilizando el endpoint:

```
PATCH {API_URL}/itemsStocks/globalAlter
```

### Comportamiento requerido

- En el **listado de stock por ítem y depósito**, al hacer **click derecho** sobre una fila (registro de stock), debe aparecer un **menú contextual** con la opción:
**“Regularización global de stock”**.


- Al seleccionar esta opción:

- El sistema debe abrir un modal o diálogo que permita ingresar el valor de `amount` (nuevo valor de `regularizacion_global`).


- El frontend debe enviar la petición `PATCH` al endpoint `itemsStocks/globalAlter`, enviando:

- `itemId` del ítem seleccionado.


- `warehouseStockId` del depósito seleccionado.


- `amount` ingresado por el usuario.






- El frontend debe mostrar los mensajes devueltos por el backend:

- En caso de éxito, mostrar un **mensaje de confirmación** con el texto de `message` (por ejemplo: “Se realizó la regularización global”).


- En caso de error (permiso, validaciones, etc.), mostrar un **mensaje de error claro**, utilizando el contenido devuelto por el backend cuando exista.





> El usuario solo verá esta opción si tiene permiso para operar sobre el stock (según lo que defina el backend para el permiso `stocksGlobalAlter`). Si el backend devuelve error de autorización, se debe mostrarlo adecuadamente.
