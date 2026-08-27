# Arquitectura

Nuxt 3 SSR con una capa server que hace de **proxy** contra la API [[gigabyte-aterrizaje/api-partpicker|BluPartPicker]].
El browser nunca ve la API key ni pega directo a partpicker.

## Flujo de datos

```
Browser → Nuxt server routes (/api/*) → BluPartPicker (header X-Api-Key)
            (proxy + caché + agrupación)
```

1. `server/utils/partpicker.ts` trae todos los items `fabricante=Gigabyte` de cada reseller activo en paralelo (`limit=500`, `moneda_out=ARS`).
2. **Excluye** ofertas cuyo nombre contenga `outlet` (case-insensitive) antes de agrupar.
3. Agrupa por producto canónico (`oracular_sku`; si falta, `source:codigo`) → un **producto** con N **ofertas**. La categoría se normaliza con `normalizeCategoria()` (PLACA/PLACA DE VIDEO/TARJETA→PLACA DE VIDEO; WATER/WATER COOLER→WATER COOLER).
4. Cachea el catálogo agrupado en memoria (**TTL 30 min**). Si una reconstrucción falla y hay caché vieja, sirve la vieja.

## Modelo agrupado

- **Product:** `id`, `nombre` (limpiado con `cleanName`, colapsa "PLACA DE PLACA DE VIDEO"→"PLACA DE VIDEO"), `categoria`, `nro_parte`, `imagen_url`, `offers[]`, `precio_min/max`, `sellers`, `in_stock`.
- **Offer:** `source`, `reseller` (label), `website`, `url_ficha`, `precio` (ARS), `isinstock`, `imagen_url`, `codigo`. Orden: en stock primero, luego precio asc.

## Endpoints internos (`server/api`)

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/api/products` | Listado. Query: `q`, `categoria`, `reseller`, `stock=1`, `sort`, `page`, `perPage`. Resumen sin offers. |
| GET | `/api/products/:id` | Ficha con todas las ofertas por vendedor. |
| GET | `/api/facets` | `total_productos`, `categorias[]`, `resellers[]` con conteos. |

- **Orden:** `relevancia` (en stock → más vendedores → precio), `precio_asc`, `precio_desc`, `nombre`, `vendedores`.
- **Robustez:** el server descarta strings vacíos y literales `"undefined"`/`"null"` (bug donde el cliente mandaba `categoria=undefined`).

## Páginas

- `/` — home: hero, stats, grid de categorías con iconos, destacados.
- `/productos` — catálogo: sidebar de filtros + grid + orden + paginación. El objeto de query se arma limpio (solo filtros activos).
- `/producto/:id` — ficha: imagen, specs, rango de precio, tabla de vendedores con link a su web.

## Ver también

- [[gigabyte-aterrizaje/stack|stack]] · [[gigabyte-aterrizaje/design-system|design-system]] · [[gigabyte-aterrizaje/api-partpicker|api-partpicker]] · [[gigabyte-aterrizaje/gigabyte-aterrizaje|gigabyte-aterrizaje]]
