---
jira_key: "COB-192"
aliases: ["COB-192"]
summary: "API - Research - Buscar si existen tablas de movimientos de banco"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-10-21 10:03"
updated: "2022-10-27 08:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-192"
---

# COB-192: API - Research - Buscar si existen tablas de movimientos de banco

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-21 10:03 |
| Actualizado | 2022-10-27 08:38 |
| Etiquetas | ninguna |
| Jira | [COB-192](https://bluinc.atlassian.net/browse/COB-192) |

## Relaciones

- **Padre:** [[COB-178]] API - Feat - Realizar transferencia entre bancos

## Descripcion

Tablas que registran los movimientos de todos los bancos.

`NEW_BYTES.dbo.BA_BP_MOVIMIENTOS_SALIDAS`

`NEW_BYTES.dbo.BA_BP_MOVIMIENTOS_ENTRADAS`



La operacion entre todas las entradas y todas las salidas del dia da como resultado el total que existe en el banco.

`[NEW_BYTES].[dbo].[MC_SALDOS_BANCOS]`



Tablas Extras complementarias.:

`BA_BP_TIPOS_OPERACIONES_SALIDAS`

`BA_BP_TIPOS_OPERACIONES_ENTRADAS`

`BA_BP_ORIGENES_ENTRADAS`

`BA_BP_DESTINOS_SALIDAS`
