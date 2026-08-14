# Tienda Oficial AMD

Creación de la tienda oficial de **AMD** (marca `id_marca=3169`) como **vendedor dedicado**, en **dev** (2026-08-11) y **producción** (2026-08-12). Es una instancia concreta del módulo OfficialStore — ver [[TareaWallet/tiendas-oficiales|Tiendas Oficiales]] para el módulo (branding CMS, scoping por marca, reemplazo de identidad en ficha).

## Qué es una "tienda oficial" (mecanismo, no obvio)

1. **Resolución del vendedor**: `official_store_branding.seller_id` es el vendedor que "es" la tienda. En login (`AuthRepository`) el `vendedorID` efectivo sale de `CASE WHEN u.vendedorTienda IS NULL THEN v.id ELSE u.vendedorTienda`, y se hace LEFT JOIN a `official_store_branding` por `seller_id` para setear `officialStoreId`.
2. **Productos**: las publicaciones viven en **`CS.dbo.productos`** (NO `LO.dbo.productos`, que no existe). `id` es identity; `precioDolar` y `precioFInal` son **columnas computadas** (excluir de INSERT).
3. **Catálogo del storefront** NO lee de `CS.dbo.productos`: lee del índice **`SEARCH_ENGINE_LO.dbo.itemsSellers`** (join a `SEARCH_ENGINE_LO.dbo.items` por `internal_id` **AND `items.id_brand = OSB.brand_id`**). Por eso solo aparecen los productos cuyo `items.id_brand` coincide con la marca (23 de 150 en prod).
4. **Reindexar** tras tocar `CS.dbo.productos`: `SyncUpRepository::syncUpResellers()` — MERGE idempotente sobre `itemsSellers` por (`sellerId`,`internalId`); requiere `id_interno>0`, `activo=1`, `ocultar=0`, vendedor `activo=1`.

## Técnica "vendedor dedicado" (replicar catálogo de otro vendedor)

Para que un vendedor nuevo "tenga" el catálogo AMD de otro (Exxit, vendedor 45), **NO alcanza con copiar `CS.dbo.productos`**. Hay que replicar además:

- **`CS.dbo.productosFotos`** (asociaciones producto→foto; las fotos viven en `PRODUCTOS.dbo.fotos`, compartidas por `id_foto`). Mapear `id_producto` viejo→nuevo por `id_interno`. Sin esto, `getFotos` viene vacío.
- **`LO.dbo.vendedoresReputacion`** (1 fila por vendedor). Sin fila, `ItemRepository::getSellerData` devuelve `null` → "idVendedor on null". Ojo: `puntajeGlobal < 4` (shadow_ban_value) shadow-banea al vendedor en el catálogo.

## Bug latente arreglado

`FichaProductoDto.php:75` hacía `$fotos[0]->checksum` sin guardia → productos **sin foto** daban **500 "Undefined array key 0"** en toda la plataforma (también los de Exxit). Fix: `$fotos[0]->checksum ?? null`. Recordar recargar php-fpm tras editar (OPcache `validate_timestamps=Off`). Ver [[memoria#Backend API v4 — Gotchas|Memoria § Backend gotchas]].

## Instancias creadas

### Dev (2026-08-11) — `db-nb-massql-dev.blu.net.ar`
- Usuario `amd@libreopcion.com` (id **326171**), vendedor dedicado **275523**, `official_store_branding` id=1.
- 156 productos AMD replicados de Exxit (vendedor 45) + fotos + reputación + reindex.

### Producción (2026-08-12) — `190.210.23.97` (`@@SERVERNAME=SAFDB2`)
- La tienda AMD **no existía** en prod → hubo que **crear también el branding + banners**.
- Usuario `amd@libreopcion.com` (id **332126**), vendedor dedicado **279547**, `official_store_branding` **id=4**. (Contraseña definida por el usuario, guardada en el gestor de credenciales — no se documenta acá.)
- 150 productos AMD de Exxit replicados como propios + 363 fotos + reputación + 2 banners + reindex. Catálogo storefront: **23**.
- Script self-contained (PDO a prod, credenciales por ENV nunca en archivo, transacción dry-run→commit). Ids resueltos EN prod (marca por `nombre='AMD' AND id_nb=43`, Exxit por `uri='exxit-computacion'`), **nada arrastrado de dev**.

## Gotcha crítico: topología dev/prod (.env)

El `.env` del contenedor `sitio-api-rest-4.1-laravel` fue **repunteado a prod** (`190.210.23.97` / user `web`); normalmente apunta a dev (`db-nb-massql-dev`). Con `.env`=prod, **la API y el frontend `:3003` hablan con PRODUCCIÓN**. Verificar SIEMPRE a qué DB se apunta antes de escribir: `config('database.connections.sqlsrv.host')` + `SELECT @@SERVERNAME` (prod=`SAFDB2`). Dev y prod comparten muchos ids (dev es clon de prod) → un id "existe" en ambos pero puede ser gente distinta. **NO hay sync automático prod→dev.**

## Pendientes

- **Deployar** el fix `FichaProductoDto:75` a prod por pipeline (sin él, productos AMD sin foto dan 500).
- **Revertir** el `.env` del contenedor a dev (ahora apunta a prod).
- **Subir assets** del microsite (logo/videos/imágenes) al CDN de prod si se cargan `sections`/`menu` (quedaron NULL).
- **Revocar** las credenciales temporales de prod (`web`).

## Ver también

- [[TareaWallet/tiendas-oficiales|Tiendas Oficiales (módulo OfficialStore)]]
- [[changelog#2026-08-12|Changelog 2026-08-12]]
- [[memoria|Memoria]]
- [[Libre Opcion|Índice del proyecto]]
