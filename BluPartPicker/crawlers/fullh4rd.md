# Scraper — Full H4rd

**URL:** https://fullh4rd.com.ar  
**Tipo:** E-commerce gamer AR (componentes, periféricos, notebooks)  
**Productos obtenidos:** ~1.446 en 76 categorías  
**Script:** `/home/hermess/claude/fullh4rd_scraper.py`  
**Output:** `/home/hermess/claude/fullh4rd_productos.json`

---

## Contexto técnico

El sitio está detrás de **Cloudflare Managed Challenge**, lo que bloquea `curl` directamente. La solución es usar **Playwright con Chromium headless**, que pasa el challenge automáticamente sin necesidad de `cf_clearance`.

### Por qué no funciona curl
- Cloudflare detecta el TLS fingerprint y el User-Agent de curl
- Devuelve `HTTP 403` con `cf-mitigated: challenge`
- No se emite cookie `cf_clearance` en este modo de challenge

---

## Estructura del sitio

### URLs de categorías
```
https://fullh4rd.com.ar/cat/{id}/{slug}/{pagina}
```
Ejemplo: `https://fullh4rd.com.ar/cat/124/nvidia/1`

### Paginación
- 12 ítems por página
- Hay botón "Siguiente" en el DOM cuando existe página siguiente
- Detectar: `Array.from(document.querySelectorAll('a')).some(a => a.innerText.trim() === 'Siguiente')`

### Estructura HTML de cada producto
```html
<div class="item product-list">
  <a href="/prod/{id}/{slug}">
    <div class="image">...</div>
    <div class="info">
      <h3>NOMBRE DEL PRODUCTO</h3>
      <div class="price">$PRECIO <span class="price-promo">$PRECIO_TACHADO</span></div>
      <div class="tags"><span class="tag">Despacho en 24hs</span></div>
      <div class="cta">
        <div onclick="instaBuy({id})">Comprar</div>
      </div>
    </div>
  </a>
</div>
```

### Extractor JS (para usar en `page.evaluate`)
```javascript
() => Array.from(document.querySelectorAll('.item.product-list')).map(el => ({
  id: (el.querySelector('[onclick*="instaBuy"]')?.getAttribute('onclick') || '').match(/\d+/)?.[0],
  name: el.querySelector('h3')?.innerText?.trim(),
  price: el.querySelector('.price')?.childNodes[0]?.textContent?.trim(),
  price_promo: el.querySelector('.price-promo')?.innerText?.trim(),
  link: el.querySelector('a')?.href,
  badge: el.querySelector('.tag')?.innerText?.trim()
}))
```

---

## Cómo replicar el scraping

### Dependencias
```bash
pip install playwright
playwright install chromium
```

### Código base

```python
from playwright.sync_api import sync_playwright
import json, time

EXTRACT_JS = (
    "() => Array.from(document.querySelectorAll('.item.product-list')).map(el => ({"
    "  id: (el.querySelector('[onclick*=\"instaBuy\"]')?.getAttribute('onclick') || '').match(/\\d+/)?.[0],"
    "  name: el.querySelector('h3')?.innerText?.trim(),"
    "  price: el.querySelector('.price')?.childNodes[0]?.textContent?.trim(),"
    "  price_promo: el.querySelector('.price-promo')?.innerText?.trim(),"
    "  link: el.querySelector('a')?.href,"
    "  badge: el.querySelector('.tag')?.innerText?.trim()"
    "}))"
)

def scrape_category(page, base_url):
    productos = []
    for pagina in range(1, 999):
        url = f"{base_url}/{pagina}"
        for intento in range(3):
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=25000)
                page.wait_for_timeout(800)
                break
            except:
                time.sleep(2)
        items = page.evaluate(EXTRACT_JS)
        if not items:
            break
        productos.extend(items)
        has_next = page.evaluate(
            "() => Array.from(document.querySelectorAll('a')).some(a => a.innerText.trim() === 'Siguiente')"
        )
        if not has_next or len(items) < 5:
            break
    return productos

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
    )
    context = browser.new_context(
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
        locale="es-AR",
    )
    page = context.new_page()

    productos = scrape_category(page, "https://fullh4rd.com.ar/cat/124/nvidia")
    print(json.dumps(productos, ensure_ascii=False, indent=2))

    browser.close()
```

---

## Categorías disponibles

| Slug | ID | Descripción |
|------|----|-------------|
| nvidia | 124 | Placas de video Nvidia |
| radeon | 115 | Placas de video AMD |
| amd-am4 | 192 | Microprocesadores AMD AM4 |
| amd-am5 | 390 | Microprocesadores AMD AM5 |
| intel-1700 | 384 | Microprocesadores Intel 1700 |
| intel-1851 | 420 | Microprocesadores Intel 1851 |
| discos-ssd | 185 | SSDs |
| discos-sata | 19 | HDDs SATA |
| memoria-dim-ddr5 | 386 | RAM DDR5 |
| memoria-dim-ddr4-3200-mhz | 272 | RAM DDR4 3200MHz |
| mb-amd-am5 | 389 | Motherboards AM5 |
| mb-intel-1851 | 419 | Motherboards Intel 1851 |
| monitores-gamer | 46 | Monitores gamer |
| monitores-led | 62 | Monitores LED |
| notebooks-gamer | 215 | Notebooks gamer |
| gabinetes-sin-fuente | 65 | Gabinetes sin fuente |
| fuentes-certificadas | 211 | Fuentes certificadas |
| coolers-p-micros | 92 | Coolers para CPU |
| teclados-gamer | 140 | Teclados gamer |
| mouse-gamer | 45 | Mouse gamer |
| sillas-gamer | 230 | Sillas gamer |

Ver lista completa en el script `/home/hermess/claude/fullh4rd_scraper.py`.

---

## Notas

- **Login no requerido** para ver precios y stock público
- El endpoint `/_func/search.php` existe pero es solo para autocompletado del buscador (POST con `search=QUERY`), no sirve para listar catálogo
- Los precios incluyen IVA
- El campo `price_promo` es el precio **tachado** (precio sin descuento); `price` es el precio actual
- El campo `badge` puede ser `"Despacho en 24hs"` o `null`
- La URL del producto sigue el patrón `/prod/{id}/{slug}`
