# Feature: Cuentas bancarias por empresa (a dónde transferir)

Muestra en **"Pedido + Info"** las cuentas bancarias de la **empresa de facturación del cliente** (`clientes.voucherCompanyCode`), para que el vendedor/cliente sepa a dónde transferir. Implementado 2026-09-09.

Rama en ambos repos: `feature/cuentas-bancarias-transferencia` (backend desde `Development`, frontend desde `development`).
PRs: backend #1638 (→Development) / #1639 (→blu-dev-staff); frontend #1332 (→development) / #1333 (→blu-dev-staff).

## Tabla nueva

`NewBytes_DBF.dbo.empresas_cuentas_bancarias` — **1:N** contra `FP_Empresas` (una empresa puede tener N cuentas, distintos bancos/monedas).

| Columna | Tipo | Nota |
|---|---|---|
| `id` | `INT IDENTITY` PK | |
| `company_code` | `INT` | → `FP_Empresas.CODEMP` (relación **lógica**, sin FK física) |
| `bank_name` | `NVARCHAR(100)` | "Banco Macro", "Banco Santander" |
| `currency` | `NVARCHAR(3)` | `ARS`/`USD`, con CHECK |
| `account_number` | `NVARCHAR(34)` | CBU/cuenta como **texto** (preserva ceros a la izq.) |
| `account_alias` | `NVARCHAR(60)` NULL | "DIGITO.MACRO" |
| `label` | `NVARCHAR(150)` NULL | display: "Banco Macro - Cuenta en pesos" |
| `active`, `sort_order`, `created_at`, `updated_at` | | operativos |

- **El CUIT NO va acá**: ya está en `FP_Empresas.CNIF` (es de la empresa, no de la cuenta).
- **`company_code` es INT** (matchea `clientes.CODEMP`/`voucherCompanyCode`, ambos INT). `FP_Empresas.CODEMP` es `nvarchar(2)` con padding (`'05'`), por eso no hay FK física. Ver [[relacion-companycode]].
- `.sql` versionados: `app/database/sql/2026_09_09_001_create_empresas_cuentas_bancarias.sql` (+ `_drop_`).
- **Seed inicial:** solo Digito Binario SRL (`CODEMP 5`): Macro ARS, Santander USD, Santander ARS.

## Backend

Endpoint reutilizado: `GET /v1/aboutOrder/{branch}-{order}` (el de "Pedido + Info").

- `OrderRepository::aboutOrder` — agrega `clientes.voucherCompanyCode` (SELECT + GROUP BY).
- `CompanyRepository::bankAccountsByCompanyCode(int $code): array` — cuentas `active=1` ordenadas por `sort_order`.
- `CompanyBankAccountDto` — mapea la fila a camelCase (`bankName`, `accountNumber`, `accountAlias`, `label`…).
- `AboutOrderInfoDto` — nuevo `?int voucherCompanyCode`.
- `AboutOrderDto` — nuevo `array bankAccounts` (se adjunta en el service, no en el constructor).
- `OrderService::aboutOrder` — si `voucherCompanyCode > 0`, resuelve `CompanyRepository` vía `app()` y llena `bankAccounts`. Si es `NULL`/`0` → `[]`.

## Frontend (`pages/orders.vue`)

- **Sección verde colapsable** debajo del textarea del modal Pedido + Info: renglón único "Recordá pasar los datos correctos para transferencia" + flechita (`a-icon type="down"`) que rota 180° al expandir. Estado `bankAccountsExpanded` (default `false`, se resetea al cerrar el modal).
- Al expandir: por cada cuenta muestra banco, tag de moneda (ARS azul / USD cyan), cuenta/CBU y alias, con botones de copiar (`copyBankData` → `navigator.clipboard` + `$notification`).
- Computed `orderBankAccounts` = `infoOrder.bankAccounts || []`.
- **También se inyecta en el texto del textarea** (`getTextoInfoPedido`), para que se copie/descargue (txt/PDF) junto con el pedido.

## Pendientes / despliegue

- ⚠️ Correr el `.sql` de creación en la base destino (staging/prod) antes de mergear — hoy la tabla **solo existe en dev**. Sin la tabla, `aboutOrder` no rompe (devuelve `bankAccounts: []`).
- Cargar las cuentas de las demás empresas (NB=4, NBE=9, Pisos=10, Laset=11) — hoy solo está Digito Binario (5).
- No hay ABM de cuentas todavía: se cargan por SQL directo.

## Ver también

- [[relacion-companycode]] — mapeo CODEMP por empresa
- [[feature-pdf-fiscal-por-empresa]] — datos del emisor por `companyCode` desde `FP_Empresas`
- [[changelog]] — entrada 2026-09-09
