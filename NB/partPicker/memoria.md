# Memoria — partPicker

Consolidado de la memoria de Claude del proyecto (`~/.claude/projects/-Users-hermess-www-partPicker/memory/`), para que quede legible en la bóveda. Ver [[partPicker]].

## Usuario

Hispanohablante, con un inventario de ~14.000 SKUs de componentes de PC. Todo el proyecto está en español —comentarios, prints, UI— y hay que mantenerlo así.

## Cómo trabajar en este proyecto

- **Matching estricto.** Solo exacto por nombre, slug suffix o Part# en la ficha. Nunca substring fuzzy. Ante la duda, no matchear.
- **No marcar falsos positivos.** Si no se obtuvieron specs (bloqueo de Cloudflare, por ejemplo), el item queda pendiente, no hecho.
- **SQLite para todo.** Nada de archivos JSON intermedios.
- **Confirmar antes de actuar** cuando la instrucción es ambigua.

## Inventario

Tres CSV importados a `scraper.db`: `items.csv` (1.558 productos), `categories.csv` (155 categorías), `brands.csv` (287 marcas).

Solo una fracción son componentes de PC relevantes para PCPartPicker; el resto son periféricos, accesorios y hogar. `PC_COMPONENT_CATEGORIES` filtra los que sí: PROCESADORES, MOTHER GIGABYTE/ASROCK/ASUS, MEMORIAS, PLACA DE VIDEO, GABINETE, GABINETE GAMER, FUENTES, COOLERS, DISCOS SSD, DISCOS HDD. No tiene sentido buscar teclados o cables en PCPartPicker.

La familia de cada artículo sale de `NewBytes_DBF.dbo.articulo.ID_FAMILIA`, que es el mismo id que `category_mapping.category_id`.

## SQL Server

`db-nb-massql-dev.blu.net.ar:4444`, base `PRODUCTOS`, usuario `cmercurio`. Credenciales solo en el `.env` del proyecto, nunca en la bóveda ni en el repo.

- Solo conecta con **`pymssql` y `tds_version='7.0'`**. `pyodbc` falla con 0x2746 por incompatibilidad de TLS.
- La instancia **distingue mayúsculas** en nombres de base: es `NewBytes_DBF`, no `newbyted_dbf`.
- Las bases (`PRODUCTOS`, `CS`, `NewBytes_DBF`) están en la misma instancia, así que el cross-database join funciona sin linked server.

> El host anterior era `190.210.23.108:1433` con usuario `web`. Quedó obsoleto: ese puerto está cerrado y la credencial ya no valida.

## Armador de PC

El usuario quiere que sus clientes armen PCs con componentes compatibles. Las 9 reglas están en `COMPATIBILIDAD.md` del repo y resumidas en [[specs-y-armador]]. Las specs con `is_compat = 1` son las que alimentan esas reglas.

**El armador se construye en otro frontend**, no en este repo.

## Referencias

- Repo: `mercurioctrl/partPicker` (privado, GitHub)
- Datasets: `docyx/pc-part-dataset` y BuildCores Open DB (`buildcores/buildcores-open-db`)

## Ver también

- [[contexto]] — decisiones y pendientes
- [[operacion]] — setup y operación
- [[specs-y-armador]] — esquema y reglas
