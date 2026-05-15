# Feature: Laset Import Framework

> Importar la operación FOB de **LASET** (CODEMP=11, empresa importadora uruguaya del grupo) desde la planilla histórica `Raw ventas FOB` hacia las tablas existentes del ERP, **sin tocar el resto del ERP**. Solo aplica a `companyCode = 11`.

Branch: `lasetImportFramework` (ambos repos).
Estado al **2026-05-14**: discovery completa + staging creado y aplicado. Cargador, reconciliación e importación de delta pendientes.

---

## 1. Contexto y descubrimiento

### Quién es Laset

Empresa **CODEMP=11** en `NewBytes_DBF.dbo.FP_Empresas`. Es **Laset Sociedad Anónima** (Uruguay), dirección `Pradines Clemente 1795`, RUT `217502910019` (12 dígitos, no-argentino). Factura en DOL, con `defaultIncoterms=14` (única empresa con incoterm default). Es importadora — triangula via **New Bytes Inc** (USA) hacia clientes LATAM (Chile 986, Paraguay 974, Colombia 240, Bolivia 197, Argentina 58, Ecuador, Panamá, USA).

El sistema soporta **11 empresas activas**, no solo NB/NBElectric/LO como dice el CLAUDE.md histórico. Ver [[contexto#Empresas activas (FP_Empresas)]].

### La planilla

`docs/laser.xlsx` (typo: el archivo se llama "laser" pero la empresa es "Laset"), pestaña **`Raw ventas FOB`**: 3008 filas × 67 columnas, años 2025-2026. **2614 filas válidas** (excluye fila 2 con SELECTORs, 367 con `Year=1900`, 22 vacías).

Cada fila es un **trade completo**: vendor (US/CH/PY) → NB Inc (US) → cliente final (LATAM), con su SKU, qty, FOB unit, costos, venta, logística, rebates, re-facturación NB Inc.

**Insight clave**: la planilla ya viene pre-linkeada (Qty compra = CANTIDAD venta en 100% de filas válidas). Una compra mayorista se splittea manualmente en N filas (1 por cliente) antes de cargarse — 339 de 438 Vendor Invoices se repiten.

### Por qué importar

La planilla cubre **todo** el flujo histórico. El ERP tiene migrado parcialmente:

| Tabla ERP | Rows `companyCode=11` | Concepto |
|---|---:|---|
| `pedprot` | 386 | Compras (cabecera) |
| `pedprol` | (líneas) | Compras (detalle) |
| `pedproi` | 158 | Cargos extra de compra ("camion", percepciones) |
| `pedclit` | 363 | Ventas (cabecera) |
| `pedclil` | (líneas) | Ventas (detalle) |
| `forwarders` | 84 | DHL, Peniel International (Miami)… |
| `FP_FactWebCliEncabezado_Uy` | 179 | CFE Uruguay emitidos |
| `FP_FactWebCliDetalle_Uy` | 1411 | Líneas de CFE Uy |

La planilla tiene 2614 filas válidas → **delta grande a importar**, especialmente histórico pre-2026.

---

## 2. Decisión clave: NO crear modelo nuevo

El framework **ya existe** en el ERP, solo bajo otros nombres. Ver el [[arquitectura#Modelo canónico ERP|mapeo canónico de tablas]]:

- **Compras** = `pedprot` + `pedprol` + `pedproi`
- **Ventas** = `pedclit` + `pedclil`
- **Stock** = `stocks` (filtrado por almacén)
- **Linkeo compra↔venta** = [[feature-asignacion-oc|`pedclil_oc_asignacion`]] (ya habilitado para Laset via `ASSIGNMENT_COMPANIES=4,11`)
- **CFE final** = `FP_FactWebCliEncabezado_Uy` + `FP_FactWebCliDetalle_Uy`

El trabajo del feature es **reconciliar la planilla con lo ya migrado** e importar el delta, **sin tocar las tablas ERP**.

---

## 3. Mapeo planilla ↔ ERP

### Compras

| Planilla | ERP |
|---|---|
| `PROVEEDOR` | `pedprot.cCodPro` |
| `PAIS PROVEEDOR` | `pedprot.countryId` |
| `MARCA` | catálogo de productos |
| `DEPOSITO` (DOM/BON/GRI/SAF/URU/ASI) | `pedprot.cCodAlm`, `warehousesId` |
| `Vendor PI` | tentativo: `pedprot.cExped` |
| `Vendor Invoice` | tentativo: `pedprot.dateVoucherNumber` |
| `Qty`, `SKU`, `Description` | `pedprol.nCanPed`, `cRef`, `cDetalle` |
| `FOB` (unit) | `pedprol.nPreDiv` |
| `AMOUNT` (=FOB×Qty) | `pedprol.nPreDiv * nCanPed` |
| `AWB` / `Tracking` | `pedprot.trackingNumber` |
| `Fecha de arribo` | `pedprot.arrivalDate` |
| `Costo extra (Camión, RMA, etc)` | `pedproi.cdescrip='camion'` + `nimporte` |
| `STATUS` (compra) | `pedprot.cEstado` |

### Ventas

| Planilla | ERP |
|---|---|
| `Pais` (destino) | `Client.idCountry` |
| `RAZON SOCIAL` / `DESTINATARIO FISCAL` | `pedclit.ccodcli` |
| `VENDEDOR` | `pedclit.ccodage` (='72' = Natalia Huang) |
| `Invoice Date` / `Fecha de Factura` | `pedclit.dfecped` |
| `Customer PI` | `pedclit.proformaInvoice` |
| `Customer Invoice` | `pedclit.cnumped` + `FP_FactWebCliEncabezado_Uy.numeroCfe` |
| `CANTIDAD`, `Modelo`, `PRECIO de venta`, `TOTAL` | `pedclil.ncanped`, `cref`, `npreunit`, `nimp` |
| `REAL COST` / `Real Mkp` | `pedclil.costForSale`, `userUtility`, `acelerator` |
| `Transporte` / Forwarder | `pedclit.forwarderId` → `forwarders` |
| `Incoterm` | `pedclit.incotermId` |
| `STATUS` (venta) | `pedclit.cestado` |

### Sin destino claro en ERP (lo único que falta)

| Planilla | Comentario |
|---|---|
| `Sell out rebate`, `Reportado AMD/NVIDIA`, `Qty a la que aplica`, `Finalización REBATE` | Tabla `rebates` existe pero es **huérfana** (12 rows, sin `companyCode`, schema primitivo, creada junto a `NewTable` vacía el mismo día — restos de intento abandonado). Modelar nuevo cuando se llegue a esa etapa. |
| `NB Inc > Cliente` (re-facturación NB Inc → cliente, %) | Mecanismo inter-company. Posible candidato: `addendum` de la CFE. |
| `APA` / `Soporte extra` | Pueden mapear a `pedclil.ncostoextra_import` |

---

## 4. Schema staging (creado 2026-05-14)

Dos tablas nuevas en `NewBytes_DBF.dbo` (cero modificación a tablas ERP):

### `laset_import_batches` (9 cols)
Cabecera por carga. Permite reimportar versiones sucesivas del Excel y hacer diff entre cargas.

- `id` INT IDENTITY PK
- `file_name`, `file_sha256`, `sheet_name`, `total_rows`, `valid_rows`
- `imported_at` (default `SYSDATETIME()`), `imported_by`, `notes`

### `laset_import_staging` (79 cols)
1 fila por fila del Excel. **67 cols crudas en NVARCHAR (lossless)** + 8 cols de matching + 4 cols sistema.

Estructura:
- `id` INT IDENTITY PK, `batch_id` FK, `source_row_number`, `created_at`
- 67 cols crudas con nombres `snake_case` y comentarios `-- col NN` referenciando orden Excel original (ej. `vendor_invoice`, `qty`, `sku`, `customer_invoice`, `cantidad`, `precio_venta`, `awb`, `costo_extra_camion`…). Palabras reservadas escapadas: `[comment]`, `[status]`.
- `match_status` NVARCHAR(20) con CHECK en `('UNMATCHED','MATCHED','PARTIAL','CONFLICT','IMPORTED','IGNORED')`, default `'UNMATCHED'`
- `matched_pedprot_nnumped` INT, `matched_pedprol_nlinea` DECIMAL(10,2), `matched_pedclit_cnumped` VARCHAR(8), `matched_pedclil_id` INT
- `match_score` DECIMAL(5,2), `match_notes`, `matched_at`

Índices: `batch`, `sku`, `customer_invoice`, `vendor_invoice`, `status`.

### Scripts SQL

- `api-rest-pedidos-laravel/app/database/sql/2026_05_14_001_create_laset_import_staging.sql`
- `api-rest-pedidos-laravel/app/database/sql/2026_05_14_001_drop_laset_import_staging.sql` (rollback simétrico)

Aplicados al SQL Server siguiendo el patrón del `database/sql/README.md` (`docker exec ... php -r "..."` con `preg_split` por `GO`). Ver [[arquitectura#DDL legacy y migraciones]].

---

## 5. Estrategia de reconciliación

**Identidad contable**: `SUM(compras) − SUM(ventas) = stocks.nstock + nstock_ingresando` por SKU+almacén+`companyCode=11`.

Tres niveles de cruce:

1. **Sanity intra-ERP**: chequear que la identidad cierra hoy con los 386 OCs + 363 ventas ya migrados. Si no cierra, hay bug previo independiente de la planilla.
2. **Sanity planilla**: en staging, `SUM(qty) − SUM(cantidad)` por SKU + `deposito` (afinando por `status` Vendidas/Retirado/Stock/Pendiente).
3. **Delta planilla vs ERP**: diferencia entre (1) y (2). Es exactamente lo que falta migrar.

### Heurística de matching staging → ERP (pendiente de implementar)

1. Match exacto `customer_invoice` ↔ `pedclit.cnumped`. Score 100.
2. Match `SKU + qty + cliente` en `pedclil` joineando `pedclit` (`companyCode=11`). Score 80.
3. Match `vendor_invoice` ↔ `pedprot.dateVoucherNumber`. Score 70.
4. Match `SKU + qty + proveedor` en `pedprol` joineando `pedprot`. Score 60.
5. Sino → `match_status='UNMATCHED'`.

Persistir resultado en `laset_import_staging.matched_*`.

---

## 6. Almacenes de Laset

`pedprot.cCodAlm` para `companyCode=11`:

| ERP | warehousesId | Planilla `DEPOSITO` |
|---|---:|---|
| DOM | 9 | DOMESTIC MIAMI |
| BON | 11, 13, 16 | BONDED PROVEEDOR |
| GRI | 10 | GRIS |
| SAF | 7, 9, 10, 14, 15 | (FASTMARK?) |
| URU | 14 | URUGUAY |
| ASI | 15 | ASIA |

---

## 7. Gotchas

- **Read-only ERP**: NUNCA `UPDATE`/`DELETE`/`ALTER` sobre tablas existentes. Toda metadata de matching vive en `laset_import_staging.matched_*`. INSERTs a ERP son fase explícita de migración. Ver [[contexto#Regla cero: tablas ERP son read-only]].
- **`pedproi` no es solo impuestos**: además de "Percepción IIBB Caba", guarda **cargos extra** del pedido de compra con `cdescrip='camion'` y `nimporte`. Linkea a `pedprot.nNumPed`, NO a `pedclit`.
- **`stocks` sin `companyCode`**: filtrar por `cCodAlm`/`ID_ALMACEN` contra los almacenes de Laset.
- **`rebates` huérfana**: NO usar — schema primitivo, sin `companyCode`, restos de intento abandonado (creada con `NewTable` vacía el 2025-11-01).
- **CFE Uy ya existe**: 179 cabeceras + 1411 líneas. Si staging matchea con un `numeroCfe`, marcar `MATCHED`.
- **Branches case-insensitive macOS**: backend usa `Development` (mayúscula), frontend `development` (minúscula). Borrar la de minúscula puede romper la mayúscula. Recovery con `git reset --hard origin/<correcto>`.
- **Quality issues planilla**: fila 2 con SELECTORs, `Year=1900` (367 rows basura), 22 vacías, cols 45/66/67 sin header, `Invoice Date` y `DEPOSITO` duplicadas. Por eso staging es todo NVARCHAR lossless.

---

## 8. Próximos pasos

- [ ] Cargador PHP (lee `docs/laser.xlsx` con `phpoffice/phpspreadsheet`, popula `laset_import_batches` + `laset_import_staging`)
- [ ] Vistas de reconciliación read-only sobre staging + ERP
- [ ] Query de la identidad contable por SKU+almacén
- [ ] Heurística de matching → poblar `matched_*`
- [ ] Decidir modelo de rebates (`Sell out rebate`, `Reportado AMD/NVIDIA`)
- [ ] Migración del delta (UNMATCHED → INSERT a pedprot/pedprol/pedproi/pedclit/pedclil + pedclil_oc_asignacion)

---

## Ver también

- [[pedidos|Índice del proyecto]]
- [[arquitectura|Arquitectura]] — modelo canónico ERP, capas, DDL legacy
- [[contexto|Contexto]] — regla cero ERP, empresas activas, gotchas
- [[memoria|Memoria]]
- [[feature-asignacion-oc|Feature Asignación OC↔Venta]] — el linkeo que ya existe
- [[changelog#2026-05-14]] — sesión de discovery + creación de staging
- Doc canónico en repo: `docs/laset-import-framework.md`
- SQL DDL: `api-rest-pedidos-laravel/app/database/sql/2026_05_14_001_create_laset_import_staging.sql`
