# companyCode — mapa por tabla

## Qué es companyCode

Identifica a qué empresa pertenece un registro. Cada empresa opera con sus propios pedidos, remitos, artículos y stock. Los valores conocidos son: 4=NB, 9=NBElectric, 5=Digito Binario, 11=Laset.

## Mapa completo

| Tabla | companyCode propio | Cómo se determina |
|---|---|---|
| pedprot | Sí | columna propia |
| pedclit | Sí | columna propia |
| albprot | Sí | columna propia |
| albclit | Sí | columna propia — heredado de pedclit (agregado 2026-05-30) |
| articulo | Sí | columna propia |
| FP_Almacen | Sí | columna propia |
| pedprol | No | hereda de pedprot vía nNumPed |
| pedproi | No | hereda de pedprot vía nnumped |
| pedclil | No | hereda de pedclit vía (cnumped, cnumsuc) |
| albprol | No | hereda de albprot vía nnumalb |
| albclil | No | hereda de albclit vía ID_NROREMCLI_ENC |
| stocks | No | hereda del artículo vía ID_ARTICULO |

## Regla general

Solo las cabeceras, el maestro de artículos y los depósitos tienen companyCode propio. Las tablas de líneas y stocks siempre lo resuelven subiendo al padre. Para filtrar cualquier tabla de líneas por company siempre hay que hacer JOIN a su cabecera.

## Reglas de integridad

### Artículos
Un pedido de companyCode=X solo puede referenciar artículos con companyCode=X. Si pedprol/pedclil apunta a un artículo de otro companyCode es un error de datos (ocurrió en Laset 2026-05-15, fix en LasetFixCrossCompanyCommand).

### Almacenes
Un pedido o remito de companyCode=X solo puede tener ítems en almacenes con companyCode=X, salvo los depósitos compartidos confirmados.

**Depósitos compartidos (única excepción válida):**

| Depósito | CCODALM | Dueño | Compartido con |
|---|---|---|---|
| NB SAF | SAF | cc=4 (NB) | cc=9 (NBElectric) |
| NBElectric | NBE | cc=9 (NBElectric) | cc=4 (NB) |

SAF y NBE son los únicos depósitos compartidos y solo entre sí (NB ↔ NBElectric). Cualquier otro cruce de companyCode entre línea y almacén es un error de datos.

### Stocks
No deben existir filas en stocks donde articulo.companyCode difiera de FP_Almacen.companyCode, salvo las excepciones SAF/NBE mencionadas arriba.

## albclit — historial del campo

La columna companyCode fue agregada el 2026-05-30. Los registros históricos sin pedclit padre (remitos legacy del ERP, 2010-2025) fueron asignados a companyCode=4 (NB) ya que todos los registros legacy pertenecían a NB.

## Ver también
- [[relacion-tablas-ped-alb|Tablas de ventas (pedclit/pedclil/albclit/albclil)]]
- [[relacion-tablas-pedprot-pedprol-pedproi|Tablas de compras (pedprot/pedprol/pedproi)]]
- [[relacion-tablas-albprot-albprol|Remitos de compra (albprot/albprol)]]
- [[relacion-tablas-articulo-stocks|Artículo y stocks]]
- [[relacion-tablas-stocks-almacen|Stocks y depósitos]]
- [[contexto|Contexto — regla cero ERP]]
