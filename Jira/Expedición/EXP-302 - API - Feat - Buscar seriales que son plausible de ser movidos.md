---
jira_key: "EXP-302"
aliases: ["EXP-302"]
summary: "API - Feat - Buscar seriales que son plausible de ser movidos "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-31 06:05"
updated: "2023-06-21 07:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-302"
---

# EXP-302: API - Feat - Buscar seriales que son plausible de ser movidos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-31 06:05 |
| Actualizado | 2023-06-21 07:12 |
| Etiquetas | ninguna |
| Jira | [EXP-302](https://bluinc.atlassian.net/browse/EXP-302) |

## Relaciones

- **Padre:** [[EXP-301 - Feat - Mover seriales|EXP-301]] Feat - Mover seriales
- **blocks:** [[EXP-304 - APP - Feat - Modal Mover Seriales|EXP-304]] APP - Feat - Modal "Mover Seriales"

## Descripcion

Crearemos un recurso para ubicar y seleccionar aquellos seriales que pueden ser movidos.

**¿cuales son los seriales que aun pueden moverse?**

- No tiene `FECHA_INGRESO` en la tabla `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`


- `ID_MOVIMIENTO = 1`  en la tabla `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`


- `ID_DEPOSITO =1`  en la tabla `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`



Solo debo ver aquellos que cumplan con estas condiciones, ademas de los filtros que yo le pase. Jamas debo ver uno que ya fue tomado en otro pedido.

  

Con esos criterios mostraremos los seriales buscados con el recurso

```
GET {{API_URL}}/v1/moveSerials?search={stringSearch}&itemId={intItemId}&orphan=true
```

```
[
{
    "serial": "F18S4W3",
    "admissionDate": "19\/05\/2023",
    "providerOrder": 234523
},
{
    "serial": "F18S4W3",
    "admissionDate": "19\/05\/2023",
    "providerOrder": 234523
}
]
```

Se deben mostrar listados, paginando de 100 en 100 en un principio (aunque esto puede cambiarlo el front).

Los filtros

`{stringSearch}` → Se trata de un string de busqueda que es reactivo al serial, y al nombre del producto

`itemId` → es el id del producto de manera especifica

`orphan` → Cuando esta en true, me devuelve aquellos que fueron cargados en un numero de pedido que ya no existe mas (relacionando ID_COMPRA, esto ya lo vimos antes y es medio confuso porque están mal nombradas las columnas, avísame cualquier cosa)
