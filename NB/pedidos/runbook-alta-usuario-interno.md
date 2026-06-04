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
