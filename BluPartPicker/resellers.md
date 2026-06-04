# Resellers — Casos puntuales por distribuidor

## Invid Computers · `source=invid`

**URL:** https://www.invidcomputers.com · **Script:** `sync_invid.py` · **Cron:** `0 */4 * * *`

### Login
```
POST /login.php
Body: usuari=30709246638 | passwd=kilo3458 | login=s | volver=
Validación: cookie `whoami` debe existir post-login
```

### Precios — Excel
- Descargado desde `genera_excel.php` (formato `.xlsx` real, openpyxl)
- Empieza en **fila 10** (las primeras 9 son headers/metadata)
- Filas donde `codigo.lower() == "codigo"` → headers repetidos → **skipear**
- Hay códigos duplicados → usar **dict** (última ocurrencia gana)
- Columnas: `codigo, producto, fabricante, nro_parte, moneda, precio_sin_iva, pct_iva, imp_interno, precio_final, precio_ars, observaciones`

### Stock
- No hay numérico. `observaciones` textual → `isinstock=1` si vacío o `"Stock Bajo"`, sino `0`
- `stock` siempre NULL

### Imágenes/URLs — scraping
- No vienen en el Excel. Scraping de 22 categorías: `/{cat}--view--grilla-{offset}` (step 20)
- Patrón URL ficha: `([\w\-]+---det--\d{7})`
- Patrón imagen: `thumb/([\w\d\-\.]+_400x400\.\w+)`
- ~3% de productos tienen imagen (el catálogo web no las tiene para todos)

### ⚠ GOTCHA CRÍTICO — Moneda
El Excel devuelve `moneda = "US$"`, no `"USD"`. **Normalizar siempre** en `parse_excel()`:
```python
if raw_moneda in ("US$", "U$S", "USD", "DOLAR", "DÓLARES", "DOLARES"):
    p["moneda"] = "USD"
```
La expresión SQL de la API usa `moneda = 'USD'` exacto. Si llega `"US$"`, la conversión de precios falla silenciosamente para los ~1.195 items de Invid.

---

## Ceven · `source=ceven`

**URL:** https://www.ceven.com · **Script:** `sync_ceven.py` · **Cron:** `0 1,5,9,13,17,21 * * *`

### Login — Akamai bot protection
- Akamai bloquea `requests` y `curl` por TLS fingerprint. **Única solución: Playwright headless**
- No es posible reusar cookies fuera del browser context
```
URL: https://www.ceven.com/sca-src-2025-1-0/checkout.ssp?is=login&login=T&cur=USD&origin=customercenter&lang=es_AR
Email: mrebreg@nb.com.ar | Password: Nb20262026
Esperar redirect a: **/my_account.ssp**
```

### API de productos (NetSuite SCA)
```
GET /api/personalized/items?language=es&currency=USD&c=5032996&country=AR&use_pcv=T&fieldset=details&pricelevel=1&n=2&offset=0&limit=100
```
- Llamado via `page.evaluate(fetch(...))` dentro del contexto del browser
- Paginar de 100 en 100 · ~464 productos totales
- `itemid` duplicados históricos: `HEL55`, `D1328DDF00W101` → dict dedup

### Categorías
- **No vienen en el item.** Llamadas separadas por `&commercecategoryurl=/catalogo/CATEGORIA/...`
- 26 categorías definidas en `CEVEN_CATEGORIES` como tuplas `(url_path, nombre_legible)`
- ~108 de 464 productos no aparecen en ninguna categoría → `categoria = NULL` (es normal)

### Campos clave del item
| Campo API | Campo DB |
|-----------|----------|
| `itemid` / `internalid` | `codigo` |
| `storedisplayname2` / `displayname` | `producto` |
| `custitem_marca` | `fabricante` |
| `onlinecustomerprice_detail.onlinecustomerprice` | `precio_final` (con IVA, pricelevel=1) |
| `itemimages_detail.urls[0].url` | `imagen_url` (espacios → `%20`) |
| `urlcomponent` | `url_ficha` (prefijo `https://www.ceven.com/`) |
| `isinstock` | `isinstock` (bool → 1/0) |
| `quantityavailable` | `stock` |

---

## Stylus · `source=stylus`

**URL:** https://www.stylus.com.ar · **Script:** `sync_stylus.py` · **Cron:** `0 2,6,10,14,18,22 * * *`

### Login
```
POST /login.php
Body: action=send | url=home.php | Email=stylus@stylus.com.ar | Password=Arbol78 | Submit=Iniciar Sesión
Validación: URL final debe ser home.php
```

### Precios — TSV por marca
- `lista_precios_xls.php?Id_Marca=N` → **TSV con extensión .xls** (no es Excel real)
- **Encoding: latin-1** (no UTF-8)
- 42 marcas scrapeadas desde `lista_precios.php`
- Columnas TSV: `RUBRO, SUBRUBRO, MARCA, CODIGO, PRODUCTO, PRECIO, IMP. INT., IVA, STOCK`
- `PRECIO`: formato `"U$S 1.282,87"` (punto=miles, coma=decimal) → `parse_usd()`
- `IVA`: `"10.5 %"` → `parse_pct()` → `pct_iva`
- `precio_final = precio_sin_iva * (1 + pct_iva/100) * (1 + imp_interno/100)`
- `STOCK`: `"Si"` → `isinstock=1`, `"No"` / `"Call"` → `isinstock=0`
- `RUBRO` → `categoria`

### Imágenes, URLs y stock numérico — scraping catálogo
- Catálogo: `https://www.stylus.com.ar/productos?TipoListado=Imagen&SortBy=4&pag=N`
- Paginación: N=1 a ~102, 9 productos por página
- Tarjeta `.product-info-wrapper` → código `.producto-codigo`, link, imagen, stock numérico
- **GOTCHA:** El filtro `?Codigo=XXX` **no funciona** — devuelve el catálogo completo
- ~253 productos del TSV no aparecen en el catálogo → `imagen_url` y `url_ficha` quedan NULL

---

## PreciosGamer · `source=preciosgamer_{resellerId}`

**URL API:** `https://api.preciosgamer.com/v1/sync/items-export/{resellerId}`  
**Script:** `sync_preciosgamer.py` · **Cron:** `0 3,7,11,15,19,23 * * *` · **Auth:** ninguna (API pública)

### 37 resellers activos
Cada reseller es un `source` independiente: `preciosgamer_{resellerId}`.

Incluye: Libre Opcion (1058), Full h4rd (1059), Armytech (1060), Venex (1061), Ignatech (1078), Katech (1079), Shopgamer (1077), Mexx Gaming (1080), y otros hasta el ID 1094.

### Paginación
```
GET /v1/sync/items-export/{resellerId}?offset=0&limit=5000&since=2000-01-01+00:00:00
```
- `since`: `finished_at` del último sync exitoso de cualquier `preciosgamer_*` (de `sync_log`)
- Paginar hasta recibir menos de 5000 items en la página
- Primer sync: `since=2000-01-01 00:00:00` para traer todo el catálogo

### Campos de la API → schema DB

| Campo API | Campo DB | Notas |
|-----------|----------|-------|
| `id` | `codigo` | ID numérico |
| `description` | `producto` | Nombre del producto |
| `brandDescription` | `fabricante` | NULL en ~31% de items → oráculo |
| `currentPrice` | `precio_final` | ARS, precio de venta al público |
| `defaultImgUrl` | `imagen_url` | |
| `destinyUrl` | `url_ficha` | Link a la tienda |
| `hide` | `isinstock` | `false`→1, `true`→0 |

- `moneda = "ARS"` · `distribuidor = 0` · `stock = NULL` (la API no lo expone)

### Inferencia de categoría (`extract_categoria()`)

La API no expone categoría. Se infiere de la primera palabra de `description`:

1. Primera palabra → categoría (`MOUSE`, `MEMORIA`, `NOTEBOOK`, etc.)
2. Primera palabra es marca conocida → usar la **segunda**
3. Primera palabra es `ACCESORIOS` / `ACCESORIO` → usar la **tercera**
4. Normalización: `AURICULARES→AURICULAR`, `MOTHERBOARD→MOTHER`, `NB→NOTEBOOK`, `SSD→DISCO`
5. Palabras de ruido filtradas: `GAMING`, `HOT`, `MINI`, `SMART`, `MICRO`, etc.

**Cobertura: 92.8%** de los 145k items.

### Oráculo de marcas (`build_brand_oracle()` + `find_brand_in_text()`)

Para items sin `brandDescription` en la API:

1. `build_brand_oracle(conn)`: indexa marcas del repositorio con `qty ≥ 2` → dict + índice por primera palabra
2. `find_brand_in_text(producto)`: escanea palabras desde pos 1, saltea `BRAND_SKIP` (`GAMER`, `WIRELESS`, `RGB`, `USB`, ...)
3. Soporta marcas multipalabra (`Trust gaming`, `TP-Link`, `Cooler master`, `Western Digital`)
4. Se reconstruye en cada sync — mejora automáticamente cuando entran nuevas marcas de distribuidores

**Cobertura: 87.9%** — 69% directa de la API + 19% inferida por el oráculo.

### Particularidades

- `BRAND_BLACKLIST`: excluye marcas basura del oráculo (`'cpu'`, `'sin definir'`, `'generico'`, `'oem'`, ...)
- El dict `RESELLERS` en el script mapea IDs → nombres legibles (solo para logging)
- Agregar un nuevo reseller: solo cambiar/agregar el ID en `RESELLERS`

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — schema DB, endpoints, índices, conversión de precios
- [[memoria]] — credenciales, gotchas críticos y próximos pasos
