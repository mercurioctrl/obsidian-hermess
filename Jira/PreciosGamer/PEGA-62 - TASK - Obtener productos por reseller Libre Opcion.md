---
jira_key: "PEGA-62"
aliases: ["PEGA-62"]
summary: "TASK - Obtener productos por reseller Libre Opcion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-07 15:24"
updated: "2024-05-31 17:37"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PEGA-62"
---

# PEGA-62: TASK - Obtener productos por reseller Libre Opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-07 15:24 |
| Actualizado | 2024-05-31 17:37 |
| Etiquetas | esperandoDependencia |
| Jira | [PEGA-62](https://bluinc.atlassian.net/browse/PEGA-62) |

## Relaciones

- **Padre:** [[PEGA-26]] API - Feat - Recoger catalogos por reseller/marketplace
- **is blocked by:** [[PEGA-80]] TASK - Obtener productos por reseller Libre Opcion - producto/precio no coincidente

## Descripcion

Basándonos en la siguiente consulta, se debe agregar a todo el procedimiento el importador para LO de modo tal que los productos puedan importarse tambien. 

Esta es una query general, pero fácilmente puede conectarse con la tabla de fotos, marcas y demás para obtener los datos faltantes.

```
SELECT 
((costo_cliente*COTIZACION) + (costo_cliente*COTIZACION)*utilidad /100) + (((costo_cliente*COTIZACION) + (costo_cliente*COTIZACION)*utilidad /100)*iva/100) AS precio_cliente_lo_pesos
FROM [CS].[dbo].[productos]
LEFT JOIN NewBytes_DBF.dbo.articulo ON CS.dbo.productos.id_interno = articulo.ID_ARTICULO
INNER JOIN NEW_BYTES.dbo.MS_COTIZACIONES ON MS_COTIZACIONES.NOMBRE = 'PESOSLO'
WHERE (productos.id = 345516)
```

Tablas complementarias

` [CS].[dbo].[productosFotos]`

`[LO].[dbo].[marcas]`
