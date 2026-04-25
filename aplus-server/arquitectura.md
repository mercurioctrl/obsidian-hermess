# Arquitectura

## Diagrama lógico

```
Retailer iframe  →  Cloudflare (proxy + cache + DDoS)
                       │
                       ▼
                    Caddy 2  (TLS + reverse proxy)
                       │
                       ▼
                  Fastify (Node 20)
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
   GET /<slug>/   GET /<slug>/    /healthz
   (HTML firma    assets/*
    URLs)         (verify HMAC)
                       │
                       ▼
              content/<slug>/assets/*  (read-only mount)
```

## Flujo de protección de assets

1. Cliente pide `GET /<slug>/` con `Referer` de un retailer whitelisteado (env `ALLOWED_REFERERS`).
2. `server.js::signHtml` lee `content/<slug>/index.html` y reescribe cada atributo `src|href|poster|data-src|data-poster` que apunte a `assets/...` agregándole `?e=<exp>&s=<hmac>`.
3. TTL configurable vía `TOKEN_TTL` (default `3600` = 1h).
4. Cliente pide los assets firmados. `server.js` valida HMAC con `crypto.timingSafeEqual` y chequea expiración antes de `sendFile`.
5. Sin firma válida → **403**. Vencida → **410**.
6. `Content-Security-Policy: frame-ancestors <ALLOWED_REFERERS>` en respuesta del HTML bloquea embed en dominios no autorizados.
7. Rate-limit por IP (Fastify con `trustProxy: true` lee XFF → IP real detrás de Caddy/Cloudflare).
   - `RATE_LIMIT_HTML=30/min`, `RATE_LIMIT_ASSETS=300/min` por defecto.

## Parámetros de URL soportados

El handler `GET /:product/` acepta query params opcionales para modificar el HTML servido (sin tocar los `index.html` de cada slug):

| Param | Valor | Efecto |
|-------|-------|--------|
| `resize` | `1` | Inyecta `<script src="https://cdn.jsdelivr.net/npm/@iframe-resizer/child"></script>` antes de `</body>`, para que el retailer pueda usar `iframe-resizer` en el parent y auto-ajustar el alto del iframe. |

**Convención**: cualquier valor distinto a lo documentado → no-op (fail closed). Si se agregan más params, extender `server.js` y esta tabla.

**Gotcha para cache**: si alguna vez se agrega cache del HTML, la cache key debe incluir el querystring porque `?resize=1` y sin él generan HTML distintos.

## Estructura de carpetas

```
aplus-server/
├── start.sh                     # build + (re)start idempotente
├── add-product.sh               # scaffolding de producto
├── watermark.sh                 # wrapper del container watermark
├── docker-compose.yml           # caddy + app (NO watermark)
├── Caddyfile
├── .env                         # secreto + whitelist (gitignore)
├── app/                         # Fastify
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
├── watermark/                   # imagen aparte, one-shot
│   ├── Dockerfile
│   └── run.sh
└── content/
    └── <product-slug>/
        ├── index.html           # URLs relativas "assets/foo.mp4"
        ├── originals/           # input watermark (JAMÁS se sirve)
        └── assets/              # output firmado y servido
```

## Decisiones clave

### HMAC en URL, no cookies
Los iframes de retailers son **contexto third-party**. Safari y Chrome (con 3rd-party cookies off) los bloquean. Por eso el gating va en la URL firmada (HMAC), no en cookie.

### Watermark fuera de compose
El container de watermark es **one-shot** (procesa `originals/` → `assets/` y muere). Meterlo en `docker-compose.yml` sería un error: no es un servicio. Ver [[aplus-server/contexto|contexto]].

### Capas defensivas (defense in depth)

| Capa | Qué protege |
|------|-------------|
| Cloudflare | Oculta IP real, DDoS, cache |
| Caddy TLS | HTTPS obligatorio |
| `frame-ancestors` CSP | Embed solo en dominios whitelist |
| `Referer` check | Bloquea hotlinking trivial |
| HMAC + TTL en URL | Links copiados se vencen |
| Rate limit por IP | Scraping masivo |
| Watermark metadata | Trazabilidad si filtran original |
| Watermark `--visible` | Copia visible cara de limpiar |

### Rate-limit in-memory
Store en memoria funciona con **1 instancia de `app`**. Si se escala horizontal, migrar a Redis.

### Rewriter basado en regex
El regex de `signHtml` solo reescribe URLs relativas que empiezan con `assets/` en atributos `src|href|poster|data-src|data-poster`. Para soportar `srcset`, `data-video`, etc., hay que extender el regex.

### Auto-resize opt-in via query param
El script de `iframe-resizer` **no** se injecta por default — solo si el retailer pasa `?resize=1`. Razones:
- No todos los retailers usan el parent script de iframe-resizer; inyectar siempre sería dependencia innecesaria.
- Mantiene los `index.html` de los slugs libres de deps externas.
- El retailer decide per-integration.

## Ver también

- [[aplus-server/stack|Stack]]
- [[aplus-server/contexto|Contexto]]
