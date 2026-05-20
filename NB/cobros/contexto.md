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

## TODOs / próximos pasos
- ✅ ALTERs ejecutados en prod: `prestar_capital`, `cobrar_capital`, `ver_capital`
- ✅ Permisos asignados: agentes 27 y 66 → `cobrar_capital=1`; agente 12 → los 3 permisos
- Merge de `feature/prestamos-capital` a main en ambos repos
- Fix bug CUIT search en `Client.php:441`
- Fix bug companyCode null en `Client.php:331`

## Ver también
- [[arquitectura]] · [[stack]] · [[changelog]]