# Alta de usuario interno

Proceso para dar de alta un nuevo agente/usuario interno en el sistema de pedidos.

## Tablas involucradas

| Tabla | Base de datos | Propósito |
|---|---|---|
| `agentes` | `NewBytes_DBF.dbo` | Registro del agente en el ERP |
| `clientes` | `NewBytes_DBF.dbo` | Cliente propio del agente (para compras internas) |
| `usuarios_nb` | `NB_WEB.dbo` | Cuenta de acceso web |
| `permisos_agente` | `NB_WEB.dbo` | Permisos y roles dentro del sistema |

## Pasos

### 1. Determinar claves a usar

```sql
-- Próximo ccodage disponible
SELECT MAX(CAST(ccodage AS INT)) + 1 FROM [NewBytes_DBF].[dbo].[agentes]

-- Próximo ccodcli disponible (formato 6 dígitos con ceros a la izquierda)
SELECT MAX(CAST(ccodcli AS INT)) + 1 FROM [NewBytes_DBF].[dbo].[clientes]
```

Notas:
- `autonum` en agentes es columna **IDENTITY** → no insertar, se genera solo
- `UserId` en usuarios_nb es columna **IDENTITY** → no insertar, se genera solo
- `id` en permisos_agente es columna **IDENTITY** → no insertar
- `ID_CLIENTE` en clientes **no es identity** → insertar manualmente
- `ccodcli` sigue el patrón `sprintf('%06d', ID_CLIENTE)` (ej: 99755 → "099755")

### 2. Preparar hashes para usuarios_nb

```php
$userPass  = md5($passwordPlano);         // → UserPass
$userHash  = md5($userName);              // → UserNameMd5, softToken, hardToken
$authToken = strtoupper(substr($userHash, 0, 16)); // → authorizationToken, handedToken
```

### 3. INSERT agentes

Copiar de un agente template (ej: ccodage 55 = Lucas Mena).  
Cambiar: `ccodage`, `capeage`, `cnbrage`, `cemail`, `ID_VENDEDOR` (= nuevo ccodage int).  
**No incluir `autonum`** (identity).

Campos relevantes a mantener del template:
- `companyCode = 4`
- `activo = 1`
- `niva = 1`
- `cnacage = 'ARGE'`
- `xRemitoVto`, `dtoMax`, `dtoGral`, `firma_puesto`

### 4. INSERT clientes

El agente tiene su propio cliente en la tabla `clientes` (para compras internas, RMA, etc).  
Copiar del cliente propio del agente template.  
**Buscar por:** `SELECT * FROM clientes WHERE cnomcli LIKE '%APELLIDO%NOMBRE%'`

Cambiar: `ccodcli`, `ID_CLIENTE`, `cnomcli`, `email`, `ccodage` (= nuevo, como string), `ID_VENDEDOR` (= nuevo int), `FECHA_ALTA = GETDATE()`.  
Limpiar: `ULTIMA_COMPRA = NULL`, `ULTIMO_VENDEDOR = NULL`, `FECHA_CAMBIO_VENDEDOR = NULL`.

Campos relevantes a mantener del template:
- `niva = 3`
- `ccodpago = 'CO'`
- `ccodgrup = '17'`
- `ccoddiv = 'DOL'`
- `ntarifapp = 1`
- `ndocidenti = 4`
- `ID_PAIS = 7`, `ID_CIUDAD = 20891`, `ID_PROVINCIA = 1`
- `companyCode = 4`, `CODEMP = 4`, `voucherCompanyCode = 4`

### 5. INSERT usuarios_nb

Copiar de un usuario template (ej: UserId 62195 = lmena).  
**No incluir `UserId`** (identity).

Cambiar:
- `UserName` = usuario (ej: `ldellavecchia`)
- `UserPass` = md5(contraseña)
- `UserEmail` = email
- `UserNameMd5` = md5(usuario)
- `agente` = nuevo ccodage (int)
- `codigoFP` = nuevo ccodcli (string con ceros, ej: "099755")
- `nomPmostrar` = usuario
- `softToken` = md5(usuario)
- `hardToken` = md5(usuario)
- `authorizationToken` = strtoupper(substr(md5(usuario), 0, 16))
- `handedToken` = strtoupper(substr(md5(usuario), 0, 16))

Limpiar: `carritoActivo = NULL`, `ck_session = NULL`, `ssid = NULL`, `ssid_update = NULL`, sesión/IP/browser = NULL.

### 6. INSERT permisos_agente

La forma más segura es clonar el registro del usuario template en PHP:

```php
$lucas = DB::connection()->select("SELECT * FROM [NB_WEB].[dbo].[permisos_agente] WHERE id_usuario_web = 62195");
$p = (array)$lucas[0];
unset($p['id']); // identity
$p['agente_fp']      = $nuevoCcodage;
$p['id_usuario_web'] = $newUserId; // obtenido después del INSERT de usuarios_nb

$colsList     = implode(', ', array_map(fn($c) => "[$c]", array_keys($p)));
$placeholders = implode(', ', array_fill(0, count($p), '?'));

DB::connection()->statement(
    "INSERT INTO [NB_WEB].[dbo].[permisos_agente] ($colsList) VALUES ($placeholders)",
    array_values($p)
);
```

> ⚠️ No armar el VALUES a mano: la tabla tiene 108 columnas, es muy fácil descontar. Usar siempre el approach dinámico de PHP.

### 7. Verificar

```sql
SELECT ccodage, capeage, cnbrage, cemail, ID_VENDEDOR, activo
FROM [NewBytes_DBF].[dbo].[agentes] WHERE ccodage = '101'

SELECT ccodcli, cnomcli, email, ID_CLIENTE
FROM [NewBytes_DBF].[dbo].[clientes] WHERE ccodcli = '099755'

SELECT UserId, UserName, UserEmail, agente, codigoFP, activa
FROM [NB_WEB].[dbo].[usuarios_nb] WHERE UserName = 'ldellavecchia'

SELECT id, agente_fp, id_usuario_web
FROM [NB_WEB].[dbo].[permisos_agente] WHERE id_usuario_web = 83729
```

## Ejemplo concreto — Lucca Román Dellavecchia (2026-06-04)

| Campo | Valor |
|---|---|
| `ccodage` / `ID_VENDEDOR` | 101 |
| `ccodcli` / `ID_CLIENTE` | 099755 / 99755 |
| `UserId` | 83729 |
| `UserName` | ldellavecchia |
| `UserEmail` | ldellavecchia@nb.com.ar |
| `permisos_agente.id` | 67 |
| Template usado | Lucas Mena (ccodage 55, UserId 62195) |
| Contraseña inicial | mst895623 |

## Notas adicionales

- `agentes.ccodage` es varchar pero numéricamente correlativo con `agentes.ID_VENDEDOR` (int)
- `usuarios_nb.agente` = ccodage como int → vincula la cuenta web con el agente ERP  
- `permisos_agente.agente_fp` = ccodage del agente
- El campo `'statistics'` en permisos_agente tiene comillas simples en el nombre de columna (es palabra reservada) → usar `[statistics]` en queries
- Todo el proceso se ejecuta dentro de una transacción (`DB::beginTransaction()` / `DB::commit()`)

## ⚠️ Empresa del usuario (companyCode)

El alta soporta cualquier empresa. El `companyCode` va en **4 lugares**:
- `agentes.companyCode`
- `clientes.companyCode`, `clientes.CODEMP`, `clientes.voucherCompanyCode`
- `usuarios_nb.companyCode`

Valores: **4=NB, 9=NBElectric (NBE), 5=Digito Binario, 11=Laset**.
Ojo: `antonellalo` (template NB) tiene `usuarios_nb.companyCode` **vacío**, pero un usuario NBE real (`acarou`) lo tiene en **9** → para NBE hay que setearlo explícitamente en 9.

`permisos_agente` NO lleva companyCode duro (solo `unlockedCompanyFilter`, que es un permiso): se clona tal cual del template para respetar "los mismos permisos que X".

## ⚠️ GOTCHA CRÍTICO — segfault del driver pdo_sqlsrv con datetime

El driver `pdo_sqlsrv` viejo del container **crashea (Segmentation fault)** al reinsertar valores `datetime` tal como los devuelve el `SELECT *`. Al leer, formatea las fechas como `'May 31 2026 12:00:00:AM'`, que NO se puede reconvertir a datetime → el proceso muere sin error atrapable.

**Peor aún:** `php artisan tinker` **enmascara el segfault como exit 0** e imprime solo las líneas previas al crash. Parece que "no pasó nada" cuando en realidad murió.

### Reglas para que funcione

1. **NO correr el script con tinker.** Correrlo como PHP bootstrapeado normal para ver el error real:
   ```php
   // /tmp/alta_run.php
   require '/var/www/app/vendor/autoload.php';
   $app = require '/var/www/app/bootstrap/app.php';
   $app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();
   use Illuminate\Support\Facades\DB;
   // ... logica ...
   ```
   ```bash
   docker exec -i api-rest-pedidos-apirest-laravel bash -lc 'php /tmp/alta_run.php; echo "EXIT=$?"'
   ```
   EXIT=139 = SIGSEGV (el driver crasheó). EXIT=0 con COMMIT OK = éxito real.

2. **Poner en NULL todas las columnas `datetime` del clon**, salvo `FECHA_ALTA = date('Y-m-d H:i:s')`. Una cuenta nueva no arrastra fechas del template.
   - `clientes` datetime a nulear: `dateModified`, `FECHA_CAMBIO_VENDEDOR`, `ID_DIVISA_BK_DATE`, `percepcion_vencimiento`, `percepcion_vencimiento_arba`, `ULTIMA_COMPRA`.
   - `usuarios_nb` datetime a nulear: `ssid_update`, `dateCreateToken`, `last_wp_update`.
   - `permisos_agente`: no tiene columnas datetime.

3. **Sanitizar `'' → null`** antes de insertar (el driver viejo devuelve NULL como `''`).

4. Usar **INSERT con valores literales escapados** (`N'...'`, comillas duplicadas), no bind de parámetros — más robusto con este driver y ~110 columnas.

5. `SET NOCOUNT ON` al inicio de la conexión (por las dudas, aunque estas tablas no tienen triggers).

## Ejemplo concreto — Maximiliano Salomon / NBE ELECTRIC (2026-07-15)

| Campo | Valor |
|---|---|
| `ccodage` / `ID_VENDEDOR` | 102 |
| `ccodcli` / `ID_CLIENTE` | 100964 / 100964 |
| `UserId` | 84051 |
| `UserName` | msalomon |
| `UserEmail` | msalomon@nbe.com.ar |
| `companyCode` | **9 (NBE ELECTRIC)** — en agentes, clientes (companyCode/CODEMP/voucherCompanyCode) y usuarios_nb |
| `permisos_agente.id` | 68 |
| Template usado | antonellalo (ccodage 47, UserId 47847, permisos id 38) |
| Nota | Permisos clonados de antonellalo (NB), pero empresa NBE (9). Targets personales (`monthlyTargetAmount`, etc.) reseteados a 0. |

## Ver también
- [[relacion-companycode]] — mapa de companyCode por empresa (9=NBElectric/NBE)
- [[contexto]] — reglas de negocio y multi-empresa
- [[pedidos]] — índice del proyecto
