---
jira_key: "PED-786"
aliases: ["PED-786"]
summary: "API - Refactor  - Agregar fechas al detalle de la orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-02 09:20"
updated: "2024-08-11 16:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-786"
---

# PED-786: API - Refactor  - Agregar fechas al detalle de la orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-02 09:20 |
| Actualizado | 2024-08-11 16:11 |
| Etiquetas | ninguna |
| Jira | [PED-786](https://bluinc.atlassian.net/browse/PED-786) |

## Relaciones

- **Padre:** [[PED-497 - Ver orden de compra|PED-497]] Ver orden de compra

## Descripcion

Agregaremos la fecha de la orden en el recurso 

```
GET {API_URL}/v1/orders/{branch-order}
```

Usaremos `date` para la fecha de `NewBytes_DBF.dbo.pedclit`

y  `makeSaleDate` para la fecha de procesado (liquidado) la fecha de `[NEW_BYTES].[dbo].[MS_REMITO_CABECERA]`
