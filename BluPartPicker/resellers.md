# Resellers — Casos puntuales

## Invid Computers · `source=invid`

- **Auth:** `POST /login.php` · campos `usuari, passwd, login=s` · validar cookie `whoami`
- **Precios:** Excel (`genera_excel.php`, openpyxl) · fila 10 en adelante · skipear filas donde `codigo == "codigo"` (headers repetidos) · deduplicar con dict
- **Stock:** No hay numérico. `observaciones` textual → `isinstock=1` si vacío o "Stock Bajo"
- **Imágenes/URLs:** Scraping de 22 categorías `/{cat}--view--grilla-{offset}` (step 20). Patrón URL: `[\w\-]+---det--\d{7}`. Patrón img: `thumb/[\w\d\-\.]+_400x400\.\w+`
- **Gotcha:** ~3% de productos tienen imagen en el catálogo web

## Ceven · `source=ceven`

- **Auth:** Playwright obligatorio — Akamai bloquea requests/curl por TLS fingerprint. No hay forma de reusar cookies fuera del browser
- **Login:** `checkout.ssp?is=login...` · email `mrebreg@nb.com.ar` · esperar redirect a `**/my_account.ssp**`
- **API:** NetSuite SCA `/api/personalized/items` · llamado via `page.evaluate(fetch(...))` · paginar de 100 en 100
- **Categorías:** NO vienen en el item. Hacer calls separados por `commercecategoryurl` con 26 categorías definidas. ~108/464 productos sin categoría (no aparecen en ninguna categoría del catálogo)
- **Gotcha:** 2 itemids duplicados históricos (HEL55, D1328DDF00W101) → dict dedup. Imágenes: reemplazar espacios con `%20`

## Stylus · `source=stylus`

- **Auth:** `POST /login.php` · campos `action=send, url=home.php, Email, Password` · validar redirect a `home.php`
- **Precios:** `lista_precios_xls.php?Id_Marca=N` → **TSV con extensión .xls**, NO Excel real · encoding latin-1 · 42 marcas desde `lista_precios.php`
- **Formato precio:** `"U$S 1.282,87"` (punto=miles, coma=decimal) → `parse_usd()`
- **Stock:** `"Si"→1`, `"No"/"Call"→0` desde TSV. Stock numérico del catálogo (scraping web)
- **Imágenes/URLs:** Scraping catálogo paginado `?TipoListado=Imagen&SortBy=4&pag=N` · ~103 páginas · tarjeta `.product-info-wrapper` · código en `.producto-codigo` como `#XXXX`
- **Gotcha:** El filtro `?Codigo=XXX` en la URL NO funciona (devuelve catálogo completo). ~253 productos del TSV no aparecen en el catálogo → imagen/url quedan NULL
