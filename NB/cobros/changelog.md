# Changelog — CashBox Cobros

## 2026-07-09 / 2026-07-11

### análisis: Intimación AGIP percepciones IIBB CABA (no es cambio de código)

Diagnóstico completo de la intimación de AGIP/ARCIBA a NB (CUIT 30-70924663-8) por
$73.103.974,46 en percepciones de IIBB CABA (27 períodos, ene-2024→may-2026).

- Se parsearon los 27 anexos y se cruzó cada CUIT contra el **padrón de Regímenes
  Generales real de AGIP** (`ARDJU008MMYYYY`, uno por mes, bajados de agip.gob.ar).
- **Hallazgo (dos bloques):** Bloque A (2024/01–2025/05, ~$6,4M) los CUIT **sí** están
  en el padrón y la alícuota coincide exacto (235/235) → error real, rectificar.
  Bloque B (2025/06–2026/05, ~$66,7M = 91%) los CUIT **no** figuran en el padrón →
  aplicar 0% fue correcto → **contestable**.
- **Patrón del Bloque B:** 96% clientes de **provincia de Buenos Aires** + 92% con
  percepción **ARBA** (no CABA) → probable **error de jurisdicción** de AGIP.
- Entregables: `intimacion/Intimaciones_AGIP_percepciones.xlsx` (Resumen + 27 hojas),
  nota [[intimacion-agip-percepciones]] y borrador [[mail-estudio-contable]].
- Scripts en `intimacion/`: `parse_anexos.py`, `bajar_cruzar_padrones.py`, `armar_excel.py`,
  `padron_por_periodo.csv`, `anexos_consolidado.csv`. Todos los cruces DB fueron solo lectura.

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

---

## 2026-07-02 — Sync a ramas de integración + features nuevas en Development

### chore: ambos repos a rama de integración y `git pull`

- `api-rest-cobros`: `feature/prestamos-capital` → **`Development`** (fast-forward `91b9dc7..312014e`, 115 archivos). El feature de préstamos de capital ya quedó integrado.
- `cobros-web-app-v1`: `feature/prestamos-capital` → **`development`** (fast-forward `e07a40c..5c8cd7f`, 38 archivos).
- Build frontend OK (`npm run build` + `pm2 start ecosystem.config.js`, 2 instancias). Verificado en `http://localhost:3002` (302 → login). API respondiendo en `http://localhost:8083/v1`.
- Ver [[memoria]] / [[contexto]] para el detalle del setup local reproducible.

### feat: Módulo AFIP Purchases (Facturas de compra a proveedores)

Grupo de rutas `/afipPurchases` (backend), `pages/afipPurchases.vue` + `components/AfipPurchases/*` + `store/afipPurchases.js` (frontend). Gestiona **remitos (Orders)** y **facturas (Invoices)** de compra a proveedores, con impuestos, divisas, tipos de compra y almacenes.

- Endpoints: `GET /orders[/{filter}]`, `GET /orders/{id}`, `POST /orders/{id}/invoice`, `GET /invoices[/{filter}]`, `GET /invoices/{id}`, `POST /invoices`, `GET /invoices/check`, `GET /taxes` · `POST /taxes`, `GET /empresas|almacenes|tiposCompra|formasPago|divisas`.
- **Check de duplicados por proveedor**: la validación de número de factura ahora considera el proveedor (antes era global). Archivos: `ServiceAfipPurchases.php`, `AfipInvoicesRepository.php` + espejo en front `ModalInvoice.vue`.
- Soporte **multi-sucursal** en filtros de remitos y facturas.
- UI: `InvoiceDetail.vue`, `InvoiceTotals.vue`, `InvoicesTab.vue`, `OrdersTab.vue`, `ModalInvoice.vue`, `ModalCompleteOrder.vue`, `TaxesSelector.vue`.

### feat: Trade Audit Logger (auditoría del flujo de cobro)

- Logger de auditoría **estructurado** para el flujo de trade/cobro. Archivos: `src/Support/TradeAuditLog.php`, `src/Service/Box/BoxTradeServiceAudit.php`, interfaces `BoxTradeRepositoryInterface` / `CreditBankInterface`.
- Fix asociados: cast incorrecto `null → 0` en `movementBankId` de `nonTaxVoucher`; tipo de propiedad en `BoxTrade` para aceptar `BoxTradeServiceAudit`.
- Tests unitarios nuevos: `tests/Unit/Service/Box/Trade/BankPaymentTest.php`, `BoxPaymentTest.php`.

### Otros cambios que entraron en Development

- Permisos de usuario para ver/ocultar el dashboard (PED-1376): `middleware/permissions.js`, `plugins/permissions.js`, `store` y `layouts/basic.vue`.
- Columnas **FACTURA** y **RECIBO** en el Excel de cta cte (`ExportExcel.php`).
- Reporte de seguros "Sin Nominar": total facturado del período + date pickers habilitados (`CreditInsuranceReport`, `ExportExcelCreditInsurance.php`).
- Fix bancos en detalle de pedido dentro del modal de cobrar (filtrados desde `bank-accounts`).
- Workflow CI `deploy-gamma.yml` agregado en el frontend.

## Ver también
- [[arquitectura]] · [[contexto]] · [[stack]] · [[memoria]]

---

## 2026-07-08 — Dashboard de Impuestos por mes

### chore: sync a ramas de integración + levantar servicios

- Ambos repos ya estaban en su rama de integración (`Development` / `development`), `git pull` sin novedades.
- Backend `cobros-api-rest` ya corriendo (8083). Frontend: PM2 estaba vacío → `npm run build` + `pm2 start ecosystem.config.js` (2 instancias online, 3002).

### feat: Dashboard de Impuestos (Statistics/Taxes)

Nuevo dashboard que muestra la carga impositiva mensual (IVA a pagar, percepciones, retenciones). Verificado end-to-end contra la base real (`NB_WEB` @ `190.210.23.97:4444`).

**Backend (`api-rest-cobros`, patrón Domain):**
- `GET /statistics/taxes?between=DD-MM-YYYY_DD-MM-YYYY` (default: mes en curso), `PermissionMiddleware`.
- Dominio `src/Domain/Statistics/Taxes/` (Controller + Service + Repository), registrado en `Repositories.php` (`taxes_repository`), `Service/ServicesStatistics.php` (`taxes_service`), `Routes/StatisticsRoute.php`.
- Agrega por mes: **IVA a pagar** = débito (`FP_FactWebCliEncabezado.TOTIVAS_EnviadoAFIP`) − crédito (`AfipComprobantesRecibidos.total_iva`); **Percepciones IIBB** (`ImportePercepCLi`); **Retenciones IIBB** (`retentionIIBB.amountPaid`); **Retenciones Ganancias** (`ganancias.profit_amount`, tabla hoy vacía → 0).
- **Desglose por jurisdicción** (`jurisdictions`): ARBA (prov 2 Bs.As.) / AGIP (prov 1 CABA) / Otras (resto, con `children` por provincia). Retenciones con jurisdicción **exacta** (`retentionIIBB.provinceId`); percepciones **aproximadas** por provincia del cliente (`clientes.ID_PROVINCIA`) — reconcilia con el total.

**Frontend (`cobros-web-app-v1`):**
- `pages/dashboard/taxes.vue` (ruta Nuxt `dashboard-taxes`): selector de rango (mes en curso por defecto), tarjetas de totales, gráfico de barras (vue-chartjs), tabla mensual + fila de totales, y tabla "Por jurisdicción" con fila **Otras expandible** al detalle por provincia.
- `store/taxes.js` (módulo Vuex auto-registrado).
- Entrada de menú **"Impuestos"** en `layouts/basic.vue` (top-level, gateada por `$can('viewTaxes')`). Se agregó después del bloque Cobros para no romper los índices hardcodeados de `updateMenuPermissions`.

**Fix de entorno (dev, no commiteado):**
- `app/.env`: `DB_HOST`/`DB_PORT` pasados de `190.210.23.108:1433` (login timeout) a `190.210.23.97:4444` (alcanzable). Sin esto ni el front ni la API leían la base.

## Ver también
- [[arquitectura#Dashboard de Impuestos (Statistics/Taxes)]] · [[contexto]] · [[stack]] · [[memoria]]

---

## 2026-05-20 — Refinamientos y nuevas funcionalidades del módulo de capital

### fix: payCapitalDebt no toca la CC del cliente

- Se intentó primero un doble impacto (TR=30 + TR=42) para neto 0 en CC, pero el resultado era restar dos veces
- Decisión final: el cobro de capital **no toca MC_CCORRIENTES_MOVIMIENTOS para nada**
- Solo impacta: MC_LOG_OPERACIONES (caja) + MC_SALDOS_CAJA + MC_PRESTAMOS_CAPITAL TIPO='C'
- Archivos: `PayCapitalDebtRepository.php`, `PayCapitalDebtService.php`

### fix: verCapital no llegaba al frontend tras login

- `AuthService::user()` construye el array de usuario manualmente y no incluía los 3 permisos nuevos
- Fix: agregar `prestarCapital`, `cobrarCapital`, `verCapital` al array de `user()`
- Archivo: `AuthService.php`

### feat: fila de totales al pie de la tabla de movimientos de capital

- Muestra saldo total en u$d y en $ debajo de la tabla de movimientos
- El total en $ es la suma fila a fila de (amountUsd × quote de cada fila), no totalUsd × cotización actual
- Respeta el toggle de visibilidad (••••)
- Archivo: `CapitalDebt.vue`

### feat: sección "Deudas de capital" en el menú Clientes

**Backend (`GET /capitalDebtClients`):**
- Nuevo `CapitalDebtClientsRepository` que consulta `MC_PRESTAMOS_CAPITAL` agrupado por cliente
- Devuelve solo clientes con saldo ≠ 0
- Columnas: `clientId`, `clientName`, `totalLentUsd`, `totalPaidUsd`, `balanceUsd`, `totalLentLocal`, `totalPaidLocal`, `balanceLocal`
- Fix post-deploy: nombre de columna `cnomcli` (no `capeage/cnbrape/cnombre`)
- Archivos: `CapitalDebtClientsRepository.php`, `CapitalDebtClients.php` (controller)

**Frontend:**
- Nueva página `capitalDebtClients.vue` + store `capitalDebtClients.js`
- Tabla con montos prestados, cobrados y saldo en u$d y $
- Click en fila abre el mismo modal `CtaCteCliente` de siempre
- Nuevo ítem "Deudas de capital" en el submenú Clientes del `TabMenu.vue`
- El título del submenú cambia dinámicamente según la sección activa

## Ver también
- [[arquitectura]] · [[contexto]] · [[stack]]