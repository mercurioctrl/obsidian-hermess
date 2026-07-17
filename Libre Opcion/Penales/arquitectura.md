# Arquitectura — Penales

## Front (`sitio-web-app-v3`)

- **Componente host:** `app/components/Home/Banners/PenalesBanner.vue` → renderiza un `<iframe>` al microsite.
  - URL: `/micrositios-files/penales-mundial/index.html?v=N&api=…&key=…`
  - `?v=N` — cache-buster; **debe subir junto con los `?v=` de los assets en `index.html`** al cambiar JS/CSS.
  - `?api=` — `$config.API_HOST4` (base de la API v4, llega al cliente vía publicRuntimeConfig).
  - `?key=` — `$config.PENALES_FIRMA_KEY` (clave HMAC para firmar el resultado).
- **Feature flag:** `HOME_PENALES_GAME` (en `.env` → `nuxt.config.js` publicRuntimeConfig). En `pages/index.vue` con `v-if="$config.HOME_PENALES_GAME"`. Sin el flag, el banner no se monta.
- **Microsite:** `app/static/micrositios-files/penales-mundial/`
  - `game.js` — motor del juego (Canvas 1920×360 desktop / 360×340 mobile). Posiciones fijas (`KEEPER_Y`, `KICK_TARGETS`, `KEEPER_JUMP_X`, `BALL_START`) calibradas a mano sobre `banner.png`.
  - `leaderboard.js` — llamadas a la API (`penales/start`, `penales/score`, `penales/ranking`) + firma HMAC del payload.
  - `index.html`, `style.css`, `assets/` (`banner.png` desktop, `banner-mobile.jpg` mobile, `sprite-arquero-mundial.jpg`, `ball.png`).
- **Marquesina LED:** en `game.js`, carteles de marcas rotando sobre el "anillo claro" del fondo (`LED_BAND`, perfil medido a píxel sobre `banner.png`).

## Back — API v4 (`sitio-api-rest-v4-laravel`)

Patrón Controller → Service → Repository. Rutas en `routes/api.php`, prefix `penales`:

| Método | Ruta | Controller |
|---|---|---|
| GET | `penales/start` | `PenalesTokenController` — emite token de sesión |
| GET | `penales/ranking` | `PenalesRankingController` — Top 10 |
| POST | `penales/score` | `PenalesScoreStoreController` — guarda resultado |

- **`PenalesTokenService`** — genera y valida el token (`nonce:timestamp:HMAC(app.key)`), one-time-use en cache (TTL 30 min, edad mínima 5 s). Firma del payload con `PAYLOAD_SECRET = 'peñales-2025-x7k9'` (debe coincidir con `PENALES_FIRMA_KEY` del front).
- **`PenalesRankingService`** — dedup por email (identidad) y "mejor marca"; valida nombre único por email.
- **`PenalesRankingRepository`** — SQL raw a `[LO].[dbo].[penales_ranking]` (`id`, `nombre`, `email`, `goles`, `atajadas`, `tiempo`, `created_at`).

### Ranking

`ORDER BY goles DESC, tiempo ASC, atajadas DESC, id ASC` — gana quien más goles hace; desempata menos tiempo, luego más atajadas, luego el más antiguo (id menor).

### Flujo de una partida

1. `GET penales/start` → token.
2. El usuario juega (mín. 5 s por el anti-cheat).
3. El front firma `{token}:{goles}:{atajadas}:{tiempo}` con la clave HMAC.
4. `POST penales/score` → valida token + firma, guarda/actualiza, devuelve posición y Top.

## Ver también

- [[contexto]] — reglas de negocio y anti-cheat en detalle.
- [[changelog]] — historial de cambios.
