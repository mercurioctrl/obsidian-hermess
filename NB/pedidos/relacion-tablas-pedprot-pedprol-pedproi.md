# Relación entre pedprot / pedprol / pedproi

Estas tres tablas representan una Orden de Compra (OC) al proveedor: pedprot es el encabezado, pedprol son las líneas de artículos, y pedproi son los cargos extra (flete, impuestos, etc.).

Son el equivalente de compras al par pedclit/pedclil que es de ventas. La nomenclatura sigue la misma lógica: "ped" = pedido, "pro" = proveedor, "t" = encabezado (tiene), "l" = líneas, "i" = cargos extra (impuestos/adicionales).

## Las tres tablas

- pedprot: encabezado de la OC al proveedor. Una fila por orden de compra. Tiene companyCode propio.
- pedprol: líneas (artículos) de la OC. Muchas filas por OC. Se relaciona con pedprot por nNumPed.
- pedproi: cargos extra de la OC (flete "camion", impuestos, etc.). Muchas filas por OC. Se relaciona con pedprot por nnumped.

## Relaciones

### pedprot → pedprol
```sql
pedprot
JOIN pedprol ON pedprol.nNumPed = pedprot.nNumPed
```

### pedprot → pedproi
```sql
pedprot
JOIN pedproi ON pedproi.nnumped = pedprot.nNumPed
```

Nota: el campo en pedproi se llama nnumped (minúsculas), no nNumPed. Mismo dato, distinto nombre de columna.

### Query completa
```sql
FROM pedprot t
JOIN pedprol l  ON l.nNumPed  = t.nNumPed
JOIN pedproi i  ON i.nnumped  = t.nNumPed
```

## Diferencia clave con pedclit/pedclil

pedprot.nNumPed es único globalmente (no necesita columna de sucursal para hacer el JOIN). Por eso los joins van solo por nNumPed, sin AND cnumsuc. En cambio pedclit usa la tupla compuesta (cnumped, cnumsuc) porque el mismo número puede existir en distintas sucursales.

## Campos principales

pedprot: nNumPed (PK), dFecPed, cCodPro (proveedor), cCodAlm (almacén), cEstado, companyCode, warehousesId, arrivalDate, trackingNumber.

pedprol: nNumPed (FK), nLinea, cRef, ID_Articulo, nCanPed (cantidad pedida), nCanEnt (cantidad entregada), nPreDiv (precio divisa).

pedproi: nnumped (FK), cserie, cdescrip (descripción del cargo, ej: "camion"), nbase, nimporte, ntasa, nporctasa.

## Gotcha

pedprot.sitio = 0 mientras pedprol.sitio = NULL. No hacer JOIN por sitio, solo por nNumPed.

## Relación con los remitos de compra

Cuando la OC se recibe, se generan albprot (encabezado del remito de compra) y albprol (líneas). El link es albprot.nnumped = pedprot.nNumPed.

## Base de datos

Todas en [NewBytes_DBF].[dbo]
