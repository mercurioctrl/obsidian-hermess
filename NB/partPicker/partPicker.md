# partPicker

Scraper de PCPartPicker que extrae **specs de compatibilidad** de componentes de PC para validar armados. Matchea los SKUs del inventario de New Bytes contra fichas de PCPartPicker (+ BuildCores y dataset local), extrae specs a SQLite y sincroniza un subconjunto a SQL Server.

**Última sync:** 2026-09-05 · **Repo:** `mercurioctrl/partPicker` (privado) · **Destino:** `db-nb-massql-dev.blu.net.ar:4444` → DB `PRODUCTOS`

> No confundir con [[BluPartPicker]], que es otro proyecto: el agregador de mayoristas y resellers con `oracular_sku`. Éste extrae specs para compatibilidad.

## Dónde vive

| Máquina | Path | Notas |
|---|---|---|
| Mac | `~/www/partPicker` | Python 3.14, Chrome del sistema |
| Servidor | `/var/www/partPicker` | Python 3.12, Chrome 152 en `DISPLAY=:1` — ver [[operacion]] |

Último commit: `f598b2b` (2026-09-02). Sin trackear en el repo: `rebuild_db.py`, `prep_instock_items.py`, `scrape_one.py`.

## Stack

- Python · SQLite (`scraper.db`, WAL) · Flask (monitor :5050)
- Selenium + `undetected-chromedriver` (bypass Cloudflare, Chrome headful)
- `pymssql` con `tds_version='7.0'` para el sync a SQL Server
- Fuentes de specs: PCPartPicker (scrape), dataset local (`dataset/`), BuildCores Open DB (opcional)

## Pipeline (scraper.py, resumable)

| Fase | Qué hace | Chrome |
| --- | --- | --- |
| 0 buildcores | specs por `part_numbers` (si está `buildcores-db/`) | no |
| 0.5 manual | specs manuales (Thermaltake, Cooler Master, Netac) | no |
| 1 index | recorre listados de 8 categorías → `products` | sí |
| 2 match | cruza SKUs vs productos (exact_name / slug_suffix / amd_core) | no |
| 2.5 dataset | specs del dataset local | no |
| 3 scrape | extrae specs de matches sin specs | sí |
| 4 search | busca SKUs sin match (Part# exacto o SKU en slug) | sí |

Con `SKIP_PCPP=1` corre solo con fuentes offline, sin abrir Chrome.

## Estado (2026-09-05)

Tablas en `PRODUCTOS`: **spec_definitions 179 · matches 2.424 · product_specs 26.243 · skus 13.998 · category_mapping 22**.

Cobertura: 2.424 de 13.998 SKUs con specs (17%). De los **344 componentes de PC en stock, 233 tienen specs (68%)** — ése es el número que importa para el armador, no el 17% global.

## Notas

- [[specs-y-armador]] — tablas SQLite↔SQL Server, cadena de joins, `is_compat`, las 9 reglas del armador, propuesta de proyecto
- [[operacion]] — cómo correr acá, origen de stock, reconstruir `scraper.db` desde SQL Server, cobertura actual
- [[contexto]] — decisiones tomadas, pendientes y próximos pasos
- [[memoria]] — memoria de Claude del proyecto (preferencias, reglas, referencias)
- [[changelog]] — historial de sesiones
