---
jira_key: "PED-507"
aliases: ["PED-507"]
summary: "API - Refactor - Al liquidar, guardaremos la cotizacion blue, ademas de la oficial (como ya venimos haciendo)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-19 10:18"
updated: "2024-01-26 03:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-507"
---

# PED-507: API - Refactor - Al liquidar, guardaremos la cotizacion blue, ademas de la oficial (como ya venimos haciendo)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-19 10:18 |
| Actualizado | 2024-01-26 03:42 |
| Etiquetas | ninguna |
| Jira | [PED-507](https://bluinc.atlassian.net/browse/PED-507) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido

## Descripcion

Actualmente solo guardamos

`[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].[COTIZACION]`, crearemos una nueva columna en la misma tabla llamada

`[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].[COTIZACION_BLUE]` y ahi guardaremos el valor que se obtiene igual que la cotizacion oficial, pero blue

```
SELECT TOP (1000) [NOMBRE]
      ,[COTIZACION]
      ,[COTIZACION_MAXIMA]
      ,[FECMODIF]
      ,[USUARIO]
      ,[COTIZACION_MINIMA_PESOS]
      ,[COTIZACION_MINIMA_CHEQUE]
      ,[IDFORMAPAGO]
      ,[id]
  FROM [NEW_BYTES].[dbo].[MS_COTIZACIONES] where id =5
```

De esta forma tendremos ambas y podremos hacer calculo estadistico de la brecha cambiara respecto a cada venta.
