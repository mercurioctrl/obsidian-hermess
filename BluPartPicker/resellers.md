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

### Stock
- No hay numérico. `observaciones` textual → `isinstock=1` si vacío o `"Stock Bajo"`, sino `0`

### ⚠ GOTCHA — Moneda
El Excel devuelve `moneda = "US$"`, no `"USD"`. **Normalizar siempre** en `parse_excel()`:
```python
if raw_moneda in ("US$", "U$S", "USD", ...):
    p["moneda"] = "USD"
```
La expresión SQL de la API usa `moneda = 'USD'` exacto. Si llega `"US$"`, la conversión falla silenciosamente.

---

## Ceven · `source=ceven`

**URL:** https://www.ceven.com · **Script:** `sync_ceven.py` · **Cron:** `0 1,5,9,13,17,21 * * *`

### Login — Akamai bot protection
- Akamai bloquea `requests` y `curl` por TLS fingerprint. **Única solución: Playwright headless**
- No es posible reusar cookies fuera del browser context
```
URL: checkout.ssp?is=login&login=T&cur=USD&origin=customercenter&lang=es_AR
Email: mrebreg@nb.com.ar | Password: Nb20262026
Esperar redirect a: **/my_account.ssp**
```

### API de productos (NetSuite SCA)
- Llamado via `page.evaluate(fetch(...))` dentro del contexto del browser
- Paginar de 100 en 100 · ~466 productos totales
- ~108 de 464 productos sin categoría (no aparecen en ninguna categoría del catálogo) — normal

### ⚠ GOTCHA — Timeouts transitorios
- El cron puede fallar con `Locator.fill: Timeout 30000ms exceeded` si el sitio de Ceven está lento
- No es un bug del script — correr manual para confirmar que el sitio esté operativo

---

## Stylus · `source=stylus`

**URL:** https://www.stylus.com.ar · **Script:** `sync_stylus.py` · **Cron:** `0 2,6,10,14,18,22 * * *`

### Login
```
POST /login.php
Body: action=send | url=home.php | Email=stylus@stylus.com.ar | Password=Arbol78
Validación: URL final debe ser home.php
```

### Precios — TSV por marca
- `lista_precios_xls.php?Id_Marca=N` → **TSV con extensión .xls** (no es Excel real)
- **Encoding: latin-1** (no UTF-8)
- Formato precio: `"U$S 1.282,87"` → `parse_usd()`
- `GOTCHA:` el filtro `?Codigo=XXX` en URL **no funciona** — devuelve catálogo completo

---

## PreciosGamer · `source=preciosgamer_{slug}`

**URL API:** `https://api.preciosgamer.com/v1/sync/items-export/123`
**Script:** `sync_preciosgamer.py` · **Cron:** `0 3,7,11,15,19,23 * * *` · **Auth:** ninguna

### Source format
El source es el **slug del nombre del reseller**, no el ID numérico:
- `preciosgamer_venex` (NO `preciosgamer_1061`)
- `preciosgamer_libre-opcion` (NO `preciosgamer_1091`)
- `preciosgamer_full-h4rd`, `preciosgamer_gaming-city`, etc.

### Modelo de sync — DELETE + INSERT
- En cada sync se hace `DELETE FROM itemsRepository WHERE source LIKE 'preciosgamer_%'`
- Luego INSERT de todo lo traído (últimas 48h)
- **No hay UPDATE** — siempre 0 actualizados, todo son nuevos
- `price_stock_history` **no se borra** — mantiene historial completo

### Parámetro `since`
```
since = ahora - 48h   (fijo, no depende del sync_log)
```

### Campos de la API → schema DB

| Campo API | Campo DB | Notas |
|-----------|----------|-------|
| `id` | `codigo` | ID interno de PreciosGamer |
| `sku` | `nro_parte` | Puede ser NULL |
| `description` | `producto` | |
| `brandDescription` | `fabricante` | NULL en ~31% → oráculo |
| `currentPrice` | `precio_final` | ARS |
| `defaultImgUrl` | `imagen_url` | |
| `destinyUrl` | `url_ficha` | |
| `hide` | `isinstock` | `false`→1, `true`→0 |

### Inferencia de categoría y marca
- **Categoría:** primera palabra de `description`, con skip de marcas y abreviaciones. 92.8% cobertura.
- **Marca:** oráculo del repositorio (711 marcas qty≥2), escaneo desde palabra 2. 87.9% cobertura total.

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — schema DB, endpoints, índices
- [[memoria]] — gotchas activos y próximos pasos
