# Competencia — Catálogo de competidores

Sección del [[stack#Frontend|frontend Nuxt 2]] para navegar el catálogo de competidores (mayoristas y revendedores). Vive en la rama **`competencia`** (basada en `development`), commit `0e048bc`. **Local, sin pushear.**

## Qué hace

Consume la **BluPartPicker API** (FastAPI externa) y muestra una grilla rica para comparar productos de la competencia: precios, stock, marca, categoría, conversión de moneda, etc.

## API BluPartPicker

- **Host:** `COMPETITORS_API_HOST` (default `http://10.10.10.7:4444`). Docs en `/redoc`, spec JSON en `/openapi.json`.
- **CORS abierto** (`*`) → se llama desde el browser con una instancia axios dedicada (`$api.competitors` en `plugins/api.js`), separada de la API de compras.
- **Escala:** ~147k items → **todo server-side** (paginación + filtros). No cargar todo en cliente.
- **Endpoints:** `/items`, `/items/{source}/{codigo}`, `/items/{source}/{codigo}/historia`, `/sources`, `/fabricantes`, `/categorias`, `/exchange-rates`, `/sync/log`.
- **Filtros de `/items` (v2.1):** `source`, `fabricante`, `categoria`, `isinstock`, `distribuidor` (1=mayorista, 0=revendedor), `q`, `moneda_out` (ARS/USD → agrega `precio_convertido`), `tc` (mayorista/blue/oficial/bolsa/cripto/tarjeta), `precio_min`/`precio_max`, `sort_by`/`sort_dir`, `limit` (máx 500)/`offset`.

## Estructura en el front

Submenú **Competencia** (`layouts/basic.vue`) con dos subsecciones:

| Subsección | Página | Filtro fijo | Vista de stats |
|---|---|---|---|
| Distribuidores | `pages/distributors.vue` | `distribuidor=1` | Tarjetas por origen (Invid, Ceven, Stylus) |
| Resellers | `pages/resellers.vue` | `distribuidor=0` | Resumen agregado (`preciosgamer_*`) |

- **Grilla reutilizable:** `components/Competitors/Catalog.vue` (prop `distribuidor`) — ambas páginas la comparten.
- **Otros componentes:** `SourceCards.vue` (tarjetas por distribuidor), `Stats.vue` (resumen), `Detail.vue` (drawer ficha + historial).
- **Estado:** `store/competitors.js` (Vuex). `initView(distribuidor)` fija la vista y carga datos/opciones.

## Gotchas

- `categoria` **solo filtra desde la API v2.1** (antes el parámetro se ignoraba; un intento previo cargaba todo el catálogo para filtrar en cliente — descartado, no escala).
- **`/sources` no marca `distribuidor`** ni lo filtra → los mayoristas se detectan muestreando `/items?distribuidor=1`. Hoy: invid, ceven, stylus. Resto = revendedores.
- `/fabricantes` (v2.1) ya **no** trae `source` por fila (agrega por marca).
- El `.env` real no se commitea (gitignored) → agregar `COMPETITORS_API_HOST` por entorno (está en `.env-example`).
- El historial (`/historia`) hoy llega vacío.

## Ver también

- [[arquitectura#Frontend — Nuxt 2 con Vuex|Arquitectura del frontend]]
- [[stack|Stack]] · [[changelog|Changelog]] · [[memoria|Memoria]]
