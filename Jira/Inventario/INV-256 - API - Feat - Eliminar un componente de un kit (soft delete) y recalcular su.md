---
jira_key: "INV-256"
aliases: ["INV-256"]
summary: "API - Feat - Eliminar un componente de un kit (soft delete) y recalcular su costo"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-20 08:45"
updated: "2025-12-05 05:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-256"
---

# INV-256: API - Feat - Eliminar un componente de un kit (soft delete) y recalcular su costo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-20 08:45 |
| Actualizado | 2025-12-05 05:44 |
| Etiquetas | ninguna |
| Jira | [INV-256](https://bluinc.atlassian.net/browse/INV-256) |

## Relaciones

- **Padre:** [[INV-253]] Crear y modificar Kits
- **has action item:** [[INV-272]] APP - Feat - Configurar y actualizar componentes dentro de un kit

## Descripcion

Permitir eliminar un componente específico de un kit (vía soft delete sobre `[articulo_kits]`) y, cada vez que se elimine, **recalcular el costo promedio** del kit como suma de los costos de los componentes restantes.

### Endpoint

```
DELETE {API_URL}/itemsKits/{itemId}/{itemIdInKit}

```

### Lógica de negocio

- Validar que el registro `(itemId, itemIdInKit, softDelete = 0)` exista en `[articulo_kits]`.


- Hacer soft delete:

```
UPDATE [NewBytes_DBF].[dbo].[articulo_kits]
SET softDelete = 1
WHERE itemId      = @itemId
  AND itemIdInKit = @itemIdInKit
  AND softDelete  = 0;

```


- **Recalcular el costo del kit** igual que en el `PATCH` pero con los componentes activos restantes:

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

- Si ya no quedan componentes activos:

- Podemos dejar explícito que el costo del kit se seteé a `0` o se mantenga el último valor. Si querés, lo fijamos en esta historia (mi recomendación: setear a `0` para que sea coherente con “suma de componentes”).







### Respuesta (ejemplo OK)

```
{
  "success": true,
  "message": "Se eliminó el componente del kit y se actualizó el costo",
  "itemId": 12345,
  "itemIdInKit": 42343
}

```

### Criterios de aceptación

- Dado un componente existente en el kit, al llamar `DELETE /itemsKits/{itemId}/{itemIdInKit}`:

- El registro queda con `softDelete = 1`.


- `ncosteprom` del kit se recalcula con los componentes restantes.




- Si el componente no existe o ya está borrado (`softDelete = 1`) → `404`.


- El recalculo de costo se ejecuta siempre después del soft delete.



[adjunto]
