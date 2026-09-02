# Changelog — partPicker

## 2026-09-02 — Correr en máquina nueva + actualización de in-stock

Sesión operativa: levantar el proyecto en un equipo limpio (sin `scraper.db` ni `.env`), reconstruir la base desde el respaldo de SQL Server y actualizar specs de los componentes en stock. Ver [[operacion]].

### Setup del entorno
- venv Python 3.12 con set acotado de deps (evitando el conflicto `pyee` de playwright/pyppeteer y el `distutils` de 3.12 vía `setuptools<81`).
- Verificada conectividad a SQL Server `:4444` y a pcpartpicker. Chrome 152 + `uc 3.5.5` pasa Cloudflare.

### Reconstrucción de scraper.db (nuevo `rebuild_db.py`)
- Confirmado que la DB `PRODUCTOS` es el respaldo (conteos exactos: product_specs 26141, skus 13998, matches 2413, spec_definitions 179, category_mapping 22).
- `rebuild_db.py` copia las 5 tablas preservando `spec_definitions.id`. Integridad verificada: 0 `spec_def_id` huérfanos.

### Origen de stock definido
- "En stock" = `NewBytes_DBF.dbo.stocks.nstock > 0` (cualquier almacén), `ID_ARTICULO = id_interno`. NO `CS.dbo.productos.stock_cliente`.
- 1.266 in-stock en el inventario; 344 son componentes de PC.

### Scrape dirigido a in-stock (nuevo `prep_instock_items.py`)
- Poblado `items`/`categories` con los 122 in-stock componentes-PC sin match y `phase='search'` → Fase 4 buscó 110.
- **Resultado: 11 nuevos matcheados con specs** (memory 6, power-supply 3, motherboard 2). Los ~99 restantes no matchearon por criterio estricto (Part# exacto).

### Match manual A620I AX (nuevo `scrape_one.py`)
- El match manual del monitor había creado el vínculo pero sin specs (Cloudflare bloquea su scrape con requests/BS4).
- `scrape_one.py` (corre `phase3` con Chrome) completó las 22 specs, incluidas las 6 de compatibilidad (Socket AM5, DDR5, Mini ITX, etc.).

### Sync a SQL Server
- `sync_sqlserver.py`: **+102 `product_specs`, +11 `matches`** insertados en `PRODUCTOS`. Verificado (2424 matches, 26243 specs).
- Cobertura final de componentes PC en stock: **68% con specs, 66% con compat**. Detalle en [[operacion#Cobertura actual de componentes PC en stock 2026-09-02]].

Archivos nuevos (repo, sin commitear): `rebuild_db.py`, `prep_instock_items.py`, `scrape_one.py`.

## Ver también

- [[partPicker]] — índice del proyecto
- [[operacion]] — cómo correr, stock, reconstrucción, cobertura
- [[specs-y-armador]] — esquema de tablas y reglas del armador
