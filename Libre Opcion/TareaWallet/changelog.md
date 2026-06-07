# Changelog — TareaWallet

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
- [[contexto]]
