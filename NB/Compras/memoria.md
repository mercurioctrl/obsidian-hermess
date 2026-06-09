# Memoria del proyecto

Hechos y gotchas cross-sesión (sincronizados desde la memoria de Claude del proyecto).

## Proyecto / setup

### Cómo correr front y back en local
- **Backend (Laravel):** Docker, contenedor `api-rest-compras-apirest-laravel` en **http://localhost:8096** (API base `/v1`). Suele estar levantado.
- **Frontend (Nuxt 2):** `cd compras-web-app-v1-/app && npm run dev` → **http://localhost:3867** (`NODE_PORT=3867` en `.env`).
- El front **no** usa 3002 (el `.env-example` dice 3002, pero el `.env` real es 3867). El **3002 lo ocupa el proyecto `pedidos`**.
- Puede faltar `node_modules`: correr `npm ci` (Node 16, compat. Nuxt 2).
- El front responde **302** sin login (middleware `auth` global) — normal.
- El log de `npm run dev` se **infla muchísimo** porque `axios.debug` está on en dev y loguea cada respuesta completa (`/fabricantes` ≈ 2648 filas). Para depurar conviene reiniciar con log limpio o apagar `axios.debug`.

### Sección Competencia
Ver [[competencia|nota dedicada]]. Resumen: feature en rama `competencia`, grilla de competidores server-side (Distribuidores / Resellers), consume BluPartPicker API.

## Referencia

### BluPartPicker API (catálogo de competidores)
- Host: `COMPETITORS_API_HOST=http://10.10.10.7:4444` (red interna). Docs `/redoc`, spec `/openapi.json`.
- ~147k items; `distribuidor=1` mayoristas (≈2.565), `distribuidor=0` revendedores (≈145k). Siempre paginar server-side.
- Gotchas: `categoria` filtra solo desde v2.1; `/sources` no marca `distribuidor` (detectar mayoristas muestreando `/items?distribuidor=1` → invid/ceven/stylus); `/fabricantes` ya no trae `source` por fila.

## Ver también

- [[competencia|Competencia]] · [[arquitectura|Arquitectura]] · [[stack|Stack]]
