---
jira_key: "PED-923"
aliases: ["PED-923"]
summary: "API - MVP - Refactor - Calcular ganancias con el costForSale solo cuando corresponda"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-30 08:05"
updated: "2025-04-29 12:26"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/PED-923"
---

# PED-923: API - MVP - Refactor - Calcular ganancias con el costForSale solo cuando corresponda

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-30 08:05 |
| Actualizado | 2025-04-29 12:26 |
| Etiquetas | MVPLaset |
| Jira | [PED-923](https://bluinc.atlassian.net/browse/PED-923) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido

## Descripcion

Siguiendo la linea de lo que venimos haciendo, solo cuando tengo en `[NewBytes_DBF].[dbo].[albclil].costForSale`

Intervendremos en 2 pasos puntuales, para cambiar cual es el parámetro costo que utilizaremos.

Si nos viene `costForSale`, lo usaremos en lugar del `ncosteprom` como se hizo siempre (solo en esos casos)

**1 - Registramos ganancias y otros detalles, para cada item**

```
        INSERT INTO [NEW_BYTES].[dbo].MS_REMITO_DETALLE_GANANCIA_ENLACE (
         [SUCURSAL_REMITO]
        ,[REMITO_FP]
        ,[ID_ARTICULO]
        ,[ART_DESCRIPCION]
        ,[GANANCIA_ART]
        ,[PORC_GAN]
        ,[CANTIDAD]
        ,[COSTO]
        ,[P_VENTA]
        ,[TIPO_R_NOTA]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
```

Rellenamos con los datos que ya tenemos y provienen del repositorio de detalles o del de la cabecera y calculamos la ganancia haciendo una operación como esta

iteramos el detalle del producto para obtener cada fila

```
PORC_GAN = (($producto->P_VENTA - $producto->costForSale) / $producto->costForSale) * 100;
```

**2- Registramos ganancias y otras informaciones como ya lo hicimos en la liquidación de efectivo**

```
        INSERT INTO [NEW_BYTES].[dbo].MS_ENLACE_REMITOS_GANANCIAS (
         [SUCURSAL_REMITO]
        ,[REMITO_FP]
        ,[TIPO_R_NOTA]
        ,[FECHA]
        ,[FECHA_PROCESADO]
        ,[GANANCIA]
        ,[USU_IDENTIFICACION]
        ,[COTIZACION]
        ,[SUCURSAL_FACTURACION]
        ,[revisado]
        ,[FECHA_D]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
```

iteramos el detalle del producto para obtener cada fila, pero esta vez sumamos todo para guardar la ganancia general

```
GANANCIA = $GANANCIA + (($producto->P_VENTA - $producto->costForSale) * $producto->ART_CANTIDAD);
```
