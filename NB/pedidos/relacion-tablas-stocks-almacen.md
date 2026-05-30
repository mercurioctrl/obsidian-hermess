# Stocks y depósitos (FP_Almacen)

## Las dos tablas

### FP_Almacen — maestro de depósitos
Un depósito físico donde se guarda mercadería. Tiene companyCode propio.

Columnas clave:
- ID_ALMACEN (PK, int)
- CCODALM (código corto, ej: 'SAF', 'DOM', 'BON')
- CNOMBRE (nombre legible)
- companyCode — a qué empresa pertenece el depósito
- Predeterminado — si es el depósito por defecto de la empresa
- deleted_at — soft delete
- Id_Pais, ID_CIUDAD, ID_Provincia — ubicación geográfica

### stocks — stock por artículo y depósito
Una fila por combinación (ID_ARTICULO, ID_ALMACEN). No tiene companyCode propio — se determina subiendo a articulo o a FP_Almacen.

Columnas clave:
- ID_ARTICULO (FK → articulo.ID_ARTICULO)
- ID_ALMACEN (FK → FP_Almacen.ID_ALMACEN)
- cref (varchar, copia del cRef del artículo)
- nstock — stock disponible principal (NB)
- nstock_lo — stock Libre Opción
- nstock_reserva_pedidos — reservado por pedidos pendientes (se recalcula)
- nstock_lo_reserva_pedidos — reservado LO por pedidos pendientes
- nstock_postventa — reservado para post-venta
- nstock_en_cola — en cola de ingreso
- nstock_ingresando — en tránsito
- nstock_virtual — calculado
- nstock_d1 — stock día 1
- nstock_seguridad — stock de seguridad mínimo
- guardarEnStock — flag
- id_auto (PK IDENTITY interna)

## Relaciones

### stocks → articulo
```sql
stocks JOIN articulo ON articulo.ID_ARTICULO = stocks.ID_ARTICULO
```

### stocks → FP_Almacen
```sql
stocks JOIN FP_Almacen ON FP_Almacen.ID_ALMACEN = stocks.ID_ALMACEN
```

### stocks → pedclil (al liquidar)
```sql
pedclil LEFT JOIN stocks ON stocks.ID_ARTICULO = pedclil.ID_Articulo
                         AND stocks.ID_ALMACEN  = pedclil.ID_ALMACEN
```

### FP_Almacen → pedprot / pedclit (depósito del pedido)
pedprot usa CCODALM (código) y warehousesId (= ID_ALMACEN).
pedclit usa ccodalm (código) y ID_ALMACEN.

```sql
FP_Almacen ON FP_Almacen.ID_ALMACEN = pedprot.warehousesId
FP_Almacen ON FP_Almacen.ID_ALMACEN = pedclit.ID_ALMACEN
```

## companyCode en depósitos y stock

FP_Almacen tiene companyCode propio — cada empresa tiene sus propios depósitos.
stocks no tiene companyCode — se determina por el artículo o por el depósito.

Para filtrar stock de una empresa:
```sql
-- vía artículo
stocks JOIN articulo ON articulo.ID_ARTICULO = stocks.ID_ARTICULO
WHERE articulo.companyCode = 4

-- vía depósito
stocks JOIN FP_Almacen ON FP_Almacen.ID_ALMACEN = stocks.ID_ALMACEN
WHERE FP_Almacen.companyCode = 4
```

Ambos deberían dar el mismo resultado si los datos son consistentes.

## Qué pasa con el stock al operar

### Al crear un pedido (pedclit/pedclil)
Se incrementa nstock_reserva_pedidos para los artículos del pedido.

### Al liquidar (crear albclit/albclil — MakeSale)
```
nstock     = nstock - cantidad      (stock NB)
nstock_lo  = nstock_lo - cantidad   (stock LO, si aplica)
nstock_postventa = nstock_postventa - cantidad (si es post-venta)
nstock_reserva_pedidos se recalcula sobre pedclil pendientes
```

### Al recibir una OC (crear albprot/albprol)
```
nstock = nstock + cantidad
```

## Base de datos

Todas en [NewBytes_DBF].[dbo]
