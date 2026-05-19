# Contexto — CashBox Cobros

## Reglas de negocio importantes

### Sistema de cajas
- Cada usuario tiene una caja identificada por `USU_IDENTIFICACION`
- Los saldos de caja se almacenan en `MC_SALDOS_CAJA` por forma de pago
- Las formas de pago principales: 1=Dólares, 2=Pesos

### Cuenta corriente de clientes
- `MC_CCORRIENTES_MOVIMIENTOS`: cada movimiento tiene TR_CODIGO que indica el tipo
  - TR=30: Créditos varios (préstamo de capital)
  - TR=42: Cobro efectivo (pago de deuda)
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
- Se puede prestar N veces y cobrar en cuotas distintas al total de cada préstamo

## Decisiones tomadas durante el desarrollo

### Fix OpenSSL para SQL Server (dev)
- ODBC Driver 18 en Debian 12 con OpenSSL 3.0 necesita `SECLEVEL=0` y legacy provider
- Se configura en `/etc/ssl/openssl.cnf` y persiste en el Dockerfile

### display_errors = Off
- PHP 8.2 emite E_DEPRECATED por static trait methods en 40+ archivos
- Estos warnings contaminaban el JSON de respuesta causando falsos CORS errors
- Solución: `display_errors=Off` + `error_reporting = E_ALL & ~E_DEPRECATED`

### Columnas de permisos en dev vs prod
- En dev: `cobro`, `cobro_admin`, `edit_credit`, `cobro_adjust_to` están en `permisos_agente`
- En prod: están en `usuarios_nb`
- `AuthRepository` usa `ISNULL(permisos_agente.X, 0)` para compatibilidad

## Bugs conocidos (preexistentes, no del feature)
1. **Búsqueda por CUIT**: `C.ccodcli = {stringFilter}` sin comillas → falla si el input tiene `-` (llega como `%`)
2. **companyCode = "null"**: el frontend envía el string literal `"null"` cuando no hay companyCode

## TODOs / próximos pasos
- Fix bug CUIT search en `Client.php:441`
- Fix bug companyCode null en `Client.php:331`
- Deploy del feature `prestamos-capital` en producción (pendiente compilar front)

## Ver también
- [[arquitectura]] · [[stack]] · [[changelog]]
