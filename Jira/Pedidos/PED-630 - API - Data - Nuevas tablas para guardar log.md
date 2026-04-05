---
jira_key: "PED-630"
aliases: ["PED-630"]
summary: "API - Data - Nuevas tablas para guardar log"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-22 09:00"
updated: "2024-04-02 19:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-630"
---

# PED-630: API - Data - Nuevas tablas para guardar log

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-22 09:00 |
| Actualizado | 2024-04-02 19:03 |
| Etiquetas | ninguna |
| Jira | [PED-630](https://bluinc.atlassian.net/browse/PED-630) |

## Relaciones

- **Padre:** [[PED-629]] API - Feat - Historial de cambios de precio por escucha 

## Descripcion

Crearemos una nueva tabla llamada  `[NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS_LOG]` con las siguientes columnas

```
[PORC_GANAN_ESTIP]
[PORC_GANAN_ESTIP2]
[PORC_GANAN_ESTIP3]
[PORC_GANAN_ESTIP4]
[PORC_GANAN_ESTIP5]
[PORC_GANAN_ESTIP6]
[PORC_GANAN_ESTIP7]
[PORC_GANAN_ESTIP8]            
[PORC_GANAN_ESTIPLO]
[PORC_GANAN_ESTIPLO1]
[PORC_GANAN_ESTIPCF]
ncosteprom
npvp1
npvp2
npvp3
npvp4
npvp5
cref
id_articulo
date (getdate)
id (autonum)
```

Estas columnas provienen de `[NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS]` y `[NewBytes_DBF].[dbo].articulos` , salvo “Date” e “id” 

Adicionalmente se agregaron [PORC_GANAN_ESTIP5], [PORC_GANAN_ESTIP6],[PORC_GANAN_ESTIP7],[PORC_GANAN_ESTIP8] a la tabla [NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS]
