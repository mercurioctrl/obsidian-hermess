# Penales — Juego "Penales Mundial 2026"

Banner jugable en el home de **Libre Opción**: el usuario patea 5 penales, se registra su puntaje y compite en un ranking. Vive como microsite aislado en un iframe dentro del front, con backend propio en la API v4.

## Stack

- **Front:** microsite vanilla JS + Canvas (1920×360) embebido en iframe, dentro de la web Nuxt 2 (`sitio-web-app-v3`).
- **Back:** Laravel 10 / API v4 (`sitio-api-rest-v4-laravel`), datos en SQL Server (tabla `[LO].[dbo].[penales_ranking]`).
- **Seguridad:** token de sesión one-time-use + firma HMAC del resultado.

## Notas del proyecto

- [[arquitectura]] — Componentes front, endpoints y flujo back, tabla y ranking.
- [[changelog]] — Registro de lo trabajado por fecha.
- [[contexto]] — Reglas de negocio, decisiones, pendientes y gotchas.

## Ramas activas

- **Front:** `test-penales-mundial` (`sitio-web-app-v3`)
- **API:** `fix-penales` (mergeada a Gamma) y `fix-penales-token-consume` (PRs #706 Gamma / #707 Development)

---
Última sincronización: 2026-07-17
