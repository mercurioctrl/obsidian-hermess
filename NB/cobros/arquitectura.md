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
| `permisos_agente` | NB_WEB | Permisos granulares por usuario/agente |

## Módulo de Préstamos de Capital

### Flujo Prestar Capital (`POST /lendCapital`)
1. Middleware: `PermissionLendCapitalMiddleware` (requiere `prestar_capital=1`)
2. `LendCapitalService` → `LendCapitalRepository`
3. INSERT en `MC_CCORRIENTES_MOVIMIENTOS` (TR_CODIGO=30, CC_IMPORTEUSD positivo)
4. ~~INSERT en `MC_LOG_OPERACIONES`~~ — **eliminado**: la caja no se impacta al prestar
5. INSERT en `MC_PRESTAMOS_CAPITAL` (TIPO='P')
- **Nota**: el dinero físico sale por "Pagar al cliente", no por esta operación

### Flujo Cobrar Deuda (`POST /payCapitalDebt`)
1. Middleware: `PermissionPayCapitalMiddleware` (requiere `cobrar_capital=1`)
2. `PayCapitalDebtService` → `PayCapitalDebtRepository`
3. INSERT en `MC_CCORRIENTES_MOVIMIENTOS` (TR_CODIGO=42, CC_IMPORTEUSD negativo)
4. INSERT en `MC_LOG_OPERACIONES` (aparece en vista Caja)
5. UPDATE `MC_SALDOS_CAJA` (suma al saldo de caja)
6. INSERT en `MC_PRESTAMOS_CAPITAL` (TIPO='C')

### Convención de signos en MC_PRESTAMOS_CAPITAL
- `TIPO=P` (Préstamo): monto positivo — cliente debe dinero
- `TIPO=C` (Cobro): monto positivo — se cobra ese monto de la deuda
- Saldo = SUM(MONTO donde TIPO=P) - SUM(MONTO donde TIPO=C)
- Los pagos son libres (parciales, no atados a préstamo específico)

### Permisos del módulo
| Permiso DB | Permiso JWT | Middleware | Protege |
|---|---|---|---|
| `prestar_capital` | `prestarCapital` | `PermissionLendCapitalMiddleware` | `POST /lendCapital` |
| `cobrar_capital` | `cobrarCapital` | `PermissionPayCapitalMiddleware` | `POST /payCapitalDebt` |
| `ver_capital` | `verCapital` | (frontend only) | Ojito en modal CapitalDebt |

## Docker (dev)
- Container: `cobros-api-rest`, puerto `8083:80`
- OpenSSL legacy provider habilitado para compatibilidad TLS con SQL Server
- `display_errors = Off` en PHP para evitar warnings en respuestas JSON

## Ver también
- [[stack]] · [[contexto]] · [[changelog]]