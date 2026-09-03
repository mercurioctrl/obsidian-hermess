
# partPicker

Scraper de PCPartPicker que extrae **specs de compatibilidad** de componentes de PC para validar armados. Matchea los SKUs del inventario de New Bytes contra fichas de PCPartPicker (+ BuildCores y dataset local), extrae specs a SQLite y sincroniza un subconjunto a SQL Server.

**Última sync:** 2026-09-02 · **Repo:** `/var/www/partPicker` · **Destino:** `db-nb-massql-dev.blu.net.ar:4444` → DB `PRODUCTOS`

> No confundir con [[BluPartPicker]], que es otro proyecto: el agregador de mayoristas y resellers con `oracular_sku`. Éste extrae specs para compatibilidad.

## Stack

- Python 3.12 · SQLite (`scraper.db`, WAL) · Flask (monitor :5050)
- Selenium + `undetected-chromedriver` (bypass Cloudflare, Chrome headful en `DISPLAY=:1`)
- `pymssql` para el sync a SQL Server
- Fuentes de specs: PCPartPicker (scrape), dataset local (`dataset/`), BuildCores Open DB (opcional)

## Pipeline (scraper.py, resumable)

| Fase         | Qué hace                                                      | Chrome |
| ------------ | ------------------------------------------------------------- | ------ |
| 0 buildcores | specs por `part_numbers` (si está `buildcores-db/`)           | no     |
| 0.5 manual   | specs manuales (Thermaltake, Cooler Master, Netac)            | no     |
| 1 index      | recorre listados de 8 categorías → `products`                 | sí     |
| 2 match      | cruza SKUs vs productos (exact_name / slug_suffix / amd_core) | no     |
| 2.5 dataset  | specs del dataset local                                       | no     |
| 3 scrape     | extrae specs de matches sin specs                             | sí     |
| 4 search     | busca SKUs sin match (Part# exacto o SKU en slug)             | sí     |

## Notas

- [[specs-y-armador]] — tablas SQLite↔SQL Server, cadena de joins, `is_compat`, las 9 reglas del armador
- [[operacion]] — cómo correr acá, origen de stock, reconstruir `scraper.db` desde SQL Server, cobertura actual
- [[changelog]] — historial de sesiones
