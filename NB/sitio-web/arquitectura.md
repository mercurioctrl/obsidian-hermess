# Arquitectura

Ver índice: [[sitio-web]]

## API REST (`sitio-api-rest-v3`, Slim 4)

Patrón de capas estricto, todo bajo `app/src/`:

```
Controller → Service → Repository → Database (PDO / SQL Server)
```

- **`App/`** — Bootstrap secuencial por `App.php`: `DotEnv → Container → ErrorHandler → Middlewares → Cors → Database → Services → Repositories → Routes → NotFound`
- **`Controller/`** — HTTP; extiende `Controller\Base`
- **`Service/`** — Lógica de negocio; extiende `Service\BaseService`
- **`Repository/`** — Queries PDO; extiende `Repository\BaseRepository`
- **`Dto/`** — Moldean la salida del repo antes de devolver al controller
- **`Middleware/`** — `PermissionMiddleware` (JWT usuarios), `TokenCmsMiddleware`/`PermissionCmsMiddleware` (CMS), `LogMiddleware`
- **`Support/`** — Mailers (PHPMailer), Redis, Excel, wrappers externos (Producteca, MS Envios)
- **`Helper/`** — `JsonRequest`, `JsonResponse`, `Pagination`, `LoggerLog`, `UploadImage`

Rutas en `app/src/App/Routes.php`. Base path por env `BASE_PATH` (default `/v1`). Rutas CMS bajo `/cms` con auth/permiso separados. DI con **Pimple** (`App/Services.php`, `App/Repositories.php`).

### Bases de datos (SQL Server)

- `NB_WEB` — datos web (usuarios, aceleradores, fotos, cms)
- `NewBytes_DBF` — ERP (artículos, stocks, clientes, familias)
- `PRODUCTOS` — contenido enriquecido (fotos, videos, subtítulos)

**Stocks:** `NewBytes_DBF.dbo.stocks` tiene una fila por almacén (`ID_ALMACEN`). Siempre filtrar por `WAREHOUSE_IDS` y agregar con `SUM + GROUP BY`, nunca tomar `[0]`. Ver [[contexto]].

## Frontend (`sitio-wep-app-v2`, Nuxt 2)

- **`pages/`** — Ruteo por archivos. Rutas custom (detalle producto `/:uri?_-_:id`, búsqueda `/:type/:name`, postventa por token) en `nuxt.config.js` vía `router.extendRoutes`.
- **`store/`** — Módulos Vuex: `carrito`, `busquedas`, `miCuenta`, `general` (CMS/banners), `settings`, `modalsPopup`, `rutas`, `brevo`. Carrito y auth persistidos con `vuex-persistedstate`.
- **`plugins/api.js`** — Inyecta `$api` (wrapper de `$axios`) por dominio: `auth`, `registro`, `productos`, `cuenta`, `postventa`. Uso: `this.$api.<dominio>.<método>()`.
- **`plugins/*.client.js`** — Plugins client-only (gtag, metricool, brevo).
- **`middleware/user-agent.js`** — Global en todas las rutas.
- **`modules/mercadopago`** — Módulo Nuxt custom para el SDK de MP.
- **`components/`** — Auto-importados (`components: true`).

Auth con `@nuxtjs/auth-next` (estrategia `local`, endpoints `/auth/login|logout|user`). `baseURL` de axios desde `API_HOST`.

## Ver también

- [[stack]] · [[infraestructura]] · [[contexto]]
