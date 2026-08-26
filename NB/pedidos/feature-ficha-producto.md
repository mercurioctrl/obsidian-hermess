# Feature: Ficha de producto (para vendedores)

Ficha de detalle de producto pensada para que los vendedores la vean **dentro de la app** (modal), en vez de mandarlos al sitio `nb.com.ar`. Hoy el nombre del producto en el detalle de una orden linkea a `https://www.nb.com.ar/fromPedidos_-_{ID_ARTICULO}`; la idea es reemplazar ese link por un modal con la ficha.

Rama backend: `feature/ficha-producto-backend` (desde `Development`). Implementado 2026-08-26. **Frontend pendiente.**

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
| cantidad por caja | `articulo.packagePerUnit` ⚠️ (aparece como fracción, ej `0.1` — semántica a confirmar) |
| stock (total / en camino) | `stocks` (SUM de `nstock` / `nstock_ingresando`) |
| descripción + bajada | `PRODUCTOS.dbo.iaDescriptions` / `subheadline` (`accepted=1`), por `itemId = ID_ARTICULO` |
| galería de fotos | `NB_WEB.dbo.fotos_productos` → `PRODUCTOS.dbo.fotos` (portada primero); URL = `STATIC_URL + checksum` = `https://static.nb.com.ar/img/{checksum}` |
| videos de YouTube | `PRODUCTOS.dbo.videos` por `codigo`; **deduplicados y acotados a 12** (la tabla tiene duplicados masivos: un código llegó a 1263 filas / 402 distintas) |

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
  "stock":    { "total", "incoming" },
  "webUrl":   "https://www.nb.com.ar/fromPedidos_-_{id}"   // fallback al sitio
}
```

Validado end-to-end contra la base con items `118855` (accesorio), `102312` (RTX 2080) y `2936` (fuente SFX).

## Pendientes

- **Frontend:** modal `ProductSheet` (galería + videos + descripción + logística + stock) reemplazando el `<a href="nb.com.ar/fromPedidos_-_${id}">` en `Orders/Detail.vue` (y ~6 lugares más: `Products/Compact.vue`, `Gallery.vue`, `AddTagItem.vue`, `SerialsModal.vue`, `Client/UserItemsModal.vue`). Dejar un botón "Ver en nb.com.ar" como fallback.
- **`packagePerUnit`:** confirmar qué representa (fracción, no u/caja entero) o buscar otra fuente para "cantidad por caja".
- **Atributos estructurados:** no existen como dato (van implícitos en la descripción de IA). Fase 2: parsear/estructurar o pedir el JSON de specs a nb.com.ar.

## Ver también

- [[relacion-tablas-articulo-stocks]] — maestro de productos y stock
- [[changelog]] — entrada 2026-08-26
