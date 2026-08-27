# Memoria

Espejo de la memoria de Claude del proyecto (`~/.claude/projects/-var-www-gigabyte-gigabyte-aterrizaje/memory/`).

## Proyecto

`/var/www/gigabyte/gigabyte-aterrizaje` — catálogo GIGABYTE tipo e-commerce **sin compra**. Repo `git@github.com:BluIncStudio/giga-partpicker.git` (rama `main`, commits sin firma de Claude, autor Catriel <catrielmercurio@gmail.com>).

- Stack Nuxt 3 SSR + Tailwind (PostCSS nativo). Datos de [[gigabyte-aterrizaje/api-partpicker|BluPartPicker]] vía `server/api/*` (oculta la key en `.env`).
- Catálogo `fabricante=Gigabyte` (~330 productos agrupados por `oracular_sku`) + whitelist de 7 resellers. RETEC/COMPUFAN `enabled:false`. Caché en memoria 30 min. Saneamiento: `normalizeCategoria()` unifica categorías (PLACA/PLACA DE VIDEO/TARJETA→PLACA DE VIDEO; WATER/WATER COOLER→WATER COOLER) y se excluyen ofertas con "outlet" en el nombre.
- UI AORUS: logo oficial (SVG máscara), `CategoryIcon`, tema claro/oscuro (`useState`+cookie), fondos de imagen con `mix-blend-multiply`.
- **Node ≥20.11 obligatorio** (portable en `~/.local/node20/bin`). Dev server: lanzar one-liner con `nohup` (multi-statement/`sleep` en foreground → exit 144).

## Referencia — API BluPartPicker

- Base `https://partpicker.blustudioinc.com`, spec `/openapi.json`, auth header `X-Api-Key` (server-side).
- Endpoints: `/items` (filtros: `fabricante`, `source`, `categoria`, `q`, `moneda_out`, `limit` máx 500), `/groups/{oracular_sku}`, `/sources`, `/fabricantes`, `/categorias`.
- Resellers → source (prefijo `preciosgamer_`): venex, maximus, mexx, armytech, full-h4rd, gaming-city, hardcore. RETEC/COMPUFAN no existen como source.

## Ver también

- [[gigabyte-aterrizaje/gigabyte-aterrizaje|gigabyte-aterrizaje]] · [[gigabyte-aterrizaje/contexto|contexto]] · [[gigabyte-aterrizaje/arquitectura|arquitectura]]
