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

## stocks — balance actual por artículo y almacén

Una fila por (ID_ARTICULO, ID_ALMACEN). Representa el saldo actual, no el historial de movimientos.

La relación con las tablas de líneas es **indirecta**: stocks no tiene FK a pedclil ni albclil. El balance se actualiza con UPDATEs al liquidar (MakeSale) o recibir una OC. Las líneas son el historial; stocks es la consecuencia acumulada.

### Regla de integridad: stocks solo existe para almacenes de la misma empresa que el artículo

No deben existir filas en stocks donde `articulo.companyCode` sea distinto al `FP_Almacen.companyCode`, salvo los depósitos compartidos confirmados (SAF y NBE entre NB cc=4 y NBElectric cc=9). Cualquier otro cruce es un error de datos.

## Cómo se referencia el artículo en cada tabla de líneas

| Tabla | Columna ID | Columna código | Columna almacén |
|---|---|---|---|
| pedclil | ID_Articulo (int) | cref (varchar) | ID_ALMACEN (int) |
| albclil | ID_Articulo (int) | cref (varchar) | ID_ALMACEN (int) |
| pedprol | ID_Articulo (int) | cRef (varchar) | stockWarehouseId (int) |
| albprol | ID_Articulo (int) | cref (varchar) | stockWarehouseId (int) |

**Ambos campos (ID_Articulo y cref) son obligatorios y deben estar siempre completos.** ID_Articulo tiene mayor peso como FK canónica, pero cref también es único y requerido.

## Regla: ID_Articulo es la fuente de verdad, no cref

Hay 13.462 filas en pedclil donde `ID_Articulo` y `cref` apuntan a artículos distintos. Esto ocurre en líneas de Laset (cc=11): el `cref` conserva el código del artículo original cc=4 (NB) y el `ID_Articulo` apunta al clon cc=11 creado por `LasetFixCrossCompanyCommand`. Son un caso particular de datos históricos — en condiciones normales ambos campos deben ser consistentes.

**Siempre joinear por ID_Articulo.**

```sql
-- Correcto
JOIN articulo ON articulo.ID_ARTICULO = pedclil.ID_Articulo

-- Puede traer artículo equivocado en casos Laset
JOIN articulo ON articulo.cRef = pedclil.cref
```

## stockWarehouseId en pedprol — legacy sin almacén

- pedprol: 69.393 de 69.764 filas tienen stockWarehouseId NULL (99.5%)
- albprol: 666 de 75.986 filas tienen stockWarehouseId NULL (< 1%)

Los pedprol con NULL son OCs legacy de NB — en la práctica pertenecen todas al depósito SAF (ID_ALMACEN=2, cc=4). Para consultas que necesiten el almacén de una OC legacy, usar `pedprot.warehousesId` como fallback o asumir ID_ALMACEN=2.

```sql
-- Fallback para OCs legacy
COALESCE(pedprol.stockWarehouseId, pt.warehousesId)
```

## Joins

### articulo con líneas de venta
```sql
pedclil JOIN articulo ON articulo.ID_ARTICULO = pedclil.ID_Articulo
albclil JOIN articulo ON articulo.ID_ARTICULO = albclil.ID_Articulo
```

### articulo con líneas de compra
```sql
pedprol JOIN articulo ON articulo.ID_ARTICULO = pedprol.ID_Articulo
albprol JOIN articulo ON articulo.ID_ARTICULO = albprol.ID_Articulo
```

### stocks con líneas de venta
```sql
pedclil LEFT JOIN stocks ON stocks.ID_ARTICULO = pedclil.ID_Articulo
                         AND stocks.ID_ALMACEN  = pedclil.ID_ALMACEN
```

### stocks con líneas de compra
```sql
-- albprol (casi siempre tiene stockWarehouseId)
albprol LEFT JOIN stocks ON stocks.ID_ARTICULO = albprol.ID_Articulo
                         AND stocks.ID_ALMACEN  = albprol.stockWarehouseId

-- pedprol (con fallback a cabecera para legacy)
pedprol LEFT JOIN pedprot pt ON pt.nNumPed = pedprol.nNumPed
        LEFT JOIN stocks   ON stocks.ID_ARTICULO = pedprol.ID_Articulo
                          AND stocks.ID_ALMACEN  = COALESCE(pedprol.stockWarehouseId, pt.warehousesId)
```

## Advertencia: siempre filtrar stocks por almacén

Un artículo puede tener hasta 16 filas en stocks (una por almacén). Sin el filtro `AND stocks.ID_ALMACEN = ...` el join devuelve múltiples filas y los totales se duplican.

## Ver también
- [[relacion-tablas-ped-alb|Tablas de ventas (pedclit/pedclil/albclit/albclil)]]
- [[relacion-tablas-pedprot-pedprol-pedproi|Tablas de compras (pedprot/pedprol/pedproi)]]
- [[relacion-tablas-stocks-almacen|Stocks y depósitos (FP_Almacen)]]
- [[relacion-companycode|companyCode por tabla]]
- [[modulo-makesale|MakeSale — flujo de liquidación]]
