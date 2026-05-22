# Feature: integrarECCN (ECCN por familia × proveedor)

> Clasificación **ECCN** (Export Control Classification Number) de la operación
> de exportación de Laset (`companyCode=11`): una tabla matriz familia × proveedor
> → ECCN, el ECCN visible por ítem en el detalle de la orden, y carga manual.

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

Fuente: `database/data/eccCategorias.csv` (versionado en el repo back). Columnas
usadas: Proveedor (0), PL=categoría (4), Código=HS (5), ECCN (6).

## Decisión de diseño — solo match exacto

Decisión explícita del usuario (2026-05-21): el cruce CSV↔DB usa **solo matches
exactos**, NO fuzzy. Casi-matches como `CABLES`↔`CABLE`, `ODD`↔`OPTICAL DRIVE`,
`FAN`↔`AIR COOLING` quedan **afuera** a propósito.

## Permiso RBAC — `eccView`

Columna `NB_WEB.dbo.permisos_agente.eccView` (SQL
`2026_05_21_002_add_ecc_view_permission.sql`, `DEFAULT 0`). Se agregó a las dos
queries de `AuthRepository` (`login()` + `getByToken()`) y a `UserDto` → viaja en
el JWT y en el objeto `user`. Frontend: `$can('eccView')` (`plugins/permissions.js`),
mismo patrón que `lasetView`.

**Gotcha**: los tokens emitidos **antes** de este deploy no traen `eccView` → el
usuario necesita re-loguearse para que el backend y el front lo vean.

## Integración en el detalle de orden

`GET /v1/orders/{branch}-{order}` — cada ítem trae `ecc: { value, editable }`
**solo si el usuario tiene `eccView`**:

- El JOIN se concatena **condicionalmente** a la query (`OrderRepository::getOrderDetail`,
  fragmentos `$eccSelect`/`$eccApply`). Sin permiso la query queda byte-idéntica a
  la original → **cero penalización de performance** para quien no lo tiene.
- `value` = ECCN resuelto por (familia, proveedor de la OC asignada). `editable` =
  la clave es resoluble (hay familia y hay OC asignada).
- El proveedor de la OC sale de `pedclil_oc_asignacion` con `OUTER APPLY TOP 1`
  (sin fan-out aunque la línea tenga varias OC).
- Gating del campo en el JSON: `OrderItemDto::$ecc` es propiedad tipada **sin
  default**; solo se asigna con `property_exists($product,'ecc_value')` → sin
  permiso queda sin inicializar y `json_encode` la omite del response.

Frontend (`components/Orders/Detail.vue`): columna **ECCN** en la tabla de ítems,
`visible: $can('eccView')`.

## Carga manual del ECCN

Cuando un ítem tiene `ecc.value = null` y `editable = true`, el front muestra un
**lápiz** que abre un **popover inline** (input + Guardar).

- Endpoint: `POST /v1/ecc` (`Http/Controllers/Ecc/EccStore.php`, invokable). Body
  `{pedclilId, eccn}`. Resuelve `(company_code, id_familia, ccodpro)` desde la línea
  y hace **upsert** en `ecc_familia_proveedor`.
- Marca `origen='M'`: una corrección manual **no la pisa** un futuro
  `ecc:import-categorias` (que reemplaza solo `origen='C'`).
- Como la tabla se indexa por (familia, proveedor), cargar el ECCN una vez lo
  resuelve para **toda línea futura** con esa misma clave. Tras guardar, el front
  refresca el detalle (`refreshModalOrder`) para que todas las líneas con esa clave
  dejen de verse en null.
- Gateado por `eccView` (403), 422 si la línea no tiene familia u OC asignada.
- API front: `$api.ecc.save(pedclilId, eccn)` en `plugins/api.js`.

## Gotcha — tabla `familias`

`familias` (PK `ID_FAMILIA`, modelo `App\Models\Category`) ya tiene `companyCode`
y `defaultTariffPosition` (posición arancelaria HS por familia). La familia linkea
a artículos por `articulo.ID_FAMILIA = familias.ID_FAMILIA`.

## Estado — 2026-05-21

Todo aplicado y probado **solo en dev**; **commiteado y pusheado** a la rama
`integrarECCN` (back `2c87867e`, front `d0083b6`):

- Tabla `ecc_familia_proveedor` + **94 vínculos** del CSV (comp=11). Sin match: 2
  proveedores (`NEW BYTES INC`=comp 4, `PNY TECHNOLOGIES INC` inexistente comp=11)
  y 18 categorías del CSV sin familia comp=11.
- Permiso `eccView` activado a **5 usuarios**: agente 12 (Catriel) + 4 de Laset
  comp=11 (nhuang, fmansilla, azamudio, asilvera).
- Columna ECCN en el detalle de orden con carga manual.
- **Pendiente prod**: los 3 SQL (`2026_05_21_00{1,2}`) están aplicados solo en dev.

## Deploy a producción

En orden:

1. **DDL** — correr cada script por separado en SSMS/sqlcmd (respetan `GO`, idempotentes):
   - `2026_05_21_001_create_ecc_familia_proveedor.sql` → crea la tabla en `NewBytes_DBF`.
   - `2026_05_21_002_add_ecc_view_permission.sql` → agrega la columna `eccView` en `NB_WEB`.
   - No pegar el `create`/`add` junto con su `drop_*` en la misma ventana (SSMS ejecuta todo y deshace lo creado).
2. **Poblar la tabla** — `php artisan ecc:import-categorias` (requiere `database/data/eccCategorias.csv` en el server). Carga los ~94 vínculos.
3. **Activar el permiso** — `UPDATE NB_WEB.dbo.permisos_agente SET eccView=1 WHERE id_usuario_web = <UserId>` para cada usuario que deba verlo (resolver el `UserId` por `usuarios_nb.UserName`, ya que los IDs pueden diferir entre dev y prod).
4. **Re-login** — los usuarios deben volver a loguearse: el permiso viaja en el JWT y los tokens viejos no lo traen.

---

## Ver también

- [[pedidos|Índice del proyecto]]
- [[feature-laset-import|Laset Import Framework]] — la operación comp=11 que esto clasifica
- [[feature-asignacion-oc|Asignación OC ↔ Venta]] — define el proveedor de cada línea
- [[contexto#Regla cero: tablas ERP son read-only]]
- [[changelog#2026-05-21 (cont.) — integrarECCN: permiso, detalle de orden y carga manual]]
- Código back: `EccImportCategoriasCommand.php`, `Http/Controllers/Ecc/EccStore.php`, `OrderRepository::getOrderDetail`
- SQL: `database/sql/2026_05_21_001_*` (tabla), `2026_05_21_002_*` (permiso)
