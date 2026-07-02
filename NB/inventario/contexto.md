# Contexto — inventario

Información de entorno local, variables de entorno y gotchas del proyecto.

## Entorno local

### Mac (hermess) — `/Users/hermess/www/inventario/`

```bash
# Backend — OPENSSL_CONF es OBLIGATORIO (ver gotchas: TLS 1.0)
cd ms-metadata
OPENSSL_CONF=$PWD/openssl_legacy.cnf .venv/bin/uvicorn main:app --reload --port 8081 --host 0.0.0.0

# Frontend
cd inventario-web-app/app
npm run dev   # http://localhost:3000 — API_HOST=http://0.0.0.0:8081
```

- Venv del backend: `.venv` (Python 3.9), todas las deps instaladas
- Ambos repos en rama `catri-fine-tuning` (2026-06-11)

### Linux (/var/www/nb/inventario) — setup activo (2026-07-02)

```bash
cd ms-metadata && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
cd inventario-web-app/app && npm run dev   # http://localhost:3000 — API_HOST=http://localhost:8000
```

- **Swagger UI**: http://localhost:{puerto}/docs
- Ambos repos en rama `development` (front) / `Development` (back) a 2026-07-02.
- **DB**: `10.10.10.47,1433` base `NB_WEB`, usuario `cmercurio`. Alternativa: `190.210.23.97,4444` / `emanzando_devweb01`.
- ⚠️ Cambiar la DB en `.env` requiere **reiniciar uvicorn** (el `--reload` no relee `load_dotenv()`).

## Variables de entorno

### ms-metadata/.env

```
DB_DRIVER=ODBC Driver 18 for SQL Server
DB_SERVER=10.10.10.47,1433          # formato host,puerto (no DB_HOST/DB_PORT). Alt: 190.210.23.97,4444
DB_NAME=NB_WEB
DB_USER=cmercurio                    # alt: emanzando_devweb01 / web
DB_PASS=...                          # la variable es DB_PASS, no DB_PASSWORD
ALLOWED_ORIGINS=http://localhost:3000,...
OPENAI_API_KEY=...                   # placeholder alcanza para levantar; real para IA
STATIC_URL=https://static.nb.com.ar/ # sin esto revienta models.py con productos con foto
```

### inventario-web-app/app/.env

```
API_HOST=http://0.0.0.0:8081   # (en linux era :8000)
NODE_PORT=3000
NODE_ENV=development
```

## Gotchas conocidos

> **Actualización 2026-06-27** (modal de seriales + índices, ver [[modulo-seriales]] y [[performance-indices]]):
> - **No batchear las subqueries de la grilla con `IN`**: se probó y empeoró 2.5–3.7× (los round trips sobre el link TLS 1.0 a prod pesan más que las subqueries inline, que corren server-side en un round trip y pegan a tablas indexadas). El fix correcto fue el índice **P2** (`ST_DETALLE_STOCK (CREF, FECHA_EGRESO)`): grilla 1.63s → 0.54s. **Medir siempre contra la DB real**; comparar viejo vs nuevo con `git show HEAD:archivo.py > _temp.py`.
> - **Palabras que se parten a la mitad en las tablas**: antd usa `word-break: break-all` en `.ant-table-row-cell-break-word`. Regla global en `assets/ant/main.less` (`word-break: keep-all; overflow-wrap: normal`) → solo corta en espacios. Un token largo se excede en vez de partirse.
> - **DDL en prod**: el SQL Server es **Enterprise** → crear índices con `WITH (ONLINE = ON)` para no lockear. El login `web` tiene ALTER+CONTROL.
> - **Modal de seriales "todos despachados"**: el endpoint serializaba a mano solo 6 campos (faltaba `present`); siempre serializar el objeto completo. Y default de depósito = **"Todos"** o esconde los disponibles.

> **Actualización 2026-06-23** (rama regularizacion-stock, ver [[modulo-regularizacion]]):
> - **cc11 no serializa**: solo 16/602 artículos con seriales (955 ser vs 107.058 albprol). Su delta no es comparable con el modelo serializado de cc4 — sus deltas raros son descuadres de columnas de stock, NO albprol faltante/sobrante. Hay 209 SKUs duplicados cc4↔cc11.
> - **Restaurar `albprol` es cost-neutral**: el recálculo de costo lo hace el flujo de recepción, no la fila. Sin triggers en albprol/albprot/articulo/stocks; `NCOSTEPROM` almacenado; el FOB usa el **último** albprol por fecha → un asiento backdated no cambia costo ni FOB.
> - **Stock ya no obliga filtro**: la pestaña Stock carga con **solo la empresa** (sin marca/categoría/búsqueda). Más pesado pero paginado. Filtro Delta combinable ("Distinto de cero").

> **Actualización 2026-06-20** (rama catri-fine-tuning2, ver [[memoria]]):
> - **Filtro empresa quedaba sin aplicar al cambiar de pestaña**: el select se veía puesto pero los datos sin filtrar; carrera (`General.vue` dispara el fetch y `updateMet` descarta el 2do fetch en vuelo con `window.__generalUpdateRunning`). Fix: setear `companyCode` (usuario o **4**) en `middleware/companyCode.js` ANTES del fetch, no en `created()`. Solo queda libre si se borra a mano dentro de la misma pestaña.
> - **N+1 catastrófico en `/items` y `/item`**: cada `dbconnection()` abre conexión nueva (TLS 1.0) y nunca cierra; un `for x in rta: getImages(x)` hace N handshakes. ~11,5s → ~1,2s con query bulk `IN` (`getImagesBulk`). Ante listados lentos buscar `for ... in rta` con helper que llama `dbconnection()`.
> - **Git (back)**: `Development` (mayúscula) es la rama canónica (trackea `origin/Development`); borrar `development` minúscula la deja huérfana (macOS case-insensitive) → `git reset --mixed origin/Development`.
> - **Nav "Precios"** nunca estuvo en git (prod tenía edición manual de `basic.vue`); agregado en `catri-fine-tuning`. `xlsx` ya estaba en package.json; deploys necesitan `npm ci`.

| Problema | Causa | Solución |
|----------|-------|---------|
| **`npm install <pkg>` con el dev server corriendo → RuntimeError / loader infinito** (ej. al instalar `xlsx`) | Instalar deps mientras `npm run dev` corre deja webpack/HMR con estado inconsistente | **Reiniciar `npm run dev`** después de instalar; en el browser hard-reload |
| **Grilla de Precios tardaba ~4.4s** | NO era `get_items_prices` (0.08s) sino la query principal `get_items_stocks` (~3.8s) con ~10 subqueries correlacionadas que Precios no muestra | **Resuelto (2026-06-15)**: path liviano `get_items_prices_grid` con `pricesView=1` (~0.9s) + count `COUNT(DISTINCT)` + paralelo. ~5s → ~1,5s. Stock intacto |
| **El `<th>` con checkbox de header queda vacío** (slot de title no renderiza) | Ant 1.x solo aplica `slots.title` si `column.title === undefined` (`lib/table/index.js`); un `title:""` lo bloquea | NO poner `title` en la columna (que quede undefined) y usar `slots: { title: '<slot>' }` |
| **Celdas editables: cambio de UX** | `EditablePriceCell` ahora muestra texto y monta el input de Ant solo al click (perf: evita miles de inputs) | Se clickea la celda para editar; no hay tab entre celdas. Es a propósito |
| **Tiempos altos/variables del SQL Server** | `190.210.23.97` es un server remoto compartido; la misma query va de 0.3s a 4s según carga | No es del código; comparar mejoras siempre en runs relativos |
| **`ULTIMA_COMPRA` no existe** en `articulo` | Solo existe en `clientes`; para artículo la fecha de ingreso es `ULTIMO_INGRESO` | Usar `articulo.ULTIMO_INGRESO` (y `ULTIMA_VENTA`) |
| **pyodbc 08001 "TCP Provider: 10054"** en todo endpoint con DB, aunque TCP y ping al server andan (parece firewall/VPN, NO lo es) | El SQL Server de prod solo habla **TLS 1.0** y OpenSSL 3.x lo rechaza por defecto (ambos drivers ODBC 17/18, con o sin `Encrypt`) | Levantar uvicorn con `OPENSSL_CONF=openssl_legacy.cnf` (commiteado en el repo: `MinProtocol=TLSv1`, `SECLEVEL=0`) |
| **Filas desalineadas** con columna fija en tablas antd 1.x | `fixed:'left'` clona la tabla en un overlay y sincroniza alturas por JS — siempre se desfasa | CSS `position:sticky` + fondos opacos por estado (misma tabla ⇒ alineación perfecta). Ver `pages/itemsPrices.vue` |
| **Cabeceras corridas** con header fijo (`scroll.y`) | Header y body son tablas separadas; con `scroll.x:'max-content'` cada una calcula anchos distintos | `scroll.x` numérico (suma de anchos visibles) + `table-layout:fixed; min-width:100%` en ambas |
| Item no aparece al deep-linkear a Productos | La query default de la pestaña lleva `noImage=1` y `stock=1`, que FILTRAN | Omitir ambos en deep-links; buscar por ID numérico (`ID_ARTICULO` via LIKE) |
| **Cabeceras se ven "por dentro" de la columna Título** al scrollear | El `<th>` sticky no recibe la CSS class confiable en la tabla de header separada de antd | Estilo **inline** vía `customHeaderCell` (fondo opaco + z-index). Sombra sutil (`2px/5%`) |
| `fetchCompetition` crashea en SSR (`Not authenticated` / token sync) | Dispatch fire-and-forget durante SSR pierde el contexto req/res de auth | Guardar con `process.client` antes de despachar |
| Servidor backend crashea al iniciar | `ALLOWED_ORIGINS` no definido (`.split(",")` sin default) | Asegurarse de que la variable esté en `.env` |
| `.env` original tenía nombres incorrectos | El código espera `DB_SERVER`, `DB_PASS`, `DB_DRIVER` (no `DB_HOST`, `DB_PASSWORD`, `DB_TYPE`) | Copiar `.env_example` y completar con los nombres correctos |
| `FastAPIDeprecationWarning: regex has been deprecated` | `main.py` usa parámetro `regex` deprecado | No rompe nada, es un warning |
| `Cannot find module ../build-version.json` al iniciar dev | Lo genera `scripts/update-build-version.js` solo al hacer `npm run build` | No rompe nada en dev |
| 401 al iniciar el frontend | El middleware `auth` redirige todas las rutas a `/login` si no hay token | Comportamiento normal |
| **Editar precio/utilidad no persiste en items nuevos** | El item no tiene fila en `ST_GANANCIA_ESTIPULADA_ARTICULOS`; `_update_gain_column` hacía `UPDATE` puro (0 filas, sin error) | **Resuelto (2026-06-24)**: upsert — inserta la fila sembrada desde los gains. Tabla sin PK, clave `cRef` nvarchar |
| **Búsqueda no encuentra items con `()` en el título** | `_` del slug es comodín de 1 char en LIKE; "(LGA1700)" agrega caracteres que no matchean | Reemplazar `_` y espacio por `%` en el término (aplicado en Stock/Precios/Productos) |

## Deploy a producción

La feature de competencia **no agrega variables `.env`** (la URL de partpicker está
hardcodeada en `competition.py`). Checklist al pasar a prod:

1. **Salida HTTPS a `partpicker.blustudioinc.com`** desde el server — si el egress
   está bloqueado, `/itemsCompetition` da 500 y la grilla degrada a "-".
2. **`requests` instalado** en el Python de prod (los scrapers ya lo usan).
3. **Permiso de escritura en `NewBytes_DBF.dbo.scrap_hg`** para el usuario de DB
   (el "Guardar y rematchear" hace UPDATE/INSERT — misma tabla del scraper hardgamers).
4. **`OPENSSL_CONF` NO hace falta en prod** (solo es workaround de dev local con
   OpenSSL 3.x — ver gotcha TLS arriba).
5. Primera llamada a `/itemsCompetition` tras cada reinicio: ~30s (warm-up del
   catálogo); instantánea después, refresca sola cada 30 min.

## Reglas de negocio relevantes

- **Precios**: al fijar un precio a mano, la utilidad derivada se aplica SIEMPRE
  a la primera del par (PL1/MAY1/LO1/PML); la segunda queda fija. Ver [[modulo-precios]].
- **Mayoristas se comparan sin IVA** (campo `precio_sin_iva` de partpicker) contra
  los precios USD propios; resellers en ARS final como referencia de clientes.
- `scrap_hg.search_keys` es compartida entre la sección Precios y el scraper de
  hardgamers — editar keywords afecta a ambos.
- Pendiente de decisión: si `libre-opcion` (canal propio) debe excluirse del
  bloque de resellers en competencia.

## Ver también

- [[inventario]] · [[arquitectura]] · [[stack]] · [[modulo-precios]]
