# Changelog

Registro de cambios por fecha. Append-only — no borrar entradas previas.

## 2026-04-14 — Homepage updates (rama `feature/homepage-updates-abril-2026`)

Reestructuración visual y arquitectural del homepage + dos páginas nuevas. 7 commits pusheados a `origin`.

### Home — reorder y limpieza

- **Featured Products movido arriba** — ahora aparece justo debajo del hero, antes de wellness goals. Da visibilidad inmediata al catálogo.
- **Ciencia & Bienestar (blog preview) eliminado del home** — el contenido queda solo en `/blog`. Componente `HomeBlogPreview.vue` borrado del repo.
- **Basado en evidencia (science ingredients) eliminado del home** — movido a la nueva página `/ciencia`.
- **QualityBadges + CertificationsSection unificados** — un único componente `home/QualityBadges.vue` que ahora recibe dos props: `badges` (feature cards con descripción) + `certifications` (row bajo el título "Estándares de fabricación premium"). El viejo `CertificationsSection.vue` se eliminó.

### Páginas nuevas

- **`pages/ciencia.vue`** — hero, re-usa `HomeScienceIngredients`, lista de quality promises y certifications. Fetch a `/cms/home` (no hay endpoint dedicado).
- **`pages/profesionales.vue`** — portal para profesionales de la salud (emulando giovegen.com/profesionales/). Hero + 4 beneficios + formulario de inscripción. **TODO:** form handler apunta a endpoint inexistente `/api/professionals`.

### Nav

- Agregado link **"Profesionales"** al header (`TheHeader.vue`). Nav ahora: `Inicio | Productos | Ciencia | Blog | Profesionales`.
- `reservedSlugs` en `pages/[slug].vue` actualizado con `ciencia` y `profesionales` para evitar que el catch-all los intercepte.

### Wellness Goals — 6 columnas + hover crossfade

- Grid cambiado de `lg:grid-cols-5` a `lg:grid-cols-6` (las 6 categorías en una sola fila desktop, 2 cols mobile, 3 cols tablet).
- **Hover crossfade estilo Horbäach** — cada card tiene dos capas absolutas que se crossfade con `group-hover:opacity-0/100 transition-opacity duration-500`:
  - Default: foto lifestyle (o SVG fallback por slug).
  - Hover: foto frasco/producto (o SVG genérico sobre gradiente por slug).
- Soporta `goal.lifestyle_image_url` y `goal.product_image_url` desde el CMS si existen (hoy no existen, los SVG se muestran como placeholders).
- **TODO:** subir fotos reales a `public/images/categories/` o agregar columnas a `wellness_goals`.

### Hero — más ancho, más impactante

- `HomeHeroSlider` ahora con `min-h-[85vh]` en desktop y `h-[clamp(480px,70vw,880px)]` en mobile.
- Tipografía del título ampliada: `text-4xl md:text-6xl lg:text-7xl xl:text-8xl`.
- Overlay con gradiente más fuerte (`from-black/60 via-black/30`).
- `HomeHeroBanner` (variante sin slider) también agrandado para mantener consistencia.

### Docs

- `naevo/docs/architecture.md` actualizado con nuevo orden del home, tabla de páginas con `/ciencia` y `/profesionales`, notas en componentes (QualityBadges dos props, WellnessGoals hover crossfade, gotcha de `reservedSlugs`).

### Commits

```
5aebd05 docs: actualizar architecture.md con home reorder y nuevas páginas
71bde08 hero: min-h-[85vh], tipografía más grande para más impacto
2a3c99c wellness-goals: grid 6 cols + hover crossfade lifestyle↔producto
e8216e9 nav: agregar Profesionales + página /profesionales
fb8d0ec home: sacar Science/BlogPreview del home; crear página /ciencia
11d2301 home: unificar QualityBadges + CertificationsSection en una sola sección
8719a62 home: mover Featured Products debajo del hero
```

### Archivos tocados

- `frontend/pages/index.vue` — reorder + remove
- `frontend/pages/ciencia.vue` — nuevo
- `frontend/pages/profesionales.vue` — nuevo
- `frontend/pages/[slug].vue` — reservedSlugs
- `frontend/components/TheHeader.vue` — nav link
- `frontend/components/home/QualityBadges.vue` — dos props
- `frontend/components/home/WellnessGoals.vue` — grid + crossfade
- `frontend/components/home/HeroSlider.vue` — tamaño
- `frontend/components/home/HeroBanner.vue` — tamaño
- `frontend/components/home/BlogPreview.vue` — **eliminado**
- `frontend/components/home/CertificationsSection.vue` — **eliminado**
- `docs/architecture.md` — doc update

## Ver también

- [[naevo|Índice]]
- [[arquitectura|Arquitectura]]
- [[contexto|Contexto y TODOs]]

## 2026-04-14 (tarde) — Iteraciones post-primer review

Siguiente tanda sobre la misma rama — 13 commits más.

### Wellness Goals — fotos reales + estilo Horbäach exacto

- **Migración y CMS editable:** se agregaron `lifestyle_image_url` y `product_image_url` a la tabla `wellness_goals` (migration `2026_04_14_000001`). El admin UI (`/admin/objetivos`) ahora tiene dos inputs de upload (preview circular + botón "Subir imagen" + "Quitar imagen") usando el mismo patrón que los banners del CMS.
- **Endpoint de upload:** `POST /api/admin/wellness-goals/upload-image` (copiado del `CmsController::uploadImage`), guarda en el volumen Docker en `storage/app/public/wellness-goals/`.
- **Fotos lifestyle:** 6 JPGs descargados de Unsplash (licencia libre), una por categoría. URLs directas del CDN de Unsplash con params `w=800&h=800&fit=crop&crop=faces,center`.
- **Fotos producto:** los 6 frascos reales de NAEVO (Hidro Curcumina, Magnesio, DHA Algal, Astaxantina, Resveratrol, Prebiótico) extraídos del volumen `products/`, procesados con **Python PIL en el host** (no hay ImageMagick) para remover el fondo blanco: pixels ≥240 → transparente, ≥220 → alpha degradado, trim al bbox, centrado en canvas 800×800 transparente. Resultado: PNGs con el frasco flotando limpio.
- **Iteración visual:** primero tenían card blanco + gradient detrás del frasco, pero el cliente pidió "sin contenedor negro" y "efecto Horbäach". Se quitó el card blanco (solo queda el círculo + título + descripción sobre el fondo gris de la sección) y el gradient del hover layer (el PNG transparente flota directo sobre el fondo). Los frascos quedaron +15% de tamaño (`w-28 h-28 lg:w-32 lg:h-32`).
- **Hover effect exacto de Horbäach:** se extrajo el CSS real del `theme.css` de horbaach.com (búsqueda en `.collection-item`) y se replicaron los valores sin cambios: imagen `scale(1.01) → scale(1.07)` con `transition 950ms cubic-bezier(.25,.46,.45,.94)`, título `translateX(7px) → 0` + `text-primary-600`, flecha `→` con fade+slide. Clases `.wg-item*` en el `<style scoped>` del componente.

### Fixes varios (primera iteración de review del cliente)

- **Logo header más grande:** `h-5 lg:h-6` → `h-8 lg:h-12` (desktop) + mobile menu `h-4` → `h-7`. Después el cliente pidió un 5% más chico → `h-[30px] lg:h-[46px]`.
- **Logo SVG:** se migró de `logo.png` a `logo.svg` (archivo original del cliente, viewBox 493×93). Actualizado en TheHeader, TheFooter, AdminSidebar y auth layout. Los contextos "oscuros" (footer/admin) mantienen `brightness-0 invert` que funciona igual con SVG.
- **Logo editable desde admin:** ver siguiente sección.
- **Descripción Salud Estética:** el wellness goal `salud-estetica` no tenía descripción. Se agregó "Cuidá tu piel, cabello y uñas desde adentro" en DB + seeder.
- **Hero /profesionales con foto real:** el placeholder del ícono de corazón fue reemplazado por una foto de una doctora con guardapolvo blanco (Unsplash, foto `lnlSIsiSjjc`). Guardada en `frontend/public/images/profesional-salud.jpg`. El hero tiene glow gradiente + ring sutil + overlay inferior para integrarse al fondo azul.

### Admin — logo editable desde `/admin/configuracion`

Patrón nuevo para exponer settings públicos al storefront:

- **Backend:** nuevo `PublicSettingController` con `const PUBLIC_KEYS` whitelist (hoy `logo_height_mobile` y `logo_height_desktop`). Ruta pública `GET /api/public-settings` devuelve un map key→value filtrado. Los 2 settings se agregaron al seeder (`SettingSeeder`) con valores default 30/46.
- **Frontend:** composable `composables/useSiteSettings.ts` con `useAsyncData('site-settings', ...)` deduped entre componentes. `TheHeader` lee los valores, aplica CSS custom properties (`--logo-h-mobile`, `--logo-h-desktop`) via `:style` binding, y un `<style scoped>` las consume con media query en breakpoint `1024px`. Fallback hardcoded 30/46 si el endpoint falla.
- **Admin UI:** `/admin/configuracion` ya era genérico (itera sobre settings por grupo). Se le agregó `keyLabels` + `keyHints` para mostrar nombres amigables ("Alto del logo en mobile (px)") en vez del key raw. Input type `number` cuando el setting es numérico.

**Cómo sumar un nuevo setting público** (futuro reference): 1) insertar row en `settings`, 2) agregar la key al array `PUBLIC_KEYS`, 3) extender la interface `PublicSettings` en `useSiteSettings.ts`, 4) opcional label/hint en configuracion.vue.

### Commits

```
2dcef7c admin: logo editable desde configuración via settings logo_height_mobile/desktop
1a5d6d3 header: logo 5% más chico
fb8cb96 logo: usar SVG en lugar de PNG (header, footer, mobile menu, admin sidebar, auth)
a378c21 profesionales: foto real de profesional de la salud en hero
acf36f9 seeder: descripción de Salud Estética
53527a8 header: logo NAEVO más grande
bfd519e wellness-goals: quitar card blanco + efecto hover Horbäach
1149ee0 wellness-goals: frascos NAEVO reales transparentes, +15% size
47a9e58 docs: agregar sección Obsidian al CLAUDE.md del proyecto
46a985d seeder: 6 wellness goals con URLs de imágenes por defecto
01afaa8 admin objetivos: inputs de upload para imágenes
54509a1 admin: endpoint upload-image + validación
56a4caa wellness-goals: migración + model para lifestyle_image_url y product_image_url
```

### Gotchas aprendidos

- **macOS TCC:** `~/Documents`, `~/Desktop`, `~/Downloads` están bloqueados por TCC incluso con `dangerouslyDisableSandbox: true` — pedirle al user que mueva los archivos a `/tmp/` con el prefijo `!`, o que habilite el permiso en System Settings → Privacy & Security → Files and Folders → Claude Code.
- **Slug con ñ:** `wellness_goals.slug = 'antiestres-sueño'` tiene ñ en la DB de producción, pero los file names en el storage usan ASCII (`antiestres-sueno-lifestyle.jpg`). Funciona por mapping manual en tinker, pero si se normaliza el slug a ASCII en el futuro hay que renombrar los archivos también.
- **`apiResource` interfere con rutas custom:** cuando se agrega una ruta tipo `Route::post('wellness-goals/upload-image', ...)` hay que declararla **antes** del `Route::apiResource('wellness-goals', ...)` sino `upload-image` se interpreta como `{id}`.
- **Python PIL en el host** es la forma práctica de procesar imágenes — no hay ImageMagick instalado ni en la Mac ni en el container backend. PIL ya viene con Python 3 en macOS.

## 2026-04-14 — Notas de ops (no hay commits nuevos)

Sin cambios en la rama `feature/homepage-updates-abril-2026` desde `e3467ea`. Dos gotchas de deploy aprendidos al correr el restore+start en el servidor de producción (AWS Ubuntu `ip-172-31-16-62`):

### Restore: warnings cosméticos de tar

Al correr `./restore.sh` en el server, tar escupe ~100 líneas de:

```
tar: Ignoring unknown extended header keyword 'LIBARCHIVE.xattr.com.apple.provenance'
```

**No es un error.** El `tar` de macOS (libarchive) mete un xattr propietario `com.apple.provenance` cuando comprime, y el GNU tar de Ubuntu no lo entiende pero lo ignora sin romper nada. La restauración completa OK igual.

**Workaround opcional** (silenciar ruido en `restore.sh`): cambiar la línea

```bash
tar -xzf "$SELECTED" -C "$TEMP_DIR"
```

por

```bash
tar -xzf "$SELECTED" -C "$TEMP_DIR" 2> >(grep -v 'LIBARCHIVE.xattr' >&2)
```

Filtra solo esos warnings sin ocultar errores reales.

### Start: Ubuntu sin docker compose v2

En el server viejo estaba solo `docker` sin el plugin `compose` v2 — `start.sh` usa la sintaxis nueva (`docker compose ...` con espacio) y falla con `docker: 'compose' is not a docker command`.

**Fix:**

```bash
sudo apt update && sudo apt install -y docker-compose-plugin
docker compose version  # verificar
```

Si el package no está en el repo (distro vieja sin repo oficial de Docker), primero agregar el repo de Docker:

```bash
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update && sudo apt install -y docker-compose-plugin
```

**Importante:** no usar `docker-compose` con guion (v1 standalone, deprecado). El script usa v2 y muchos comandos fallan si se fuerza v1.
