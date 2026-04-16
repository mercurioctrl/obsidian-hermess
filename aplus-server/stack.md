# Stack

## Runtime

| Componente | Versión | Rol |
|------------|---------|-----|
| Docker Compose | v2 | Orquestación |
| Caddy | `caddy:2-alpine` | TLS + reverse proxy |
| Node | `node:20-alpine` | Runtime del server |
| Alpine (watermark) | `alpine:3.20` | Base del container ffmpeg |

## Dependencias Node (`app/package.json`)

- **fastify** `^4.28.1` — framework HTTP
- **@fastify/static** `^7.0.4` — `sendFile` seguro desde mount read-only
- **@fastify/rate-limit** `^9.1.0` — rate-limit por IP (in-memory)

Standard library:
- `node:crypto` — HMAC-SHA256 + `timingSafeEqual`
- `node:path`, `node:fs` — resolución segura de paths

## Watermark (`watermark/Dockerfile`)

- **ffmpeg** — reencodeo con `libx264 + movflags +faststart` + `drawtext` (overlay opcional) + metadata `copyright/comment/title`
- **imagemagick** (+ `imagemagick-jpeg`, `imagemagick-webp`) — anotaciones EXIF + overlay `annotate`

## Infra asumida

- **Cloudflare proxied** delante del VPS (oculta IP, cache de assets, DDoS)
- **VPS Ubuntu** + Docker instalado
- Let's Encrypt gestionado automáticamente por Caddy (certs en volume `caddy_data`)

## Variables de entorno (`.env`)

| Var | Default | Descripción |
|-----|---------|-------------|
| `TOKEN_SECRET` | autogenerado | Clave HMAC (hex 64 chars). **No rotar a la ligera** |
| `TOKEN_TTL` | `3600` | Vida del link firmado (seg) |
| `ALLOWED_REFERERS` | (vacío = permisivo) | CSV de orígenes aceptados |
| `RATE_LIMIT_HTML` | `30` | Req/min por IP al HTML |
| `RATE_LIMIT_ASSETS` | `300` | Req/min por IP a assets |

## Puertos

- `80`, `443` expuestos por Caddy
- `3000` interno (Fastify), solo accesible por Caddy vía network `aplus`

## Healthcheck

`GET http://app:3000/healthz` → `{ ok: true }` cada 30s.

## Ver también

- [[aplus-server/arquitectura|Arquitectura]]
- [[aplus-server/contexto|Contexto]]
