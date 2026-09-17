# Import de "Database Proveedores" y "Codigos SLI" al ERP

> Reconstrucción **forense** (2026-09-16) del método con el que dos hojas de la
> planilla de Laset llegaron —o no— al ERP. Hecha sobre evidencia: git, código
> versionado, archivos en disco, transcripts de Claude Code, historial de shell y
> memoria del proyecto. **No se ejecutó ninguna importación ni se consultó la base.**
> Lo que no se pudo confirmar está marcado como **no determinado**.

Ver también: [[Laset]] · [[feature-integrar-eccn]] · [[feature-laset-import]] · [[feature-laset-cuenta-corriente-proveedores]]

---

## ⚠️ Alcance: hay dos "Laset" distintos

Esta investigación se hizo sobre el **ERP de pedidos de NB** (`/Users/hermess/www/pedidos`,
monorepos `api-rest-pedidos-laravel` + `pedidos-web-app-v1`), donde Laset es la
**empresa `companyCode = 11`**. Ahí es donde viven la planilla, el CSV y el importador.

**NO** se revisó el **ERP propio de Laset** (`/var/www/laset`, monorepos `backLaset`/`frontLaset`
de `LasetCorp`, host `hermess-pc`) — ver [[Laset]] y [[arquitectura]]. Esa máquina no es
alcanzable desde acá, así que sus transcripts (`~/.claude/projects/-var-www-laset/`) y su
git quedaron fuera. **Si algo de esto se hizo también allá: no determinado.**

---

## Veredicto

| Hoja | ¿Se importó al ERP? | Destino |
|---|---|---|
| **`Codigos SLI`** (~201 filas × 11 cols) | **SÍ** — feature [[feature-integrar-eccn\|integrarECCN]], 2026-05-21 | `NewBytes_DBF.dbo.ecc_familia_proveedor` |
| **`Database Proveedores`** (101 filas × 8 cols) | **NO hay evidencia de que se haya importado nunca** | — |

Y un dato que corrige la memoria de todos: **la fuente de `Codigos SLI` no fue
`Cotizaciones y Proformas ….xlsx` sino el archivo aparte `SLI.xlsx`** (probado abajo).

### Qué se revisó para afirmarlo

| Fuente | Resultado |
|---|---|
| Transcripts de Claude Code del proyecto (3 `.jsonl`) | `Database Proveedores` aparece **1 sola vez**, en un listado de hojas del xlsx (2026-07-17, comparando planilla dev vs. raíz). Ningún comando ni código de import de proveedores. La sesión del 2026-05-21 (cuando se hizo el ECCN) ya no existe en disco. |
| Git de ambos monorepos: `log --all`, `status`, `stash list`, `log --all --name-only --diff-filter=A` | Repos **limpios**, **sin stashes**, **sin nada sin commitear**. Aparece toda la cadena ECCN. **Nada** de un import de maestro de proveedores. |
| `scripts/*.py`, comandos `laset:*` / `ecc:*` (29), `Services/Laset/*` (11) | Existe el análogo de **clientes** (`Database Clientes`), no el de proveedores. |
| `.sql` / `.json` / `.csv` del proyecto, `/tmp`, `$HOME` | Único artefacto relacionado: `eccCategorias.csv`. |
| `~/.zsh_history` | Sin comandos relacionados. |
| Memoria de Claude + `CLAUDE.md` + esta bóveda | Documentan el feature ECCN; nada de import de proveedores. |

---

## 1. La fuente real fue `SLI.xlsx`, no la planilla de Cotizaciones

Comparación de contenido (clave = `Proveedor` + `PL`):

| Archivo | Filas de datos en `Codigos SLI` | Claves distintas |
|---|---|---|
| `SLI.xlsx` (raíz del monorepo, 2026-05-21) | 201 | 141 |
| `eccCategorias.csv` (lo que se importó) | 201 | 141 |
| `Cotizaciones y Proformas 2025.10.01.xlsx` | 205 | 145 |

- CSV vs `SLI.xlsx`: **diferencia cero** en ambas direcciones.
- CSV vs planilla de Cotizaciones: 20 claves de un lado, 24 del otro. La diferencia es
  sistemática: la planilla (más nueva) dice **`LST GLOBAL`** donde el CSV dice
  **`NEW BYTES INC`**, más filas nuevas.

Es decir: **el CSV es una foto de mayo 2026 y la planilla que hoy está en la raíz es posterior.**
Esto explica el gotcha registrado en su momento ("sin match: `NEW BYTES INC` = comp 4").

> Las dos copias del CSV en disco (raíz del monorepo y `app/database/data/`) tienen
> **contenido idéntico fila por fila**; sólo difieren en 202 bytes de fin de línea.

---

## 2. Qué se importó y adónde

| Tabla | Rol | Filtro de empresa |
|---|---|---|
| **`NewBytes_DBF.dbo.ecc_familia_proveedor`** | Destino real: matriz familia × proveedor → ECCN + posición arancelaria | **Sí** — `company_code`, importado con `--company=11` |
| `NB_WEB.dbo.permisos_agente` | Sólo DDL: columna BIT `eccView` | No aplica (tabla de auth) |

`FP_Proveedores`, `familias` y `articulo` **sólo se leen** para resolver claves; nunca se
escriben (regla de tablas ERP read-only, ver [[contexto]]).

Estructura de la tabla y su DDL: [[feature-integrar-eccn]].

---

## 3. Mapeo columna → campo

Header real del CSV:
`Proveedor, Direccion, Codigo Postal, EIN, PL, Código, ECCN (When Required), Firma, Teléfono, Mail, Puesto`

| # | Columna | ¿Se importa? | Campo destino | Tipo | Transformación |
|---|---|---|---|---|---|
| 0 | `Proveedor` | **Sí, como clave** | `ccodpro` | `NVARCHAR(10)` | Se **resuelve**: normaliza y busca en `FP_Proveedores` (`companyCode=11`) por `cnompro` **o** `NombreComercial`; guarda el `CCODPRO`. Sin match → fila descartada |
| 1 | `Direccion` | No | — | — | — |
| 2 | `Codigo Postal` | No | — | — | — |
| 3 | `EIN` | No | — | — | — |
| 4 | `PL` (product line) | **Sí, como clave** | `id_familia` | `INT` | Se **resuelve** contra `familias.cnomfam` (`companyCode=11`) → `ID_FAMILIA`. Sin match → fila descartada |
| 5 | `Código` (HS) | **Sí** | `codigo_arancelario` | `NVARCHAR(20)` NULL | `trim()`; vacío → `NULL` |
| 6 | `ECCN (When Required)` | **Sí** | `eccn` | `NVARCHAR(20)` NOT NULL | `trim()`, literal |
| 7 | `Firma` (firmante del SLI) | No | — | — | — |
| 8 | `Teléfono` | No | — | — | — |
| 9 | `Mail` | No | — | — | — |
| 10 | `Puesto` | No | — | — | — |

Campos que no vienen del CSV: `id` (IDENTITY), `company_code` = `11`, `origen` = `'C'`,
`created_at` = `SYSDATETIME()`, `updated_at` = NULL.

> **Las 7 columnas restantes (dirección, CP, EIN, firmante, teléfono, mail, puesto)
> quedaron sin importar.** Están en el CSV versionado pero ninguna query las lee. El
> documento SLI en sí lo genera el microservicio de comprobantes
> (`${COMPROBANTES}/voucher/laset/sli/{invoice}/{token}`, front commit `9d9c7ba`,
> 2026-05-22). **De dónde saca esos datos ms-comprobantes: no determinado** (ese repo no
> está en esta máquina).

### Hoja `Database Proveedores`

Header real (101 × 8): columna A sin título (alias), `RAZON SOCIAL PROVEEDOR`, `DIRECCION`,
`PAIS`, `CODIGO POSTAL`, `NRO ID FISCAL`, `PICK UP/DELIVERY`, `WAREHOUSE`.

**Mapeo: no existe.** No hay parser, comando, service, endpoint, SQL ni commit que la lea.

---

## 4. Procedimiento (lo que efectivamente se corrió)

Todo por **CLI**. **No hay pantalla del front para esta importación** — el front sólo
consume el resultado (columna ECCN en el detalle de orden) y permite carga manual fila a fila.

**0. Exportar la hoja a CSV.** `SLI.xlsx` hoja `Codigos SLI` → `eccCategorias.csv`, mismas
11 columnas, mismo orden, sin transformaciones. **Mecanismo exacto no determinado**: no hay
script de extracción versionado ni rastro en el historial de shell. Por la coincidencia
exacta de contenido y las fechas de archivo (ambos 2026-05-21), lo más probable es un
"Guardar como CSV" manual, pero **no está confirmado**.

**1. Dejar el CSV versionado** en `app/database/data/eccCategorias.csv`.

**2. Aplicar el DDL** (SSMS, por separado, respetando los `GO`; idempotentes):
```
database/sql/2026_05_21_001_create_ecc_familia_proveedor.sql   -- en NewBytes_DBF
database/sql/2026_05_21_002_add_ecc_view_permission.sql        -- en NB_WEB
```

**3. Ensayo en seco:**
```bash
php artisan ecc:import-categorias --dry-run
```

**4. Importar:**
```bash
php artisan ecc:import-categorias
# firma completa: [--path=<csv>] [--company=11] [--dry-run]
# --path default: database_path('data/eccCategorias.csv')
```

**5. Activar el permiso RBAC:**
```sql
UPDATE NB_WEB.dbo.permisos_agente SET eccView = 1 WHERE id_usuario_web = <UserId>;
```

**6. Re-loguear a los usuarios** — `eccView` viaja dentro del JWT.

> **No determinado**: fecha y orden exactos de ejecución de los pasos 2–5 (no hay
> transcript de esa sesión). Sí está confirmado el resultado y que los comandos son
> éstos, porque es el único camino que el código ofrece.

---

## 5. Código involucrado

Todo **commiteado**; nada pendiente ni en stash.

**Backend** — commit `2c87867e`, *"feat(ecc): clasificación ECCN por familia×proveedor"*,
2026-05-21 13:37:21 -0300, rama `integrarECCN` (ya contenida en `origin/Development`).

| Archivo | Rol |
|---|---|
| `app/Console/Commands/EccImportCategoriasCommand.php` | **El importador** |
| `database/data/eccCategorias.csv` | La data (201 filas, 26 proveedores, 38 product lines) |
| `database/sql/2026_05_21_001_create_*.sql` + `drop_*` | DDL + rollback de la tabla |
| `database/sql/2026_05_21_002_add_ecc_view_permission.sql` + `drop_*` | Permiso `eccView` |
| `app/Http/Controllers/Ecc/EccStore.php` + `routes/api.php:345` | `POST /v1/ecc` (carga manual, `origen='M'`) |
| `app/Repositories/Order/OrderRepository.php:696` | JOIN condicional en el detalle de orden |
| `app/Dto/Order/OrderItemDto.php`, `Dto/Auth/UserDto.php`, `Repositories/Auth/AuthRepository.php` | Gating por permiso + `eccView` en el JWT |

**Frontend** — commit `d0083b6`, *"feat(ecc): columna ECCN en el detalle de orden con carga
inline"*, 2026-05-21 13:39:00 -0300, rama `integrarECCN`.

### Núcleo del importador

Índices de columna hardcodeados:
```php
private const COL_PROVEEDOR = 0;
private const COL_PL        = 4;
private const COL_CODIGO    = 5;
private const COL_ECCN      = 6;
```

Normalización usada en todos los matches:
```php
$s = strtoupper(trim((string) $s));
$s = preg_replace('/\s+/', ' ', $s) ?? '';
$s = str_replace(['.', ','], '', $s);
```

Resolución de proveedor (doble índice, `cnompro` gana sobre `NombreComercial`):
```php
'SELECT ccodpro, cnompro, NombreComercial FROM NewBytes_DBF.dbo.FP_Proveedores WHERE companyCode = ?'
```

Persistencia idempotente, transaccional, en chunks de 200:
```php
$db->beginTransaction();
$deleted = $db->table(self::TABLE)
    ->where('company_code', $company)->where('origen', 'C')->delete();
foreach (array_chunk($payload, 200) as $chunk) { $db->table(self::TABLE)->insert($chunk); }
$db->commit();
```

---

## 6. Decisiones y gotchas

### Cómo se matchearon los proveedores
- **Por razón social normalizada, NO por ID fiscal.** El EIN está en el CSV (columna 3)
  pero el importador nunca lo lee. Match contra `FP_Proveedores.cnompro` y, como alias
  secundario, `NombreComercial`; siempre con `companyCode = 11`.
- **Match exacto, NO fuzzy** — decisión explícita del usuario (2026-05-21). Casi-matches
  (`CABLES`↔`CABLE`, `ODD`↔`OPTICAL DRIVE`, `FAN`↔`AIR COOLING`) quedan afuera **a
  propósito**, para no inventar clasificaciones aduaneras.
- Se usa `FP_Proveedores` (moderna), no la legacy `proveedo`.

### Sin match
- Fila sin match en **cualquiera** de los dos ejes → **se descarta**; el comando la reporta
  agrupada como warning. No se da de alta ningún proveedor ni familia.
- Filas con `Proveedor` o `PL` vacío, o completamente vacías → salteadas.
- En la corrida real: **2 proveedores** (`NEW BYTES INC`, que existe pero como `companyCode=4`,
  y `PNY TECHNOLOGIES INC`, inexistente en comp=11) y **18 categorías** sin familia comp=11.

### Duplicados
El CSV tiene 201 filas pero sólo 141 claves `(proveedor, PL)` distintas — trae duplicados por
diseño. El importador **deduplica por `(id_familia, ccodpro)`: gana la primera aparición**. Si
un duplicado trae **distinto** ECCN o distinto HS, lo trata como **conflicto**: los imprime y
**aborta sin escribir nada**. Que la importación haya terminado bien implica que no hubo
conflictos en ese CSV.

### Altas vs. actualizaciones
- No hay update fila a fila: es **reemplazo total del segmento `origen='C'` del company**
  (`DELETE` + `INSERT`).
- **Las filas `origen='M'` (carga manual desde el front) nunca se pisan** — ése es el motivo
  de que exista la columna `origen`.
- Por lo tanto el comando es **idempotente**.

### Otros
- **El permiso viaja en el JWT**: activar `eccView` en la base no alcanza, hay que **re-loguearse**.
- **Costo cero sin permiso**: el JOIN en `getOrderDetail` se concatena condicionalmente; sin
  `eccView` la query queda byte-idéntica.
- **El CSV está desactualizado** respecto de la planilla actual: para re-importar hoy habría que
  regenerar `eccCategorias.csv` desde la hoja `Codigos SLI` de `Cotizaciones y Proformas 2025.10.01.xlsx`
  (205 filas). Eso solo arregla el match `NEW BYTES INC` → `LST GLOBAL`, que existe como
  `CCODPRO 002607` en comp=11 (ver [[feature-laset-cuenta-corriente-proveedores]]).
- **dblib / SQL Server 2012**: el DDL evita `CREATE OR ALTER` y `DROP IF EXISTS`; el import usa
  inserts en batch en vez de loops de UPDATE.

### Qué falló
**Nada.** No hay registro de ninguna falla — ni en el transcript disponible, ni en el doc del
feature, ni en la memoria. Los 2 proveedores y 18 categorías sin match fueron **decisión
aceptada, no bug**: consecuencia directa de la política de match exacto.

---

## 7. `Database Proveedores`: qué existe en su lugar

No se importó, pero existe el **patrón hermano para clientes**, que es lo que habría que copiar:

- Hoja **`Database Clientes`** (685 × 15) → `NewBytes_DBF.dbo.clientes`, comp=11.
- Parser `scripts/laset_database_clientes_to_json.py` (xlsx → JSON).
- Service `Services/Laset/FixClientesDatosComp11Service.php`: `preview()`/`execute()`, match por
  razón social normalizada, **sólo rellena campos vacíos, nunca pisa**, país resuelto contra
  `FP_Paises` con tabla de alias, scopeado `companyCode = 11`, transaccional e idempotente.
- Comando `php artisan laset:fix-clientes-datos-comp11 --file=<xlsx> [--dry-run]`.
- Commit `a7eee599`. Completa `cdnicif` (ID fiscal), `cdircli` (dirección), `ID_PAIS`.

El otro lugar donde el sistema **escribe** proveedores comp=11 es el import de cuenta corriente
de proveedores ([[feature-laset-cuenta-corriente-proveedores]]), que da de alta los faltantes en
`FP_Proveedores` con `CCODPRO` secuencial — pero sólo con
`(CCODPRO, companyCode, NombreComercial, cnompro, Fecha_Alta)`, **sin** dirección, país, CP ni
ID fiscal.

> **O sea: los proveedores comp=11 están hoy "pelados" exactamente en los campos que trae la
> hoja `Database Proveedores`. Ésa es la brecha que esa hoja llenaría.**

---

## 8. Estado final

| Dato | Valor | Confianza |
|---|---|---|
| Filas de datos en el CSV importado | **201** | Verificado sobre el archivo |
| Claves `(proveedor, PL)` distintas | **141** | Verificado |
| Proveedores distintos en el CSV | **26** | Verificado |
| Product lines distintas | **38** | Verificado |
| **Vínculos insertados en `ecc_familia_proveedor` (dev)** | **94** (`origen='C'`, `company_code=11`) | Documentado el 2026-05-21; **no re-verificado contra la base** |
| Proveedores sin match | 2 | Documentado |
| Categorías sin familia | 18 | Documentado |
| Usuarios con `eccView` (dev) | 5 (agente 12 Catriel + 4 de Laset comp=11) | Documentado |
| **Producción** | Al 2026-05-21 los 3 SQL estaban aplicados **sólo en dev** ("falta prod"). **Si se aplicó después: no determinado** | — |

### Cómo verificarlo

```sql
-- 1) Total cargado, separando import (C) de carga manual (M)
SELECT company_code, origen, COUNT(*) AS filas
  FROM NewBytes_DBF.dbo.ecc_familia_proveedor
 GROUP BY company_code, origen
 ORDER BY company_code, origen;
-- Esperado en dev: company_code=11, origen='C' -> 94

-- 2) Desglose legible por proveedor y familia
SELECT p.cnompro AS proveedor, f.cnomfam AS familia,
       e.eccn, e.codigo_arancelario, e.origen, e.created_at
  FROM NewBytes_DBF.dbo.ecc_familia_proveedor e
  LEFT JOIN NewBytes_DBF.dbo.FP_Proveedores p
         ON p.CCODPRO = e.ccodpro AND p.companyCode = e.company_code
  LEFT JOIN NewBytes_DBF.dbo.familias f
         ON f.ID_FAMILIA = e.id_familia
 WHERE e.company_code = 11
 ORDER BY p.cnompro, f.cnomfam;

-- 3) Integridad: FK lógicas que no resuelven (deberían ser 0)
SELECT COUNT(*) AS huerfanas
  FROM NewBytes_DBF.dbo.ecc_familia_proveedor e
 WHERE e.company_code = 11
   AND ( NOT EXISTS (SELECT 1 FROM NewBytes_DBF.dbo.FP_Proveedores p
                      WHERE p.CCODPRO = e.ccodpro AND p.companyCode = e.company_code)
      OR NOT EXISTS (SELECT 1 FROM NewBytes_DBF.dbo.familias f
                      WHERE f.ID_FAMILIA = e.id_familia) );

-- 4) ¿Está el feature instalado?
SELECT OBJECT_ID('NewBytes_DBF.dbo.ecc_familia_proveedor', 'U') AS tabla_ecc;
SELECT COUNT(*) AS col_eccView
  FROM NB_WEB.sys.columns
 WHERE object_id = OBJECT_ID('NB_WEB.dbo.permisos_agente') AND name = 'eccView';
```

Sin tocar SQL, el mismo chequeo en seco:
```bash
php artisan ecc:import-categorias --dry-run
```
imprime filas del CSV, proveedores y familias comp=11 encontrados, vínculos resueltos y los sin
match — sin escribir nada.

**Para `Database Proveedores`:** nada que verificar — no hay filas cargadas desde esa hoja.

---

## Pendientes

- [ ] Confirmar si el feature ECCN llegó a **producción** (los 3 SQL + el import).
- [ ] Revisar el ERP propio de Laset (`/var/www/laset`, host `hermess-pc`) por si el import de
      `Database Proveedores` se hizo allá.
- [ ] Si se quiere completar el maestro de proveedores comp=11 (dirección, país, CP, ID fiscal):
      clonar el patrón de `Database Clientes` descrito en §7.

---
Fuente en el repo: `docs/import-proveedores-sli.md` (`api-rest-pedidos-laravel`, rama
`docs/import-proveedores-sli`, commit `5fc7667c`).
Última actualización: 2026-09-16
