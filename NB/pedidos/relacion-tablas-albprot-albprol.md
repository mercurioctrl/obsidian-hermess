# Relación entre pedprot/pedprol/pedproi y albprot/albprol

## Qué es cada tabla

- pedprot: encabezado de la Orden de Compra (OC) al proveedor.
- pedprol: líneas de artículos de la OC.
- pedproi: cargos extra de la OC (flete, impuestos).
- albprot: encabezado del remito de compra (recepción). Se crea cuando la OC se recibe.
- albprol: líneas del remito de compra. Espeja las líneas de pedprol al momento de la recepción.

albproi NO existe como tabla en esta base de datos (confirmado 2026-05-15).

## Relación pedprot → albprot

albprot nace de pedprot cuando la OC se recibe físicamente. El link es:

```sql
albprot ON albprot.nnumped = pedprot.nNumPed
```

Un pedprot puede tener uno o ningún albprot. Si NOT EXISTS albprot para un pedprot, la OC todavía no fue recibida.

## Relación albprot → albprol

```sql
albprot
JOIN albprol ON albprol.nnumalb = albprot.nnumalb
```

## Query completa: OC + líneas + remito de compra + líneas del remito

```sql
FROM pedprot t
JOIN pedprol   pl ON pl.nNumPed  = t.nNumPed
JOIN albprot   at ON at.nnumped  = t.nNumPed
JOIN albprol   al ON al.nnumalb  = at.nnumalb
```

## Equivalencia con el mundo de ventas

El par pedprot/pedprol es el equivalente de compras a pedclit/pedclil (ventas).
El par albprot/albprol es el equivalente de compras a albclit/albclil (ventas).

| Compras   | Ventas   | Qué es                        |
|-----------|----------|-------------------------------|
| pedprot   | pedclit  | Encabezado del pedido         |
| pedprol   | pedclil  | Líneas del pedido             |
| pedproi   | —        | Cargos extra (solo en compras)|
| albprot   | albclit  | Encabezado del remito         |
| albprol   | albclil  | Líneas del remito             |

## Diferencia clave entre compras y ventas

En compras, nnumalb (albprot) es único globalmente, igual que nNumPed (pedprot). Los joins van solo por nnumalb o nNumPed sin necesidad de columna de sucursal.

En ventas, albclit usa la tupla (cnumped, cnumsuc) porque el número de pedido no es único globalmente.

## Campos clave

pedprot: nNumPed (PK), companyCode, cCodPro, cCodAlm, warehousesId, dFecPed, arrivalDate.

albprot: nnumalb (PK), nnumped (FK → pedprot.nNumPed), companyCode, dfecalb, dfecent, ccodpro, ccodalm, lfacturado.

pedprol: nNumPed (FK), nLinea, cRef, ID_Articulo, nCanPed, nCanEnt, nPreDiv.

albprol: nnumalb (FK), nlinea, cref, ID_Articulo, ncanent, nprediv.

## Detectar OCs sin remito

```sql
SELECT t.nNumPed
FROM pedprot t
WHERE t.companyCode = ?
  AND NOT EXISTS (
      SELECT 1 FROM albprot a
      WHERE a.nnumped = t.nNumPed AND a.companyCode = ?
  )
```

## Base de datos

Todas en [NewBytes_DBF].[dbo]

## Ver también
- [[relacion-tablas-pedprot-pedprol-pedproi|OC (pedprot/pedprol/pedproi)]]
- [[relacion-tablas-ped-alb|Tablas de ventas (pedclit/pedclil/albclit/albclil)]]
- [[relacion-tablas-stocks-almacen|Stocks y depósitos]]
- [[relacion-companycode|companyCode por tabla]]
