# Relación entre articulo / stocks y las tablas de líneas

## Las dos tablas maestras

- articulo: maestro de productos. Contiene descripción, precio, marca, familia, cRef (código legible), ID_ARTICULO (PK numérica interna), companyCode.
- stocks: stock por artículo y almacén. Una fila por (ID_ARTICULO, ID_ALMACEN). Contiene nstock, nstock_lo, nstock_reserva_pedidos, etc.

## Cómo se relacionan con las tablas de líneas

Todas las tablas de líneas (pedclil, albclil, pedprol, albprol) referencian al artículo de dos maneras:

- Por ID_Articulo (int): join directo con articulo.ID_ARTICULO. Es la FK limpia.
- Por cRef (varchar): join alternativo con articulo.cRef. Se usa en algunos contextos por compatibilidad con el ERP legacy.

La regla general es: ID_Articulo es la FK preferida. cRef se usa cuando el sistema legacy no tenía ID numérico o cuando hay búsquedas textuales.

## Joins articulo con cada tabla de líneas

### pedclil → articulo
```sql
pedclil
JOIN articulo ON articulo.ID_ARTICULO = pedclil.ID_Articulo
-- alternativo por cRef:
JOIN articulo ON articulo.cRef = pedclil.cref
```

### albclil → articulo
```sql
albclil
JOIN articulo ON articulo.ID_Articulo = albclil.ID_Articulo
-- alternativo por cRef:
JOIN articulo ON articulo.cRef = albclil.cref
```

### pedprol → articulo
```sql
pedprol
JOIN articulo ON articulo.ID_ARTICULO = pedprol.ID_Articulo
```

### albprol → articulo
```sql
albprol
JOIN articulo ON articulo.ID_ARTICULO = albprol.ID_Articulo
```

## Cómo se relaciona stocks con las tablas de líneas

stocks no tiene FK directa con las tablas de líneas. El join siempre pasa por el artículo Y el almacén:

```sql
stocks ON stocks.ID_ARTICULO = pedclil.ID_Articulo
        AND stocks.ID_ALMACEN = pedclil.ID_ALMACEN
```

La PK efectiva de stocks es (ID_ARTICULO, ID_ALMACEN): un artículo puede tener filas de stock en múltiples almacenes.

### Consulta típica: líneas de pedido con stock disponible
```sql
FROM pedclil PL
LEFT JOIN stocks S ON S.ID_ARTICULO = PL.ID_Articulo
                   AND S.ID_ALMACEN = PL.ID_ALMACEN
```

## Qué hace el sistema con stocks al liquidar un pedido

Al crear un remito (MakeSale), el sistema:
1. Lee pedclil JOIN stocks para ver disponibilidad antes de liquidar.
2. Al confirmar, descuenta del stock:
   - nstock = nstock - cantidad (stock NB)
   - nstock_lo = nstock_lo - cantidad (stock LO)
   - nstock_postventa = nstock_postventa - cantidad (si corresponde)
3. Recalcula nstock_reserva_pedidos sobre pedclil pendientes.

Al recibir una OC (Fase D Laset), el sistema suma al stock:
- nstock = nstock + cantidad (recepción)

## Campos de stock más usados en las queries

- nstock: stock disponible principal (NB)
- nstock_lo: stock Libre Opción
- nstock_reserva_pedidos: cantidad reservada por pedidos pendientes (se recalcula)
- nstock_postventa: stock reservado para post-venta
- nstock_en_cola: en cola de ingreso
- nstock_ingresando: en tránsito/ingresando
- nstock_virtual: stock virtual calculado
- ID_ALMACEN: almacén al que pertenece la fila de stock

## Regla: articulo.companyCode debe coincidir con el companyCode del pedido

Cada empresa tiene sus propios artículos en la tabla articulo, separados por companyCode. Un pedido (pedclit, pedprot) con companyCode=11 debe referenciar solo artículos con companyCode=11. Si una línea de pedido apunta a un artículo de otro companyCode, es un error de datos.

Esto ocurrió en el proyecto Laset (2026-05-15) cuando una carga fallida dejó pedprol/pedclil cc=11 apuntando a artículos cc=4 (NB). El fix fue LasetFixCrossCompanyCommand: clonó los artículos cc=4 como cc=11 y remapeó los ID_Articulo en pedprol y pedclil.

## Base de datos

- articulo y stocks: [NewBytes_DBF].[dbo]
- stocks también se cruza con [NewBytes_DBF].[dbo].[FP_Almacen] por ID_ALMACEN para obtener nombre y código del almacén.
