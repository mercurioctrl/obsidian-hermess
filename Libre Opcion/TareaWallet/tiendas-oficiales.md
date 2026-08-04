# Tiendas Oficiales — Libre Opción

Feature de **tiendas oficiales** en la API v4 (LIO-720, LIO-769, LIO-771, LIO-772, LIO-776).
Una tienda oficial vincula un vendedor (`seller_id`) con una **marca** (`brand_id`) y le da
identidad propia (branding cargado desde un CMS): colores, fuentes, logo, banners, secciones
(hero, video) y menús. En el catálogo se prioriza a las tiendas oficiales y se las excluye del
listado común de vendedores.

## Módulo `OfficialStore`

| Capa | Archivo | Rol |
|------|---------|-----|
| Controller | `Http/Controllers/OfficialStore/OfficialStoreController.php` | `GET /v4/tienda-oficial/{slug}` (público, `routes/api.php:187`) |
| Service | `Service/OfficialStore/OfficialStoreService.php` | `getBySlug()` — arma el objeto de branding |
| Service | `Service/OfficialStore/OfficialStoreInventoryScopeService.php` | Resuelve `brand_id` para scopear el inventario del seller |
| Repository | `Repository/OfficialStore/OfficialStoreRepository.php` | Queries a las tablas de branding |

## Tablas nuevas (SQL Server, `[LO].[dbo]`)

- **`official_store_branding`** — fila por tienda: `id`, `slug`, `seller_id`, `brand_id`,
  `is_active`, `shape`, `font_family`, `title_font_family`, `title_font_weight`,
  colores (`brand_primary_color`, `brand_secondary_color`, `brand_gradient`,
  `interactive_color`, `surface_color`, `text_on_surface`), `logo_checksum`,
  `created_at`, `updated_at`.
- **`official_store_branding_banners`** — banners asociados a la tienda.

El repo hidrata además `media`, `menu` y `sections` (hero, video) traídos del **CMS** (LIO-720/769).

## Reglas de negocio clave

### 1. Reemplazo de identidad en la ficha de producto (`FichaProductoDto`)
Si el item pertenece a una tienda oficial (llega `officialStoreSlug` + `officialStoreName`):
- `seller.nombre` → `"Tienda oficial {name}"` (`FichaProductoDto.php:214`)
- `seller.isOfficialStore = true`
- `seller.uri` → `"/tienda-oficial/{slug}"`
- Se **bloquea/neutraliza la reputación** del seller asociado (no se muestra la del vendedor real).

### 2. Scoping de inventario por marca (`OfficialStoreInventoryScopeService`)
- `resolveBrandIdForSeller($sellerId, $officialStoreId)`:
  - `404` si la tienda no existe
  - `403` si la tienda no pertenece al vendedor autenticado
  - devuelve el `brand_id` → el inventario del seller se filtra **solo a esa marca**
- `resolveBrandIdForAuthenticatedSeller($sellerId)` — resuelve la tienda del seller logueado.

### 3. Priorización / exclusión en catálogo y búsqueda
La feature tocó de forma transversal casi todos los listados públicos para **priorizar tiendas
oficiales** y **excluir a los sellers oficiales del listado común de vendedores**:
`CatalogueRepository`, `SuggestionRepository`, `BrandRepository`, `CategoryRepository`,
`AttributesListRepository`, `IntervalPricesRepository`, `OnlyResellerRepository`,
`ResellersByItemIdRepository`, `ItemRepository` y `Support/MainQuery.php`.

También se agregó soporte en **auth/user** (`AuthRepository`, `UserDto`) e **inventario del
vendedor** (`InventoryProductsService`) para filtrar por la marca de su tienda oficial.

## Endpoint público

```
GET /v4/tienda-oficial/{slug}
→ { id, slug, brand:{id,name}, sellerId, alias, isActive, shape,
    fontFamily, colors:{...}, logoChecksum, banners:[...],
    media, menu, sections:[hero, video, ...] }
```

## Ver también

- [[TareaWallet]]
- [[changelog]]
- [[contexto]]
