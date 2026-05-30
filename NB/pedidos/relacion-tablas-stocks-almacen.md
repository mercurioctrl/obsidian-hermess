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
Una fila por combinación (ID_ARTICULO, ID_ALMACEN). No tiene companyCode propio.

Columnas clave:
- ID_ARTICULO (FK → articulo.ID_ARTICULO)
- ID_ALMACEN (FK → FP_Almacen.ID_ALMACEN)
- cref — copia del cRef del artículo
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
- id_auto (PK IDENTITY interna)

## Columna de depósito en las tablas de líneas

Todas las tablas de líneas tienen su propio campo de depósito a nivel de ítem. Un pedido puede tener ítems de distintos depósitos.

| Tabla | Columna | FK a |
|---|---|---|
| pedclil | ID_ALMACEN | FP_Almacen.ID_ALMACEN |
| albclil | ID_ALMACEN | FP_Almacen.ID_ALMACEN |
| pedprol | stockWarehouseId | FP_Almacen.ID_ALMACEN |
| albprol | stockWarehouseId | FP_Almacen.ID_ALMACEN |

El nombre cambia entre ventas (ID_ALMACEN) y compras (stockWarehouseId), pero apuntan a la misma tabla.

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
```sql
FP_Almacen ON FP_Almacen.ID_ALMACEN = pedprot.warehousesId
FP_Almacen ON FP_Almacen.ID_ALMACEN = pedclit.ID_ALMACEN
```

## Regla: companyCode y depósitos

Un pedido o remito no puede tener un ítem en un almacén de otro companyCode, salvo depósitos explícitamente compartidos.

### Depósitos compartidos confirmados

| Depósito | CCODALM | companyCode dueño | Compartido con |
|---|---|---|---|
| NB SAF | SAF | 4 (NB) | 9 (NBElectric) |
| NBElectric | NBE | 9 (NBElectric) | 4 (NB) |

SAF y NBE son los únicos depósitos compartidos. Cualquier otro cruce de companyCode entre línea y almacén es un error de datos.

### Errores de datos conocidos (no corregidos, solo documentados)
- 10 pedidos de DIGITO BINARIO (cc=5) con líneas en SAF (cc=4) — 2025, mayoría servidos
- 1 pedido cc=1 con líneas en SAF — 2026-05-26, pendiente
- 6 pedprot NB (cc=4) con líneas en almacenes Laset (DOM/GRI/ASI cc=11) — mayo 2026, residuo de migración Laset Fase C/D

## Qué pasa con el stock al operar

### Al crear un pedido (pedclit/pedclil)
Se incrementa nstock_reserva_pedidos para los artículos del pedido.

### Al liquidar (crear albclit/albclil — MakeSale)
```
nstock     = nstock - cantidad
nstock_lo  = nstock_lo - cantidad   (si aplica)
nstock_postventa = nstock_postventa - cantidad (si aplica)
nstock_reserva_pedidos se recalcula sobre pedclil pendientes
```

### Al recibir una OC (crear albprot/albprol)
```
nstock = nstock + cantidad
```

## Ver también
- [[relacion-tablas-articulo-stocks|Artículo y stocks]]
- [[relacion-tablas-ped-alb|Tablas de ventas (pedclit/pedclil/albclit/albclil)]]
- [[relacion-tablas-pedprot-pedprol-pedproi|Tablas de compras (pedprot/pedprol/pedproi)]]
- [[relacion-companycode|companyCode por tabla]]
- [[modulo-makesale|MakeSale — flujo de liquidación]]
