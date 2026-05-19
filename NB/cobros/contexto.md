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
- **Al prestar**: NO se impacta la caja. El dinero físico sale por "Pagar al cliente"
- **Al cobrar**: SÍ se impacta la caja (suma saldo + log de operaciones)

### Visibilidad de montos en el modal de capital
- Por defecto los montos aparecen ocultos (••••) — privacidad ante terceros
- El ícono de ojo en el footer alterna la visibilidad
- Si el usuario no tiene `ver_capital=1`, el ojito muestra error y no revela

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
- En prod: pueden estar en `usuarios_nb`
- `AuthRepository` usa `ISNULL(permisos_agente.X, 0)` para compatibilidad

### Permisos del módulo de capital — patrón
- Cada permiso nuevo tiene su propio Middleware en `src/Middleware/`
- El permiso se agrega al JWT en ambas queries de `AuthRepository` (login y getById)
- Permisos solo de frontend (como `ver_capital`) no tienen middleware, se chequean en el componente

## Bugs conocidos (preexistentes, no del feature)
1. **Búsqueda por CUIT**: `C.ccodcli = {stringFilter}` sin comillas → falla si el input tiene `-`
2. **companyCode = "null"**: el frontend envía el string literal `"null"` cuando no hay companyCode

## TODOs / próximos pasos
- Ejecutar los ALTER en prod para los permisos: `prestar_capital`, `cobrar_capital`, `ver_capital`
- Merge de `feature/prestamos-capital` a main en ambos repos
- Fix bug CUIT search en `Client.php:441`
- Fix bug companyCode null en `Client.php:331`

## Ver también
- [[arquitectura]] · [[stack]] · [[changelog]]