---
jira_key: "EXP-527"
aliases: ["EXP-527"]
summary: "API - Refactor - Extender informacion para el recurso de envios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-02-02 09:53"
updated: "2026-02-12 13:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-527"
---

# EXP-527: API - Refactor - Extender informacion para el recurso de envios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-02 09:53 |
| Actualizado | 2026-02-12 13:59 |
| Etiquetas | ninguna |
| Jira | [EXP-527](https://bluinc.atlassian.net/browse/EXP-527) |

## Relaciones

- **Padre:** [[EXP-13 - Feat - Etiquetas y seguimiento|EXP-13]] Feat - Etiquetas y seguimiento
- **action item from:** [[EXP-457 - API - Feat - Agregar un recurso para traer informacion completa y|EXP-457]] API - Feat - Agregar un recurso para traer informacion completa y complementaria de lo referido al envio (para evaluar datos de cotizacion y posteriormente de armado)
- **has action item:** [[EXP-528 - APP - Feat - Extender informacion del envio y como se confecciona el paquete|EXP-528]] APP - Feat - Extender informacion del envio y como se confecciona el paquete

## Descripcion

Con la idea de allanar el camino para que sepan cuando algo esta mal, y puedan a su vez auto gestionarse la solución, empezaremos a mostrar informacion sobre como están conformados los bultos y medidas de los items en base a la cual se calcula la paqueteria. 

Una posible forma de hacer esto, es agregar una extensión (`extended`) al recurso 

```
GET /v1/shipments/{branch-order}/details?zipCode={zipCode}&extended={true/false}
```

Y cuando es así, agregaremos al objeto 

Para poder hacer esto podremos configurar una query o consulta que nos muestre cantidad de bultos y medidas tomadas en cuenta para la paqueteria (debe estar claro si tomo informacion del producto o la categoria) en una linea similar a la query que vimos la semana pasada

```
SELECT
    x.cRef,
    x.cdetalle,
    x.packagePerUnit_articulo,
    x.packagePerUnit_familia,
    x.ncanped,
    x.cantidad_en_unidades,
    SUM(x.cantidad_en_unidades) OVER () AS total_cantidad_en_unidades
FROM (
    SELECT
        a.cRef,
        a.cdetalle,
        a.packagePerUnit AS packagePerUnit_articulo,
        b.packagePerUnit AS packagePerUnit_familia,
        d.ncanped,
        d.ncanped * COALESCE(a.packagePerUnit, b.packagePerUnit) AS cantidad_en_unidades
    FROM [NewBytes_DBF].[dbo].[articulo] a
    LEFT JOIN [NewBytes_DBF].[dbo].[familias] b
        ON b.ID_FAMILIA = a.ID_FAMILIA
    LEFT JOIN [NewBytes_DBF].[dbo].[pedclil] d
        ON d.cref = a.cRef
    WHERE
        d.cnumped = '10447287'
        AND d.cnumsuc = '0002'
        AND a.cRef <> 102048
) x;

```

La idea final es ver en el área, un accionable “mas informacion” que nos permita acceder a toda esta informacion y con un enlace de front, ir a completarla cuando haga falta

[adjunto]
