# Troubleshooting

Ver también: [[Laset]] · [[operaciones]] · [[arquitectura]]
Versión completa en el repo: `/var/www/laset/docs/troubleshooting.md`.

## Back
- **500 `Adaptive Server is unavailable (172.31.10.208)`** → DB del backup es de otra red (VPC AWS),
  sin ruta. Usar `db-nb-massql-dev.blu.net.ar,4444` (user `cmercurio`) en los `.env`.
- **500 Laravel `valid cache path` / `vendor/autoload.php not found`** → falta `vendor/` y/o `storage/`
  (ambos gitignoreados). Ver [[operaciones]].
- **composer: "affected by security advisories"** → `--no-security-blocking`.
- **composer: `ext-gd`/`ext-zip` (cobros)** → `--ignore-platform-reqs`.
- **`Unable to read environment file`** → `.env` en 600, `chmod 644`.
- **`all predefined address pools have been fully subnetted`** → usar `laset-net` compartida; no red por app; no `prune`.
- **`container name already in use` / puerto ocupado** → falta sufijo `-laset` / puerto 81xx-39xx.
- **`docker compose up --build` falla en `pecl install sqlsrv`** → no buildear; usar imagen `*-laset` (`image:`).

## Dominio único / SSO

### Entrar a una app desloguea de TODAS
Ese back valida el permiso leyéndolo del **payload del token**, pero el token lo emitió otra app y
cada back mete su propia forma de usuario. Falta el campo → 401 → `auth-next` borra el token
compartido → se cae la sesión de todo el ERP.
**Fix:** el middleware relee el usuario de la base por `UserId` (`getByToken()` / `getById()`).

### La app se ve bien pero no responde a nada / vuelve al login sola
Los assets dan 404 y la app **no hidrata** (el SSR igual pinta el HTML, por eso "parece" andar).
Causa: `build.publicPath` absoluto. Nuxt 2 le prepende `router.base` → monta en
`/pedidos/pedidos/_nuxt/`. **Fix:** `publicPath: '_nuxt/'`.

### La pantalla abre desde el menú pero **buscar** da 404 (`/compras/compras/providers`)
`$router.push(resolve(...).href)`. En vue-router 3 `resolve()` arma el href con
`createHref(base, fullPath)` — **ya trae el `router.base`** — y `push()` se lo vuelve a anteponer
al escribir la history. Con `base: '/'` no se notaba. **Fix:** `resolvedRoute.route.fullPath`.
Excepción: si el href alimenta un `<a :href>` (`itemsPrices.vue`, `productHref`) **sí** lo necesita.

### Un asset o endpoint propio da 404 (logo, `/api/version`) y la app igual "anda"
Al revés: al path le **falta** el base, así que se pide contra la raíz de `laset.local`. El
serverMiddleware y los estáticos sí cuelgan del base. **Fix:** armarlo con
`$router.options.base` (trae la barra final). Suele fallar en silencio — el `fetch` de
`BuildVersion.vue` tenía un `catch` que dejaba el modal "Versión de la aplicación" con los campos
vacíos y una fecha inválida, sin error a la vista.

### Los comprobantes no abren, o abren los de la otra empresa
`COMPROBANTES` del `.env`. Dos causas con el mismo síntoma: `http://localhost:3907` **sin
`/comprobantes`** (la app sólo sirve bajo su base), o apuntar al servicio de NB
(`comprobantes.lio.red`, `omega.`, `gamma.`), que no tiene las rutas de Laset —
`/voucher/laset/factura/...` sólo existe en el local. **Fix:**
`COMPROBANTES=http://laset.local/comprobantes` en los 6 fronts.
⚠️ `process.env` se **inlinea en el build**: no alcanza con reiniciar PM2.

### 401 `Signature verification failed` entre backs
Ese back firma con otra clave. Todos usan `md5(JWT_SIGNATURE_KEY)` HS256. Comparar sin exponer el
secreto: `grep -hE '^JWT_SIGNATURE_KEY=' <back>/app/.env | cut -d= -f2- | md5sum | cut -c1-8`.

### ms-metadata rechaza los tokens de los backs PHP
PyJWT exige el parámetro `audience` cuando el token trae claim `aud`, y los PHP ponen ahí un sha1
de IP+User-Agent+hostname. **Fix:** `jwt.decode(..., options={"verify_aud": False})`.

### El navegador bloquea las llamadas a un back Phinx (CORS), pero `curl` anda
`Cors.php` está, pero los warnings de PHP 8 se imprimen **antes** de los headers y PHP ya no puede
enviarlos. **Fix:** `display_errors` apagado en `public/index.php` (escape `DEBUG_OUTPUT=1`).
Se nota porque la respuesta sale como `text/html` con los warnings delante del JSON.

### 500 `could not be opened in append mode: chmod()`
El dir `logs/` del back es del usuario del host y Apache corre como `www-data`.
**Fix:** `chgrp -R 33 <back>/app/logs && chmod -R g+w` (+ `g+s`).

### 500 `SSL Provider: certificate verify failed: self-signed certificate`
El contenedor trae **ODBC Driver 18**, que cifra y valida el certificado; el del SQL Server es
autofirmado. (Expedición trae el 17 y por eso no falla.)
**Fix:** `Encrypt = 1; TrustServerCertificate = 1;` en el DSN.

## Front
- **`npm install` falla en `canvas`/node-pre-gyp** (comprobante-pdf) → `--ignore-scripts`.
- **build falla `ERR_OSSL_EVP_UNSUPPORTED`** → `NODE_OPTIONS=--openssl-legacy-provider`.
- **`pm2 start: Script not found nuxt.js`** → install no dejó `nuxt`, reinstalar con `--ignore-scripts`.
- **`ERESOLVE`** → `--legacy-peer-deps`.
- **Host sin RAM al levantar fronts** → bajar `instances` a `2` (no `'max'`).

## Importador de la planilla (comp=11)

Detalle completo del proceso en [[import-planilla-comp11]].

### "El campo file no se pudo subir" al subir un .xlsx
Es la regla `uploaded` de Laravel: PHP **no recibió** el archivo. Nunca es permisos. Dos causas:
- **`upload_max_filesize = 2M`** (default Ubuntu) y la planilla pesa ~4 MB. `apache-uploads.ini`
  ya trae 100M pero hay que **montarlo** por docker-compose en
  `/etc/php/8.1/apache2/conf.d/` — ojo, **no** en `/usr/local/etc/php/conf.d/`, que es la ruta
  de las imágenes oficiales `php:*` y esta imagen (Ubuntu + mod_php) no lee.
  Verificar **por HTTP**, no con `php -i` del CLI: el CLI lee otra `conf.d` y miente.
- Un `curl` copiado de Chrome ("Copy as cURL") **no incluye el binario** del archivo: manda 0
  bytes. Usar `-F 'file=@archivo.xlsx'`.

### "El campo file debe ser un archivo de tipo: xlsx"
libmagic 8.1.2 no reconoce los .xlsx que exporta Excel (devuelve `application/octet-stream`) y
`mimes:xlsx` compara contra `guessExtension()`. **Rechaza todo archivo**. No falta
`shared-mime-info`: finfo funciona bien con .txt, .zip y .png. Resuelto con
`App\Support\XlsxUpload` (extensión + firma ZIP leída del archivo).

### `[ABORT Fase D stock] N grupos delta sin fila en stocks`
Una orden con `warehousesId` NULL o un almacén que no está en `FP_Almacen` comp=11 (típico:
`cCodAlm='SAF'`, de cargas manuales). El ASSERT tira **toda** la transacción, así que una sola
orden vieja bloquea la migración entera. `--skip-bloqueadas` ahora las difiere. Para ubicarlas:

```sql
SELECT nNumPed, warehousesId, cCodAlm FROM NewBytes_DBF.dbo.pedprot t
 WHERE t.companyCode = 11
   AND NOT EXISTS (SELECT 1 FROM NewBytes_DBF.dbo.FP_Almacen fa
                    WHERE fa.companyCode = 11 AND fa.ID_ALMACEN = t.warehousesId);
```

### Fase D "falla" sin decir por qué
El job guarda el output, pero recortaba a los últimos 1500 chars y el stack de Symfony tapaba
la línea del error. Mirar `laset_import_jobs.result` → `fase_d.output_tail` (ya corregido para
que las líneas de error vayan primero).

### El Delta Check marca cientos de SKUs y los datos están bien
Comparaba criterios distintos de cada lado. Corregido. Si vuelve a dar números grandes **con
el ERP por encima de la planilla**, la causa suele ser otra: se importó **sin wipe previo** y
Fase C apiló sobre lo que ya había.

## DB — el clon del esquema quedó viejo
El esquema se clonó de NB el 2026-09-04; el código siguió avanzando allá. Síntoma:
`SQLSTATE[42S22] Invalid column name '<x>'` en una pantalla cualquiera.
Caso real: `pedprol.doNotUpdateCost` (abrir una orden de compra). Fix: agregar la columna
copiando tipo/nullability/default de su columna hermana y versionar el SQL en `db-laset/`.

## Cuenta corriente de proveedores

Ledger `NEW_BYTES.dbo.MS_MOV_CTACTE_PROVEEDORES`. `TR_CODIGO` 38 y 32 suman deuda; 30, 40,
44 y 128 restan. `COTIZACION` es el **EUR/USD del movimiento** (1 en las cuentas en
dólares), **no** un rate contra el peso — de ahí que la columna "$" mostrara basura.

### Los dólares de una cuenta en euros están inflados
Se valuaba toda la historia al TC de cierre de la hoja. **Fix:** cada movimiento a su TC
real — la factura al del pago que la canceló (`Asignado USD`/`Asignado EUR`), el pago a
`Pagado Dolares`. Lo impago sí va al de cierre: es un pasivo vivo en euros.

### Faltan movimientos y hay un "Ajuste de cierre" enorme
El bloque de resumen de la planilla está en la **columna 1** y comparte fila con el libro,
que arranca en la **4**; el filtro de rótulos descartaba la fila entera. **No cambiaba
ningún saldo**, así que las cuentas en dólares parecían correctas. **Fix:** el rótulo sólo
descarta si está dentro de las columnas del libro.

### El saldo en euros no coincide
No se deriva de `COTIZACION`: fila por fila sale exacto, el total no. Para eso está
`IMPORTE_ORIGEN`/`MONEDA_ORIGEN`, y el cierre son dos líneas ("Ajuste de cuenta" en la
moneda de la cuenta + "Diferencia de cambio" sólo en USD).
Control: Danicoop (`002418`) = **€39.007,00 / u$d 46.597,01**, 57 movimientos.

### Ves datos nuevos con columnas viejas
Estás en `compras-laset-dev.blu.net.ar`, que **comparte la base** con este host pero corre
su propio código. Una reimportación se ve allá al instante; los cambios de código no.

## Pantallas que muestran datos de la otra empresa (o de menos)

### El front muestra IVA / impuestos / columnas en pesos en Laset
El front decide con `user.companyCode === 11` (`plugins/permissions.js`, y `isLaset` en
`ProviderOrderInbound/Detail.vue`). Ese valor sale de `agentes.companyCode`, así que **un
usuario con agente de otra empresa ve la UI que no corresponde**. Se resuelve con
`FORCE_COMPANY_CODE=11` en el `.env` del back, no tocando el maestro de agentes.

Dos cosas que hacen perder tiempo acá:
- **El override tiene que ir en el repositorio de auth, no en un Dto**: el token se arma con
  `makeToken($login)`, el objeto crudo de `AuthRepository::login()`. Si se pone en el Dto,
  `/auth/user` devuelve el valor forzado pero **el JWT no**, y el front lee del JWT.
- **Cada back tiene su propio `/auth/login`** (pedidos :8193, compras :8196, cobros :8183,
  expedición :8184). Como el SSO comparte la firma, vale el companyCode del back donde se
  logueó: hay que setear la variable en todos. Postventa no usa companyCode.

Para verificar sin navegador:
```bash
curl -s http://localhost:8196/v1/auth/login -H 'Content-Type: application/json' \
  --data-raw '{"username":"USUARIO","password":"CLAVE"}'   # decodificar el payload del JWT
```

### El detalle de venta no muestra las OC asignadas
El endpoint responde `{"enabled": false}`, no un error: kill switch
`ASSIGNMENT_FEATURE_ENABLED` en el `.env` de pedidos (el default del repo es `false`).
`ASSIGNMENT_COMPANIES` tiene que incluir el companyCode. Tras cambiarlo: `php artisan config:clear`.

### El detalle de una OC no muestra los subtotales
El front los gatea con `currencyQuote > 0` y la OC tiene `pedprot.nValDiv = NULL`. En comp=11
todas las OCs son `DOL` y la cotización va en 1. Las creadas por el camino stock-only quedaban
sin ella (ya corregido el INSERT):

```sql
SELECT COUNT(*) FROM NewBytes_DBF.dbo.pedprot
 WHERE companyCode = 11 AND cCodDiv = 'DOL' AND nValDiv IS NULL;
```

### El favicon no aparece aunque el archivo esté bien
Con dominio único, `href: '/favicon.ico'` se pide contra la **raíz** (404), no contra
`/pedidos/favicon.ico`. El `href` tiene que llevar el `router.base` de la app — la misma
trampa que `build.publicPath`. Verificar qué pide el navegador, no sólo que el archivo exista:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://laset.local/favicon.ico          # 404
curl -s -o /dev/null -w "%{http_code}\n" http://laset.local/pedidos/favicon.ico  # 200
```
Cambiar el `head` de `nuxt.config.js` **requiere rebuild**: queda embebido en el bundle.
