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
