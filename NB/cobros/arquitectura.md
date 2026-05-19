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
│   │   ├── Middleware/   # PermissionMiddleware, PermissionAdminMiddleware
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
- `PermissionAdminMiddleware` valida flag `cobro_admin`
- Token expuesto en el frontend vía `@nuxtjs/auth-next`

## Base de datos

- **SQL Server** — raw SQL parameterizado, sin ORM
- Bases: `NB_WEB`, `NEW_BYTES`, `NewBytes_DBF`
- Wrapper custom: `MyPdo` / `MyPdoStatement` en `Database.php`
- `BaseRepository::execute($sql, $fetchMode, $params)` — método estándar

### Tablas clave del módulo de préstamos
| Tabla | Base | Descripción |
|---|---|---|
| `MC_PRESTAMOS_CAPITAL` | NEW_BYTES | Cuenta corriente de préstamos (TIPO P/C) |
| `MC_CCORRIENTES_MOVIMIENTOS` | NEW_BYTES | Movimientos de cuenta corriente del cliente |
| `MC_LOG_OPERACIONES` | NEW_BYTES | Log de operaciones por caja |
| `MC_SALDOS_CAJA` | NEW_BYTES | Saldo por caja y forma de pago |
| `MC_FORMAS_PAGO` | NEW_BYTES | Formas de pago y cotización |

## Módulo de Préstamos de Capital

### Flujo Prestar Capital
1. `POST /lendCapital` → `LendCapitalService`
2. INSERT en `MC_CCORRIENTES_MOVIMIENTOS` (TR_CODIGO=30, positivo)
3. INSERT en `MC_LOG_OPERACIONES`
4. UPDATE `MC_SALDOS_CAJA` (reduce saldo de caja)
5. INSERT en `MC_PRESTAMOS_CAPITAL` (TIPO=P)

### Flujo Cobrar Deuda
1. `POST /payCapitalDebt` → `PayCapitalDebtService`
2. INSERT en `MC_CCORRIENTES_MOVIMIENTOS` (TR_CODIGO=42, negativo)
3. INSERT en `MC_LOG_OPERACIONES`
4. UPDATE `MC_SALDOS_CAJA` (aumenta saldo de caja)
5. INSERT en `MC_PRESTAMOS_CAPITAL` (TIPO=C)

### Convención de signos en MC_PRESTAMOS_CAPITAL
- `TIPO=P` (Préstamo): monto positivo — cliente debe dinero
- `TIPO=C` (Cobro): monto positivo — se cobra ese monto de la deuda
- Saldo = SUM(P) - SUM(C)

## Docker (dev)
- Container: `cobros-api-rest`, puerto `8083:80`
- OpenSSL legacy provider habilitado para compatibilidad TLS con SQL Server
- `display_errors = Off` en PHP para evitar warnings en respuestas JSON

## Ver también
- [[stack]] · [[contexto]] · [[changelog]]
