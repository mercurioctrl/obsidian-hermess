# Arquitectura — CashBox Cobros

## Estructura del monorepo

```
/var/www/nb/cobros/
├── api-rest-cobros/      # Backend PHP 8.2 + Slim 4
│   ├── app/src/
│   │   ├── App/          # Bootstrap: Routes, Services, Repositories, Database
│   │   ├── Controller/   # Slim controllers (extienden Base)
│   │   ├── Service/      # Lógica de negocio
│   │   ├── Repository/   # SQL Server queries (sin ORM)
│   │   ├── Middleware/   # PermissionMiddleware, PermissionAdminMiddleware, etc.
│   │   ├── Domain/       # Patrón vertical slice (features nuevas)
│   │   └── Helper/       # Pagination, Filter, ExportExcel
│   └── docker/           # Dockerfile + apache config
└── cobros-web-app-v1/    # Frontend Nuxt 2 + Ant Design Vue
    └── app/
        ├── pages/        # Rutas (file-based routing)
        ├── components/   # Componentes Vue (Modal/, Table/)
        ├── store/        # Vuex modules
        └── assets/       # LESS, Ant Design theme overrides
```

## Patrones arquitectónicos

### Backend — dos patrones coexistentes

**Legacy (mayoría del código):**
```
Controller/{Feature} → Service/{Feature} → Repository/{Feature}
```
Registrados por string key en `Repositories.php` y `Services.php`, inyectados vía Pimple DI.

**Domain (features nuevas):**
```
Domain/{Feature}/{Action}/Controller + Repository
```
Vertical slice / use-case. Preferir para código nuevo.

### Request lifecycle
```
Route → Middleware (JWT + permisos) → Controller.__invoke() → Service → Repository → SQL Server
```

### Autenticación
- JWT emitido por el backend, enviado en header `Authorization: Bearer`
- `PermissionMiddleware` valida token y flag `cobro`
- `PermissionAdminMiddleware` valida flag `cobro_admin` (o `cobro`)
- Cada permiso nuevo tiene su propio middleware en `src/Middleware/`
- Token expuesto en el frontend vía `this.$auth.user.{permiso}`
- **Importante**: `AuthService::user()` construye el array manualmente — agregar campos nuevos ahí también

## Base de datos

- **SQL Server** — raw SQL parameterizado, sin ORM
- Bases: `NB_WEB`, `NEW_BYTES`, `NewBytes_DBF`
- Wrapper custom: `MyPdo` / `MyPdoStatement` en `Database.php`
- `BaseRepository::execute($sql, $fetchMode, $params)` — método estándar
- Tabla de clientes: `NewBytes_DBF.dbo.clientes` — nombre: `cnomcli`, razón social: `cnomcom`, CUIT: `cdnicif`

### Tabla creada para el módulo de préstamos
```sql
CREATE TABLE NEW_BYTES.dbo.MC_PRESTAMOS_CAPITAL (
    ID_PRESTAMO         INT             IDENTITY(1,1)   NOT NULL,
    ID_CLIENTE          INT                             NOT NULL,
    ID_CCMOVIMIENTO     INT                             NOT NULL,
    MONTO_TOTAL_USD     DECIMAL(18,4)                   NOT NULL,
    MONTO_TOTAL         DECIMAL(18,4)                   NOT NULL,  -- en moneda local
    ID_FORMAPAGO        INT                             NOT NULL,
    COTIZACION          DECIMAL(18,4)                   NOT NULL,
    USU_IDENTIFICACION  NVARCHAR(50)                    NOT NULL,
    OBSERVACIONES       NVARCHAR(200)                   NULL,
    CREATED_AT          DATETIME        DEFAULT GETDATE() NOT NULL,
    TIPO                CHAR(1)         NOT NULL        DEFAULT 'P',  -- 'P'=Préstamo, 'C'=Cobro
    CONSTRAINT PK_MC_PRESTAMOS_CAPITAL PRIMARY KEY (ID_PRESTAMO)
);
-- Columnas legacy (no usadas activamente):
-- PAGADO BIT, MONTO_PAGADO DECIMAL(18,4)
```

### Otras tablas clave del módulo
| Tabla | Base | Descripción |
|---|---|---|
| `MC_PRESTAMOS_CAPITAL` | NEW_BYTES | Ledger de préstamos (TIPO P/C) |
| `MC_CCORRIENTES_MOVIMIENTOS` | NEW_BYTES | Movimientos de CC del cliente |
| `MC_LOG_OPERACIONES` | NEW_BYTES | Log de operaciones por caja |
| `MC_SALDOS_CAJA` | NEW_BYTES | Saldo por caja y forma de pago |
| `MC_FORMAS_PAGO` | NEW_BYTES | Formas de pago y cotización |
| `permisos_agente` | NB_WEB | Permisos granulares por usuario/agente |

## Módulo de Préstamos de Capital — archivos

```
Backend:
  src/Controller/LendCapital/LendCapital.php          POST /lendCapital
  src/Controller/LendCapital/CapitalDebt.php          GET  /capitalDebt/{clientId}
  src/Controller/LendCapital/PayCapitalDebt.php       POST /payCapitalDebt
  src/Controller/LendCapital/CapitalDebtClients.php   GET  /capitalDebtClients
  src/Service/LendCapital/LendCapitalService.php
  src/Service/LendCapital/PayCapitalDebtService.php
  src/Repository/LendCapital/LendCapitalRepository.php
  src/Repository/LendCapital/PayCapitalDebtRepository.php
  src/Repository/LendCapital/CapitalDebtClientsRepository.php
  src/Middleware/PermissionLendCapitalMiddleware.php
  src/Middleware/PermissionPayCapitalMiddleware.php

Frontend:
  pages/capitalDebtClients.vue         Sección "Deudas de capital"
  store/capitalDebtClients.js          Store Vuex
  components/Modal/CapitalDebt.vue     Modal cuenta corriente de capital
  components/Modal/LendCapital.vue     Modal prestar capital
  components/Table/CtaCteCliente.vue   Botones en tabla de CC
  components/Table/TabMenu.vue         Ítem "Deudas de capital" en submenú Clientes
```

## Flujos del módulo de capital

### Prestar Capital (`POST /lendCapital`)
1. Middleware: `PermissionLendCapitalMiddleware` (requiere `prestar_capital=1`)
2. INSERT en `MC_CCORRIENTES_MOVIMIENTOS` (TR=30, positivo)
3. INSERT en `MC_PRESTAMOS_CAPITAL` (TIPO='P')
- **Sin impacto en caja** — el dinero físico sale por "Pagar al cliente"

### Cobrar Deuda (`POST /payCapitalDebt`)
1. Middleware: `PermissionPayCapitalMiddleware` (requiere `cobrar_capital=1`)
2. INSERT en `MC_LOG_OPERACIONES` (TR=42, aparece en vista Caja)
3. UPDATE `MC_SALDOS_CAJA` (suma saldo de caja)
4. INSERT en `MC_PRESTAMOS_CAPITAL` (TIPO='C')
- **Sin impacto en `MC_CCORRIENTES_MOVIMIENTOS`** — la CC del cliente no se toca

### Ver deuda por cliente (`GET /capitalDebt/{clientId}`)
- Devuelve todos los movimientos P/C del cliente ordenados ASC
- El saldo acumulado se calcula en el frontend fila por fila

### Vista de clientes con deuda (`GET /capitalDebtClients`)
- Agrupa MC_PRESTAMOS_CAPITAL por cliente
- Solo devuelve clientes con saldo (HAVING SUM ≠ 0)
- Columnas: totalLentUsd, totalPaidUsd, balanceUsd, totalLentLocal, totalPaidLocal, balanceLocal

### Permisos del módulo
| Permiso DB | Permiso JWT | Middleware | Protege |
|---|---|---|---|
| `prestar_capital` | `prestarCapital` | `PermissionLendCapitalMiddleware` | `POST /lendCapital` |
| `cobrar_capital` | `cobrarCapital` | `PermissionPayCapitalMiddleware` | `POST /payCapitalDebt` |
| `ver_capital` | `verCapital` | (frontend only) | Ojito en modal CapitalDebt |

## Módulo AFIP Purchases (Facturas de compra) — archivos

Compras a proveedores: remitos (Orders) y facturas (Invoices), con impuestos, divisas,
tipos de compra, almacenes y empresas. Grupo de rutas `/afipPurchases` protegido por
`PermissionMiddleware`.

```
Backend (src/{capa}/AfipPurchases/):
  Controller/  AllOrders, OrderDetail, InvoiceOrder, AllInvoices, InvoiceDetail,
               CreateInvoice, CheckInvoiceCsufac, CreateTax, AllTaxes,
               AllEmpresas, AllAlmacenes, AllTiposCompra, AllFormasPago,
               AllDivisas, AllAfipPurchases, AfipPurchaseDetail
  Service/     AfipPurchasesService, AfipOrdersService, AfipInvoicesService, AfipSharedService
  Repository/  AfipPurchasesRepository, AfipOrdersRepository, AfipInvoicesRepository, AfipSharedRepository
  Dto/         OrderListDto, OrderDetailDto, InvoiceListDto, InvoiceDetailDto, TaxDto, DivisaDto, ...
  Support/     CompanyCodes.php

Frontend:
  pages/afipPurchases.vue          Página con tabs Remitos / Facturas
  store/afipPurchases.js           Store Vuex
  components/AfipPurchases/         OrdersTab, InvoicesTab, InvoiceDetail, InvoiceTotals,
                                    ModalInvoice, ModalCompleteOrder, TaxesSelector
```

### Endpoints principales
| Método | Ruta | Uso |
|---|---|---|
| GET | `/afipPurchases/orders[/{filter}]` | Listar remitos (multi-sucursal) |
| GET | `/afipPurchases/orders/{id}` | Detalle de remito |
| POST | `/afipPurchases/orders/{id}/invoice` | Facturar un remito |
| GET | `/afipPurchases/invoices[/{filter}]` | Listar facturas |
| GET | `/afipPurchases/invoices/{id}` | Detalle de factura |
| POST | `/afipPurchases/invoices` | Crear factura |
| GET | `/afipPurchases/invoices/check` | Check de duplicado (por proveedor) |
| GET/POST | `/afipPurchases/taxes` | Listar / crear impuestos |
| GET | `/afipPurchases/{empresas,almacenes,tiposCompra,formasPago,divisas}` | Catálogos |

### Decisiones de diseño
- **Check de factura duplicada por proveedor**: la validación de número de factura usa
  `(número + proveedor)` en vez de número global — dos proveedores pueden repetir número.
- **Multi-sucursal**: los filtros de remitos/facturas soportan múltiples sucursales
  (`CompanyCodes.php` centraliza los códigos de empresa).
- Separación `AfipShared*` para lógica común entre Orders e Invoices.

## Trade Audit Logger

Auditoría estructurada del flujo de cobro (trade). Registra cada paso del `ExecuteTrade`
para trazabilidad.

```
src/Support/TradeAuditLog.php               Logger estructurado (formato de auditoría)
src/Service/Box/BoxTradeServiceAudit.php    Wrapper de auditoría sobre el trade
src/Repository/Box/BoxTradeRepositoryInterface.php   Interface para inyección/mock
src/Service/Bank/Transfer/CreditBankInterface.php    Interface para inyección/mock
tests/Unit/Service/Box/Trade/{BankPayment,BoxPayment}Test.php   Tests
```

- Se introdujeron **interfaces** (`BoxTradeRepositoryInterface`, `CreditBankInterface`)
  para poder testear el flujo de pago con mocks.
- Fixes de tipos: `movementBankId` de `nonTaxVoucher` casteaba mal `null → 0`; se ajustó
  el tipo de propiedad en `BoxTrade` para aceptar `BoxTradeServiceAudit`.

## Docker (dev)
- Container: `cobros-api-rest`, `network_mode: host`, Apache escuchando en **puerto 8083**
  (`docker/apache/ports.conf` → `Listen 8083`). `app/` montado por volumen (PHP live sin rebuild).
- Base reescrita a imagen `php:8.2-apache-bookworm` (Dockerfile local, no commiteado).
- DSN sqlsrv con `Encrypt=0; TrustServerCertificate=1` (`Database.php`, cambio local).
- OpenSSL legacy provider habilitado para compatibilidad TLS con SQL Server.
- `display_errors = Off` en PHP para evitar warnings en respuestas JSON.
- Frontend Nuxt 2 en **puerto 3002** vía PM2 (`ecosystem.config.js`, cluster 2 instancias,
  `NODE_OPTIONS=--openssl-legacy-provider`). Ver [[memoria]].

## Ver también
- [[stack]] · [[contexto]] · [[changelog]] · [[memoria]]