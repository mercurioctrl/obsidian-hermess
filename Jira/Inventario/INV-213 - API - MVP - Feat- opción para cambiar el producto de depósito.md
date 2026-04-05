---
jira_key: "INV-213"
aliases: ["INV-213"]
summary: "API - MVP - Feat-  opción para cambiar el producto de depósito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-10-17 09:18"
updated: "2025-12-02 03:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-213"
---

# INV-213: API - MVP - Feat-  opción para cambiar el producto de depósito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-17 09:18 |
| Actualizado | 2025-12-02 03:28 |
| Etiquetas | ninguna |
| Jira | [INV-213](https://bluinc.atlassian.net/browse/INV-213) |

## Relaciones

- **Padre:** [[INV-211]] API - MVP - Feat- Agregar repo con pestaña de producto por depósito
- **action item from:** [[INV-214]]  APP  - MVP - Feat-  opción para cambiar el producto de depósito
- **relates to:** [[INV-259]] API - MVP - Refactor - Registro de stock -> Agregar control de stock al snapshot

## Descripcion

Se debe implementar un nuevo recurso que permita **mover stock de un depósito a otro**, dentro de una misma compañía.
El objetivo es poder realizar transferencias internas de inventario entre distintos `stockWarehouseId`, respetando las cantidades disponibles en el depósito de origen.

Solo podrá moverse una cantidad **menor o igual al stock actual** del depósito origen.
Cada transferencia deberá quedar registrada para auditoria en `[NB_WEB].[dbo].[registro_stock]`, incluyendo información de quién la realizó, fecha, motivo y los ítems involucrados.

## Entonces ¿que hacemos exactamente?

Queremos poder transferir stock de un depósito A (`fromWarehouseId`) a un depósito B (`toWarehouseId`) de forma consistente y auditable.

"Transferir" acá significa:

- Restar X unidades del depósito A


- Sumar esas mismas X unidades al depósito B


- Guardar un log perfecto de lo que pasó, que sirva después para auditoría / reclamos / diferencias de inventario



Y todo esto tiene que ser atómico, o sea: o pasa todo junto, o no pasa nada. No queremos que reste pero no sume, ni que loguee solo la mitad.

---

## 2. De dónde sale el stock disponible

El stock físico que tiene cada warehouse está registrado en la tabla:

```
[NewBytes_DBF].[dbo].[stocks]
```

En esa tabla, para cada `itemId` y cada `warehouseId`, existe un campo:

```
[NewBytes_DBF].[dbo].[stocks].nstock
```

Ese `nstock` es “cuántas unidades de este item tengo en este depósito”.

Ejemplo mental:

- itemId = 123836


- warehouseId = 2 (SAFcom)


- nstock = 42



Eso significa: “Tengo 42 unidades del item 123836 en el depósito 2”.

Entonces: ese `nstock` es la fuente de verdad que usamos para validar y actualizar.

---

## 3. Paso previo: validación

Antes de mover stock, hacemos esto:

- Buscamos la fila origen
`[NewBytes_DBF].[dbo].[stocks]`
con `itemId = X` y `warehouseId = fromWarehouseId`.


- Leemos `nstock_origen_actual`.


- Comparamos:

- si `nstock_origen_actual` >= `quantity_a_mover` → OK


- si no, rechazamos (no hay stock suficiente en ese depósito).





Esto evita que alguien pida mover 10 cuando en ese depósito hay 3.

⚠ Importante: esta validación y la actualización van a ir dentro de la misma transacción del lado SQL Server para evitar condiciones de carrera (dos usuarios moviendo stock del mismo depósito al mismo tiempo).

---

## 4. Actualización de stock (si validó)

Si hay stock suficiente, hacemos dos updates en la misma transacción:

### 4.1. Restar en el depósito origen

```
UPDATE [NewBytes_DBF].[dbo].[stocks]
SET nstock = nstock - @cantidad
WHERE itemId = @itemId
  AND warehouseId = @fromWarehouseId;

```

### 4.2. Sumar en el depósito destino

```
UPDATE [NewBytes_DBF].[dbo].[stocks]
SET nstock = nstock + @cantidad
WHERE itemId = @itemId
  AND warehouseId = @toWarehouseId;

```

Detalles importantes:

- Esto se hace bajo `BEGIN TRANSACTION ... COMMIT` para que sea atómico.


- Si algo falla en el medio (por ejemplo no pudimos insertar en el log), hacemos `ROLLBACK` y no se mueve nada.


- Se puede usar `WITH (ROWLOCK, UPDLOCK)` o equivalente para evitar que otro proceso te meta la mano mientras estás leyendo/restando/sumando.  



Nadie más puede venir al mismo tiempo a descontar el mismo stock y generarte -3 unidades fantasma.

## 5. Guardar registros para auditoría en `[NB_WEB].[dbo].[registro_stock]`

Como regla: **cada vez que tocamos stock en el sistema, lo registramos en **`registro_stock`.

### 5.1. Nuevo campo en `registro_stock`

Vamos a agregar una columna nueva:

```
[NB_WEB].[dbo].[registro_stock].warehouseId
```

(o `warehouseIdo` como lo nombraste que me habías mencionado que usabas según el conjunto de tablas).

Inicializaremos por única vez todos los registros en 2 (como hacemos para NB) cuando vamos agregando este parámetro a las distintas tablas

---

### 5.2. ¿Qué vamos a guardar en el log?

Por **cada transferencia de stock**, vamos a generar **dos registros** en `[NB_WEB].[dbo].[registro_stock]`:

- Un registro para el depósito ORIGEN (el que pierde stock)


- Un registro para el depósito DESTINO (el que gana stock)



Esto es clave porque nos deja leer el historial por depósito y ver entradas/salidas.

#### Registro para ORIGEN:

- `warehouseId` = depósito origen


- `itemId`


- `cantidad` NEGATIVA (ej: `-10`)


- `sAnterior` = stock en ese depósito ANTES de aplicar el movimiento


- `sPosterior` = stock en ese depósito DESPUÉS del movimiento


- `agente` = usuario / proceso que ejecutó


- `justificacion` = reason que mandaron desde el front


- Snapshot de todos los otros campos de stock al momento del cambio:

- `[nstock_lo]`


- `[nstock]`


- `[nstock_en_cola]`


- `[nstock_d1]`


- `[nstock_reserva_pedidos]`


- `[nstock_lo_reserva_pedidos]`


- `[nstock_postventa]`





Esos campos son como una foto del estado completo del stock y sus reservas cuando se hizo el movimiento. Sirve para peritaje después (“¿quién se llevó mis 10 unidades?”).

#### Registro para DESTINO:

Exactamente lo mismo pero:

- `warehouseId` = depósito destino


- `cantidad` POSITIVA (ej: `+10`)


- `sAnterior` = stock que ese depósito tenía antes de sumar


- `sPosterior` = stock después de sumar



Con esto, cuando mirás el log:

- ves que en depósito 2 salió -10


- ves que en depósito 5 entró +10


- y podés reconstruir cualquier ajuste.



---

### 5.3. Orden correcto de las operaciones dentro de la transacción

El orden dentro del backend debería ser así (todo o nada):

- `BEGIN TRANSACTION`


- Leer `nstock` actual del origen → `sAnterior_origen`


- Validar que `sAnterior_origen >= cantidad`


- Calcular `sPosterior_origen = sAnterior_origen - cantidad`


- Hacer UPDATE restando en origen


- Leer `nstock` actual del destino → `sAnterior_destino`


- Calcular `sPosterior_destino = sAnterior_destino + cantidad`


- Hacer UPDATE sumando en destino


- INSERT registro_stock (origen) con cantidad negativa y sAnterior/sPosterior del origen


- INSERT registro_stock (destino) con cantidad positiva y sAnterior/sPosterior del destino


- COMMIT



Si en cualquier paso del 2 al 10 falla → `ROLLBACK`.
Sin COMMIT, no se mueve nada.

Esto garantiza consistencia entre:

- lo que quedó en stocks


- lo que dice el log


- lo que le vamos a devolver a la API



---

```
POST {API_URL}/v1/stock-transfers
```

**Payload**

```
{
  "fromWarehouseId": 2,
  "toWarehouseId": 5,
  "reason": "Reorganización de stock después del inventario",
  "items": [
    {
      "itemId": 123836,
      "quantity": 10
    },
    {
      "itemId": 987654,
      "quantity": 3
    }
  ]
}
```

**Validaciones:**

- `fromWarehouseId` y `toWarehouseId` deben existir, ser distintos y de la misma `companyCode`


- No puede transferirse más cantidad que el `[NewBytes_DBF].[dbo].[stocks].nstock` disponible en el depósito origen.


- Los `itemId` deben pertenecer a la `companyCode` de ambos depósitos.



**Devuelve**

```
{
  "success": true,
  "message": "Se movio entre depositos de manera satisfactoria",
  "data": {
    "transferId": 8451,
    "fromWarehouseId": 2,
    "toWarehouseId": 5,
    "reason": "Reorganización de stock después del inventario",
    "createdAt": "2025-10-29T14:22:18Z",
    "items": [
      {
        "itemId": 123836,
        "quantity": 10,
        "status": "moved"
      },
      {
        "itemId": 987654,
        "quantity": 3,
        "status": "moved"
      }
    ]
  }
}
```

### **Criterios de aceptación**

- ✅ Se puede crear una transferencia entre dos depósitos distintos.


- ✅ No se permite mover más unidades que las disponibles en el depósito origen en `[NewBytes_DBF].[dbo].[stocks].nstock`.


- ✅ Se registra correctamente el movimiento con sus líneas e ítems asociados.


- ✅ El stock se descuenta del depósito origen y se suma al depósito destino.


- ✅ La API devuelve la estructura estándar (`success`, `message`, `data`).


- ✅ Los intentos inválidos (stock insuficiente, depósito inexistente, etc.) devuelven error con detalle del motivo.


- ✅ Se registra fecha y usuario que ejecutó la transferencia y lo demás en `[NB_WEB].[dbo].[registro_stock]`
