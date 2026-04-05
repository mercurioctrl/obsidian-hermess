---
jira_key: "EXP-303"
aliases: ["EXP-303"]
summary: "API - Feat - Mover seriales seleccionados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-31 06:05"
updated: "2023-06-21 07:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-303"
---

# EXP-303: API - Feat - Mover seriales seleccionados

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
| Jira | [EXP-303](https://bluinc.atlassian.net/browse/EXP-303) |

## Relaciones

- **Padre:** [[EXP-301]] Feat - Mover seriales
- **blocks:** [[EXP-304]] APP - Feat - Modal "Mover Seriales"

## Descripcion

Con este recurso, moveremos los seriales que seleccionamos previamente, para esto es necesario tener un pedido de destino y los seriales, a través del modal [link](https://lioteam.atlassian.net/browse/EXP-304) 

```
POST {{API_URL}}/v1/moveSerials 
```

```
{
"destinyProviderId": 19384
"serials": [
  "F18S4W3",
  "F18S4W4",
  "F18S4W5"
  ]
}
```

Antes de procesarlo verificamos que cada uno

- No tiene `FECHA_INGRESO` en la tabla 


- `ID_MOVIMIENTO = 1`  en la tabla `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`


- `ID_DEPOSITO =1`  en la tabla `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`


- El `destinyProviderId` debe contener el articulo especifico tambien. (Ej: Si el serial `F18S4W3`, pertenece al `itemId` 32434, entonces en `destinyProviderId` debe estar el `itemId` 32434 tambien, caso contrario, informar falla)



Y de darse todas estos criterios, lo movemos para el pedido de destino haciendo el update en `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`

Esta acción se encuentra restringida por le mismo permiso que te deja cargar o no seriales según el usuario.

Como ya hemos hecho antes, se deben mostrar diferenciados aquellos que pudieron moverse y los que no.
