# Changelog blu-web-v1

> Registro de cambios relevantes fuera del código (assets, decisiones, etc.)
> Ver también: [[base-de-conocimiento]] · [[arquitectura]] · [[stack]]

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
- **Admin:** `pages/cmsadmin/catalogo.vue` — CRUD productos + upload múltiple de
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

Manual (pocos): admin `/cmsadmin/catalogo` → botón "Nuevo producto" → luego "Subir"
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
