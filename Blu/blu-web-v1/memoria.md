# Memoria — blu-web-v1

Consolidación de [[base-de-conocimiento|Claude memory]] del proyecto para consulta rápida en Obsidian. Fuente autoritativa: `~/.claude/projects/-var-www-blu-blu-web-v1/memory/` (Linux; en sesiones viejas era Mac `-Users-hermess-www-blu-blu-web-v1`).

> Ver también: [[blu-web-v1]] · [[arquitectura]] · [[changelog]]

## Preferencias del usuario

- **Sin co-autor en commits** — NUNCA agregar `Co-Authored-By` ni modificar autorías de git
- **Simplicidad** — iterar rápido cuando algo no gusta, preferir simple sobre complejo
- **Estilo visual:** pills estilo Apple, tipografía estilo Mercury Bank (letter-spacing negativo, grids ultra sutiles), minimalismo
- **Sin colores extra en estados activos** — efectos limpios (rotación, escala) sin gradientes coloridos
- **Efecto glitch solo en hover**, no en estados permanentes
- **Tildes en español argentino** — siempre correctas en todo texto en español
- **Botones nunca `disabled`** — siempre activos, validación en el click

## Feedback de workflow

- **Features full-stack:** proponer bullets → ejecutar todo → dejar corriendo → push en repos separados
- **Commits:** mensajes en español, concisos, sin co-autor, uno por concepto claro
- **Commitear solo lo tocado:** el working tree de la branch `catri-fork-2026-temporada-2` tiene ~45 archivos modificados de sesiones previas que NO son míos. Usar `git add <paths específicos>`, nunca `git add -A`.
- **Push con conflicto de fast-forward:** `git pull --rebase --autostash origin <branch>` (autostash porque hay cambios sin commitear en el tree).
- **Rondas de copy:** el usuario suele pedir muchos micro-ajustes de texto seguidos; conviene NO rebuildear/pushear tras cada uno — acumular y hacer un solo build+push cuando dice "hacé el push".
- **Descarga archivos protegidos:** fetch+blob+objectURL con Bearer token, NO `<a href>` (el token no viaja en links)

## Build y deploy (PM2 en 3008)

El front **NO usa dev server** en la máquina; corre el build de producción con PM2 y **no hay HMR**. Todo cambio requiere:

```bash
npm run build && pm2 restart BLUWeb
# verificar: curl -s -o /dev/null -w "%{http_code}" http://localhost:3008/   (200 = OK)
```

- `ecosystem.config.cjs`: app **`BLUWeb`**, cluster mode, **puerto 3008**, usuario `hermess` (NO root), PM2_HOME `/home/hermess/.pm2`.
- Otros proyectos corren en Docker (gigaerp, blufixture, naevo, minisaas) con `node .output/server/index.mjs` cwd=`/app` — no confundir con BLUWeb.
- Backend Laravel `blu-api-laravel` en Docker → `:8060`. MySQL `:3308`, Redis `:6381`.
- El dev server (`npm run dev`, 3000) puede chocar con un container Docker que ocupa `127.0.0.1:3000` (Nuxt bindea IPv6 `[::1]:3000`). Ver [[changelog#2026-05-07 — Polish visual de la propuesta Gigabyte|gotcha IPv4/IPv6]].

### Assets estáticos rompen en dev desde rutas con corchetes

En `npm run dev`, `<img src="/...">` **estático** da **400** en SSR (`virtual:public?... 400`)
cuando el archivo de ruta tiene **corchetes en el nombre** (`pages/propuestas/[slug].vue`).
El transform de assets de vite-node no resuelve la URL pública en archivos `[ ]`. Solo pasa
en dev — en producción (PM2 build) los `src` estáticos sirven bien.

- **Fix:** binding dinámico contra una `const` string → `const bluLogo='/img/logo.svg'`,
  luego `:src="bluLogo"`. El string en runtime evita el transform.
- Aplica a logos/imágenes de `[slug].vue` y `MonitorPresentation.vue`.
- Ver [[changelog#2026-06-17 — Toggle del fee + gotcha de assets estáticos en dev|changelog 2026-06-17]].

## Ver sitios que bloquean bots (Gigabyte, AORUS)

WebFetch y `curl` reciben **403 Access Denied** (Akamai) en gigabyte.com y aorus.com. Para ver/capturar la página real:

- **Playwright + Chrome del sistema:** `chromium.launch({ channel: 'chrome' })` (el chromium bundled de Playwright NO está descargado → da "Executable doesn't exist").
- `/usr/bin/google-chrome` y `/usr/bin/firefox` instalados. Playwright: `cd /tmp && npm install playwright@1.60.0 --no-save`.
- Patrón: userAgent de browser real, `goto` con `waitUntil:'domcontentloaded'`, `waitForTimeout`, scroll por % de page height + screenshot por parada, `getComputedStyle` para extraer colores reales.
- Mismo patrón sirve para screenshotear la landing local en `:3008` y verificar diseño en vez de adivinar.
- Existe el skill **`/replicarMicrosite <url>`** que automatiza replicar microsites de producto (descarga assets, extrae colores del CSS). Considerarlo primero.

## Landing del monitor Gigabyte (estética oficial)

`components/Propuestas/MonitorPresentation.vue`, slug `gigabyte-monitor` (token `gbt-mo27-2026`).

- **Identidad = página oficial del MO27Q28G, NO el sistema Blu.** Color de marca **AZUL** Gigabyte: `$accent: #00A0E9` (cyan botones/labels), `$blue-accent: #0446F2` (headings). **El naranja `#FF6600` es de AORUS** (sub-marca), no de la línea Gigabyte Gaming — error fácil de cometer.
- Títulos en **`Aldrich` mayúsculas**, fondo negro plano (sin GlowBackground), UI rectangular `border-radius: 4px`, `.textwall` de texto en outline tras el hero.
- **Todo el copy vive en arrays `const` del `<script setup>`** (heroStats, problems, marketRows, regionRows, mexxAudit, ejes, pitch, funnel, ads, adsKpis, roadmap, pillars) — editar textos = tocar esos arrays, no el template.
- Producto: 27" QHD 2560×1440, 280Hz, 0.03ms, WOLED 4ta gen (Primary RGB Tandem OLED).

Ver [[changelog#2026-06-12/13 — Landing del monitor Gigabyte MO27Q28G estética del sitio oficial|changelog 2026-06-12/13]] y [[arquitectura#Propuestas comerciales detrás de token|arquitectura → propuestas]].

## HTML nativo en admin

**NUNCA usar Nuxt UI (`UInput`, `UButton`, `UFormField`) en formularios del admin panel.** El sitio público tiene dark mode global (`@nuxtjs/color-mode`, preference: 'dark') y los componentes heredan esos estilos — inputs sin borde visible, labels invisibles, botones como texto plano. Los `:deep()` con `!important` no son confiables porque Nuxt UI cambia sus clases internas entre versiones.

**Usar:** `<input>`, `<button>`, `<label>`, `<select>` con estilos scoped.
**SÍ funcionan:** `<UIcon>` (iconos), `<UModal>` (wrapper), `<UBadge>` (badges de estado).

## Password en UpdateUserRequest

Si un campo no está en las `rules()` del FormRequest de Laravel, `$request->validated()` lo descarta silenciosamente. Corregido el 2026-04-15 agregando `'password' => 'sometimes|string|min:8'` al `UpdateUserRequest`. El cast `'hashed'` del modelo se encarga del hash automático — no hace falta `Hash::make()` manual.

## Sistema de permisos admin (2026-04-15)

Permisos granulares por sección: columna `permissions` JSON en `users`, getter `hasPermission(section)` en el store, middleware que chequea ruta → sección, sidebar filtrado por permiso, checkboxes en la página de usuarios. Admin role siempre tiene todos (bypass). Códigos: `contactos`, `citas`, `timeslots`, `catalogo`, `reclutamiento`, `usuarios`. Al agregar nueva sección, registrar en 5 lugares (ver [[changelog#2026-04-15 — Sistema de permisos por sección  fixes admin panel|changelog]]).

## Dominio canónico (trampa no-obvia)

**`blustudioinc.com`** — la razón social legal es "BLU STUDIO GROUP LLC" pero el dominio **no es** `blustudiogroup.com`. Todos los handles sociales (`@blustudioinc`) confirman el dominio real. Si aparece `blustudiogroup.com` en el código es un bug — corregido masivamente en el commit `5b87943` del 2026-04-15.

**Dónde vive hardcodeado:** ver [[arquitectura#Lugares donde el dominio vive hardcodeado|arquitectura → dominio]].

## i18n

- Strategy: `prefix_except_default` con `es` como default → `/es` **NO existe** (intencional), el español vive en `/`, solo `/en` tiene prefijo. No es un bug.

## Catálogo de merch (2026-04-13)

- Galería pública + admin + import desde CSV, 451+ productos iniciales
- Imágenes en `storage/app/public/catalog/{sku}/` del backend Laravel
- **Pipeline de normalización GD:** detectar tipo por contenido (clientes suben PNGs con `.jpg`), whiten ≥230 RGB, `imagecropauto` con threshold 0.5, canvas cuadrado con 8% padding. Idempotente via `catalog:normalize-images`. Ver [[arquitectura#Pipeline de normalización de imágenes|arquitectura]] y [[changelog#2026-04-13 — Normalización de imágenes del catálogo|changelog]].

## Patrón de dominio backend Laravel

Convención `app/Src/BackOffice/{Domain}/{Action}/` con Controller + Request + Service + Response. Ver [[arquitectura#Contexto en el monorepo|arquitectura]] para los dominios existentes.

## Assets aboutUs (2026-04-04)

Clientes actuales: **ASUS, Acer, Brother, ADATA, XPG**. Hikvision fue removido previamente (commit `082c81b`). SVGs en `public/img/clients/`.

## Propuestas comerciales (2026-05-06)

Ruta dinámica `/propuestas/[slug]?token=` para servir landings personalizadas a clientes,
detrás de un token, con identidad visual del cliente parametrizable vía `--brand` CSS var.
Excluida de i18n y del sitemap, con `noindex, nofollow`. El catálogo de propuestas y sus
tokens viven hardcoded en `pages/propuestas/[slug].vue` (no DB). Un slug puede delegar el
render a un componente con `kind: '<tipo>'` (ver [[#Landing del monitor Gigabyte estética oficial|landing del monitor]]).

**Patrón importante:** assets del cliente en `public/clients/<slug>/`, fuentes corporativas
opcionales en `public/fonts/<slug>/` registradas en `assets/css/fonts.css`. Brand kits
internos pesados (PDFs/AI/zips) en `assets/html/<cliente>Brand/` **NO se commitean**.

**Confidencialidad:** una propuesta nunca debe mencionar competidores del cliente
(ej: en la propuesta de Gigabyte se quitó el strip con ASUS/Acer/Brother/ADATA/XPG/Hikvision).

Propuestas activas: **Gigabyte** marketing → `/propuestas/gigabyte?token=gbt-mkt-2026` (inline,
acento naranja, Aldrich, sub-marcas AORUS/AERO/AORUS Mark); **Gigabyte monitor** →
`/propuestas/gigabyte-monitor?token=gbt-mo27-2026` (componente, estética azul oficial).
Detalles en [[changelog#2026-05-06 — Propuestas comerciales detrás de token propuestasslug|changelog]] y [[arquitectura#Propuestas comerciales detrás de token|arquitectura]].

## Commits importantes

| Commit | Descripción |
|--------|-------------|
| `b7fdc9d` + `58f87d8` + `1dcd5f8` + `106030c` | Landing monitor MO27Q28G, estética Gigabyte azul + rondas de copy (2026-06-12/13) |
| `fc176ff` | toggle ojo para ocultar/mostrar fee mensual en propuestas |
| `30a41b5` + `37248e5` + `41bd510` | Propuestas comerciales detrás de token, identidad Gigabyte (2026-05-06) |
| `cbe1159` | docs: dominio canónico blustudioinc.com + archivos de descubrimiento SEO (2026-04-15) |
| `5b87943` | fix: corregir dominio a blustudioinc.com en SEO y sitemap (2026-04-15) |
| `2e4a750` | feat: agregar logo BIMI en /bimi/logo.svg (2026-04-15) |
| `7a68533` + `5ca9918` | Catálogo de merch completo (frontend + backend gamma) |
| `4e09142` | Rediseño bento grid servicios |
| `f9c9dfe` | Pills Apple + fondo fijo servicios + Mercury style marketing |
| `e0d4f35` | Fondos animados Unicorn Studio |
