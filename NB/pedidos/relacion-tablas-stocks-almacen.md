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

## Columna de depósito en las tablas de líneas

Todas las tablas de líneas tienen su propio campo de depósito a nivel de ítem (un pedido puede tener ítems de distintos depósitos):

| Tabla | Columna | FK a |
|---|---|---|
| pedclil | ID_ALMACEN | FP_Almacen.ID_ALMACEN |
| albclil | ID_ALMACEN | FP_Almacen.ID_ALMACEN |
| pedprol | stockWarehouseId | FP_Almacen.ID_ALMACEN |
| albprol | stockWarehouseId | FP_Almacen.ID_ALMACEN |

El nombre cambia entre el mundo ventas (ID_ALMACEN) y compras (stockWarehouseId), pero apuntan a la misma tabla.

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

### FP_Almacen → cabeceras
pedprot usa CCODALM (código) y warehousesId (= ID_ALMACEN).
pedclit usa ccodalm (código) y ID_ALMACEN.

```sql
FP_Almacen ON FP_Almacen.ID_ALMACEN = pedprot.warehousesId
FP_Almacen ON FP_Almacen.ID_ALMACEN = pedclit.ID_ALMACEN
```

## companyCode y depósitos

### Regla general
Un pedido o remito (sea de venta o compra) no puede tener un ítem en un almacén de otro companyCode. El almacén de cada línea debe pertenecer al mismo companyCode que la cabecera.

### Excepción conocida: depósitos compartidos
Algunos depósitos son compartidos entre empresas. El companyCode en FP_Almacen indica el "dueño" del depósito pero no impide que otras empresas lo usen.

Depósitos compartidos confirmados (2026-05-30):
- **NBE** — compartido entre cc=4 (NB) y cc=9. Los 754 pedclil cc=4 con almacén NBE (cc=9) NO son errores.

Depósitos pendientes de confirmar si son compartidos o errores:
- SAF (cc=4): usado desde cc=5 (50 casos en pedclil) y cc=1 (2 casos)
- DOM, GRI, ASI (cc=11 Laset): cruzados desde cc=4 en pedprol (residuo migración Laset, probablemente errores)

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

## Ver también
- [[relacion-tablas-articulo-stocks|Artículo y stocks]]
- [[relacion-tablas-ped-alb|Tablas de ventas (pedclit/pedclil/albclit/albclil)]]
- [[relacion-tablas-pedprot-pedprol-pedproi|Tablas de compras (pedprot/pedprol/pedproi)]]
- [[relacion-companycode|companyCode por tabla]]
- [[modulo-makesale|MakeSale — flujo de liquidación]]
