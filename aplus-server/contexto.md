# Contexto

## Modelo de amenazas

El proyecto asume que el contenido A+ (sobre todo los videos MP4) **tiene valor** y que los retailers o terceros van a intentar copiarlo. Las defensas escalan según la amenaza:

| Amenaza | Defensa principal |
|---------|-------------------|
| Copiar URL del asset y usarla en otro sitio | HMAC + TTL en URL (link se vence) |
| Embed del iframe en dominio no autorizado | CSP `frame-ancestors` + `Referer` check |
| Scraping masivo | Rate limit por IP + Cloudflare |
| Descargar MP4 con devtools y redistribuir | Watermark metadata + `--visible` overlay |
| Strip de metadata con `ffmpeg -map_metadata -1` | Por eso existe `--visible` para contenido sensible |
| DDoS / enumeration | Cloudflare proxied delante |

## Reglas operativas

### No hacer
- ❌ **No commitear `.env`** (está en `.gitignore`).
- ❌ **No mover `TOKEN_SECRET`** al repo ni a config hardcoded.
- ❌ **No servir directo desde `content/<slug>/originals/`** — solo `assets/` se expone.
- ❌ **No agregar endpoints públicos sin rate-limit.**
- ❌ **No meter el container de watermark en `docker-compose.yml`** — es one-shot, no un servicio.
- ❌ **No reemplazar el reencode de videos por `-c copy`** — pierde el watermark grabado y el `+faststart` para streaming progresivo.

### Gotchas

- **`TOKEN_SECRET` no se rota a la ligera**: cambiarlo invalida instantáneamente todos los HTML ya servidos con tokens viejos. `start.sh` lo autogenera **solo** si aún es el placeholder (grep por `^TOKEN_SECRET=cambiar`).
- **`docker compose down -v` BORRA certs** (volume `caddy_data`). `start.sh` lo advierte. Usar solo `down`.
- **Caddy reload idempotente**: `start.sh` siempre llama `caddy reload`; si el Caddyfile no cambió, es no-op. Si cambió, recarga graceful sin downtime.
- **Sed portable**: `start.sh` usa `sed -i.bak ... && rm -f .bak` porque BSD sed (macOS) y GNU sed (Linux) difieren en la sintaxis de `-i`. No simplificar a `sed -i` sin probar en ambos.
- **Rewriter de HTML**: el regex en `signHtml` solo soporta atributos `src|href|poster|data-src|data-poster`. Si se agrega `srcset` u otro, hay que extender el regex.
- **Rate-limit es in-memory**: funciona con 1 instancia de `app`. Si se escala horizontal, migrar a Redis.

## Convenciones

- **Slug de producto**: `^[a-z0-9][a-z0-9_-]{0,63}$`. Validado en `server.js::validProductName` y en `add-product.sh`.
- **Originales** en `content/<slug>/originals/` y **nunca se sirven**; el servidor solo sirve desde `content/<slug>/assets/`.
- **HTML** en `content/<slug>/index.html` debe usar URLs **relativas** (`assets/hero.mp4`), no absolutas, para que el rewriter las tome.
- **Tag de watermark** formato `aplus/<slug>/<retailer>/<YYYYMMDD-HHMM>` para que `ffprobe`/`identify` puedan rastrear filtraciones.

## Flujos

### Primera vez
```bash
cp .env.example .env               # opcional: start.sh lo hace solo
# editar Caddyfile: email + dominio real
./start.sh                         # autogenera TOKEN_SECRET
```

### Cambios de código o config
```bash
./start.sh    # rebuild incremental + caddy reload graceful
```

### Nuevo producto
```bash
./add-product.sh rog-strix-rtx5090
# (opcional) poner originales en content/rog-strix-rtx5090/originals/
./watermark.sh rog-strix-rtx5090 fravega --visible
```

### Deploy a VPS
`rsync` del folder entero al Ubuntu y correr `./start.sh`. `.env`, `content/` y los volumes de Caddy persisten entre ejecuciones.

## Ver también

- [[aplus-server/arquitectura|Arquitectura]]
- [[aplus-server/stack|Stack]]
## Replicación de microsites (A+ content)

El flujo para agregar un producto nuevo al servidor **no es copiar el HTML del sitio oficial**. Se usa el skill [[Skills/replicar-microsite/SKILL|Replicar Microsite]] que genera un `index.html` semántico desde cero, optimizado para iframe.

### Reglas aprendidas (2026-04-16, con TUF B550M-PLUS WIFI II)

- **NO mantener la estructura original si usa `fullpage.js` / `owl-carousel` / `position:absolute` viewport-full**. En iframe rompe los anchors (fullpage los construye), no inicializa los carousels y pierde las galerías. **Rebuild completo desde cero con Swiper + HTML semántico.**
- **Galerías anidadas** a más de 1 nivel de la nav principal son un anti-patrón. Siempre surfacearlas como anchor propio (ej: `#galeria`, `#armoury`).
- **ASUS tiene 3 tipos de galería** que hay que saber reconocer:
  - **Lightbox del producto** (`dlcdnwebimgs.asus.com/gain/<uuid>/`): la galería principal — 6-10 fotos 2400×2400. Usar main Swiper + thumbs Swiper acoplados + lightbox.
  - **Armoury Crate** (filter chips verticales + slider por chip): mini-Swiper por chip con 1-3 slides.
  - **Fan overlay** (base image + overlays cross-fade por chip): CSS puro, no necesita Swiper.
- **CDNs de ASUS**: `www.asus.com/websites/global/products/<id>/img/...` es el fallback confiable. `dlcdnimgs.asus.com` tira **403 AccessDenied**. `dlcdnwebimgs.asus.com/gain/<uuid>/` es solo para la galería lightbox del producto. `media/global/gallery/<slug>...` **puede traer imágenes de accesorios/gabinetes en bundle, NO la mother** — confirmar abriendo una antes de usar.

### Iframe-ready (obligatorio para este servidor)

Todo `index.html` servido desde `content/<slug>/` debe:
- Usar `container-type: inline-size` en `<body>` + `@container` queries (nunca viewport units `vw/vh`).
- Enviar `postMessage({type:'microsite:height', height:N, slug:'<slug>'})` al padre via ResizeObserver + click + load/resize para auto-resize del iframe.
- No tener `position: fixed`, `overflow:hidden` en html/body, ni scrolls internos.
- Usar URLs **relativas** `assets/...` (para que el rewriter HMAC del server las firme).

