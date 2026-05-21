# Feature: integrarECCN (ECCN por familia × proveedor)

> Clasificación **ECCN** (Export Control Classification Number) de la operación
> de exportación de Laset (`companyCode=11`). Primer paso: una tabla matriz que
> vincula familia de producto × proveedor → ECCN + código arancelario.

Branch: `integrarECCN` (back y front), creada 2026-05-21 desde `lasetImportFramework`.

---

## Qué es el ECCN

El **ECCN** es un string de normativa de exportación de EE.UU. (`EAR99`, `5A992`,
`4A994`, `4A001`, `5A992C`, …) que clasifica un producto para control de
exportación. No depende solo del producto: depende de **dos ejes** — el **tipo de
producto** (familia/categoría) y el **proveedor**. Conocido el ítem → su familia,
y asignada la OC (ver [[feature-asignacion-oc]]) → su proveedor, el ECCN queda
determinado.

## Tabla — `ecc_familia_proveedor`

Matriz de doble entrada en `NewBytes_DBF.dbo`. DDL:
`database/sql/2026_05_21_001_create_ecc_familia_proveedor.sql` (+ drop simétrico).

| Columna | Tipo | Nota |
|---|---|---|
| `id` | INT IDENTITY | PK |
| `company_code` | INT (def 11) | company de familia/proveedor |
| `id_familia` | INT | FK lógica → `familias.ID_FAMILIA` |
| `ccodpro` | NVARCHAR(10) | FK lógica → `FP_Proveedores.CCODPRO` |
| `eccn` | NVARCHAR(20) | ej. `EAR99`, `5A992` |
| `codigo_arancelario` | NVARCHAR(20) | HS code, ej. `8473.30.5100` |
| `origen` | CHAR(1) | `C`=CSV / `M`=manual (con CHECK) |
| `created_at` / `updated_at` | DATETIME2 | |

UNIQUE `(company_code, id_familia, ccodpro)`. Las FK son **lógicas, no enforced**
— no se acopla a tablas maestras del ERP (ver [[contexto#Regla cero: tablas ERP son read-only]]).

## Comando — `ecc:import-categorias`

```bash
php artisan ecc:import-categorias [--path= --company=11 --dry-run]
```

`app/Console/Commands/EccImportCategoriasCommand.php`. Lee el CSV fuente, resuelve
proveedor y familia por `companyCode` con **match exacto normalizado** (mayúsculas,
sin puntos/comas, espacios colapsados), y arma el vínculo familia × proveedor →
ECCN. Filas del CSV sin match en **ambos** ejes se descartan. **Idempotente**:
borra+reinserta las filas `origen='C'` del company; respeta las `origen='M'`.
Dblib-safe (un DELETE + INSERT batcheado, sin loop de UPDATE).

## Fuente de datos — `eccCategorias.csv`

`database/data/eccCategorias.csv` (versionado en el repo back). Columnas usadas:
Proveedor (0), PL=categoría (4), Código=HS (5), ECCN (6). El resto (dirección,
EIN, firma, contacto) se ignora.

## Decisión de diseño — solo match exacto

Decisión explícita del usuario (2026-05-21): el cruce CSV↔DB usa **solo matches
exactos**, NO fuzzy. Casi-matches como `CABLES`↔`CABLE`, `ODD`↔`OPTICAL DRIVE`,
`FAN`↔`AIR COOLING` quedan **afuera** a propósito — se resolverán en un paso
posterior si hace falta.

## Gotcha — tabla `familias`

`familias` (PK `ID_FAMILIA`, modelo `App\Models\Category`) ya tiene `companyCode`
y `defaultTariffPosition` (posición arancelaria HS por familia). La familia linkea
a artículos por `articulo.ID_FAMILIA = familias.ID_FAMILIA`.

## Estado — paso 1 (2026-05-21)

Tabla creada + comando corrido en dev: **94 vínculos** cargados (comp=11),
idempotencia verificada. Sin match:

- **2 proveedores** del CSV: `NEW BYTES INC` (es comp=4, no Laset) y
  `PNY TECHNOLOGIES INC` (no existe en comp=11).
- **18 categorías** del CSV sin familia comp=11 (ADAPTER, BAREBONE, CABLES,
  CAMERA, CHAIR, FAN, FLASH DRIVE, GADGET, LAPTOP, MEDIA PLAYER, MICRO SD, ODD,
  PAD, PERIPHERAL, SERVER, SMARTPHONE, TPM, WEBCAM).

---

## Ver también

- [[pedidos|Índice del proyecto]]
- [[feature-laset-import|Laset Import Framework]] — la operación comp=11 que esto clasifica
- [[feature-asignacion-oc|Asignación OC ↔ Venta]] — define el proveedor de cada línea
- [[contexto#Regla cero: tablas ERP son read-only]]
- [[changelog#2026-05-21 — Feature integrarECCN (paso 1)]]
- Código: `app/Console/Commands/EccImportCategoriasCommand.php`, `database/data/eccCategorias.csv`
- SQL: `database/sql/2026_05_21_001_create_ecc_familia_proveedor.sql`
