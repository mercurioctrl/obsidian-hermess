# TareaWallet — Libre Opción API v4 + Frontend

Documentación de análisis e implementación de features en la API Laravel v4 y frontend Nuxt.js del marketplace Libre Opción.

## Notas

- [[changelog]] — Historial de cambios por fecha
- [[contexto]] — Decisiones de sesión, gotchas, flujos técnicos importantes
- [[arquitectura-recategorizacion]] — Sistema de recategorización de productos (Job, Matcher, DB tables)

## Resumen por área

### Pasarelas de pago (2026-06-07)
Integración de MODO, GetNet y Payway en el checkout.
- MODO QR operativo en sandbox (`ecommerce-modal.preprod.modo.com.ar`)
- Fix crítico en [[contexto#2026-06-07]]: `medioPagoId` sobreescrito por `ACTUALIZAR_PEDIDO` en Vuex
- Fix crítico: OPcache PHP-FPM cachea rutas — reiniciar contenedor tras agregar rutas nuevas

### Recategorización (2026-05-12)
- Review de rama LIO-630 (Franco): concurrencia, restricción stock
- Ver [[arquitectura-recategorizacion]] para diseño DB-driven propuesto

### Wallet / Airdrop (2026-05-11)
- Análisis flujo wallet (TR_CODIGO 475/476, HMAC SHA256)
- Diseño airdrop OpcionFest $15.000 ARS — queries y lógica en [[contexto#2026-05-11]]

## Última sincronización

2026-06-07
