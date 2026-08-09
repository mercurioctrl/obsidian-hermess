# Changelog — TareaWallet

## 2026-07-30

### Verificación del endpoint calificationReviews (reseñas del vendedor)

- **feat (script):** `scripts/verify-calification-reviews.sh` — verificador de caja negra de la "Validación principal" de `GET /v4/seller/{sellerId}/calificationReviews`. Golpea el endpoint real (público, sin JWT), compara vista `viewType=seller` vs pública y valida los 7 criterios de aceptación. Exit ≠ 0 si algo falla. Requiere `curl` + `jq`.
- **bug detectado (criterio 7 — paginación):** `pagination.total` (de `countCalificaciones`) sobrecuenta porque no aplica los filtros `calificacionComentario <> ''` ni `calificacionType` que sí aplica el `SELECT` de `data`. Ej. seller 447: `total=3162` vs filas reales `963`. **Fix pendiente:** replicar filtros en `countCalificaciones()`.
- **análisis:** los 3 endpoints (`calificationReviews`, `review`, `reply`) ya estaban implementados en `CalificacionesVendedor` / `CalificacionService` / `CalificacionRepository`. Detalle en [[calificaciones-vendedor]].
- Gotcha confirmado: `status` llega como `"0"` (string) por tipado del driver PDO sqlsrv — no es fallo del ISNULL.
- Archivos: `scripts/verify-calification-reviews.sh` (nuevo)

---

## 2026-06-07

### Integración MODO (billetera digital) — Checkout

- **feat:** Controller `CreateModoIntention.php` — crea payment request en MODO SDK v2 (`/v2/payment-requests/`), retorna `{ qr, id, deeplink }`
- **feat:** Autenticación MODO SDK v2 via `POST /v2/stores/companies/token` (reemplaza SDK v1)
- **feat:** `TokenizeGetNet.php` y `TokenizePayway.php` — tokenización de tarjetas para GetNet y Payway
- **feat:** Formularios de pago en frontend: `FormPagoGetNet.vue`, `FormPagoModo.vue`, `FormPagoPayway.vue`
- **feat:** `checkout-pago.vue` — inyección de MODO (id 5079) en lista de medios de pago si no viene de la API
- **fix (crítico):** `checkout.js` — `obtenerPedido` en asyncData de `confirmar.vue` hacía `ACTUALIZAR_PEDIDO` que sobreescribía `medioPagoId` a 0 (API v3 no conoce MODO). Fix: guardar `medioPagoIdPrevio` antes del commit y restaurar via `ACTUALIZAR_PAQUETES` si la API devolvió 0
- **fix (crítico):** PHP-FPM tenía OPcache activo con rutas viejas en memoria — las nuevas rutas (`payment/modo/create-intention`, `payment/getnet/tokenize`, `payment/payway/tokenize`) retornaban 404 hasta reiniciar el contenedor
- **fix:** `confirmar.vue` — `processPaymentModo()` carga MODO SDK (`ecommerce-modal.preprod.modo.com.ar/bundle.js`) y llama `window.ModoSDK.modoInitPayment({ version: '2', qrString, checkoutId, deeplink })`
- Archivos API: `routes/api.php`, `CreateModoIntention.php`, `TokenizeGetNet.php`, `TokenizePayway.php`, `PaymentProcessorFactory.php`
- Archivos Frontend: `checkout.js`, `confirmar.vue`, `checkout-pago.vue`, `api4.js`, `FormPagoModo.vue`

---

## 2026-05-12

### Rama: LIO-630 — Recategorización (review/mejoras de Franco)

- **feat:** Control de concurrencia doble en el Job de recategorización: el Service verifica corrida activa antes de despachar (409), y el Job hace UPDATE atómico al marcar `running` para evitar race conditions
- **feat:** Restricción forzada `solo_con_stock=true` — si se envía `false` retorna 422. No se puede ejecutar sobre productos sin stock.
- Archivos: `RecategorizarDispatchController.php`, `RecategorizarDispatchService.php`, `RecategorizacionRepository.php`

### Rama: LIO-627 — Favoritos desde ficha de producto

- **feat:** Migración del recurso para guardar en favoritos directamente desde la ficha del producto
- Archivos: `FavoritosStoreItemController.php`, `FavoritoService.php`, `FavoritoRepository.php`

### Rama: LIO-629 — Coupon self-delete

- **feat:** Endpoint para que el usuario elimine sus propios cupones

### Rama: LIO-625 — Estadísticas de categoría/productos por email

- **feat:** Recurso de estadísticas de categoría/productos con envío automático por email diario
- Archivos: `CategoriasEstadisticasController.php`, `CategoriasEstadisticasService.php`, `CategoriasEstadisticasRepository.php`, `estadisticas.blade.php`

### Rama: LIO-615 — Orden de imágenes del reseller

- **feat:** Lógica para cambiar el orden de las imágenes del producto desde la ficha
- Archivos: `ProductoImagenesOrdenarController.php`, `ProductoImagenesService.php`, `ProductoImagenesRepository.php`

---

## 2026-05-11

### Análisis módulo Wallet

- Investigación del flujo de ingreso a la wallet (TR_CODIGO 475 → comisión referido)
- Diseño del airdrop OpcionFest ($15.000 ARS, TR_CODIGO 476)
- Ver [[contexto]] para queries y detalles de implementación

## Ver también

- [[TareaWallet]]
- [[arquitectura-recategorizacion]]
- [[calificaciones-vendedor]]
- [[contexto]]

---

## 2026-08-04

### Tiendas Oficiales (LIO-720 / 769 / 771 / 772 / 776)

- **feat:** Nuevo módulo `OfficialStore` — `GET /v4/tienda-oficial/{slug}` (público). Controller + `OfficialStoreService::getBySlug()` + `OfficialStoreRepository`. Tablas nuevas `official_store_branding` y `official_store_branding_banners`.
- **feat:** `OfficialStoreInventoryScopeService` — scopea el inventario del vendedor a la `brand_id` de su tienda oficial (404 si no existe, 403 si la tienda no le pertenece).
- **feat (CMS, LIO-720/769):** se traen al LO las secciones (hero, video), menús y banners cargados en el CMS de la tienda oficial (`buildSections`, `buildMenu`, `buildBanners`, `buildMedia`).
- **feat:** Soporte de tienda oficial en auth/user, inventario del vendedor, catálogo público y búsqueda de productos. Filtro por marca de la tienda en inventario y catálogo (LIO-771).
- **fix (ficha de producto, LIO-776):** cuando el item es de una tienda oficial, `FichaProductoDto` reemplaza el nombre del vendedor por `"Tienda oficial {name}"`, apunta la URI a `/tienda-oficial/{slug}`, marca `isOfficialStore=true` y **bloquea la reputación** del seller asociado.
- **fix (búsqueda/facetas):** priorizar tiendas oficiales y excluir a los sellers oficiales del listado común de vendedores; excluir ofertas de marcas no permitidas en búsquedas, sugerencias y listado de vendedores. Alcance transversal a `CatalogueRepository`, `SuggestionRepository`, `BrandRepository`, `CategoryRepository`, `AttributesListRepository`, `IntervalPricesRepository`, `OnlyResellerRepository`, `ResellersByItemIdRepository`, `ItemRepository`, `MainQuery`.
- **fix (LIO-762):** se refrescan juntos `id_brand` y `brand_name` para que queden alineados (item aparecía con marca genérica).
- Detalle completo en [[tiendas-oficiales]].

### Otros

- **fix (LIO-735):** arreglo de email en review "calificar vendedor" (campo obligatorio `type`).
- **hotfix:** `home-marcas` excluye marcas con `activa = 0`.
- **chore:** ignorar `docker-compose.override.yml` en git.


---

## 2026-08-06

### Setup de entorno local — v3 + v4 + front (rama blu-dev-staff)

- **chore:** Las 3 ramas (`sitio-api-rest-v3`, `sitio-api-rest-v4-laravel`, `sitio-web-app-v3`) cambiadas a `blu-dev-staff`; v4 actualizada por fast-forward (14 commits, incluye tests de DTOs).
- **infra:** API v3 legacy levantada **en local** (`lo-website-api-rest`, puerto 8081). Se creó `sitio-api-rest-v3/docker-compose.yml` (gitignorado; el versionado es el `.example`) con `name: lo-api-rest-v3` y conexión a la red de la v4. Build de imagen (PHP 8.1 + driver SQL Server) + `composer install` dentro del contenedor. DB remota staff ya configurada en su `.env`.
- **fix (login v4):** `POST /v4/auth/login` daba **HTTP 500** (`json_decode(): ... false given` en `AuthService:247`). Causa: la v4 delega el login en la v3 (`loginV3` hace `curl` server-side) y la v3 no respondía. **No era CORS.** Fix: `API_V3_URL` en el `.env` de la v4 pasa de `http://localhost:8081/` a **`http://lo-website-api-rest`** (nombre de contenedor, porque la llamada es server-side desde el contenedor v4). Login verificado → HTTP 200.
- **gotcha (Docker):** `docker compose up` de LO borró `nb-api-rest` por **colisión de nombre de proyecto** (mismo basename `sitio-api-rest-v3`). Restaurado + `name:` explícito para evitar reincidencia.
- **gotcha (reforzado):** tras cambiar `API_V3_URL` hubo que recargar php-fpm (`kill -USR2`) porque OPcache servía el `config.php` viejo — `config:clear` no alcanza.
- **CORS:** confirmado que ya estaba en wildcard (`Access-Control-Allow-Origin: *`) sin cambios.
- Detalle completo en [[entorno-local]] y [[contexto#2026-08-06]].


---

## 2026-08-09

### Documentación y memoria persistidas (entorno local)

- **docs:** nueva guía commiteable `documentacion/guias_ejecucion/entorno-local-completo.md` — stack local completo, dependencia login v4→v3, gotchas (colisión compose, php-fpm/OPcache), CORS wildcard.
- **docs:** `api-legacy-v3.md` — agregada sección "Correr en local (Docker)" + nota de que el login v4 depende de la v3.
- **chore:** `sitio-api-rest-v3/docker-compose.example.yml` — `name: lo-api-rest-v3` (fix colisión de proyecto) + bloque comentado de red v4; sacado el mount roto de `local.ini`.
- **chore:** `sitio-api-rest-v4-laravel/app/.env.example` — documentada la opción v3 local (`API_V3_URL=http://lo-website-api-rest`).
- **memoria:** nueva `project_cors.md` (CORS ya es wildcard, no reinvestigar); `project_v3_local_setup.md` enlazada a la guía del repo.
- Detalle en [[entorno-local]].
