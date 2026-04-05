---
jira_key: "LIO-577"
aliases: ["LIO-577"]
summary: "APP/API - Feat - Ficha de edición de producto"
status: "Ready for QA"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-19 12:38"
updated: "2026-03-27 10:43"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/LIO-577"
---

# LIO-577: APP/API - Feat - Ficha de edición de producto

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-19 12:38 |
| Actualizado | 2026-03-27 10:43 |
| Etiquetas | esperandoDependencia |
| Jira | [LIO-577](https://bluinc.atlassian.net/browse/LIO-577) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **is cloned by:** [[LIO-583]] APP/API - Review - Ficha de edición de producto -> Observaciones en el breadcrumb y cambio de utilidad

## Descripcion

Se debe poder abrir una ficha completa de cada producto desde mi inventario, para editar todos sus atributos en un mismo lugar y guardarlos con un solo botón.

---

## Contexto

La tabla de inventario (`ProductoTienda.vue`) ya tiene edición inline de `price` y `utility`, y hay historias implementadas (o en camino) para `active`, `instantFlash`, `hide` y `description`. Esta historia unifica todos esos campos en una **ficha de edición**, y agrega secciones de galería de imágenes y descripción larga que serán solo maqueta por ahora (sin llamada a backend hasta que esté listo el recurso).

**Endpoints ya disponibles (todos via **`PATCH /v4/inventories/products/{id}/list`**):**

| Campo | Body |
| --- | --- |
| Precio | `{ "price": 34900 }` |
| Utilidad | `{ "utility": 30.5 }` |
| Activo | `{ "active": true \| false }` |
| Instant Flash | `{ "instantFlash": true \| false }` |
| Visible | `{ "hide": 0 \| 1 }` |
| Título | `{ "description": "Nuevo título" }` |

Todos los campos modificados se pueden enviar en un único PATCH (el endpoint ya lo soporta). La ficha acumula los cambios localmente y los envía todos juntos al presionar "Guardar".

**Endpoints pendientes (lo haremos en el proximo paso cuando estos parametros ya funcionen):**

- Galería de imágenes — recurso de backend a definir


- Descripción larga del producto — recurso de backend a definir



---

## UX / Flujo de navegación

### Cómo se abre la ficha

La ficha se abre desde el **menú de 3 puntos** (kebab menu) de cada fila en la tabla de inventario. Al hacer clic en los 3 puntos, aparece un menú con opciones, una de las cuales es "Editar ficha". Al seleccionarla, la vista del catálogo reemplaza la tabla con la ficha del producto seleccionado (no es un modal overlay — es un cambio de vista dentro de la misma página).

### Navegación dentro de la ficha

En la parte superior de la ficha se muestra:

- **Breadcrumb:** `Productos > [Nombre del producto]`

- "Productos" es un link que vuelve al listado


- El nombre del producto es el ítem activo (no clickeable)




- **Botón "← Volver"** al lado izquierdo del breadcrumb, que también vuelve al listado



### Guardar y descartar

Al pie de la ficha (o en el header junto al breadcrumb) hay dos botones:

- **Guardar:** envía un único PATCH con todos los campos modificados. Si hay errores, muestra toast y permanece en la ficha.


- **Descartar cambios:** abre un `PopConfirm` preguntando "¿Estás seguro que deseas descartar los cambios?". Si el usuario confirma, vuelve al listado sin guardar. Si cancela, permanece en la ficha con los cambios intactos.



> Si no hubo ningún cambio (el usuario abrió la ficha y no modificó nada), el botón "Descartar cambios" vuelve directamente al listado sin mostrar el PopConfirm.


---

## Criterios de aceptación

### Acceso a la ficha

- Cada fila del inventario muestra un menú de 3 puntos


- Al hacer clic en los 3 puntos aparece un dropdown con la opción "Editar ficha"


- Al seleccionar "Editar ficha", la tabla se reemplaza por la vista de ficha del producto


- El menú se cierra al hacer clic fuera de él



### Navegación

- La ficha muestra el breadcrumb `Productos > [Nombre del producto]`


- El botón "← Volver" y el link "Productos" en el breadcrumb tienen el mismo comportamiento


- Al volver, la lista retoma el estado previo (filtros, scroll, paginación)



### Guardar

- El botón "Guardar" está deshabilitado si no hubo ningún cambio


- Al guardar, se envía un único PATCH solo con los campos modificados


- Al guardar con éxito, muestra toast de éxito y vuelve a la lista


- La fila en la lista refleja los datos actualizados tras guardar


- Al guardar con error, muestra toast de error y permanece en la ficha


- No se permite guardar si el precio es menor al costo



### Descartar cambios

- Si no hubo cambios, "Descartar cambios" vuelve al listado directamente


- Si hubo cambios, "Descartar cambios" abre el PopConfirm de confirmación


- Al confirmar en el PopConfirm, vuelve al listado sin guardar


- Al cancelar el PopConfirm, permanece en la ficha con los cambios intactos


- El mismo comportamiento aplica al botón "← Volver" y al link del breadcrumb



### Campos

- Los toggles (Activo, Instant Flash, Visible) reflejan el estado actual al abrir la ficha


- Al editar el precio, la utilidad y la ganancia se recalculan en tiempo real


- Las secciones "Imágenes" y "Descripción" se muestran con badge "Próximamente" y campos deshabilitados


- Ningún campo de las secciones maqueta realiza llamadas a la API
