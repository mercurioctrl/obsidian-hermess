---
jira_key: "PED-127"
aliases: ["PED-127"]
summary: "API - Refactor - Listar ordenes de compra -> Agregar cotizacion y percepciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-06 17:00"
updated: "2023-10-09 09:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-127"
---

# PED-127: API - Refactor - Listar ordenes de compra -> Agregar cotizacion y percepciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-06 17:00 |
| Actualizado | 2023-10-09 09:35 |
| Etiquetas | ninguna |
| Jira | [PED-127](https://bluinc.atlassian.net/browse/PED-127) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-125]] APP - Feat - Modal de liquidacion

## Descripcion

Agregaremos en el objeto 

```
{API_URL}/v1/orders
```

```
[
    {
        "date": "2023-05-22 09:33:56",
        "orderNumber": "10314626",
        "branchNumber": "0010",
        "albumNumber": "X001000021371",
        "realAlbumNumber": "00021371",
        "clientDescription": "MERCURIO CATRIEL EDUARDO",
        "clientID": 26806,
        "observation": "INTERNO",
        "status": "s",
        "invoice": "B000400038173",
        "token": "25d899a4e9d147f1ace0ab982d4e9b",
        "voucherId": 502911,
        "seller": "Sin dendedor",
        "totalInPesos": 198044,
        "finalTotalInPesos": 198044,
        "total": 643,
        "finalTotal": 643,
        "percepction": 3.52, <- Se agrega, si no esta disponible viene en cero
        "currency": 211.0 <- Se agrega, si no esta disponible viene en cero
    }
  ...
```



**Sobre el parámetro** `percepction`

Este parametro es un monto nominal en dolares (no es un porcentaje), y lo que haremos sera tomarlo de `[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].IMPPERCEP` si existe . En caso de que no exista en `[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].IMPPERCEP`, lo tomaremos de `[NewBytes_DBF].[dbo].[clientes].percepcion` (esto si es un porcentaje, por lo que debemos hacer el calculo del monto con el total del pedido sin iva).

En caso de que no estén ninguno d  los dos entonces tendremos que devolver el parámetro en cero.

**Sobre el parámetro** `currency`

Este parámetro es la cotización del dolar. Tomaremos la cotización del pedido en caso de estar disponible (`[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].COTIZACION`) y si no esta disponible tomaremos la cotización del día.
