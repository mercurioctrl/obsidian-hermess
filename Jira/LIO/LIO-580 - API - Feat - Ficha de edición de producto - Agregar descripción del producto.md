---
jira_key: "LIO-580"
aliases: ["LIO-580"]
summary: "API - Feat - Ficha de edición de producto -> Agregar descripción del producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-25 09:12"
updated: "2026-03-30 10:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-580"
---

# LIO-580: API - Feat - Ficha de edición de producto -> Agregar descripción del producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-25 09:12 |
| Actualizado | 2026-03-30 10:57 |
| Etiquetas | ninguna |
| Jira | [LIO-580](https://bluinc.atlassian.net/browse/LIO-580) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-581]] APP - Feat - Ficha de edición de producto -> Agregar descripción del producto

## Descripcion

Como vendedor, quiero poder guardar una descripción personalizada y con formato en mi producto, para destacarlo con información adicional, imágenes y estilo propio más allá del título.

## Endpoint existente a extender

`PATCH /api/v4/inventories/products/{productId}/list`

Hoy soporta los campos `description`, `utility`, `price`, `active`, `instantFlash`. Se extiende para aceptar el nuevo campo `customDescription`, que almacena HTML arbitrario generado por un editor de texto enriquecido, solo cuando este tiene contenido.

---

## Decisión de diseño: tabla separada

El campo **no se agrega como columna en **`[CS].[dbo].[productos]`. En cambio, se crea una tabla dedicada en `[LO].[dbo]`.

**Por qué:**

- `[CS].[dbo].[productos]` es la tabla de mayor tráfico del sistema y ya tiene muchos JOINs. Agregar una columna `NVARCHAR(MAX)` la haría más pesada en operaciones que no necesitan el campo.


- SQL Server almacena `NVARCHAR(MAX)` fuera de la página de datos (LOB pages) pero igual agrega overhead en metadata por fila.


- La descripción personalizada es **contenido del vendedor**, no del catálogo base. Separar responsabilidades es coherente con el esquema existente: las tablas de vendor-content viven en `[LO].[dbo]` (ej. `productosPreguntas`, `productosRespuestas`).


- El JOIN en `findByIdComplete()` es `LEFT JOIN`, por lo que no rompe productos sin descripción.


- El listado de inventario (`listProducts`) **no necesita** este campo y no se modifica.



---

## Cambios requeridos

### 1. DB — Nueva tabla en `[LO].[dbo]`

**Archivo:** no aplica (DDL a ejecutar antes del deploy)

```
CREATE TABLE [LO].[dbo].[productos_descripcion_personalizada] (
    producto_id   INT           NOT NULL PRIMARY KEY,
    contenido     NVARCHAR(MAX) NOT NULL,
    actualizacion DATETIME      NOT NULL DEFAULT GETDATE()
);
```

> `producto_id` es PK directamente (relación 1:1 con `[CS].[dbo].[productos]`). No hace falta columna `id` autoincremental.


---

## Request de ejemplo

```
PATCH /api/v4/inventories/products/8472/list
Authorization: Bearer <token>
​
{
  "customDescription": "<h2>Características</h2><p>Este producto incluye <strong>garantía extendida</strong>.</p><img src=\"https://cdn.ejemplo.com/img/producto.jpg\" />"
}
```

Borrar la descripción existente:

```
{
  "customDescription": null
}
```

Combinado con otros campos (soportado):

```
{
  "customDescription": "<p>Mi descripción</p>",
  "active": true,
  "price": 45900
}
```

## Response esperada

```
{
  "message": "Registro actualizado",
  "status": 200,
  "success": true,
  "product": {
    "id": 8472,
    "description": "Notebook Dell Inspiron 15",
    "customDescription": "<h2>Características</h2><p>Garantía extendida incluida.</p>",
    "price": 45900,
    "active": true
  }
}
```

Cuando no hay descripción guardada, `customDescription` devuelve `null`.

---

## Tabla afectada

```
-- DDL (ejecutar antes del deploy):
CREATE TABLE [LO].[dbo].[productos_descripcion_personalizada] (
    producto_id   INT           NOT NULL PRIMARY KEY,
    contenido     NVARCHAR(MAX) NOT NULL,
    actualizacion DATETIME      NOT NULL DEFAULT GETDATE()
);
​
-- UPSERT en runtime (vía MERGE):
MERGE [LO].[dbo].[productos_descripcion_personalizada] AS target
USING (SELECT :producto_id, :contenido) AS source (producto_id, contenido)
    ON target.producto_id = source.producto_id
WHEN MATCHED THEN
    UPDATE SET contenido = source.contenido, actualizacion = GETDATE()
WHEN NOT MATCHED THEN
    INSERT (producto_id, contenido, actualizacion)
    VALUES (source.producto_id, source.contenido, GETDATE());
​
-- DELETE cuando customDescription = null:
DELETE FROM [LO].[dbo].[productos_descripcion_personalizada]
WHERE producto_id = :producto_id;
​
-- JOIN en findByIdComplete():
LEFT JOIN [LO].[dbo].[productos_descripcion_personalizada] [PDP]
    ON [PDP].producto_id = [P].id
```

---

## Criterios de aceptación

- `PATCH` con `customDescription: "<p>texto</p>"` inserta/actualiza en `[LO].[dbo].[productos_descripcion_personalizada]` y lo devuelve en el response


- `PATCH` con `customDescription: null` elimina la fila de `productos_descripcion_personalizada` (si existía)


- `PATCH` sin el campo `customDescription` no toca la tabla `productos_descripcion_personalizada`


- `customDescription` puede combinarse con `description`, `price`, `utility`, `active`, `instantFlash` en un mismo request


- Un request con **solo** `customDescription` (sin otros campos) funciona correctamente sin error "No se enviaron campos válidos"


- Si `customDescription` viene como tipo no-string y no-null (ej: número, array), devuelve 400


- Solo el vendedor dueño del producto puede actualizarlo (verificado en `findById()` antes del update)


- El campo `customDescription` aparece en el DTO devuelto tras la actualización


- `listProducts()` no se ve afectado (no hace JOIN a la nueva tabla)


- La tabla `[CS].[dbo].[productos]` no recibe ningún cambio de esquema



---

## Notas técnicas

- El `MERGE` de SQL Server es el UPSERT idiomático para este motor. Alternativa más simple si el equipo lo prefiere: `IF EXISTS (SELECT 1 ...) UPDATE ... ELSE INSERT ...`.


- `null` en el campo borra la fila entera en lugar de guardar NULL en `contenido`. Esto mantiene la tabla liviana y evita filas vacías; la ausencia de fila equivale a "sin descripción".


- El contenido HTML **no se sanitiza en el backend** en esta historia. Si en el futuro se renderiza en el sitio público con `v-html`, evaluar sanitización server-side (HTMLPurifier o similar).


- `listProducts()` y `countProducts()` **no se modifican**: el listado de inventario no necesita `customDescription` y no debe verse penalizado por el JOIN.


- El DDL debe ejecutarse en staging y producción **antes** del deploy del código. Al ser una tabla nueva (no ALTER TABLE), no hay riesgo de bloqueo sobre `productos`.


- No afecta el cache Redis existente (`item_description_{id}`, `item_specs_{id}` son para la ficha pública).
