# companyCode — mapa por tabla

## Qué es companyCode

Identifica a qué empresa pertenece un registro. Cada empresa opera con sus propios pedidos, remitos, artículos y stock. Los valores conocidos son: 4=NB, 9, 5, 11=Laset.

## Mapa completo

| Tabla | companyCode propio | Cómo se determina |
|---|---|---|
| pedprot | Sí | columna propia |
| pedclit | Sí | columna propia |
| albprot | Sí | columna propia |
| albclit | Sí | columna propia — heredado de pedclit (agregado 2026-05-30) |
| articulo | Sí | columna propia |
| pedprol | No | hereda de pedprot vía nNumPed |
| pedproi | No | hereda de pedprot vía nnumped |
| pedclil | No | hereda de pedclit vía (cnumped, cnumsuc) |
| albprol | No | hereda de albprot vía nnumalb |
| albclil | No | hereda de albclit vía ID_NROREMCLI_ENC |
| stocks | No | hereda del artículo vía ID_ARTICULO |

## Regla general

Solo las cabeceras y el maestro de artículos tienen companyCode propio. Las tablas de líneas y stocks siempre lo resuelven subiendo al padre. Para filtrar cualquier tabla de líneas por company siempre hay que hacer JOIN a su cabecera.

## Regla de integridad

Un pedido de companyCode=X solo puede referenciar artículos con companyCode=X. Si pedprol/pedclil apunta a un articulo de otro companyCode es un error de datos (ocurrió en Laset 2026-05-15, fix en LasetFixCrossCompanyCommand).

## albclit — historial del campo

La columna companyCode fue agregada el 2026-05-30. Los registros históricos sin pedclit padre (remitos legacy del ERP, 2010-2025) fueron asignados a companyCode=4 (NB) ya que todos los registros legacy pertenecían a NB.

## Ver también
- [[relacion-tablas-ped-alb|Tablas de ventas (pedclit/pedclil/albclit/albclil)]]
- [[relacion-tablas-pedprot-pedprol-pedproi|Tablas de compras (pedprot/pedprol/pedproi)]]
- [[relacion-tablas-albprot-albprol|Remitos de compra (albprot/albprol)]]
- [[relacion-tablas-articulo-stocks|Artículo y stocks]]
- [[relacion-tablas-stocks-almacen|Stocks y depósitos]]
- [[contexto|Contexto — regla cero ERP]]
