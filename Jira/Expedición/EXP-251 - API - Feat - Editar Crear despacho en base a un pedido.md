---
jira_key: "EXP-251"
aliases: ["EXP-251"]
summary: "API - Feat - Editar / Crear despacho en base a un pedido "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-22 10:59"
updated: "2024-06-04 14:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-251"
---

# EXP-251: API - Feat - Editar / Crear despacho en base a un pedido 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-22 10:59 |
| Actualizado | 2024-06-04 14:23 |
| Etiquetas | ninguna |
| Jira | [EXP-251](https://bluinc.atlassian.net/browse/EXP-251) |

## Relaciones

- **Padre:** [[EXP-249 - Feat - Vincular despacho Editar despacho|EXP-249]] Feat - Vincular despacho / Editar despacho
- **relates to:** [[EXP-414 - BD - Actualización - Eliminar nombres de despachos incorrectos|EXP-414]] BD - Actualización - Eliminar nombres de despachos incorrectos

## Descripcion

Este recurso sirve para modificar o crear el registro en las tablas `[NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS]` y `[NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA]`. En el caso de que no existan, deben crerse, y en caso de que existan, editarse.

```
POST {API_URL}/v1/linkDispatch/{00010837} <- Numero de pedido en pedprot
```

Los parámetros que puede recibir, son los siguientes, pueden estart todos o solo algunos. En caso de no existir el registro asociado a el numero de pedido debe crearse.

```
{
"incomeDispatchId": 8968,
"providerOrder": "00010837",
"providerId": "000918",
"invoiceDate": 20230321.0,
"otherProviderId": " ",
"invoiceNumber": " ",
"type": "Importada",
"Description": "OCEAN SERVICE"
}
```

**Tablas relacionadas**

`[NewBytes_DBF].[dbo].[PedProT], [NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA]` y `[NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS]`
