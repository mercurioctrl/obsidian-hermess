# Relación entre articulo / stocks y las tablas de líneas

## articulo — maestro de productos

Columnas clave para las relaciones:
- ID_ARTICULO (int, PK) — identificador numérico interno, FK en todas las tablas de líneas
- cRef (varchar) — código legible heredado del ERP legacy. Puede coincidir con ID_ARTICULO (cuando se migró) o ser distinto
- companyCode — empresa dueña del artículo
- ID_PRODUCTO (varchar) — SKU del fabricante (ej: '100-100001488BOX'), usado por Laset para el bridge planilla↔ERP
- ncosteprom / ncosto — costo promedio y costo unitario
- npvp1..6 / npremayor1..5 — listas de precios de venta y mayorista
- Id_Marca, ID_FAMILIA, ccodfam — clasificación
- kit (tinyint) — si es un kit (bundle de componentes)
- companyCode — empresa dueña. Un pedido cc=X solo puede referenciar artículos cc=X

## stocks — balance actual por artículo y almacén

Una fila por (ID_ARTICULO, ID_ALMACEN). Representa el saldo actual, no el historial de movimientos.

La relación con las tablas de líneas es **indirecta**: stocks no tiene FK a pedclil ni albclil. El balance se actualiza con UPDATEs al liquidar (MakeSale) o recibir una OC (Fase D). Las líneas son el historial; stocks es la consecuencia acumulada.

## Cómo se referencia el artículo en cada tabla de líneas

| Tabla | Columna ID | Columna código | Columna almacén |
|---|---|---|---|
| pedclil | ID_Articulo (int) | cref (varchar) | ID_ALMACEN (int) |
| albclil | ID_Articulo (int) | cref (varchar) | ID_ALMACEN (int) |
| pedprol | ID_Articulo (int) | cRef (varchar) | stockWarehouseId (int, casi siempre NULL) |
| albprol | ID_Articulo (int) | cref (varchar) | stockWarehouseId (int) |

## Regla crítica: ID_Articulo es la fuente de verdad, no cref

En pedclil y albclil existen 13.462 filas donde `ID_Articulo` y `cref` apuntan a artículos distintos. Esto ocurre en líneas de Laset (cc=11): el `cref` conserva el código del artículo original cc=4 (NB) y el `ID_Articulo` apunta al clon cc=11 creado por `LasetFixCrossCompanyCommand`.

**Siempre joinear por ID_Articulo. Nunca asumir que cref y ID_Articulo son consistentes.**

```sql
-- Correcto
JOIN articulo ON articulo.ID_ARTICULO = pedclil.ID_Articulo

-- Incorrecto para Laset (puede traer artículo de otra empresa)
JOIN articulo ON articulo.cRef = pedclil.cref
```

## stockWarehouseId en pedprol es casi siempre NULL

- pedprol: 69.393 de 69.764 filas tienen stockWarehouseId NULL (99.5%)
- albprol: 666 de 75.986 filas tienen stockWarehouseId NULL (< 1%)

El campo `stockWarehouseId` en pedprol fue agregado tarde (feature Laset). Las OCs históricas no lo tienen. Para consultas que necesiten el almacén de una OC, usar `pedprot.warehousesId` (almacén de la cabecera) como fallback.

## Joins

### articulo con líneas de venta
```sql
-- por ID (correcto siempre)
pedclil JOIN articulo ON articulo.ID_ARTICULO = pedclil.ID_Articulo
albclil JOIN articulo ON articulo.ID_ARTICULO = albclil.ID_Articulo
```

### articulo con líneas de compra
```sql
pedprol JOIN articulo ON articulo.ID_ARTICULO = pedprol.ID_Articulo
albprol JOIN articulo ON articulo.ID_ARTICULO = albprol.ID_Articulo
```

### stocks con líneas de venta (incluye almacén)
```sql
pedclil LEFT JOIN stocks ON stocks.ID_ARTICULO = pedclil.ID_Articulo
                         AND stocks.ID_ALMACEN  = pedclil.ID_ALMACEN
```

### stocks con líneas de compra
```sql
-- albprol tiene stockWarehouseId casi siempre poblado
albprol LEFT JOIN stocks ON stocks.ID_ARTICULO = albprol.ID_Articulo
                         AND stocks.ID_ALMACEN  = albprol.stockWarehouseId

-- pedprol: usar cabecera como fallback para el almacén
pedprol LEFT JOIN pedprot pt ON pt.nNumPed = pedprol.nNumPed
        LEFT JOIN stocks ON stocks.ID_ARTICULO = pedprol.ID_Articulo
                         AND stocks.ID_ALMACEN  = COALESCE(pedprol.stockWarehouseId, pt.warehousesId)
```

## Distribución de stocks por almacén

Un artículo puede tener stock en múltiples almacenes (promedio 1, máximo 16 filas en stocks para un mismo artículo). Por eso el join a stocks siempre debe incluir ID_ALMACEN — sin ese filtro se obtienen múltiples filas y los totales se duplican.

## Ver también
- [[relacion-tablas-ped-alb|Tablas de ventas (pedclit/pedclil/albclit/albclil)]]
- [[relacion-tablas-pedprot-pedprol-pedproi|Tablas de compras (pedprot/pedprol/pedproi)]]
- [[relacion-tablas-stocks-almacen|Stocks y depósitos (FP_Almacen)]]
- [[relacion-companycode|companyCode por tabla]]
- [[modulo-makesale|MakeSale — flujo de liquidación]]
