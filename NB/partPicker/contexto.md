# Contexto — partPicker

Decisiones, pendientes y cosas que conviene saber antes de retomar. Ver [[partPicker]].

## El objetivo real

Las specs no son el fin: son insumo de un **armador de PC** que valide compatibilidad entre componentes, para que los clientes armen equipos que funcionen. El armador **se hace en otro frontend**, no en este repo. Este proyecto solo produce y mantiene los datos.

La propuesta completa de ese proyecto (arquitectura, fases, riesgos) está en [[specs-y-armador]], sección 8.

## Decisiones tomadas

- **Matching estricto, sin excepciones.** Solo match exacto por nombre, slug suffix o Part# de la ficha. Nunca substring fuzzy. Precisión sobre cobertura: un match falso contamina las specs de un producto y rompe el armador silenciosamente.
- **Si no se obtuvieron specs, queda pendiente.** Un bloqueo de Cloudflare no se marca como hecho. Nada de falsos positivos en el progreso.
- **Todo en SQLite, sin JSON intermedios.** `specs_results.json` quedó como dump histórico; ningún script lo vuelve a leer.
- **El stock sale de `NewBytes_DBF.dbo.stocks.nstock`**, no de `CS.dbo.productos.stock_cliente`. Ese último es el catálogo web/marketplace y da otra cifra. Costó un diagnóstico equivocado antes de detectarlo.
- **La normalización de specs va a una tabla tipada, una sola vez**, no parseada en vivo en cada request. Los valores vienen sin normalizar de tres fuentes distintas.

## Pendientes

| Pendiente | Por qué importa |
|---|---|
| **Automatizar el sync** | `sync_sqlserver.py` no lo dispara nada: ni cron, ni el scraper al terminar, ni un botón del monitor. Se corre a mano. |
| **Optimizar el sync a `executemany`** | Hoy inserta fila por fila con commit cada 100: re-actualiza las ~26k existentes para insertar unas pocas nuevas. Una carga completa tarda ~80 min. |
| **Sincronizar `products`** | Es la tabla con la categoría de cada producto y no viaja a SQL Server. Hoy la categoría se deriva de `spec_definitions.category`, que funciona pero deja afuera las 56 specs sin `spec_def_id`. |
| **260 discrepancias sin resolver** | Conflictos BuildCores vs. valor cargado, con UI de resolución en el monitor. No se sincronizan, así que desde SQL Server un valor puede estar en disputa sin que se note. |
| **Subir cobertura de PSU y cooler** | Son el cuello de botella del armador: 81 y 90 productos contra 563 de placas de video. Un armado necesita las 7 categorías a la vez. |
| **`.env.example` desactualizado** | Le falta `SQLSERVER_PORT`, que es variable nueva. Quien clone el repo no se entera de que existe. |

## Cosas que no funcionaron

- **`pyodbc` contra este SQL Server** — error 0x2746 (connection reset) por incompatibilidad de TLS. Solo anda `pymssql` con `tds_version='7.0'`.
- **`pip install -r requirements.txt` en Python 3.12** — conflicto de `pyee` entre `playwright` y `pyppeteer`, que el scraper no usa. Ver [[operacion#Setup en máquina limpia]].
- **Match manual del monitor** — crea el vínculo pero Cloudflare bloquea su scrape con requests/BS4, así que deja el producto sin specs. Hay que completarlo con Chrome (`scrape_one.py`).
- **Filtrar stock por `CS.dbo.productos.stock_cliente`** — deja la pantalla prácticamente vacía. Tabla equivocada.

## Ver también

- [[partPicker]] — índice
- [[specs-y-armador]] — esquema de tablas y propuesta del armador
- [[operacion]] — setup, stock, reconstrucción
- [[changelog]] — historial
