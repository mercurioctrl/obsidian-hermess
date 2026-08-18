# Decisión: Listas de precios nombradas y extensibles por companyCode

> Estado: **planificado** (2026-08-18). Diseño acordado con Catriel. Aún sin implementar.

## Problema

Las listas de precios A–E están **hardcodeadas en 3 lugares**:
- `app/app/Support/Price.php` → `getLetra()`: fórmulas escritas a mano.
- `app/app/Repositories/Product/ProductRepository.php`: el SELECT solo trae `npvp1,npvp2,npvp5,npvp6`.
- Frontend `pedidos-web-app-v1/app/components/Orders/Detail.vue`: el dropdown muestra la letra cruda, no un nombre.

No se pueden nombrar las listas ni agregar nuevas sin editar PHP. Además cada empresa quiere **nombres distintos** para la misma lista.

## Composición actual (referencia, `Price.php::getLetra`)

Cliente normal (type != 1):
- **A** = `npvp1`
- **B** = `npvp1 - (npvp1 * ndto2 / 100)`
- **C** = `npvp1 - (npvp1 * ndto3 / 100)`
- **D** = `npvp5`
- **E** = `npvp6`
- Especiales: **SP** (si specialPrice>0) = `npvp5 + npvp5*specialPrice/100`; **MK** (si specialPriceFromCost>0) = `ncosteprom*(1+specialPriceFromCost/100)`; **PM** (precio manual, si no coincide con ninguna).
- Utilidad base (`categoryBaseUtility` / `itemBaseUtility`) se suma a A–E al final.
- La letra aplicada se persiste en `pedclil.listaPrecio`.

Qué lista le toca al cliente: `ntarifapp` (tabla clientes) → hoy mapeado en `ClientParametersService`. (1→A/B/C, 5→D, 6→E, 2→npvp2).

## Columnas disponibles en `articulo` (verificado 2026-08-18)

`npvp1..npvp6` y `ndto1..ndto6` (todas decimal). **NO existen npvp7/npvp8** (los ESTIP7/8 son solo % de margen, sin columna de precio).
→ Techo: **6 listas base** (una por npvp) + derivadas por descuento (ndtoN) + especiales (SP/MK/PM).

Hoy sin usar como lista: `npvp2, npvp3, npvp4` y `ndto1, ndto4, ndto5, ndto6`.

## Decisión: definiciones en datos + activación/nombre por companyCode (2 tablas)

**`priceList`** — definición global (la fórmula, igual para todas las empresas):

| columna | ejemplo | nota |
|---|---|---|
| id | 1 | |
| code | A, B, D… | **clave inmutable** (la que guarda `pedclil.listaPrecio`) |
| source_column | npvp1, npvp5 | qué npvpN |
| type | direct / discount / markup_from_cost / special | operación |
| discount_column | ndto2, ndto3 | solo para discount |
| default_ntarifapp | 1, 5, 6 | tarifa de cliente que cae acá por defecto |
| default_name | "Lista A" | fallback de nombre |
| sort_order | 10, 20 | orden display |

**`priceList_company`** — nombre + on/off por empresa:

| columna | ejemplo | nota |
|---|---|---|
| id | | |
| price_list_id | → priceList.id | |
| companyCode | 4, 11, 9 | |
| name | "Lista A" / "Minorista" | **el nombre varía por empresa** |
| active | 1/0 | switch de prendido/apagado |

### Ejemplo (requerimiento real)

Lista A: mismo `code=A`, `source_column=npvp1`, `type=direct`.
- companyCode **4 (NB)** → name = "Lista A"
- companyCode **11 (Laset)** → name = "Minorista"

companyCodes por ahora: **NB=4, Laset=11, NBE=9**.

## Invariantes / riesgos

- **`code` inmutable**: pedidos históricos lo referencian en `pedclil.listaPrecio`. Renombrar = cambiar `name`, nunca `code`. A–E se preservan.
- **Fallback de nombre**: si una empresa tiene la lista activa pero sin fila de nombre → usar `default_name` (o el `code`). Nunca vacío.
- **Qué companyCode manda**: el del **artículo** (`A.companyCode`, ya está en la query). Cuidado con casos cross-company (ver fix ya documentado).
- **Cast numérico en PHP** al leer npvp (driver pdo_sqlsrv local devuelve strings).
- El mapeo `ntarifapp → lista` debería leerse del catálogo (`default_ntarifapp`) para no dejar 2da fuente de verdad.

## Plan de trabajo

1. Migraciones de las 2 tablas + **seed que replica A–E exactas** para las empresas (nombres por empresa). Objetivo: **cero cambio de comportamiento** en el corte.
2. Refactor `Price.php::getLetra()` → **loop sobre listas activas filtradas por companyCode**, con cache por companyCode. Validar precios idénticos a hoy.
3. Ampliar SELECT de `ProductRepository` para traer todos los npvp1..npvp6 (+ ndto necesarios).
4. DTO de precio con `[{code, name, price}]` (o mapa de nombres al lado). `GET /v1/priceList` filtrado por companyCode/active.
5. Frontend `Detail.vue`: dropdown por `name`, sigue mandando `code`.
6. Validación end-to-end activando una lista hoy inactiva (ej. npvp2/npvp3) en una empresa de prueba.

Pasos 1–2 son el corazón: refactor puro respaldado por el seed, no debe mover ningún precio.

## Alcance elegido

"Catálogo en tabla + loop" (sin ABM por ahora; activación/nombres vía seed/SQL). El ABM sin deploy queda como mejora futura.

---

## Implementación paso 1 (2026-08-18) — HECHO en dev

Rama `feature/listas-precios-nombradas` en ambos repos.

### Columnas de la tabla `priceList` (ya existía vacía en NewBytes_DBF.dbo)
Preexistentes: `id (identity, SIN PK)`, `natarifappId (NOT NULL)`, `name`, `description`, `algorithm`, `commission`.
Agregadas: `code`, `source_column`, `type`, `discount_column`, `default_active (bit)`, `sort_order`, **`color` (nvarchar(9), hex '#RRGGBB')**.
Índice: `UX_priceList_code` (único plano, NO filtrado — ver quirk abajo).

### Tabla nueva `priceList_company` (override por empresa)
`id`, `price_list_id` (FK lógica, no enforced), `companyCode`, `name`, `active (bit)`, **`color`**, `UX (price_list_id, companyCode)`.

### Resolución efectiva (nombre + color + active)
```sql
COALESCE(pc.name,  pl.name)           -- nombre
COALESCE(pc.color, pl.color)          -- color
COALESCE(pc.active, pl.default_active) -- prendido/apagado
FROM priceList pl LEFT JOIN priceList_company pc ON pc.price_list_id=pl.id AND pc.companyCode=@cc
```
Si la empresa no tiene fila → hereda el default global. Listas nuevas nacen `default_active=0`.

### columnaCompanyCode verificados en articulo
4=NB (23844 art.), 9=NBE (1461), 10=? (10), 11=Laset (924).

### Ejemplo real sembrado
Lista A: NB(4)="Lista A" #1677FF; NBE(9) hereda; Laset(11)="Minorista" #13C2C2.

### Quirks del driver dblib/FreeTDS del container (¡importantes!)
- **Índice filtrado** (`WHERE ... IS NOT NULL`) → todo INSERT falla con **20018** (exige ANSI_NULLS/QUOTED_IDENTIFIER ON, que dblib tiene OFF). Usar índice único **plano**.
- **`IF NOT EXISTS(SELECT) + INSERT`** en un batch `unprepared()` → **20019** "results pending". Usar `INSERT ... SELECT ... WHERE NOT EXISTS`.
- **`unprepared()` multi-statement** (varias sentencias + GO) ejecuta **solo la primera**. `USE`/`SET` en batch aparte SÍ persisten a llamadas siguientes; para `CREATE TABLE` en otra DB, abrir conexión Laravel con `database` override (default del container = NB_WEB, no NewBytes_DBF).
- **Crear UNIQUE/PK** vía dblib exige setear antes (sentencias sueltas): `SET QUOTED_IDENTIFIER/ANSI_NULLS/ANSI_PADDING/ANSI_WARNINGS/CONCAT_NULL_YIELDS_NULL ON`.
- `priceList.id` es IDENTITY pero **sin PK** → no se puede declarar FK que lo referencie: FK lógica.
- El `.sql` para el DBA (sqlcmd, SET options ON por default) usa la forma canónica; estos workarounds son solo para aplicar en dev vía el driver viejo.

### Pendiente (próximos pasos)
2. Refactor `Price.php::getLetra()` a loop data-driven por companyCode.
3. Ampliar SELECT de `ProductRepository` (npvp3/npvp4).
4. DTO con `[{code, name, color, price}]` + `GET /v1/priceList` filtrado por companyCode/active.
5. Frontend `Detail.vue`: dropdown por nombre + chip de color.
6. Validación activando una lista hoy inactiva.

---

## Paso 2 (2026-08-18) — HECHO y validado: refactor de Price::getLetra() data-driven

Archivos:
- **Nuevo `app/app/Support/PriceListCatalog.php`**: `forCompany($companyCode)` devuelve las listas ACTIVAS de la empresa (code, source_column, type, discount_column, name, color) con `COALESCE(pc.X, pl.X)`. Cacheado 300s (memo por request + `Cache::remember`, mismo criterio que products.currency_quote). Si las tablas no existen o falla la query → devuelve `[]` (try/catch).
- **`app/app/Support/Price.php`**:
  - `getLetra()` ahora es un dispatcher: pide el catálogo por `companyCode`; si está vacío → `getLetraLegacy()` (código original intacto, fallback seguro); si no → `getLetraFromCatalog()`.
  - `getLetraFromCatalog()`: itera el catálogo y arma `$this->priceList[code]`. SP/MK/PM y utilidad base (categoría > ítem) se mantienen igual. `adivinarLetra`/`adivinarLetraSave` sin cambios.
  - `computeListValue()`: direct = npvpN; discount = npvpN - npvpN*ndtoN/100; markup_from_cost = ncosteprom*(1+spc/100). Redondeo a 5 igual que legacy.

**Deploy seguro**: si el backend deploya antes de que el DBA corra el SQL, el catálogo da `[]` y usa el legacy → cero riesgo. Como legacy y catálogo dan resultados idénticos para A–E, la transición es transparente.

**Validación**: 400 productos × 6 escenarios (type 0/1, categoryBaseUtility, itemBaseUtility, specialPrice, specialPriceFromCost) × todas las empresas = **2400 comparaciones, 0 diferencias** en priceList, letra y savedPriceList (getLetraLegacy vs getLetraFromCatalog por reflexión).

Falta: paso 3 (ProductRepository npvp3/4), 4 (DTO con name/color + GET /v1/priceList filtrado), 5 (frontend), 6 (validación activando lista nueva).
