---
jira_key: "INV-258"
aliases: ["INV-258"]
summary: "API - Feat - SyncUp para actualizar el stock (nstock) de kits según el stock de sus componentes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-20 09:07"
updated: "2025-12-18 07:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-258"
---

# INV-258: API - Feat - SyncUp para actualizar el stock (nstock) de kits según el stock de sus componentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-20 09:07 |
| Actualizado | 2025-12-18 07:52 |
| Etiquetas | ninguna |
| Jira | [INV-258](https://bluinc.atlassian.net/browse/INV-258) |

## Relaciones

- **Padre:** [[INV-253]] Crear y modificar Kits
- **relates to:** [[PED-1175]] API - Review - Problema con kits y duplicaciones
- **has action item:** [[INV-289]] API - Refactor - Kit con 

## Descripcion

Implementar un proceso de **syncUp periódico** (cada *X* minutos, configurable) que:

- Recorra todos los artículos marcados como kit:
`[NewBytes_DBF].[dbo].[articulo].kit = 1`


- Para cada kit y cada depósito/warehouse, calcule cuántos kits se pueden armar con el stock actual de sus componentes en:
`[NewBytes_DBF].[dbo].[stocks].nstock` donde `id_articulo = itemIdInKit`


- Actualice el `nstock` del kit (en la tabla `stocks` para el `id_articulo = itemId` del kit) con esa cantidad máxima posible.



> Un kit solo puede tener como `nstock` **el mínimo** de kits posibles que se pueden armar considerando **todos** sus componentes y sus `quantityNeeded`.


---

### Endpoint del syncUp

```
POST {API_URL}/itemsKits/syncUp

```

- Sin body o con parámetros opcionales (por ejemplo, restringir a un `stockWarehouseId` o `companyCode`).


- Este endpoint ejecuta la misma lógica que el job programado.



---

### Reglas de negocio del cálculo

Para cada **kit** `K` y cada **depósito** `D`:

- Se toman todos los componentes activos del kit:

- Desde `[articulo_kits]` donde:

- `itemId = K.itemId`


- `softDelete = 0`


- `puase = 0` *(componentes pausados no cuentan para la composición actual del kit)*






- Para cada componente `C` del kit:

- Se obtiene el stock de ese componente en el depósito `D`:

```
SELECT nstock
FROM [NewBytes_DBF].[dbo].[stocks]
WHERE id_articulo = itemIdInKit
  AND id_deposito = D

```





- Se calcula:

```
kits_posibles_por_componente = FLOOR( nstock_componente / quantityNeeded )

```



- Cantidad de kits posibles:

- Se toma el **mínimo** entre todos los componentes:

```
kitBuildableQty = MIN( kits_posibles_por_componente )

```




- Actualización de stock del kit:

- Se actualiza `[stocks].nstock` del **kit** (no de los componentes) para ese depósito:

```
UPDATE [NewBytes_DBF].[dbo].[stocks]
SET nstock = @kitBuildableQty
WHERE id_articulo = @kitItemId
  AND id_deposito = @stockWarehouseId;

```


- Si no existe registro de stock para el kit en ese depósito, se puede:

- Crear el registro con `nstock = @kitBuildableQty`, o


- Dejarlo como está según la convención actual (acláralo si ya tenés una política definida).







> En resumen: **el stock del kit es stock virtual derivado del stock de sus componentes**.


---

### Ejemplos de negocio (explícitos)

#### Ejemplo 1 – Todos quantityNeeded = 1

Kit `K` con componentes:

- `a` (quantityNeeded = 1)


- `c` (quantityNeeded = 1)


- `d` (quantityNeeded = 1)



Stock en `stocks` para un depósito:

- `a.nstock = 2`


- `c.nstock = 3`


- `d.nstock = 5`



Cálculo:

- `kits_posibles_por_a = FLOOR(2 / 1) = 2`


- `kits_posibles_por_c = FLOOR(3 / 1) = 3`


- `kits_posibles_por_d = FLOOR(5 / 1) = 5`



→ `kitBuildableQty = MIN(2, 3, 5) = 2`
→ `[stocks].nstock` del kit = **2**

#### Ejemplo 2 – Un componente requiere más de una unidad

Mismo kit `K`, pero:

- `quantityNeeded(a) = 1`


- `quantityNeeded(c) = 1`


- `quantityNeeded(d) = 5`



Stocks:

- `a.nstock = 10`


- `c.nstock = 3`


- `d.nstock = 5`



Cálculo:

- `kits_posibles_por_a = FLOOR(10 / 1) = 10`


- `kits_posibles_por_c = FLOOR(3 / 1) = 3`


- `kits_posibles_por_d = FLOOR(5 / 5) = 1`



→ `kitBuildableQty = MIN(10, 3, 1) = 1`
→ `[stocks].nstock` del kit = **1**

#### Ejemplo 3 – Falta stock en una pieza

Si cualquier componente:

- No tiene registro de stock en ese depósito
**o**


- Tiene `nstock = 0`



Entonces en el cálculo:

- `kits_posibles_por_ese_componente = 0`


- `kitBuildableQty = 0`


- `[stocks].nstock` del kit para ese depósito = **0**



---

### Criterios de aceptación

- **Actualización correcta de nstock del kit**

- Dado un kit con componentes y stocks como en los ejemplos:

- Tras ejecutar `POST /itemsKits/syncUp`, el `nstock` del kit en `[stocks]` coincide con el valor esperado (`MIN(FLOOR(nstock / quantityNeeded))`).






- **Consideración de quantityNeeded**

- Cuando un componente tiene `quantityNeeded > 1`, el cálculo usa la división entera (`FLOOR`) y limita correctamente el `nstock` del kit.




- **Caso con componente sin stock o sin registro**

- Si al menos un componente no tiene stock (0 o sin fila en `stocks` para ese depósito), el kit queda con `nstock = 0` en ese depósito.




- **Respeto a componentes pausados y softDelete**

- Componentes con `softDelete = 1` o `puase = 1` **no deben ser considerados** para el cálculo (es como si no formasen parte del kit actual).




- **Idempotencia razonable**

- Ejecutar el syncUp varias veces seguidas sin cambios de stock no debe generar inconsistencias; el `nstock` del kit se mantiene estable.
