---
jira_key: "PED-631"
aliases: ["PED-631"]
summary: "API - SynUp - Guardar log de precios y enviar correo con las diferencias"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-22 09:03"
updated: "2024-04-16 12:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-631"
---

# PED-631: API - SynUp - Guardar log de precios y enviar correo con las diferencias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-22 09:03 |
| Actualizado | 2024-04-16 12:11 |
| Etiquetas | ninguna |
| Jira | [PED-631](https://bluinc.atlassian.net/browse/PED-631) |

## Relaciones

- **Padre:** [[PED-629]] API - Feat - Historial de cambios de precio por escucha 
- **is blocked by:** [[PED-660]] API - SynUp - Guardar log de precios y enviar correo con las diferencias - Tabla excede los límites del fondo

## Descripcion

o que haremos aca es llenar la tabla  `[NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS_LOG]`, pero solo con aquellos items donde uno de los parametros sea diferente al ultimo registro de ese item. Lo que se busca es poder capturar aquellos que cambiaron, ya sea una de sus utilidades o precios y generar un registro que documente ese cambio ingresando una nueva fila en `[NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS_LOG]`



Para esto evaluaremos el valor actual de las columnas

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
```

y lo compararemos con el ultimo registro que tenemos, en caso de que hubieran cambiado, crearemos un nuevo registro cambiando el valor que cambio, o los valores que cambizaron desde sus valores actuales en `[NEW_BYTES].[dbo].[ST_GANANCIA_ESTIPULADA_ARTICULOS]`  y `[NewBytes_DBF].[dbo].articulos` a nuestra tabla de log.

Adicionalmente iremos almacenando la secuencia de aquellos que cambiaron para al final de la tarea enviar un correo que contenga una tabla con una fila por cada uno de los cambios y que en la columna se vean los 17 valores que capturamos con el asunto “Ultimos cambios de precios”

Adicionalmente esta tabla solo registra los utlimos 10 dias de cambios,por lo que en cada proceso hay que finalizar expirando (haard delete) todos los registros que se crearon y son mas viejos de 10 dias.



solo sobre id_deposito =1
