# Cómo se importa Laset (comp=11): qué hace el front y qué queda por CLI

> Mapa operativo del import de la operación Laset al ERP de pedidos de NB
> (`companyCode = 11`). Responde tres preguntas: **qué se dispara solo desde la
> pantalla**, **qué hay que correr a mano**, y **de dónde sale cada dato**.
> Estado verificado sobre el código al 2026-09-16.

Ver también: [[Laset]] · [[import-proveedores-sli]] · [[feature-laset-import]] · [[feature-sync-laset-botones]] · [[feature-integrar-eccn]]

---

## ⚠️ Esto es el ERP de NB, no el ERP propio de Laset

Todo lo de acá corre en el **ERP de pedidos de NB** (monorepos `api-rest-pedidos-laravel`
+ `pedidos-web-app-v1`), donde Laset es la empresa `companyCode = 11`. **No** es el ERP
propio de Laset (`/var/www/laset`, `backLaset`/`frontLaset`, host `hermess-pc` — ver [[Laset]]).

---

## Resumen: las tres capas

| Qué | ¿Automático desde el front? | Dónde |
|---|---|---|
| Import de ventas/compras + **alta de proveedores, clientes y artículos** | **SÍ** | `/syncLaset` → "Importar todo" |
| Cuenta corriente de clientes y de proveedores | **SÍ**, botón propio | `/syncLaset` |
| Fixes de mantenimiento (marcas, proformas, re-vincular facturas, wipe) | **SÍ**, botón propio | `/syncLaset` |
| **ECCN / `Codigos SLI`** | **NO — sólo CLI** | `php artisan ecc:import-categorias` |
| **`Database Proveedores`** (datos fiscales del proveedor) | **No existe** | — |

---

## 1. El importador del front (`/syncLaset`)

### Botones disponibles

| Botón | Endpoint | Qué hace |
|---|---|---|
| **Importar todo** / **Importar seleccionadas (N)** | `POST /v1/laset/import-jobs` | Dispara la cadena completa (abajo) |
| (preview antes de importar) | `POST /v1/laset/import-jobs/preview` | Muestra qué se va a tocar |
| (seguimiento) | `GET /v1/laset/import-jobs/{id}` | Progreso por fase |
| **Importar cuenta corriente** | `POST /v1/laset/ccte-import` | Cta cte histórica de **clientes** |
| **Importar cta cte proveedores** | `POST /v1/laset/prov-ccte-import` | Cta cte histórica de **proveedores** (+ alta automática) |
| **Re-vincular facturas** | `POST /v1/laset/relink-facturas` | CFE Uruguay |
| **Fix marcas comp=11** | `POST /v1/laset/fix-marcas-comp11` | `articulo.Id_Marca` + cleanup `FP_Marcas` |
| **Completar proforma (CSUPROF)** | `POST /v1/laset/fix-csuprof-temp` | `pedprot.CSUPROF_TEMP` desde `vendor_pi` |
| **Borrar todo comp=11** | `POST /v1/laset/wipe-transactional` | Wipe transaccional (ver gotcha abajo) |
| (reimport de la planilla) | `POST /v1/laset/reimport` | Recarga el staging desde `Raw ventas FOB` |

Todos los botones de mantenimiento siguen el patrón **preview → confirmar**
(ver [[feature-sync-laset-botones]]).

### Qué encadena "Importar todo"

`LasetRunImportJobCommand` (`laset:run-import-job`), en este orden exacto:

```
1)   laset:aggregate-match              (sólo si hay UNMATCHED/NEW en el subset)
2)   laset:import-fase-c                ← acá se crean los maestros
3)   laset:import-fase-d  --skip-bloqueadas
3.5) laset:fix-albprol-faltante
3.6) laset:fix-stock-almacen-comp11
4)   reconciliación
```

Cada paso corta la cadena si devuelve exit code ≠ 0. Los pasos 3.5 y 3.6 son
idempotentes: si no hay gap, no hacen nada.

---

## 2. De dónde sale cada dato

### La fuente es UNA hoja: `Raw ventas FOB`

De la planilla `Cotizaciones y Proformas ….xlsx` — **3.400 filas × 67 columnas**.

```
scripts/laset_xlsx_to_json.py "Raw ventas FOB"   (openpyxl; PhpSpreadsheet tarda >15 min)
   → laset:import-staging
      → NewBytes_DBF.dbo.laset_import_staging
```

Mapa de columnas (`LasetImportStagingCommand::COLUMN_MAP`, 0-based) — las primeras:

| Col | Campo staging | | Col | Campo staging |
|---|---|---|---|---|
| 0 | `pais` | | 8 | `deposito` |
| 1 | `razon_social` | | 9 | `vendor_pi` |
| 2 | `destinatario_fiscal` | | 10 | `vendor_invoice` |
| 3 | `vendedor` | | 11 | `qty` |
| 4 | `invoice_date` | | 12 | `sku` |
| **5** | **`proveedor`** | | 13 | `description` |
| 6 | `marca` | | 14 | `categoria_producto` |
| 7 | `pais_proveedor` | | … | (hasta 66) |

### Los maestros se auto-crean en Fase C

Fase C resuelve cada nombre contra el maestro con **match exacto sobre `companyCode=11`**;
el que no matchea, **lo crea**:

```sql
-- Proveedor  (LasetImportFaseCCommand.php:1019)
INSERT INTO NewBytes_DBF.dbo.FP_Proveedores
    (CCODPRO, cnompro, NombreComercial, Fecha_Alta, CCODDIV, companyCode, Id_EstadoProveedor)
VALUES (?, ?, ?, SYSDATETIME(), ?, 11, 1)

-- Cliente
INSERT INTO NewBytes_DBF.dbo.clientes
    (ccodcli, cnomcli, cnomcom, ID_CLIENTE, ccodage, ccoddiv, ID_VENDEDOR, ID_DIVISA,
     CODEMP, companyCode, FECHA_ALTA, perfil)

-- Artículo (clona el "gemelo" de otra company, o lo crea desde cero con la planilla)
INSERT INTO NewBytes_DBF.dbo.articulo (...)
```

Códigos: `CCODPRO` / `ccodcli` = `MAX(CAST(… AS INT)) + 1`, padded a 6 dígitos.
**Secuenciales, sin significado.**

> **El punto clave:** `cnompro` = `NombreComercial` = **el string tal cual venía en la
> celda**. La fuente (`Raw ventas FOB`) trae el *nombre* del proveedor, no sus datos.
> Por eso los proveedores comp=11 no tienen dirección, país, CP ni ID fiscal.
> Ver [[import-proveedores-sli]] §7.

### Otras dos puertas de entrada de proveedores

| Comando | Nombre sale de |
|---|---|
| `laset:stock-only-autocreate-catalog` | Misma columna `proveedor`, líneas sin venta |
| `laset:prov-ccte-import` | **Nombre de la pestaña** del Excel de Estado de Cuenta |

Los tres insertan los mismos 5–7 campos.

---

## 3. Lo que NO está en el front

### ECCN / `Codigos SLI` — sólo CLI

En todo el grupo `Route::prefix('laset')` **no hay ningún endpoint de ECCN**. Lo único
expuesto es `POST /v1/ecc`, que es la **carga manual de un ECCN suelto** desde el detalle
de orden (el lapicito de la columna ECCN). El import masivo es únicamente por comando.

Procedimiento completo para correrlo en otro servidor:

```bash
# 1) El CSV tiene que estar en el server
#    app/database/data/eccCategorias.csv   (va versionado en el repo)

# 2) Aplicar los 2 DDL — en SSMS, por separado, respetando los GO (idempotentes)
#    database/sql/2026_05_21_001_create_ecc_familia_proveedor.sql   → en NewBytes_DBF
#    database/sql/2026_05_21_002_add_ecc_view_permission.sql        → en NB_WEB

# 3) Ensayo en seco: reporta el cruce, no escribe nada
php artisan ecc:import-categorias --dry-run

# 4) Importar
php artisan ecc:import-categorias
#    firma: [--path=<csv>] [--company=11] [--dry-run]
```

```sql
-- 5) Activar el permiso a cada usuario que deba ver el dato
UPDATE NB_WEB.dbo.permisos_agente SET eccView = 1 WHERE id_usuario_web = <UserId>;
```

**6) Los usuarios deben re-loguearse** — `eccView` viaja dentro del JWT, los tokens viejos
no lo traen.

Detalle del mapeo, decisiones de matching y verificación: [[import-proveedores-sli]].

### `Database Proveedores` — no existe

Ni front, ni CLI, ni parser, ni service. Es la hoja que tendría los datos fiscales de los
101 proveedores. Ver [[import-proveedores-sli]] para la spec de lo que habría que construir.

---

## 4. Equivalente CLI de la pantalla

Si en el otro servidor no tenés el front a mano, la cadena completa es:

```bash
# Cargar / recargar el staging desde la planilla
php artisan laset:import-staging --file="Cotizaciones y Proformas 2025.10.01.xlsx"

# La cadena que dispara "Importar todo"
php artisan laset:run-import-job <jobId>
#   o los pasos sueltos, en este orden:
php artisan laset:aggregate-match
php artisan laset:import-fase-c   --staging-ids=<ids>
php artisan laset:import-fase-d   --skip-bloqueadas
php artisan laset:fix-albprol-faltante
php artisan laset:fix-stock-almacen-comp11

# Cuentas corrientes
php artisan laset:ccte-import         # clientes
php artisan laset:prov-ccte-import    # proveedores

# ECCN (no tiene botón)
php artisan ecc:import-categorias
```

**Antes de cualquier proceso**, punto de restauración:

```bash
php artisan laset:snapshot     # ANTES
php artisan laset:restore      # deja todo como estaba
```

Ver [[feature-laset-snapshot-restore]].

---

## 5. Gotchas al llevarlo a otro servidor

- **El wipe por UI no sirve contra prod.** "Borrar todo comp=11" es síncrono y tarda ~1:28
  → siempre da timeout HTTP. Correrlo por CLI (`laset:wipe-transactional`). Falla atómico,
  no deja el wipe a medias.
- **Timeout de freetds en prod.** Las queries del wipe tardan 25s+ y el default de freetds
  las mata (error 20003). Hay que subir el timeout en `freetds.conf` — **fix efímero: vive
  dentro del container**, se pierde al recrearlo.
- **`laset:snapshot` es ciego a los huérfanos** que el wipe sí borra. Resguardarlos aparte.
- **El permiso viaja en el JWT** (`eccView`, `lasetView`): activarlo en la base no alcanza,
  hay que re-loguearse.
- **Match exacto en todos lados.** Cualquier variación de tipeo en la celda (`ASUS` vs
  `ASUS TEK`, con/sin `LTDA`) crea un maestro nuevo en vez de reusar el existente.
  Conviene revisar duplicados antes de dar por buena una corrida:

```sql
SELECT CCODPRO, cnompro, Fecha_Alta
  FROM NewBytes_DBF.dbo.FP_Proveedores
 WHERE companyCode = 11
 ORDER BY cnompro;
```

- **Regla cero:** todo `UPDATE`/`DELETE` lleva `WHERE … companyCode = 11`. NB=4, NBE=9,
  LO=12 son intocables. Ver [[contexto]].
- **"Planilla = verdad":** ante diferencia entre staging y ERP comp=11, gana la planilla.

---

## Pendientes

- [ ] Desplegar ECCN a **producción** (los 2 DDL + el import + activar `eccView`).
      Al 2026-05-21 estaba aplicado sólo en dev.
- [ ] Construir el import de `Database Proveedores` para completar dirección / país / CP /
      ID fiscal de los proveedores comp=11.

---
Última actualización: 2026-09-16
