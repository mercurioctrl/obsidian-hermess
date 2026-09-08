# Feature: Ficha de producto (para vendedores)

Ficha de detalle de producto pensada para que los vendedores la vean **dentro de la app** (modal), en vez de mandarlos al sitio `nb.com.ar`. Hoy el nombre del producto en el detalle de una orden linkea a `https://www.nb.com.ar/fromPedidos_-_{ID_ARTICULO}`; la idea es reemplazar ese link por un modal con la ficha.

Rama backend: `feature/ficha-producto-backend` (desde `Development`). Implementado 2026-08-26; ampliado 2026-08-31 (stock disponible + webUrl por empresa); 2026-09-07 (`unitsPerBox` como cantidad por caja, PR #1636). **Frontend pendiente.**

## Endpoint

`GET /v1/items/{id}/sheet` — read-only, keyed por `ID_ARTICULO` (el mismo `record.id` que usa el link actual). Patrón Controller → Service → Repository:
- `Http/Controllers/Product/ProductSheet.php`
- `Services/ProductSheet/ProductSheetService.php`
- `Repositories/ProductSheet/ProductSheetRepository.php`

## Fuentes de datos — dos capas

El ERP tiene lo logístico/comercial; el **contenido de marketing** vive en la base **`PRODUCTOS`** (la misma de donde ya salían las fotos). Por eso el link histórico iba a nb.com.ar.

| Dato | Fuente |
|---|---|
| sku, código, nombre, garantía, kit, companyCode | `NewBytes_DBF.dbo.articulo` (`ID_PRODUCTO`, `codigo`, `cDetalle`, `cpredef2`) |
| marca (+logo) | `NB_WEB.dbo.marcas` (`referencia`, `imagen` = URL completa) |
| categoría | `familias` — **join por `ID_FAMILIA`** (el join por `ccodfam` falla por padding inconsistente: `'58'` vs `'0023 '`) |
| peso / medidas | `articulo.weightAverage` (g), `high/width/lengthAverage` (mm) |
| cantidad por caja | `articulo.packagePerUnit` — viene como **fracción de caja que ocupa 1 unidad** (ej `0.0083`); `unitsPerBox` devuelve su **inverso** `round(1/x)` = u/caja (ej. 120). Ver [[#unitsPerBox como cantidad por caja (2026-09-07)]] |
| stock (disponible / total / en camino) | `stocks`: `available` = SUM(`nstock`) − SUM(`nstock_reserva_pedidos`) con piso en 0; `total` = SUM(`nstock`); `incoming` = SUM(`nstock_ingresando`) |
| descripción + bajada | `PRODUCTOS.dbo.iaDescriptions` / `subheadline` (`accepted=1`), por `itemId = ID_ARTICULO` |
| galería de fotos | `NB_WEB.dbo.fotos_productos` → `PRODUCTOS.dbo.fotos` (portada primero); URL = `STATIC_URL + checksum` = `https://static.nb.com.ar/img/{checksum}` |
| videos de YouTube | `PRODUCTOS.dbo.videos` por `codigo`; **deduplicados y acotados a 12** (la tabla tiene duplicados masivos: un código llegó a 1263 filas / 402 distintas) |

## Stock disponible (2026-08-31)

El bloque `stock` expone tres números, con el mismo criterio de reserva que usa `OrderRepository`:
- **`available`** = `SUM(nstock) − SUM(nstock_reserva_pedidos)`, con piso en 0 (lo realmente vendible).
- **`total`** = físico total (`SUM(nstock)`).
- **`incoming`** = ingresando (`SUM(nstock_ingresando)`).

## unitsPerBox como cantidad por caja (2026-09-07)

`articulo.packagePerUnit` **no** es "unidades por caja": es la **fracción de caja que ocupa una unidad** (ej. `0.0083`). La cantidad por caja es su inverso, así que `logistics.unitsPerBox` ahora devuelve `round(1 / packagePerUnit)` → `1 / 0.0083 = 120`. Si el valor crudo es `0`/`null` (sin dato de bulto), devuelve `null` en vez de dividir por cero. Cambio en `ProductSheetService.php` (commit `71fdb788`, PR #1636).

## webUrl por empresa (2026-08-31)

El link al producto ya no está hardcodeado a nb.com.ar: sale según `companyCode` desde **`config/companySites.php`** (`companyCode` = `FP_Empresas.CODEMP`).

| companyCode | Empresa | Dominio |
|---|---|---|
| 4 | NB Distribuidora | `https://www.nb.com.ar` |
| 9 | NBElectric | `https://nbe.com.ar` |
| 11 | Laset | `https://laset.com.ar` |
| *otro* | — | **default `nb.com.ar`** |

Los dominios son overrideables por env (`SITE_URL_NB`, `SITE_URL_NBE`, `SITE_URL_LASET`). El path `/fromPedidos_-_{id}` es igual para las tres (a confirmar si NBE/Laset usan otro).

## Objeto devuelto (`ProductSheet`)

```jsonc
{
  "id", "sku", "code", "name", "warranty",
  "subheadline", "description",
  "isKit", "companyCode",
  "brand":    { "id", "name", "logo" },
  "category": { "id", "name" },
  "images":   [ { "url", "isCover" } ],
  "videos":   [ { "videoId", "url" } ],           // url = youtube.com/watch?v=
  "logistics":{ "weightGr", "dimensionsMm": { "height","width","length" }, "unitsPerBox" },
  "stock":    { "available", "total", "incoming" },
  "webUrl":   "https://{dominio-empresa}/fromPedidos_-_{id}"
}
```

Validado end-to-end contra la base: items por empresa (NB=4, NBE=9, Laset=11) devuelven el dominio correcto; `available` verificado (ej. item 22: total 550, reservado 13 → available 537).

## Pendientes

- **Frontend:** modal `ProductSheet` (galería + videos + descripción + logística + stock) reemplazando el `<a href="{webUrl}">` en `Orders/Detail.vue` (y ~6 lugares más: `Products/Compact.vue`, `Gallery.vue`, `AddTagItem.vue`, `SerialsModal.vue`, `Client/UserItemsModal.vue`). Dejar un botón "Ver en el sitio" usando `webUrl` como fallback.
- **`packagePerUnit`:** confirmar qué representa (fracción, no u/caja entero) o buscar otra fuente para "cantidad por caja".
- **Path del webUrl:** confirmar si NBE/Laset usan el mismo `/fromPedidos_-_{id}` o uno distinto (hoy es común a las tres).
- **Atributos estructurados:** no existen como dato (van implícitos en la descripción de IA). Fase 2: parsear/estructurar o pedir el JSON de specs a nb.com.ar.

## Ver también

- [[relacion-tablas-articulo-stocks]] — maestro de productos y stock
- [[changelog]] — entradas 2026-08-26 y 2026-08-31
