# Contexto — CashBox Cobros

## Reglas de negocio importantes

### Sistema de cajas
- Cada usuario tiene una caja identificada por `USU_IDENTIFICACION`
- Los saldos de caja se almacenan en `MC_SALDOS_CAJA` por forma de pago
- Las formas de pago principales: 1=Dólares, 2=Pesos

### Cuenta corriente de clientes
- `MC_CCORRIENTES_MOVIMIENTOS`: cada movimiento tiene TR_CODIGO que indica el tipo
  - TR=30: Créditos varios (solo al prestar capital)
  - TR=42: Cobro efectivo (aparece en log de caja)
- `CC_IMPORTEUSD` es siempre en dólares; positivo = crédito al cliente, negativo = cobro

### Cotización
- Todas las cuentas guardan valores en dólares
- El importe en pesos se deriva: `monto_usd * cotizacion`
- La cotización del día se obtiene de `MC_FORMAS_PAGO.FP_COTIZACION`

### Préstamos de capital (`MC_PRESTAMOS_CAPITAL`)
- `TIPO=P`: préstamo otorgado al cliente
- `TIPO=C`: cobro/pago recibido del cliente
- El saldo = SUM(P.MONTO_TOTAL_USD) - SUM(C.MONTO_TOTAL_USD)
- Los pagos son parciales y libres — no están atados a un préstamo específico
- **Al prestar**: impacta CC (TR=30 positivo), NO impacta caja
- **Al cobrar**: NO impacta CC, SÍ impacta caja (log + saldo)

### Visibilidad de montos en el modal de capital
- Por defecto los montos aparecen ocultos (••••)
- El ícono de ojo en el footer alterna la visibilidad
- Si el usuario no tiene `ver_capital=1`, el ojito muestra error y no revela

### Total en pesos en el modal de capital
- No es `totalUsd × cotización actual`
- Es la suma fila a fila de `amountUsd × quote` de cada movimiento individual

### Dashboard de Impuestos (carga impositiva mensual)
- **IVA a pagar** = IVA débito (ventas, `TOTIVAS_EnviadoAFIP`) − IVA crédito (compras, `AfipComprobantesRecibidos.total_iva`). Negativo = saldo técnico a favor.
- **Carga impositiva total** del mes = IVA a pagar + percepciones IIBB + retenciones IIBB + retenciones ganancias.
- **Jurisdicciones** (`FP_Provincias.Id_Provincia`): AGIP = 1 (Capital Federal), ARBA = 2 (Buenos Aires), resto = "Otras".
- **Retenciones IIBB**: jurisdicción exacta (cada registro tiene `provinceId`).
- **Percepciones IIBB**: NO tienen jurisdicción a nivel factura → se aproximan por la provincia registrada del cliente (`clientes.ID_PROVINCIA`). Es aproximado (cliente multi-jurisdicción puede no ser fiel) pero reconcilia con el total.
- La tabla `NEW_BYTES.dbo.ganancias` (retenciones ganancias) está **vacía** hoy → esa categoría muestra 0 hasta que se carguen datos.
- `MS_REMITO_PERCEPCIONES.IMPPERCEP_ARBA/CABA` NO sirve para desglosar percepciones: cubre solo remitos (miles vs millones), no reconcilia con `ImportePercepCLi`.

## Decisiones tomadas

### Fix OpenSSL para SQL Server (dev)
- ODBC Driver 18 + OpenSSL 3.0 necesita `SECLEVEL=0` y legacy provider en `/etc/ssl/openssl.cnf`

### display_errors = Off
- PHP 8.2 emite E_DEPRECATED por static trait methods → contamina respuestas JSON
- Solución: `display_errors=Off` + `error_reporting = E_ALL & ~E_DEPRECATED`

### AuthService::user() — mapeo manual
- El endpoint `/user` construye el array de permisos manualmente
- **Cualquier permiso nuevo en AuthRepository debe agregarse también en AuthService::user()**
- Error detectado: `verCapital` llegaba en el token del login pero no del refresh

### payCapitalDebt — sin impacto en CC
- Se intentó doble movimiento (TR=30 + TR=42 negativos) para neto 0 en CC, pero restaba doble
- Decisión final: el cobro de capital no toca CC; solo impacta caja

### Columnas de nombre en clientes
- `NewBytes_DBF.dbo.clientes`: nombre = `cnomcli`, razón social = `cnomcom`, CUIT = `cdnicif`
- No usar `capeage`/`cnbrape`/`cnombre` (son columnas de agentes/otra tabla)

## Bugs conocidos (preexistentes, no del feature)
1. **Búsqueda por CUIT**: `C.ccodcli = {stringFilter}` sin comillas → falla si el input tiene `-`
2. **companyCode = "null"**: el frontend envía el string literal `"null"` cuando no hay companyCode
3. **`/heartbeat` da 500 aunque la base esté OK**: `Repository/Health/HeartbeatRepository` arma su propio PDO **sin** `Encrypt=0; TrustServerCertificate=1`, entonces el ODBC Driver 18 falla la verificación del certificado self-signed. La conexión real (`src/App/Database.php`) sí los incluye y funciona. No confiar en el heartbeat para saber si la base está viva.
4. **DB host en `app/.env`** (gitignored): server alcanzable = `190.210.23.97:4444` (DB `NB_WEB`). Traía `190.210.23.108:1433` que da login timeout. Si el front no carga datos, revisar `DB_HOST`/`DB_PORT`.

## Convención de ramas (importante)

La rama de integración tiene distinta capitalización en cada repo:
- `api-rest-cobros` → **`Development`** (D mayúscula), staging `Gamma`, prod `main`
- `cobros-web-app-v1` → **`development`** (minúscula), staging `gamma`, prod `main`

Ramas de trabajo con prefijos de ticket Jira: `COB-<n>-...`, `API-COB-...`, `APP-COB-...`, `PED-...`.

## TODOs / próximos pasos
- ✅ ALTERs ejecutados en prod: `prestar_capital`, `cobrar_capital`, `ver_capital`
- ✅ Permisos asignados: agentes 27 y 66 → `cobrar_capital=1`; agente 12 → los 3 permisos
- ✅ `feature/prestamos-capital` integrado en `Development`/`development` (2026-07-02)
- Fix bug CUIT search en `Client.php:441`
- Fix bug companyCode null en `Client.php:331`

## Ver también
- [[arquitectura]] · [[stack]] · [[changelog]] · [[memoria]]