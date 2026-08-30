# La API de NBE

Parte de [[portal]].

**Base:** `https://api.nbe.com.ar/v1` — instancia propia de `sitio-api-rest-v3` con
`COMPANY_CODES=9`. Ver [[configuracion#Empresa NB vs NBE]].

**Auth:** JWT en `Authorization: Bearer`, 3 horas de vida. CORS abierto (`*`), el navegador la
llama directo.

**No tiene documentación.** Todo lo de acá salió de leer el PHP y verificarlo con curl contra la
API real. Ante una duda: buscar el DTO en `src/Dto/`, el repo en `src/Repository/`, y comprobar.

## Trampas

Cada una costó debugging. Están acá para que no se repita.

### La barra final

`GET /v1?query` → **404**. `GET /v1/?query` → 200.

El catálogo vive en la raíz y `ofetch` se come la barra al unir `baseURL` + `'/'`. Como el header
`Authorization` dispara **preflight OPTIONS**, y `$app->options('/{routes:.+}')` no matchea la
raíz, el preflight también da 404 → el navegador aborta con `Failed to fetch`, sin respuesta y
sin pista.

**Usar siempre `useApi().catalogue(query)`**, nunca `get('/')`.
Arreglo real: que `$app->options()` del backend cubra la raíz.

### Dólares vs pesos

Precios de artículos en **dólares** (`price.value` neto, `price.finalPrice` con IVA), con
`cotizacion` al lado. Pero el cotizador de envíos devuelve `total` en **pesos** — se ve en
`ShoppingCartService::addEnvio`, que lo divide por la cotización.

### Envío e interés no están en el carrito hasta confirmar

`processShoppingCart` hace, en orden: `addEnvio` (agrega `PRODUCT_ID_ENVIO` con la tarifa) →
`addInteresesDePago` (agrega `PRODUCT_ID_INTERESES` sobre el total **ya con envío**) → crea el
pedido. El checkout replica ese orden en el front.

### El catálogo no pagina

`GET /` devuelve todo lo que matchea, sin `limit`/`offset`. En NBE son ~1.300 artículos (1,1 MB):
se trae entero y se pagina en cliente.

### Los listados de cuenta paginan con techo

`Pagination::setPagination` rechaza `limit > 50` y `offset > 200`, y **exige ambos juntos**.
El histórico de pedidos y comprobantes llega hasta ~200 registros.

### Dos formatos de fecha

Órdenes: `"27-08-2026"` (dd-mm-yyyy, por `CONVERT(...,105)`). Otros: `"2026-08-27 14:03:00.000"`.
Ninguno lo parsea `Date` confiablemente. `parseApiDate()` maneja los dos.

### `POST /carrito/item` es un "set"

Array de `{productId, amount, type}`, y **`amount: 0` borra la línea**. Mandar la cantidad final,
no el delta.

### El stock es un semáforo

`Alto` / `Medio` / `Bajo` / `Sin stock`. `amountStock` es numérico pero viene **topeado en
`initialC`**: no es el stock real.

### Permisos por rol

`/priceListExcel`, `/priceListCsv` y `/miCuenta/comprobantes` pasan por `PermissionMiddleware`
(tabla `userPermissions`). Sin permiso devuelven **401** — el portal lo distingue del token
vencido y avisa sin cerrar sesión.

### Otros

- **No hay campo de orden de compra**: `process` solo acepta `note`, la OC va con prefijo `OC: `
- **El medio de pago es obligatorio**; sin datos de envío se asume retiro en sucursal (`3999`)
- **Crear sub-usuario pide la contraseña del titular** (`adminCurrentPass`)
- **El link del mail de recuperación** apunta a nb.com.ar y no lleva el email, solo el token
- **El cotizador de envíos es externo** (`API_MS_ENVIOS`); si cae, el checkout sigue sin precios

## Lo que la API no tiene

Saldo y vencimiento de comprobantes · promociones · cotizaciones · atributos como facetas ·
"más comprado por cliente" (`mas_vendidos` es global) · observación por línea · importación
por texto/Excel.

Por eso varias features del [[contexto|spec original]] quedaron afuera. Ver [[estado]].

## Ver también

- [[arquitectura]] · [[estado]] · [[configuracion]]
