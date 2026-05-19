# Changelog — CashBox Cobros

## 2026-05-18 / 2026-05-19

### feat: Módulo de Préstamos de Capital

**Backend (`api-rest-cobros` — rama `feature/prestamos-capital`):**
- `POST /lendCapital` — registra préstamo a cliente (MC_CCORRIENTES_MOVIMIENTOS + MC_LOG_OPERACIONES + MC_SALDOS_CAJA + MC_PRESTAMOS_CAPITAL)
- `GET /capitalDebt/{clientId}` — cuenta corriente de préstamos del cliente
- `POST /payCapitalDebt` — registra pago parcial (inserción con TIPO=C, inverso del préstamo)
- Fix `buildLoan()`: doble división por cotización cuando se prestaba en pesos → ahora `importUsd = amount` (ya convertido en prepareData)
- Tabla `MC_PRESTAMOS_CAPITAL` creada con columnas: `PAGADO`, `MONTO_PAGADO`, `TIPO`

**Frontend (`cobros-web-app-v1` — rama `feature/prestamos-capital`):**
- `CapitalDebt.vue` — modal tipo cuenta corriente: muestra todos los movimientos (P/C) con saldo acumulado por fila, botón "Registrar pago" al pie
- `LendCapital.vue` — modal para prestar capital (selector de monto, forma de pago, observaciones)
- `CtaCteCliente.vue` — agregados botones "Prestar Capital" y "Ver Deuda de Capital"

**DB (producción ejecutado manualmente):**
```sql
ALTER TABLE NEW_BYTES.dbo.MC_PRESTAMOS_CAPITAL ADD PAGADO BIT NOT NULL DEFAULT 0;
ALTER TABLE NEW_BYTES.dbo.MC_PRESTAMOS_CAPITAL ADD MONTO_PAGADO DECIMAL(18,4) NOT NULL DEFAULT 0;
ALTER TABLE NEW_BYTES.dbo.MC_PRESTAMOS_CAPITAL ADD TIPO CHAR(1) NOT NULL DEFAULT 'P';
```

**Fixes de entorno (dev, no commiteados):**
- OpenSSL legacy provider + SECLEVEL=0 en `/etc/ssl/openssl.cnf` → resuelve TCP Provider error 0x2746 con ODBC Driver 18
- `display_errors=Off` + `E_ALL & ~E_DEPRECATED` → evita que warnings de PHP 8.2 contaminen respuestas JSON
