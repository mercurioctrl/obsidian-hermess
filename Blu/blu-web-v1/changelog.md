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
