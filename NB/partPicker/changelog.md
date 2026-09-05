# Changelog — partPicker

## 2026-09-05 — Corrección del origen de stock

Al sincronizar la bóveda se detectó que [[specs-y-armador]] daba por bloqueante que "solo 1 producto con specs tiene stock". Era un diagnóstico sobre la tabla equivocada: `CS.dbo.productos.stock_cliente` es el catálogo web, no la existencia real.

Corregido contra `NewBytes_DBF.dbo.stocks` (`nstock > 0`): **2.869 artículos en stock, 243 con specs**. La nota quedó actualizada y el riesgo bajado de "alto" a resuelto. Ver [[operacion#Origen del stock dato clave]].

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

## 2026-08-28 → 09-02 — Carga inicial a SQL Server (desde la Mac)

Sesión desde `~/www/partPicker` en la Mac. Es la que **creó y pobló las tablas en `PRODUCTOS`**, o sea el respaldo del que después se reconstruyó `scraper.db` en la máquina nueva.

### Migración del destino SQL Server
- Host viejo `190.210.23.108:1433` (user `web`) → **`db-nb-massql-dev.blu.net.ar:4444`** (user `cmercurio`). El 1433 estaba cerrado; el login `web` fallaba con error 18456 en el host nuevo.
- Descartado que fuera el protocolo: las 5 versiones de TDS (7.0 a 7.4) daban el mismo 18456. Era credencial.
- `SQLSERVER_PORT` como variable nueva del `.env`; antes el 1433 estaba hardcodeado en `sync_sqlserver.py`.

### `matches` agregada al sync
- Faltaba en el `SYNC_CONFIG`: sin ella, del lado de SQL Server quedaban `product_specs` con una `product_url` suelta y `skus` con `id_interno`, **sin nada que las una**. La cadena de joins no se podía completar.
- Agregada al `CREATE_TABLES` y al `SYNC_CONFIG`.

### Carga completa
- 5 tablas creadas desde cero e insertadas: spec_definitions 179 · product_specs 26.141 · category_mapping 22 · skus 13.998 · matches 2.413.
- Tardó ~80 min por insertar fila a fila. `skus` y `matches` se cargaron en paralelo con `executemany` por lotes (segundos) — confirma que la optimización pendiente vale la pena.
- Verificado el join completo end-to-end: 2.413 SKUs con specs.

### Documentación
- Nueva nota [[specs-y-armador]]: estructura de tablas, cadena de joins, `is_compat`, las 9 reglas, trampas del dato y propuesta de proyecto del armador.
- Detectado que `CS.dbo.productos` tiene **una fila por revendedor** (447.247 filas / 16.448 `id_interno`): toda query necesita `ROW_NUMBER` para deduplicar. Hay 1.253 pares `(id_interno, id_usuario)` duplicados, así que filtrar por revendedor tampoco alcanza.

### Git
- Commit `f598b2b` + push. El repo llevaba **5 meses sin actualizar** (último push 2026-03-21): no estaban `COMPATIBILIDAD.md`, `sync_sqlserver.py`, la fase BuildCores ni las pestañas nuevas del monitor.
- `scraper.db` sacado del tracking (ya estaba en `.gitignore` pero seguía trackeado).

## Ver también

- [[partPicker]] — índice del proyecto
- [[operacion]] — cómo correr, stock, reconstrucción, cobertura
- [[specs-y-armador]] — esquema de tablas y reglas del armador
