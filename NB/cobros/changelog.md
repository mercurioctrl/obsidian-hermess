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

---

## 2026-05-19 — Refinamientos del módulo de Préstamos de Capital

### fix: lendCapital no impacta la caja al prestar

- Se eliminó la llamada a `registerBox()` en `LendCapitalService::execute()`
- El préstamo ya **no** genera línea en la vista Caja (MC_LOG_OPERACIONES)
- La caja solo se impacta cuando el cliente paga con `payCapitalDebt`
- Archivos: `LendCapitalService.php`

### feat: pago de capital acepta monto en pesos

- Si se selecciona Pesos como forma de pago, el campo muestra "Importe $"
- Debajo aparece el equivalente en u$d con la cotización del día
- Conversión: `usd = pesos / quote` antes de enviar al backend
- El backend siempre recibe y almacena en USD
- Archivo: `CapitalDebt.vue`

### feat: montos ocultos por defecto + permiso ver_capital

- Al abrir el modal "Cuenta de Préstamos de Capital", todos los importes aparecen como ••••
- Ícono de ojo en el footer alterna entre oculto/visible
- Si el usuario no tiene `ver_capital=1`, el ojito muestra error sin revelar
- Archivo: `CapitalDebt.vue`

### feat: permisos granulares para el módulo de capital

Tres nuevos permisos en `NB_WEB.dbo.permisos_agente`:

```sql
ALTER TABLE NB_WEB.dbo.permisos_agente ADD prestar_capital BIT NOT NULL DEFAULT 0;
ALTER TABLE NB_WEB.dbo.permisos_agente ADD cobrar_capital  BIT NOT NULL DEFAULT 0;
ALTER TABLE NB_WEB.dbo.permisos_agente ADD ver_capital     BIT NOT NULL DEFAULT 0;
```

- `prestar_capital` → protege `POST /lendCapital` (`PermissionLendCapitalMiddleware`)
- `cobrar_capital` → protege `POST /payCapitalDebt` (`PermissionPayCapitalMiddleware`)
- `ver_capital` → controla visibilidad de montos en el frontend (no tiene middleware propio)
- Los tres permisos se incluyen en el JWT (`AuthRepository` — login y getById)
- Archivos: `AuthRepository.php`, `PermissionLendCapitalMiddleware.php`, `PermissionPayCapitalMiddleware.php`, `LendCapitalRoute.php`

## Ver también
- [[arquitectura]] · [[contexto]] · [[stack]]