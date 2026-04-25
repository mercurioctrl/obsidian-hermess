# Migración desde `/micrositios-files/` de Libre Opción

Estado de la migración de los micrositios de Libre Opción a [[aplus-server/aplus-server|aplus-server]]. El **plan operativo completo** vive en `README.md` del proyecto (3 fases + rollback + gotchas). Esta nota captura **decisión estratégica + contexto técnico** que no pertenece al código.

## Decisión (2026-04-16)

**Opción elegida: migración full** — todos los micrositios de LO pasan a `aplus.tudominio.com`, sin hybrid.

### Opciones que se consideraron

1. **(a) Migración full** ✅ — todos los slugs a aplus-server.
2. **(b) Hybrid** ❌ — LO se queda en `/micrositios-files/`, aplus-server solo para Fravega/ML/Compragamer.
3. **(c) Reverse proxy** ❌ — LO proxya `aplus.tudominio.com` por debajo manteniendo `/micrositios-files/<slug>/`.

### Por qué (a)

El punto de aplus-server es protección: HMAC + TTL + watermark per-retailer + `frame-ancestors`. En hybrid, **el retailer más importante queda con menos protección** — al revés de lo que tiene sentido.

### Por qué NO (b)

- **Content drift**: dos copias del mismo microsite, tarde o temprano divergen.
- **Doble mantenimiento**: cada cambio → `add-product.sh` + copy manual a `/micrositios-files/`.
- **Asimetría de watermark**: si leakea un video, para retailers externos sabés de dónde vino; para LO, no.
- **UX inconsistente**: mismos productos, experiencia distinta según el retailer.

### Por qué NO (c)

- El browser nunca habla directo con aplus-server → `frame-ancestors` no protege nada para LO.
- El `Referer` que ve aplus-server viene del servidor de LO (o ninguno), no del browser → check de referer se vuelve trivial.
- Hay que proxyear también los assets firmados → más config en el frontend/Caddy de LO.
- Ganás same-origin, pero para contenido **read-only sin cookies ni interacción** no aporta nada medible.

## Contexto técnico observado

### Integración actual de LO

Observado en DevTools de `gamma.libreopcion.com` (2026-04-16):

```html
<div class="syndication-iframe-wrapper">
  <iframe
    src="/micrositios-files/<slug>/index.html"
    title="Contenido sindicado <PRODUCTO>"
    loading="lazy"
    frameborder="0"
    class="syndication-iframe"
    style="height: 7891px;">  <!-- alto medido, no hardcodeado -->
</div>
```

Hallazgos:

- **Same-origin**: LO sirve micrositios desde su propio dominio (`public/micrositios-files/<slug>/index.html` en el Nuxt repo).
- **Ya usan iframe-resizer (o equivalente)**: el `height: 7891px` es un valor medido → hay un parent postMessage listener ajustando el alto.
- **CSS propio en `.syndication-iframe-wrapper` + `.syndication-iframe`**: el snippet de aplus-server para LO **debe mantener estas classes** para no romper el layout.
- **Slugs kebab-case**: ej. `asus-sindicate-limited-edition` — compatibles con la regex de aplus-server.

### Snippet target (post-migración)

```html
<div class="syndication-iframe-wrapper">
  <iframe
    src="https://aplus.tudominio.com/<slug>/?resize=1"
    title="Contenido sindicado <PRODUCTO>"
    class="syndication-iframe"
    loading="lazy"
    frameborder="0"
    referrerpolicy="strict-origin-when-cross-origin"
  ></iframe>
</div>
```

Si LO ya tiene `@iframe-resizer/parent` cargado globalmente, solo hay que inicializarlo sobre `.syndication-iframe`. Si no, agregarlo al snippet.

## Trade-offs aceptados

| Ganas | Pagás |
|-------|-------|
| HMAC + TTL en assets | +1 DNS + TLS handshake (~50-100ms primer asset, mitigado por CF + HTTP/2 reuse) |
| Watermark per-retailer → trazabilidad si leakea | Hay que cambiar `SyndicationIframe.vue` para leer de `APLUS_WHITELIST` |
| `frame-ancestors` CSP → embed bloqueado fuera de whitelist | Source of truth del contenido pasa de LO repo a aplus-server |
| Rate limit por IP | Coordinación entre 2 deploys (LO + aplus-server) |

## Prerequisitos antes de arrancar

- [ ] Dominio real elegido (hoy es placeholder `aplus.tudominio.com` en `Caddyfile`).
- [ ] VPS Ubuntu listo + Cloudflare proxied.
- [ ] `.env` con `ALLOWED_REFERERS` incluyendo `libreopcion.com`, `www.libreopcion.com`, `gamma.libreopcion.com`.
- [ ] Equipo de LO briefeado — el cambio en `SyndicationIframe.vue` es de ellos.
- [ ] Ver [[Libre Opcion/Libre Opcion]] en la bóveda para contexto del proyecto de LO.

## Fases (resumen — detalle en `README.md`)

- **Fase 0** — levantar aplus-server en el VPS con dominio real (1 día).
- **Fase 1** — piloto con 1 producto de tráfico medio-bajo (1-2 días).
- **Fase 2** — migración gradual con `APLUS_WHITELIST`, batches de 5-10 slugs/semana (2-3 semanas).
- **Fase 3** — cleanup: remover whitelist, borrar `/micrositios-files/` del repo de LO (1 día).

**Rollback seguro por slug** durante Fase 2: sacar el slug del whitelist → vuelve automáticamente al legacy.

## Ver también

- [[aplus-server/arquitectura|Arquitectura]] — flujo HMAC + rewriter
- [[aplus-server/integracion-retailers|Integración con retailers]] — snippets + gotchas por retailer
- [[aplus-server/contexto|Contexto]] — modelo de amenazas + reglas operativas
