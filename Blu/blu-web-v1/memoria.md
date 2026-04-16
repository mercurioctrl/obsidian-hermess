# Memoria — blu-web-v1

Consolidación de [[base-de-conocimiento|Claude memory]] del proyecto para consulta rápida en Obsidian. Fuente autoritativa: `~/.claude/projects/-Users-hermess-www-blu-blu-web-v1/memory/`.

> Ver también: [[blu-web-v1]] · [[arquitectura]] · [[changelog]]

## Preferencias del usuario

- **Sin co-autor en commits** — NUNCA agregar `Co-Authored-By` ni modificar autorías de git
- **Simplicidad** — iterar rápido cuando algo no gusta, preferir simple sobre complejo
- **Estilo visual:** pills estilo Apple, tipografía estilo Mercury Bank (letter-spacing negativo, grids ultra sutiles), minimalismo
- **Sin colores extra en estados activos** — efectos limpios (rotación, escala) sin gradientes coloridos
- **Efecto glitch solo en hover**, no en estados permanentes
- **Tildes en español argentino** — siempre correctas en todo texto en español

## Feedback de workflow

- **Features full-stack:** proponer bullets → ejecutar todo → dejar corriendo → push en repos separados
- **Commits:** mensajes en español, concisos, sin co-autor, uno por concepto claro
- **Descarga archivos protegidos:** fetch+blob+objectURL con Bearer token, NO `<a href>` (el token no viaja en links)

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

## Commits importantes

| Commit | Descripción |
|--------|-------------|
| `cbe1159` | docs: dominio canónico blustudioinc.com + archivos de descubrimiento SEO (2026-04-15) |
| `5b87943` | fix: corregir dominio a blustudioinc.com en SEO y sitemap (2026-04-15) |
| `2e4a750` | feat: agregar logo BIMI en /bimi/logo.svg (2026-04-15) |
| `7a68533` + `5ca9918` | Catálogo de merch completo (frontend + backend gamma) |
| `4e09142` | Rediseño bento grid servicios |
| `f9c9dfe` | Pills Apple + fondo fijo servicios + Mercury style marketing |
| `e0d4f35` | Fondos animados Unicorn Studio |
