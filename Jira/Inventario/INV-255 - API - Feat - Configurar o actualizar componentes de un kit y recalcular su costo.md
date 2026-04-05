---
jira_key: "INV-255"
aliases: ["INV-255"]
summary: "API - Feat - Configurar o actualizar componentes de un kit y recalcular su costo"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-20 08:42"
updated: "2025-12-05 05:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-255"
---

# INV-255: API - Feat - Configurar o actualizar componentes de un kit y recalcular su costo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-20 08:42 |
| Actualizado | 2025-12-05 05:43 |
| Etiquetas | ninguna |
| Jira | [INV-255](https://bluinc.atlassian.net/browse/INV-255) |

## Relaciones

- **Padre:** [[INV-253 - Crear y modificar Kits|INV-253]] Crear y modificar Kits
- **has action item:** [[INV-272 - APP - Feat - Configurar y actualizar componentes dentro de un kit|INV-272]] APP - Feat - Configurar y actualizar componentes dentro de un kit

## Descripcion

Permitir **agregar o actualizar** la relación entre un kit (`itemId`) y uno de sus componentes (`itemIdInKit`), guardando la cantidad necesaria por unidad de kit y si el componente está pausado.

Cada vez que se modifica esta relación, se debe recalcular el costo promedio (`[articulo].ncosteprom`) del kit como la **suma de los costos promedio de todos los componentes multiplicados por sus cantidades**.

### Endpoint

```
PATCH {API_URL}/itemsKits/{itemId}

```

> `itemId` = artículo padre que es el kit.


### Payload (ejemplo)

```
{
  "itemIdInKit": 42343,
  "quantityNeeded": 2,
  "paused": false
}

```

### Tablas involucradas

- Kit y componentes:

- `[NewBytes_DBF].[dbo].[articulo]`




- Relación kit ↔ componentes:

- `[NewBytes_DBF].[dbo].[articulo_kits]` con columnas:

- `itemId`


- `itemIdInKit`


- `quantityNeeded`


- `puase` 


- `createDate`


- `userIdCreator`


- `softDelete`







### Lógica de negocio

- Validar que:

- `itemId` exista y tenga `kit = 1`.


- `itemIdInKit` exista y tenga `kit=0`.


- `itemId != itemIdInKit` (no se puede incluirse a sí mismo).


- `quantityNeeded > 0`.




- Insertar o actualizar la relación en `[articulo_kits]`:

- **Si no existe** `(itemId, itemIdInKit, softDelete = 0)` → `INSERT`.


- **Si ya existe** `(itemId, itemIdInKit, softDelete = 0)` → `UPDATE`.



Ejemplo:

```
IF NOT EXISTS (
    SELECT 1
    FROM [NewBytes_DBF].[dbo].[articulo_kits]
    WHERE itemId = @itemId
      AND itemIdInKit = @itemIdInKit
      AND softDelete = 0
)
BEGIN
    INSERT INTO [NewBytes_DBF].[dbo].[articulo_kits] (
        itemId, itemIdInKit, quantityNeeded, puase, createDate, userIdCreator, softDelete
    ) VALUES (
        @itemId, @itemIdInKit, @quantityNeeded, @paused, GETDATE(), @userId, 0
    );
END
ELSE
BEGIN
    UPDATE [NewBytes_DBF].[dbo].[articulo_kits]
    SET quantityNeeded = @quantityNeeded,
        puase          = @paused
    WHERE itemId        = @itemId
      AND itemIdInKit   = @itemIdInKit
      AND softDelete    = 0;
END
```



- **Recalcular el costo del kit** (`[articulo].ncosteprom`):

Después de insertar/actualizar, recalcular:

```
UPDATE A
SET A.ncosteprom = C.totalCost
FROM [NewBytes_DBF].[dbo].[articulo] A
CROSS APPLY (
    SELECT SUM(K.quantityNeeded * H.ncosteprom) AS totalCost
    FROM [NewBytes_DBF].[dbo].[articulo_kits] K
    INNER JOIN [NewBytes_DBF].[dbo].[articulo] H
        ON H.itemId = K.itemIdInKit
    WHERE K.itemId     = A.itemId
      AND K.softDelete = 0
      AND A.itemId     = @itemId
) C
WHERE A.itemId = @itemId;

```

Regla de negocio:

- El costo del kit siempre será la **suma de los costos promedio actuales de todos sus componentes** multiplicados por `quantityNeeded`.


- Cualquier cambio en la configuración de componentes dispara este recalculo.





### Respuesta (ejemplo OK)

```
{
  "success": true,
  "message": "Se configuró el componente del kit y se actualizó el costo",
  "itemId": 12345,
  "component": {
    "itemIdInKit": 42343,
    "quantityNeeded": 2,
    "paused": false
  }
}

```

### Criterios de aceptación

- Dado un `itemId` kit existente, al llamar `PATCH /itemsKits/{itemId}` con un payload válido:

- Se crea/actualiza el registro correspondiente en `[articulo_kits]`.


- `ncosteprom` del kit queda igual a la suma de `quantityNeeded * ncosteprom` de todos sus componentes activos (`softDelete = 0`).




- Si `itemId` no existe o no es kit → `404`.


- Si `itemIdInKit` no existe → `404`.


- Si `quantityNeeded <= 0` → `400`.


- Si `itemId = itemIdInKit` → `400` o `409` (regla de no auto-contenencia).


- Si el kit no tiene componentes activos (caso límite) y aun así se llama al recalculo:

- Se define que el recalculo devuelva `0` o se mantiene el valor anterior (aclarar en implementación; si querés lo fijamos explícito en otra iteración).





[adjunto]
