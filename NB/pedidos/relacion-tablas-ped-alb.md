# Relación entre pedclit / pedclil / albclit / albclil

Estas cuatro tablas forman dos pares encabezado-líneas que representan el ciclo de vida de una venta: primero el pedido, luego el remito (albarán) que se genera al liquidarlo.

## Las cuatro tablas

- pedclit: encabezado del pedido de cliente. Una fila por pedido.
- pedclil: líneas (ítems) del pedido. Muchas filas por pedido.
- albclit: encabezado del remito/albarán de cliente. Una fila por remito. Se crea cuando el pedido se liquida.
- albclil: líneas (ítems) del remito. Muchas filas por remito.

La nomenclatura sigue una lógica: "ped" = pedido, "alb" = albarán/remito, "clit" = encabezado de cliente, "clil" = líneas de cliente.

## Relaciones

### Dentro del pedido
pedclit se relaciona con pedclil por (cnumped, cnumsuc). Un pedido tiene muchas líneas.

### Dentro del remito
albclit se relaciona con albclil por ID_NROREMCLI_ENC. Un remito tiene muchas líneas. Importante: este join NO usa CNUMALB (que es el número legible del remito), sino el ID interno ID_NROREMCLI_ENC.

### Entre pedido y remito
albclit se relaciona con pedclit por (cnumped, cnumsuc). Un pedido puede tener uno o ningún remito. El remito nace cuando el pedido se liquida/descarga.

### Entre líneas de pedido y líneas de remito
No hay FK directa entre pedclil y albclil. Para cruzarlas hay que pasar por las cabeceras (pedclit → albclit) o comparar por CREF / ID_ARTICULO.

## Joins SQL

Pedido con sus líneas:
```sql
FROM pedclit P
JOIN pedclil PL ON PL.cnumped = P.cnumped AND PL.cnumsuc = P.cnumsuc
```

Pedido con su remito:
```sql
FROM pedclit P
JOIN albclit A ON A.cnumped = P.cnumped AND A.cnumsuc = P.cnumsuc
```

Remito con sus líneas:
```sql
FROM albclit A
JOIN albclil AL ON AL.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC
```

Query completa (pedido + ítems del pedido + remito + ítems del remito):
```sql
FROM pedclit P
JOIN pedclil  PL ON PL.cnumped = P.cnumped AND PL.cnumsuc = P.cnumsuc
JOIN albclit  A  ON A.cnumped  = P.cnumped AND A.cnumsuc  = P.cnumsuc
JOIN albclil  AL ON AL.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC
```

## Advertencias

- Nunca hacer JOIN solo por cnumped. La PK efectiva de pedclit y albclit es (cnumped, cnumsuc) porque el mismo número de pedido puede existir en distintas sucursales.
- El join entre albclit y albclil usa ID_NROREMCLI_ENC, no CNUMALB.
- pedclil y albclil no tienen relación directa entre sí.

## Base de datos
Todas estas tablas están en [NewBytes_DBF].[dbo]
