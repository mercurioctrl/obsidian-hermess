---
jira_key: "EXP-250"
aliases: ["EXP-250"]
summary: "API - Feat - Leer informacion del despacho"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-22 10:59"
updated: "2023-04-17 09:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-250"
---

# EXP-250: API - Feat - Leer informacion del despacho

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-22 10:59 |
| Actualizado | 2023-04-17 09:45 |
| Etiquetas | ninguna |
| Jira | [EXP-250](https://bluinc.atlassian.net/browse/EXP-250) |

## Relaciones

- **Padre:** [[EXP-249 - Feat - Vincular despacho Editar despacho|EXP-249]] Feat - Vincular despacho / Editar despacho

## Descripcion

Este recurso sirve para obtener informacion del despacho (que puede existir o no, vinculada a un pedido o ingreso de mercaedera)

```
GET {API_URL}/v1/linkDispatch/{00010837} <- Numero de pedido en pedprot
```

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
