---
jira_key: "EXP-66"
summary: "API - Feat - Serializar salida"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-14 12:33"
updated: "2023-01-27 12:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-66"
---

# EXP-66: API - Feat - Serializar salida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-14 12:33 |
| Actualizado | 2023-01-27 12:01 |
| Etiquetas | ninguna |
| Jira | [EXP-66](https://bluinc.atlassian.net/browse/EXP-66) |

## Descripción

```
POST {API_URL}/v1/orders/{pedido}/serials/{itemId}
```

**Carga útil**

```
[
  {
    "mode":"list", //indica el modo para la lista
    "serials": [
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
    ]
}
]
```

**Procesar la carga útil con los seriales para un item determinado, dentro de un pedido determinado.**

- Chequear si el serial esta disponible para ser utilizado


- Agregar el conjunto de seriales a la tabla de salida del pedido



---

**Chequear si el serial esta disponible para ser utilizado**

La tabla `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]` es la tabla general donde todos los seriales que ingresan a la empresa se guarda. Es donde se guarda el estado del serial, como su ubicación y otros dato relacionados al trackeo general de la mercadería.

Se necesita saber si el serial puede ser utilizado para “tomarlo” dentro de un pedido, para esto nos basaremos en el siguiente criterio.

- La fecha de egreso debe estar en `NULL`.


- El parámetro `ID_MOVIMIENTO` debe estar en la posición `1`


- El parámetro `ID_DEPOSITO` debe estar en la posición `1`


- No pude haber mas seriales, que los que al pedido le corresponden.



Si se cumplen todos esos requisitos para un serial, entonces se procesa.

**Agregar el conjunto de seriales a la tabla de salida del pedido**

Así como hay un estado general, hay un detalle que permite ver dentro de que ventas estuvo ese serial. Es decir que cada pedido crea un registro ítem por ítem para los seriales que salen.

Existen 2 tablas importantes `[NEW_BYTES].[dbo].[ST_REMITOS_VENTA_CABECERA_SALIDA]` y `[NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA]` 

Lo que se hace es crear el registro en la tabla (si ya no existe ) en `[NEW_BYTES].[dbo].[ST_REMITOS_VENTA_CABECERA_SALIDA]` y luego a medida que llegan los seriales a este recurso se guardan uno a uno en el detalle de `[NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA]`

Podría decirse que este proceso es parecido a [link](https://lioteam.atlassian.net/browse/EXP-42) pero es su contrario, ya que aca se da salida a los seriales y se gurda el detalle. Si bien la tabla utilizada, en realidad sera marcada en un paso posterior, en el despacho.
