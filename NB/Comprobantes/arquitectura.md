# Arquitectura

Arquitectura de [[Comprobantes]]: dos repos independientes desplegados por separado que se hablan por HTTP.

```
[ Nuxt SSR web app ]  --axios-->  [ Slim 4 API ]  --PDO sqlsrv-->  [ SQL Server (NB) ]
 servicio-compobante-pdf-web-app    microservicio-comprobantes-v2
```

Ver [[stack|tecnologías]] para versiones concretas.

## Servicio 1 — API (`microservicio-comprobantes-v2`)

### Bootstrap

`app/public/index.php` → `app/src/App/App.php` hace `require` en orden fijo de los archivos de wiring:

```
DotEnv → Container → ErrorHandler → Middlewares → Cors → Database → Services → Repositories → Routes → NotFound
```

### Container (Pimple)

DI con **Pimple** (`$container['foo'] = fn(...) => ...`), no PSR-11 moderno. Cada feature nueva se cablea en 3 lugares:

1. `app/src/App/Services.php` — registra el service
2. `app/src/App/Repositories.php` — registra el repository
3. `app/src/App/Routes.php` — registra la ruta HTTP → `App\Controller\XxxController:method`

### Capas

`Controller` (thin: parsea request, devuelve JSON) → `Service` (business logic) → `Repository` (SQL contra SQL Server).

- `src/Dto/` — shapes de la respuesta JSON (ReceiptDto, VoucherDto, etc.)
- `src/Support/` — adapters a sistemas externos: **FacturuUY**, **MSCobros**, **MSExpedicion**, **MSPostventa**, `TokenManager`.
- `src/Middleware/PermissionMiddleware.php` — valida JWT en el Authorization header.

### DB

PDO decorado en `src/App/Database.php` (`MyPdo` / `MyPdoStatement`) que loguea cada query vía Monolog (`LoggerLog`).

- DSN `sqlsrv:` → SQL Server en prod (datos de negocio de NB).
- `phinx.php` apunta a MySQL → DB **separada**, solo para estado local de la app. **No migraciones de negocio**, las de SQL Server requieren coordinación DBA.

### Auth

JWT Firebase. Dos variantes en paralelo por tipo de comprobante:

- Protegidas por header (`Authorization: Bearer ...`) → `->add(App\Middleware\PermissionMiddleware::class)`.
- Públicas por token en URL (ej: `/F/{receiptNumber}/{token}`) → validan el token one-shot embebido. **No** llevan middleware.

### Mapa de rutas

| Prefijo                                                     | Controller                        | Propósito                              |
|-------------------------------------------------------------|-----------------------------------|----------------------------------------|
| `/auth`                                                     | `Auth`                            | Login / emite JWT                      |
| `/F`, `/FUy`                                                | `ReceiptController`               | Facturas AR / UY (Facturu)             |
| `/voucherTypes`, `/CreateVoucher`, `/clientByCreateVoucher` | `VoucherController`               | Metadata y creación                    |
| `/I`                                                        | `AfterSaleController`             | After-sale (entrega/recepción)         |
| `/C`                                                        | `CobrosController`                | Cobros / movimientos de caja           |
| `/operationalOrder`                                         | `ExpedicionController`            | Órdenes operativas (volanta)           |
| `/dispatchVoucher`                                          | `DispatchController`              | Remitos                                |
| `/padron`                                                   | `PadronController`                | Lookups ARBA / AGIP                    |
| `/electricalCertificate`                                    | `ElectricalCertificateController` | Certificados eléctricos                |
| `/facturu`                                                  | `FacturuController`               | Integración Facturu UY                 |

## Servicio 2 — Web app (`servicio-compobante-pdf-web-app`)

### Dos paths de renderizado de PDF

**Importante:** conviven dos formas de generar el mismo PDF. Al tocar layout hay que revisar los dos, porque duplican lógica de jsPDF y pueden divergir.

1. **Client-side (legacy)** — páginas en `app/pages/voucher/**` hacen fetch a la API y construyen el PDF en el browser con `jspdf`. Un `.vue` por tipo de comprobante.
2. **Server-side (nuevo)** — `app/serverMiddleware/pdf-router.js` monta un router Express en `/api`, y `api/generar-pdf.js` arma el mismo PDF server-side llamando a la API PHP (`${API_HOST}/F/:id/:token`) y streamea la respuesta.

### Router manual

Nuxt no puede expresar `/voucher/F/:id/:token` al lado de `/voucher/F/:id` con routing por archivos. Solución: `nuxt.config.js > router.extendRoutes` registra manualmente las variantes con `:token`. **Regla:** si se agrega un `_id.vue` nuevo que también necesite variante con token, agregar la entrada en `extendRoutes`.

La ruta `/voucher/certificate/:id/qr` también vive ahí (Nuxt por default habría puesto `qr` primero).

### Query flags

- `show=1` — mostrar (no descargar)
- `print=1` — imprimir
- `unbranding=1` — ocultar logos (solo en F)
- En `/C`: `branch`/`cnumalb`, `id`, `bankId`, `ctaCteId`, `retentionId`, `simultaneousId` — mutuamente excluyentes con reglas específicas (ver `documentation.md` del repo).

## Mapeo URL Nuxt → API PHP

| Nuxt URL                                                  | API PHP                                     |
|-----------------------------------------------------------|---------------------------------------------|
| `/voucher/F/:id/:token`                                   | `GET /F/:receiptNumber/:token`              |
| `/voucher/afterSale/:type/:id/:token`                     | `GET /I/:afterSaleId/:token`                |
| `/voucher/C/:boxId` (+ query params)                      | `GET /C/:box`                               |
| `/voucher/remito/:id/:token`                              | `GET /dispatchVoucher/:pedido/:token`       |
| `/voucher/volanta/:pedido`                                | `GET /operationalOrder/:pedido`             |
| `/voucher/certificate/:id`, `/voucher/certificate/:id/qr` | `GET /electricalCertificate/:id`            |

Ver [[contexto]] para gotchas de dominio.

## Ver también

- [[Comprobantes]]
- [[stack]]
- [[contexto]]
- [[changelog]]
