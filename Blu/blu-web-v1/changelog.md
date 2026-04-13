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
