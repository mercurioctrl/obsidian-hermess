# Changelog blu-web-v1

> Registro de cambios relevantes fuera del código (assets, decisiones, etc.)
> Ver también: [[base-de-conocimiento]] · [[arquitectura]] · [[stack]]

## 2026-04-15 — Sistema de permisos por sección + fixes admin panel

Feature de permisos granulares para el admin panel: cada usuario tiene un array
`permissions` (JSON) que controla qué secciones del staffpanel puede ver y acceder.
Archivos principales modificados: `stores/auth.js`, `middleware/admin.js`,
`layouts/admin.vue`, `pages/staffpanel/usuarios.vue`, más 6 archivos del backend.

### Backend — sitio-api-rest-v1-laravel

- **Migration:** `2026_04_15_100000_add_permissions_to_users_table.php` — columna
  `permissions` JSON nullable en `users`. Todos los usuarios existentes (admin/staff)
  reciben todos los permisos en la migración.
- **Model `User.php`:** `permissions` en `$fillable` + cast `'permissions' => 'array'`
- **`LoginResponse.php`:** devuelve `permissions` array en la respuesta del login
- **`ListUserService.php`:** incluye `permissions` en el select de la lista
- **`UpdateUserRequest.php` + `CreateUserRequest.php`:** validación
  `'permissions.*' => 'string|in:contactos,citas,timeslots,catalogo,reclutamiento,usuarios'`
- **Fix `UpdateUserRequest`:** se agregó `'password' => 'sometimes|string|min:8'`
  a las rules — antes el campo se descartaba silenciosamente por `$request->validated()`
  y cambiar contraseña desde el admin no funcionaba

### Frontend — blu-web-v1

- **`stores/auth.js`:** nuevo getter `hasPermission(section)` — admin role siempre
  retorna true, otros chequean el array `user.permissions`
- **`middleware/admin.js`:** mapa `ROUTE_SECTION` de rutas a códigos de permiso,
  redirige a `/staffpanel` si el usuario no tiene permiso para la sección
- **`layouts/admin.vue`:** cada nav item tiene `v-if="auth.hasPermission('code')"`,
  dashboard siempre visible
- **`pages/staffpanel/usuarios.vue`:** columna "Permisos" en la tabla (muestra
  "Todos" / "X/6" / "Sin acceso"), checkboxes en modal crear/editar con toggle
  "Seleccionar todos"

### Migración a HTML nativo en el admin panel

Se reemplazaron todos los componentes Nuxt UI (`UInput`, `UButton`, `UFormField`)
en formularios del admin por HTML nativo (`<input>`, `<button>`, `<label>`) con
estilos scoped. **Razón:** el sitio público tiene dark mode global
(`@nuxtjs/color-mode`, preference: 'dark') y los componentes Nuxt UI heredan esos
estilos oscuros — inputs sin borde visible, labels invisibles, botones como texto
plano. Los `:deep()` con `!important` no son confiables.

Archivos migrados a HTML nativo:
- `pages/staffpanel/login.vue` — inputs + botón "Iniciar sesión"
- `pages/staffpanel/usuarios.vue` — form del modal crear/editar + botones

**Regla para futuras páginas admin:** siempre usar HTML nativo en forms.
`<UIcon>` y `<UModal>` sí funcionan. Ver [[memoria#HTML nativo en admin|memoria]].

### Checklist actualizada para nueva sección admin

Son ahora **7 pasos** (antes 4) al agregar una sección:
1. Crear `pages/staffpanel/{seccion}.vue` con HTML nativo
2. Agregar NuxtLink con `v-if` de permiso en `layouts/admin.vue`
3. Excluir de i18n en `nuxt.config.ts`
4. Agregar al mapa `ROUTE_SECTION` en `middleware/admin.js`
5. Agregar al array `SECTIONS` en `usuarios.vue`
6. Agregar al `in:` de `UpdateUserRequest` y `CreateUserRequest`
7. (Opcional) Migration para dar permiso a usuarios existentes

---

## 2026-04-15 — BIMI, dominio canónico y archivos de descubrimiento SEO

Tres cambios chicos enhebrados el mismo día que tocan el perímetro SEO/identidad
del sitio. Commits: `2e4a750` (BIMI), `5b87943` (fix dominio), `cbe1159` (docs).

### Logo BIMI en `/bimi/logo.svg`

- Nuevo archivo `public/bimi/logo.svg` — logo blanco "B." de Blu sobre fondo negro,
  1255 bytes, SVG Tiny 1.2 Portable/Secure (`baseProfile="tiny-ps"`, `version="1.2"`).
- Validado contra el perfil BIMI: tiene `<title>`, viewBox cuadrado `0 0 500 500`,
  sin scripts/animaciones/filters/xlink/refs externas, sin `x`/`y` en el root, bajo
  el límite de 32KB.
- Accesible en `https://blustudioinc.com/bimi/logo.svg` para el registro DNS de BIMI.
- **Nota:** el estándar BIMI rechaza SVGs normales — cualquier reemplazo futuro debe
  cumplir las mismas restricciones (ver checklist en [[base-de-conocimiento#SEO, dominio canónico y archivos de descubrimiento|CLAUDE.md → SEO]]
  o [[arquitectura#SEO y archivos de descubrimiento|arquitectura → SEO]]).

### Fix del dominio canónico `blustudiogroup.com` → `blustudioinc.com`

**Gotcha no-obvio:** la razón social legal de la empresa es "BLU STUDIO GROUP LLC"
(visible en PDFs de constitución y EIN), pero el dominio público **no es**
`blustudiogroup.com`. El dominio real es `blustudioinc.com` y coincide con todos los
handles sociales (`@blustudioinc` en Instagram, YouTube, Threads, LinkedIn).

Lugares corregidos (4 archivos, 12 ocurrencias):

- `nuxt.config.ts` → `site.url` + `runtimeConfig.public.siteUrl` (dos lugares)
- `public/robots.txt` → línea `Sitemap:`
- `public/llms.txt` → 6 URLs (servicios IT/Marketing/BI/Recruiting + web + contacto + idiomas)
- `public/.well-known/security.txt` → `Contact:` + `Canonical:`

Guardado como [[memoria#Dominio canónico blustudioinccom|memoria de proyecto]] para
que futuras sesiones no vuelvan a caer en la trampa.

### Sitemap

Ya existía: `@nuxtjs/sitemap` declarado en `nuxt.config.ts`. Genera `/sitemap.xml`
automáticamente en build, incluye todas las rutas con variantes i18n. El `robots.txt`
estático lo referencia explícitamente. No requirió nueva configuración — solo se
corrigió la URL base.

### Nueva sección en CLAUDE.md del proyecto

Se agregó sección "SEO, dominio canónico y archivos de descubrimiento" al
`CLAUDE.md` de `blu-web-v1` enumerando:

- Dominio canónico (+ por qué NO es el otro)
- Lugares donde el dominio vive hardcodeado
- Archivos de descubrimiento en `public/`: `sitemap.xml`, `robots.txt`, `llms.txt`,
  `.well-known/security.txt`, `bimi/logo.svg` (con checklist del perfil BIMI)

### Skill nuevo `/guardarContexto`

Se creó `~/.claude/skills/guardar-contexto/SKILL.md` para sistematizar el proceso
de persistir aprendizajes no-obvios al cerrar una sesión. El skill aplica el
principio "no guardar lo derivable" y clasifica cada fact entre CLAUDE.md del
proyecto y memoria de Claude según corresponda. Es el motor de la sincronización
automática de contexto sin tener que depender de que el usuario lo pida a mano.

---

## 2026-04-15 — Rename `/cmsadmin` → `/staffpanel`

El panel de administración del sitio pasó de vivir en `/cmsadmin` a `/staffpanel`.
La nomenclatura anterior sonaba genérica ("CMS admin"); `staffpanel` deja explícito
que es el panel interno para el equipo.

### Archivos tocados en el rename

- `pages/cmsadmin/` → `pages/staffpanel/` (via `git mv`, 7 archivos: index, login, contactos, citas, timeslots, catalogo, usuarios)
- `middleware/admin.js` — redirect a `/staffpanel/login`
- `stores/auth.js` — redirect de logout a `/staffpanel/login`
- `layouts/admin.vue` — 7 NuxtLinks y la lógica de `route.path.startsWith(...)`
- `pages/staffpanel/login.vue` — 2 redirects post-login al dashboard
- `nuxt.config.ts` — las 7 entries en `i18n.pages` que excluyen las rutas del sistema de i18n
- `CLAUDE.md` del proyecto y del monorepo

### Gotcha para renames futuros de rutas admin

Cualquier nueva ruta admin debe listarse explícitamente en `nuxt.config.ts > i18n.pages`
como `'staffpanel/nueva-ruta': false`, si no `@nuxtjs/i18n` le genera variantes
localizadas (/en/staffpanel/...) que no existen. La convención ya está documentada
en `CLAUDE.md > Admin Panel`.

### Verificación

`/staffpanel/login` responde 200 en el dev server. No hay referencias a `cmsadmin`
en el repo (`grep -r cmsadmin --include='*.vue' --include='*.ts' --include='*.js'`).

---

## 2026-04-13 — Catálogo de merch

Feature full-stack nueva: catálogo de merchandising corporativo con galería pública,
admin y flujo de import desde CSV. Commits: `1b5d1b3` (front) + `7a68533` (docs) +
`5ca9918` en [[arquitectura#Contexto en el monorepo|API Laravel]] (branch `gamma`).

### Frontend — `blu-web-v1`

- **Nueva página pública:** `pages/catalogoMerch.vue` — galería grid filtrable por
  categoría con búsqueda + lightbox. Rutas i18n `/catalogo-merch` ↔ `/merch-catalog`.
  Usa `GlowBackground` con accent magenta `#FF00D0`.
- **Link desde marketing:** card rosa en `pages/services/marketing.vue` debajo del
  `BentoGrid`, antes de `ServiceProcess`.
- **Admin:** `pages/staffpanel/catalogo.vue` — CRUD productos + upload múltiple de
  imágenes, set cover, delete. Nueva entry "Catálogo" (ícono `i-lucide-package`) en
  `layouts/admin.vue` entre Horarios y Usuarios. Excluida de i18n.
- **i18n keys:** `catalogoMerch.*` y `seo.catalogoMerch.*` en es/en.

### Backend — [[stack#Backend consumido|sitio-api-rest-v1-laravel]] (branch gamma)

- **Migraciones:** `products` (sku unique, category, title, description, active,
  sort_order) y `product_images` (product_id, path, sort_order, is_cover).
- **Dominio:** `app/app/Src/BackOffice/Catalog/` con List/Create/Update/Delete +
  Image/Upload/Delete/SetCover.
- **Storage:** imágenes en `storage/app/public/catalog/{sku}/`, requiere
  `php artisan storage:link`.
- **Import:** comando `php artisan catalog:import <ruta>` idempotente — lee CSV con
  columnas `sku, categoria, descripcion` y copia imágenes desde `<ruta>/images/{sku}/*`.

### Trampa crítica

El `.env` del backend trae `APP_URL=http://localhost` por default, pero la API corre
en puerto `8060`. Sin ajustar a `APP_URL=http://localhost:8060` las URLs de imagen
se generan con host incorrecto y dan 404 desde el front.

### Carga inicial

Import ejecutado con el catálogo Stanley 2025:
- 451 productos creados
- 247 con imágenes (683 archivos copiados al storage)
- 204 sin imágenes (el CSV no traía `drive_folder_url` para esos SKUs)
- 9 categorías: ADVENTURE, BAR, CAFÉ, CLASICOS, HIDRATACION, MASTER SERIES, MATE,
  MATE SYSTEM, OUTDOOR.

### Cómo agregar más productos en el tiempo

Manual (pocos): admin `/staffpanel/catalogo` → botón "Nuevo producto" → luego "Subir"
en el card.

Lote grande (flow validado):
```bash
docker cp ~/Downloads/nueva_tanda blu-api-laravel:/tmp/nueva_tanda
docker exec blu-api-laravel php artisan catalog:import /tmp/nueva_tanda
```

---

## 2026-04-04 — Actualización de assets aboutUs

Cambios en la página [[arquitectura#Sitio público|/nosotros]] (`aboutUs.vue`).

### Imágenes reemplazadas
- `public/img/aboutus/manifesto.jpg` — nueva foto editorial
- `public/img/aboutus/strip-1.jpg`, `strip-2.jpg`, `strip-3.jpg` — nuevo photo strip

### Imágenes mantenidas (sin cambio)
- `public/img/aboutus/unit-marketing.jpg`
- `public/img/aboutus/unit-bi.jpg`
- `public/img/aboutus/unit-recruiting.jpg`

### SVGs de clientes
- **Reemplazados:** `acer.svg`, `adata.svg`, `brother.svg` (nuevas versiones)
- **Mantenido:** `asus.svg` (versión anterior)
- **Nuevo:** `xpg.svg` — agregado como cliente

### Clientes actuales en aboutUs.vue
ASUS, Acer, Brother, ADATA, XPG — ver [[base-de-conocimiento#Estructura de Archivos Importantes|lista de archivos de clientes]]

> Hikvision fue removido previamente (commit `082c81b`).

---

## 2026-04-13 — Normalización de imágenes del catálogo

Refinamiento visual del [[arquitectura#Catálogo de merch|catálogo de merch]] para
que todas las fotos del cliente queden con un marco blanco uniforme. Dos partes:
frontend (cards con fondo blanco y padding interno) y backend (pipeline GD que
recorta márgenes y encaja sobre canvas cuadrado).

### Frontend — `pages/catalogoMerch.vue`

- `.cm-card__media`, `.cm-modal__media` y `.cm-thumb` ahora tienen `background: #fff`
- `<img>` interno con `padding` (12px card, 20px modal, 4px thumb) → queda marco blanco
- `filtered` computed ahora oculta productos con `active=false` o sin `images[]`,
  además del filtro del backend (doble seguro)

### Backend — `NormalizeImage` (GD puro)

Nuevo servicio en `app/app/Src/BackOffice/Catalog/Image/NormalizeImage.php`:

1. Detecta tipo real por contenido (`getimagesize`), no por extensión
2. Flatten sobre canvas blanco (maneja transparencia)
3. `whitenBackground()` — snap a blanco puro todo pixel con RGB ≥ 230
4. `imagecropauto(IMG_CROP_THRESHOLD, 0.5, white)` — recorta contenido real
5. Canvas cuadrado con 8% padding relativo al lado mayor
6. Save atómico con `.tmp` + `rename()`

Enganchado en:
- `UploadImage` (admin panel, tras `storeAs`)
- `ImportCatalog` (comando, tras `put`)

Nuevo comando artisan **`catalog:normalize-images`** con flags `--sku=X` y
`--product=ID`, idempotente — procesa 683 imágenes en ~2 min.

### Gotchas del proceso

- **`Copia de *.jpg` que son PNGs** — 20 archivos del cliente tenían extensión `.jpg`
  pero bytes PNG (export Mac). La primera versión usaba `pathinfo()` y fallaba.
  Fix: detectar tipo por contenido con `getimagesize()`. **Regla aplicable a todo
  procesamiento de uploads de cliente**: no confiar nunca en la extensión.
- **Threshold del cropauto** — 0.2 dejaba bordes visibles en productos con sombras
  suaves. Subir a 0.5 + pase de whiten previo resolvió todo.
- **`libpng warning: iCCP: too many profiles`** — warnings inofensivos por perfiles
  ICC corruptos en PNGs del cliente, GD los procesa OK igual.
- **Uniformidad visual absoluta imposible** con aspect ratios distintos — un vaso
  angosto siempre se ve más flaco que uno ancho en la misma card cuadrada. El
  pipeline garantiza que el "largo útil" sea idéntico (86% del canvas), no que
  el área ocupada lo sea.

### Ajuste fino posterior

Tuning de constantes en `NormalizeImage.php`:
- `PADDING_RATIO = 0.08` — 8% de margen en el lado mayor del contenido
- `CROP_THRESHOLD = 0.5` — tolerancia del cropauto
- `WHITEN_THRESHOLD = 230` — RGB mínimo para snapear a blanco puro

Si aparecen imágenes nuevas "chicas" o con margen extra, reprocesar con
`docker exec blu-api-laravel php artisan catalog:normalize-images --sku=XXX`.

### Backup

Antes del primer run masivo se guardó snapshot del volumen en el container:
`/tmp/catalog-backup.tgz` (`tar czf` sobre `catalog/`). Si se necesita revertir,
extraer ese tarball sobre `storage/app/public/`.

## 2026-05-06 — Propuestas comerciales detrás de token (`/propuestas/[slug]`)

Nueva ruta dinámica para servir propuestas comerciales personalizadas a clientes,
detrás de un token por URL, con el look del sitio (GlowBackground, Helvetica,
paleta de servicios) e identidad de marca del cliente parametrizable.

Commits: `30a41b5` (base), `37248e5` (identidad Gigabyte), `41bd510` (cleanup).

### Página `pages/propuestas/[slug].vue`

- `definePageMeta({ layout: false })` — sin Header/Footer del sitio.
- `useHead`: `<meta robots="noindex, nofollow">`.
- Catálogo `PROPOSALS` hardcoded (in-page) con slug → `{ token, client, brand,
  services[9], dashboardItems, exclusions, monthlyFee, ... }`.
- Gate: si `slug` no existe en `PROPOSALS` o `query.token` no matchea →
  pantalla "Acceso restringido" con logo Blu, sin filtrar contenido.
- Estructura mantiene la del HTML original (`assets/html/Gigabyte Propuesta.html`):
  nav, hero "Marketing que se diseña / no se improvisa", marquee, sobre Blu,
  para el cliente (con sub-marcas), 4 verticales, 9 servicios, dashboard 100%,
  pricing card con fee animado, exclusiones, cierre, footer.
- Animaciones: `IntersectionObserver` para reveals + counters (`100%` y fee USD).
- Excluida de i18n (`'propuestas/[slug]': false` en `nuxt.config.ts`) y del
  sitemap (`exclude: ['/propuestas/**', '/staffpanel/**']`).

### Identidad de marca por cliente — patrón `--brand`

Cada propuesta puede definir un `brand` con `{ logo, color, subBrands[] }`.
La página expone `--brand` como CSS variable a nivel `.proposal` y la usa en:

- Nav: logo del cliente al lado del logo Blu (con drop-shadow tinte brand).
- Client-section: orb del fondo, accent de "idioma del canal", borders y badges.
- Brand showcase: card con logo principal + grid de sub-marcas con tag.

Esto permite replicar el patrón con futuros clientes sin tocar el código:
basta con sumar entrada al `PROPOSALS` y depositar logos en
`public/clients/<slug>/`.

### Gigabyte — primera propuesta (token `gbt-mkt-2026`)

- Logos copiados desde `assets/html/gigabyteBrand/` a `public/clients/gigabyte/`:
  `gigabyte.png`, `aorus.png`, `aorus-silver.png`, `aero.png`.
- Fuente corporativa **Aldrich** copiada a `public/fonts/aldrich/` y registrada
  en `assets/css/fonts.css`. Aplicada en propuesta a labels técnicos
  (section-labels, kickers, badges, mono-tags, meta de servicios, footer) —
  el cuerpo y los titulares siguen en Helvetica para no perder identidad Blu.
- Color de marca **`#FF6600`** (naranja Gigabyte) como acento secundario
  exclusivo del client-section. Magenta y azul de Blu siguen siendo dominantes
  en el resto.
- Sub-marcas en showcase: AORUS (gaming), AERO (creator), AORUS Mark (lifestyle).

### Cleanup confidencialidad (`41bd510`)

Eliminado el strip fallback con ASUS/Acer/Brother/ADATA/XPG/Hikvision —
una propuesta confidencial no debe mencionar competidores del cliente.
Solo queda el showcase del cliente al que va dirigida la propuesta.

### Cómo agregar un nuevo cliente

1. Sumar entrada en `PROPOSALS` dentro de `pages/propuestas/[slug].vue`.
2. `mkdir public/clients/<slug>/` y dejar logos PNG/SVG.
3. Definir `brand: { logo, color, subBrands[] }` en la entrada.
4. URL final: `https://blustudioinc.com/propuestas/<slug>?token=<token>`.

### URL de la propuesta Gigabyte

`https://blustudioinc.com/propuestas/gigabyte?token=gbt-mkt-2026`

## 2026-05-07 — Polish visual de la propuesta Gigabyte

Sesión de ajustes finos sobre `pages/propuestas/[slug].vue` (sin cambios estructurales,
solo copy y estilos) para afinar la propuesta antes de presentarla.

### Cambios

- **Nav:** invertido el orden a "GIGABYTE × Blu" (cliente primero), `nav__client-logo`
  pasa a `height: 41px` en desktop para que el logo Gigabyte tenga peso visual.
- **Marca textual:** "Blu Studio | MKT · IT · BI · RECRUITING" reemplaza
  "Blu.Inc // MKT · IT · BI · RECRUITING" en el side-note del hero.
- **Hero copy:** nuevo lede "Integramos **marketing, comunicación y soporte** al canal
  en una ejecución coordinada, medible y **orientada a performance** — para maximizar
  el impacto de cada inversión." Más alineado al lenguaje del canal IT.
- **Color de acento por sección:**
  - "se diseña." (hero) y punto de "Activamos oportunidades." (sobre Blu) ahora en
    azul Blu `#0474f4` (override inline sobre `.accent` y `.dot`).
  - Punto de "idioma del canal." (cliente) en naranja Gigabyte `#FF6600`.
  - Bullet de "X sub-marcas" en `.mono-tag--brand` ahora en `$accent` (rosa) en vez de `--brand`.
- **Marquesina:** `scroll-x` acelerada de 38s → 14s (~2.7×) — la animación lenta
  daba sensación de quietud en la página.
- **Stats-row sobre Blu:** `padding: 28px 24px 16px 24px` simétrico en cada `.stat`
  para que las labels (FRENTES DE SERVICIO, SOPORTE INTEGRAL, etc.) no queden pegadas
  al borde divisor con el cell siguiente.

### Gotcha de entorno (no del código)

Cuando se levanta `npm run dev` en blu-web-v1, el puerto `3000` puede estar tomado
por otro container Docker (en este caso `aplus-server-app-1`, que mappea
`127.0.0.1:3000`). Síntoma: `localhost:3000` devuelve `{"message":"Route GET:/ not found",
"statusCode":404}` con formato Nitro/Fastify, no Nuxt. La razón: Nuxt dev bindea a
`[::1]:3000` (IPv6), Docker a `127.0.0.1:3000` (IPv4) — `localhost` resuelve primero
a IPv4 y pega al container equivocado. Solución: `docker stop aplus-server-app-1`
o entrar por `http://[::1]:3000`.

## 2026-05-08 — Continuación polish Gigabyte (commits del día)

Sesión larga de iteración sobre la propuesta Gigabyte: copy, color de acentos por
sección, confetti en el CTA y arreglos mobile. Cuatro commits en `catri-fork-2026-temporada-2`
(`d63de68`, `9395365`, `a03252d`, `3758db7`).

### Estructura — Verticales

Removido el grid de 9 tiles (Blu.IT, Blu.Marketing, Blu.Bi, Blu.Recruiting + cells soft +
center "Servicios"). Se conserva el header "Cuatro verticales, una sola operación." +
el párrafo descriptivo. Razón: el grid quedaba repetitivo y comía espacio sin aportar
información — el resto de la página ya lo cubre.

### Copy y servicios

- **Servicio 07:** rebautizado "Soporte **360°** en IT" (antes "en marketing"). Nuevo
  desc: "Nos aseguramos de que los recursos, sistemas y herramientas funcionen —
  soporte continuo a equipos, partners y operaciones." Marca explícita el alcance IT
  como vertical Blu transversal a la propuesta de marketing.
- **Servicio 09:** cierre del desc cambia a "...próximos pasos y trazabilidad."
  (antes terminaba "...próximos pasos — todo trazado.").
- **Hero side-note:** "Blu Studio | MKT · IT · BI · RECRUITING" (separador `|`,
  no `//`).
- **Cierre:** "¿Querés transformar **tus objetivos** en realidad?" (antes "¿Listos
  para transformar..."). Ambos signos de pregunta en blanco; "tus objetivos" en azul.

### Identidad — sub-marcas Gigabyte

- AERO usa el `Aero.png` cuadrado (más limpio que el wordmark). Para emparejar el
  visual con AORUS y la 3ra card, se baja la altura solo de AERO con
  `logoMaxHeight: 23.6` en la data del sub-brand y un binding inline `:style` sobre
  el `.sub-brand__logo`.
- 3ra card pasa de "AORUS Mark / aorus-silver.png" a usar `buchino.png` (el águila
  AORUS — copiado a `public/clients/gigabyte/buchino.png`). El `name` del data sigue
  siendo "AORUS Mark" para no tocar el dataset, solo cambia el logo visible.
- Para que los tags ("GAMING · HIGH-END", "CREATOR · WORKSTATION", "LIFESTYLE · ESPORTS")
  queden todos en la misma línea base sin importar el alto real de cada logo, se envuelve
  el `<img>` en un `.sub-brand__logo-slot` de `height: 36px` con flex center. El logo
  vive centrado dentro del slot fijo.

### Color por sección — uso del nuevo dot

El `<span class="dot">` heredaba siempre rosa (`$accent`). Se sobreescribe con
`style="color: #..."` inline en los puntos finales para alinear cada sección a su
identidad cromática:

- **Azul Blu (`#0474f4`):** "se diseña.", "Activamos oportunidades.",
  "Nueve servicios, una sola operación.", "visible en tiempo real.",
  "inversión clara, mensual y abierta.", `%` del 100% (`-webkit-text-fill-color`
  en `.big-counter .units`).
- **Naranja Gigabyte (`#FF6600`):** "idioma del canal." (sección "Para el cliente").
- **Rosa (`$accent`):** bullet de "X sub-marcas" (`.mono-tag--brand::before` ahora
  fija a `$accent` en vez de `var(--brand)`).

### CTA con confetti — `fireConfetti()`

El botón "Avancemos con Gigabyte" del closer pasa de `<a href="mailto:...">` a
`<button @click="fireConfetti">`. La función está en el `<script setup>` del slug y
no depende de librerías:

- Crea un `<div>` overlay `position:fixed;inset:0;pointer-events:none;z-index:9999`
  appended a `body`.
- Genera 180 partículas (mezcla de cuadrados ~6-14px y círculos), colores
  `#FF00D0`, `#0474f4`, `#FF6600`, `#00D985`, `#9c44ff`, `#00CFCE`, `#fff`.
- Origen: bounding rect del botón (`event.currentTarget.getBoundingClientRect()`,
  centro). Velocidad inicial random con ángulo entre -30° y -150° desde la horizontal.
- RAF tick: gravedad `vy += 0.35`, drag `vx *= 0.992`, fade en los últimos 40 frames.
- `cancelAnimationFrame` + `layer.remove()` cuando todas mueren (~3-4s).

`.cta` necesitó `border:none; cursor:pointer; font-family:inherit` para que el
`<button>` se vea idéntico al `<a>` que reemplaza.

### Fixes mobile (≤900px)

- **Tachado de "No se improvisa.":** la pseudo-línea diagonal absoluta con
  `transform: rotate(-3deg)` se rompía cuando el span wrappeaba a 2 líneas (una sola
  raya inclinada cruzando ambas). En `@media (max-width: 900px)` se desactiva el
  `::after` y se usa `text-decoration: line-through; text-decoration-color: $accent`,
  que sigue cada línea de texto. Desktop conserva el tachado diagonal estilizado.
- **Chip del nav "Propuesta · Mayo 2026":** se split en
  `<span class="tag">Propuesta<span class="tag__date"> · Mayo 2026</span></span>`
  con `.tag__date { display: none }` en mobile. El chip muestra solo "Propuesta" en
  mobile y "Propuesta · Mayo 2026" en desktop sin duplicar markup.

### Sobre Blu — stats-row

Padding simétrico `28px 24px 16px 24px` en cada `.stat` (antes era `28px 20px 4px 0`,
con left=0 los labels quedaban pegados al borde divisor con la celda anterior).
Desktop fue lo único que se ajustó; mobile heredaba el problema y ahora también queda bien.

### Marquesina

`scroll-x` acelerada de **38s → 14s** (≈2.7×). La animación lenta daba sensación
de quietud entre el hero y el bloque "Sobre Blu".

### Nav — orden invertido

Pasa de "Blu × {cliente}" a "{cliente} × Blu" — la propuesta está dirigida al cliente,
así que su logo lleva la lectura. `nav__client-logo` sube a `height: 41px` desktop
para que GIGABYTE tenga peso visual contra el `nav__logo` de Blu (22px).

### Assets versionados (`a03252d`)

Se sumaron al repo todos los archivos en `assets/html/gigabyteBrand/` (111 archivos,
+22994 líneas): logos PDF/PNG/AI (GBT, AORUS, AERO, mascotas), fuentes TTF/OTF (AORUS,
Akzidenz, DINPro, Industry, Roboto, Teko, Aero Matics, Aldrich), Manual de Marca PDF
(9.5MB) y los PNG ya copiados a `public/clients/gigabyte/`. Convención: el material
fuente de marca se versiona como `assets/html/{cliente}Brand/`, los assets servidos
en runtime van a `public/clients/{slug}/`.

## 2026-06-12/13 — Landing del monitor Gigabyte MO27Q28G (estética del sitio oficial)

Nueva propuesta `gigabyte-monitor` servida en `/propuestas/gigabyte-monitor?token=gbt-mo27-2026`:
una landing one-page de **estrategia comercial integral** para posicionar el monitor
Gigabyte MO27Q28G a través del reseller MEXX en Argentina. Componente nuevo
`components/Propuestas/MonitorPresentation.vue`. Commits en `catri-fork-2026-temporada-2`:
`b7fdc9d` (base), `58f87d8` + `1dcd5f8` + `106030c` (rondas de copy).

### Mecanismo de dispatch por `kind`

`pages/propuestas/[slug].vue` ahora puede **delegar el render a un componente** según el
campo `kind` de la propuesta. El slug `gigabyte-monitor` define `kind: 'monitor'` y la
página hace `<MonitorPresentation v-else-if="proposal.kind === 'monitor'">`. Las propuestas
sin `kind` (ej. `gigabyte`) se siguen renderizando inline en la página. El gate por token
es el mismo para ambos tipos.

### Contenido hardcoded en arrays del `<script setup>`

Todo el copy de la landing (heroStats, problems, marketRows, regionRows, mexxAudit, ejes,
pitch, funnel, ads, adsKpis, roadmap, pillars) vive en arrays `const` dentro del
`<script setup>` de `MonitorPresentation.vue`. **Para editar textos se tocan esos arrays,
no el template.** Toda la sesión de ajustes de copy (poder adquisitivo, márgenes, garantía,
Ahora 12/18, cifras de Ads $23.333/día, activaciones del roadmap, etc.) fue editar strings
en esos arrays.

### Identidad visual = AZUL Gigabyte, no naranja

La landing imita la página oficial https://www.gigabyte.com/es/Monitor/MO27Q28G. Decisión
cromática clave: **la línea Gigabyte Gaming usa azul, el naranja `#FF6600` es de AORUS**
(sub-marca). La primera versión usó naranja por arrastre de la propuesta de marketing
anterior; se corrigió a:

- `$accent: #00A0E9` (cyan de botones/labels del sitio oficial)
- `$blue-accent: #0446F2` (azul profundo de los headings Gigabyte)
- Reemplazos de todos los `rgba(255,0,208,...)` (magenta) y `rgba(255,102,0,...)` (naranja)
  por el azul correspondiente.

### Otros detalles de la estética Gigabyte

- **Tipografía:** `Aldrich` en MAYÚSCULAS en `.hero-title` y `.sec-head h2` (la fuente ya
  estaba cargada en `assets/css/fonts.css`). Imita headlines tipo "PERFECT VIEWING ANGLE".
- **Fondo negro plano:** se removió el `GlowBackground` (orbs) del componente; glows internos
  del hero/closer bajados de opacidad.
- **UI rectangular:** botones/badges/chips a `border-radius: 4px` (no píldoras), como el botón
  "Buy Now" del sitio oficial.
- **`.section-label`** (eyebrows): cyan con barra horizontal de 22px, estilo labels Gigabyte.
- **`.textwall`:** muro de texto repetido en outline detrás del hero ("Perfect Black ·
  Tandem OLED · 280Hz"), firma visual de la página oficial.
- **Textos secundarios en blanco:** el token `$ink-mute` se subió de `rgba(255,255,255,0.45)`
  a `#ffffff` puro por pedido (labels de stats, headers de tabla, nav, footer se veían apagados).

### Gigabyte/AORUS bloquean bots — cómo se vio la página real

WebFetch y `curl` reciben **403 Access Denied** (Akamai) en gigabyte.com y aorus.com. Se
cargó la página real con **Playwright + el Chrome del sistema** (`chromium.launch({
channel: 'chrome' })`), screenshots por scroll y extracción de colores con `getComputedStyle`.
Mismo patrón sirvió para screenshotear la landing local en `:3008` y verificar el diseño.
Existe un skill `/replicarMicrosite <url>` que automatiza esto. Ver
[[memoria#Ver sitios que bloquean bots Gigabyte AORUS|memoria]].

### Producto MO27Q28G

27" QHD 2560×1440, 280Hz, 0.03ms, WOLED 4ta gen (Primary RGB Tandem OLED), DisplayHDR True
Black 500, 99.5% DCI-P3. Estrategia: el producto es superior pero caro en USD vs Chile/Uruguay
y nadie comunica su valor en Argentina → ganar en valor percibido, no en precio.

## 2026-06-17 — Toggle del fee + gotcha de assets estáticos en dev

Sesión de cierre sobre las propuestas. Dos cosas que faltaban documentar.

### Toggle ojo para ocultar/mostrar el fee mensual (commit `fc176ff`)

En `pages/propuestas/[slug].vue`: el monto del fee mensual arranca **oculto** detrás de
una máscara `*,***` y se revela con un botón tipo ojo. El contador (`animateFee`) no
corre mientras el monto está en `display:none`, así que se dispara al revelar si todavía
no había animado:

```js
const feeHidden = ref(true);
function toggleFee() {
	feeHidden.value = !feeHidden.value;
	if (!feeHidden.value && feeDisplay.value === 0 && proposal.value) {
		animateFee(proposal.value.monthlyFee);
	}
}
```

Estructura visual: `.fee-value` contiene `.fee-mask` (`*,***`, `aria-hidden`) + `.fee-real`
(el contador), y la clase `.amount--hidden` alterna cuál se ve. Sirve para presentar la
propuesta y revelar el precio recién al final.

### Gotcha: assets estáticos rompen en dev desde archivos de ruta con corchetes

Al previsualizar la landing del monitor con `npm run dev`, las imágenes daban **400** en
SSR. El log mostraba `__nuxt_vite_node__/resolve/virtual:public?/clients/.../gigabyte.png
... 400 Bad Request`. **Causa:** el transform de assets estáticos de Vite (vite-node) no
resuelve `<img src="/...">` cuando el archivo importador tiene **corchetes en el nombre**
(`[slug].vue`). `index.vue` y demás funcionan; solo rompe en rutas dinámicas con `[ ]`.

**Fix:** pasar el `src` a **binding dinámico** contra una `const` string — el string en
runtime evita el transform de assets:

```js
const bluLogo = '/img/logo.svg';        // luego  :src="bluLogo"
const clientLogo = '/clients/gigabyte/gigabyte.png';
```

Se aplicó a los 3 logos de `[slug].vue` y a los de `MonitorPresentation.vue`. **Solo afecta
al dev server** — en producción (PM2 build) los `src` estáticos sirven bien, por eso nunca
se había notado. Ver [[memoria#Assets estáticos rompen en dev desde rutas con corchetes|memoria]].
