# Integración con retailers

Guía paso a paso para que un retailer (Fravega, Mercado Libre, Compragamer, Libre Opción, etc.) embeba una ficha A+ de [[aplus-server/aplus-server|aplus-server]] en la página de producto.

## 1. Qué le pedís al retailer

El retailer tiene que pegar un `<iframe>` en el bloque de descripción larga / ficha extendida del producto. Es un tag HTML estándar — cualquier CMS serio lo admite.

### Snippet canónico (recomendado)

```html
<iframe
  src="https://aplus.tudominio.com/tuf-rtx5080/?resize=1"
  width="100%"
  style="border:0; display:block; width:100%; min-height:800px;"
  loading="lazy"
  referrerpolicy="strict-origin-when-cross-origin"
  title="ASUS TUF RTX 5080 — Ficha A+"
></iframe>
<script src="https://cdn.jsdelivr.net/npm/@iframe-resizer/parent"></script>
<script>iframeResize({ license: 'GPLv3', log: false }, 'iframe[src*="aplus.tudominio.com"]');</script>
```

Esto da:
- Ancho 100% (ocupa todo el contenedor del retailer).
- Alto auto-ajustado al contenido real via `iframe-resizer` (ver [[aplus-server/arquitectura#Parámetros de URL soportados|arquitectura]]).
- `loading="lazy"` para no bloquear el LCP del retailer.
- `referrerpolicy=strict-origin-when-cross-origin` para que el server reciba el `Referer` y pase el check.

### Snippet mínimo (sin auto-resize)

Si el retailer no puede meter el script del parent en su CSP o la integración es muy restrictiva:

```html
<iframe
  src="https://aplus.tudominio.com/tuf-rtx5080/"
  width="100%"
  height="2400"
  style="border:0; display:block; width:100%;"
  loading="lazy"
  referrerpolicy="strict-origin-when-cross-origin"
  title="ASUS TUF RTX 5080 — Ficha A+"
></iframe>
```

- `height` fijo generoso: el contenido de adentro scrollea si es más largo, pero queda feo. Preferible que el `index.html` del slug tenga altura consistente.

## 2. Qué config va del lado aplus-server

### `.env`

```bash
ALLOWED_REFERERS=https://www.fravega.com,https://www.mercadolibre.com.ar,https://compragamer.com,https://libreopcion.com
```

- Dominio por retailer. Incluir `www` si el retailer lo usa. Si tienen staging (`gamma.libreopcion.com`), agregarlo también.
- `ALLOWED_REFERERS` hace **dos** cosas al mismo tiempo:
  1. Valida el `Referer` del request al HTML (403 si no matchea).
  2. Va al header `Content-Security-Policy: frame-ancestors` → bloquea el embed en navegador si el iframe se renderiza en otro dominio.

### `Caddyfile`

```
aplus.tudominio.com {
    encode zstd gzip
    header {
        X-Content-Type-Options nosniff
        Referrer-Policy strict-origin-when-cross-origin
        Strict-Transport-Security "max-age=31536000; includeSubDomains"
        -Server
    }
    reverse_proxy app:3000
}
```

Cloudflare proxied delante (ocultar IP + cache + DDoS). Ver [[aplus-server/stack|Stack]].

### Deploy de un nuevo producto

```bash
./add-product.sh tuf-rtx5080
# poner imágenes/videos en content/tuf-rtx5080/originals/
./watermark.sh tuf-rtx5080 libreopcion --visible
rsync -avz content/tuf-rtx5080/ user@vps:/srv/aplus/content/tuf-rtx5080/
```

El retailer pega su snippet apuntando a `https://aplus.tudominio.com/tuf-rtx5080/`.

## 3. Testing de integración

Checklist antes de entregar:

- [ ] **Referer whitelisted**: abrir `https://aplus.tudominio.com/<slug>/` pegando el link directo en el navegador → **debe dar 403** (no hay Referer de retailer). Si da 200 con `ALLOWED_REFERERS` seteado, el match está mal.
- [ ] **Iframe en retailer**: abrir la página de producto del retailer → iframe se carga, assets aparecen (video, imágenes, CSS).
- [ ] **Expiración**: en DevTools, copiar la URL firmada de un asset. Esperar > `TOKEN_TTL` seg. Refrescar el asset directamente → **410 Expired**. El HTML tiene `Cache-Control: no-store`, así que recargar la página siempre re-firma.
- [ ] **Embed fuera de whitelist**: poner el iframe en un HTML local con dominio distinto → navegador bloquea por `frame-ancestors`.
- [ ] **Hotlinking**: copiar URL de asset firmado, pegarla en otro `<img>` fuera del iframe → carga mientras no expire (HMAC solo gatea **quién firma**, no quién pide; para eso está el rate-limit por IP).

## 4. Por retailer — gotchas conocidos

### Libre Opción / Compragamer / retailers con Nuxt SSR
- El iframe va en el campo `descripcion_html` del producto (o equivalente). Ese campo se renderiza tal cual en la ficha.
- Como el retailer es SPA-hydrated, el iframe puede cargar después del primer paint → `loading="lazy"` está bien.
- Tener en cuenta que si el retailer filtra HTML con un sanitizer (tipo DOMPurify), puede que strippee el `<iframe>`. Chequear con el equipo del retailer antes.

### Fravega
- Usan un editor con whitelist de tags. Pedir que permitan `iframe` con `src` apuntando a `aplus.tudominio.com`. Suele requerir ticket.
- No todos los productos tienen acceso al campo de HTML libre — depende de la categoría.

### Mercado Libre
- ML **no permite iframes arbitrarios** en la descripción estándar. Para A+ content hay que usar el programa "Mercado Ads A+" o insertarlo solo en productos con categoría PLUS/Oficial.
- Si no hay más opción, alternativa: servir el contenido ya rendered + CSS inlined como HTML estático y que ML lo inserte, pero se pierde el watermark dinámico. Hablar caso por caso.

### Retailers con CSP estricto
- Si el retailer tiene `Content-Security-Policy: script-src 'self'`, el script del parent de iframe-resizer desde CDN va a fallar. Opciones:
  1. Self-host del parent script en el dominio del retailer.
  2. Usar el snippet mínimo con altura fija.

## 5. Preguntas frecuentes del integrador

**¿Por qué no dan una URL de JSON con los datos y nosotros armamos el layout?**
Porque el valor del A+ content es el **layout visual** (videos sync, tipografía, animaciones). Entregar JSON obligaría al retailer a reimplementar la presentación — y además perderíamos el watermark inline y el control de la experiencia. Si el retailer quiere armarlo, le damos el HTML + CSS fuente como proyecto aparte (no este server).

**¿El iframe impacta el SEO del retailer?**
No. El contenido del iframe es indexado separado (en otro dominio). El retailer no se beneficia ni se perjudica. Si le importa SEO del copy, debe tener su propia descripción corta **fuera** del iframe.

**¿Funciona en AMP?**
`<iframe>` en AMP requiere `<amp-iframe>` con restricciones (sandbox, min-height 100px, no en primer viewport). Caso por caso.

**¿Soporta dark mode?**
Hoy no. El `index.html` del slug es estático. Si se pide, podemos pasar `?theme=dark` como query param y que `server.js` inyecte una `<meta>` o clase al `<html>` — ver [[aplus-server/arquitectura#Parámetros de URL soportados|arquitectura]] para el patrón.

## Ver también

- [[aplus-server/arquitectura|Arquitectura]] — cómo funciona internamente el signing + rewriter
- [[aplus-server/stack|Stack]] — versiones y deps
- [[aplus-server/contexto|Contexto]] — modelo de amenazas y reglas operativas
