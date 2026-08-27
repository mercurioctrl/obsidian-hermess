# API BluPartPicker

Catálogo unificado de tecnología argentina (mayoristas + resellers). Fuente de datos de [[gigabyte-aterrizaje/gigabyte-aterrizaje|gigabyte-aterrizaje]]. Ver también la nota raíz [[BluPartPicker]].

- **Base:** `https://partpicker.blustudioinc.com`
- **Spec:** `GET /openapi.json` (el `/docs` es Swagger UI JS).
- **Auth:** header `X-Api-Key`. La key vive en `.env` y solo se usa server-side.

## Endpoints usados

| Ruta | Uso |
|------|-----|
| `GET /items` | Listado con filtros. Base del catálogo. |
| `GET /groups/{oracular_sku}` | Comparador del mismo producto en todas las fuentes (referencia). |
| `GET /sources` | Nombres de fuentes (mapeo de resellers). |
| `GET /fabricantes`, `/categorias` | Marcas/categorías con conteo. |

### `GET /items` — params relevantes

`fabricante` (usamos `Gigabyte`), `source`, `categoria`, `q`, `isinstock`, `distribuidor` (`0`=resellers ARS, `1`=mayoristas USD), `moneda_out`+`tc`, `sort_by`, `limit` (máx 500), `offset`. Los resellers ya vienen en **ARS** (`precio_final`). Mismo modelo → mismo `oracular_sku`.

## Mapeo resellers → source (prefijo `preciosgamer_`)

| Reseller | source | Estado |
|----------|--------|--------|
| VENEX | `preciosgamer_venex` | ✅ |
| MAXIMUS | `preciosgamer_maximus` | ✅ |
| MEXX | `preciosgamer_mexx` | ✅ |
| ARMYTECH | `preciosgamer_armytech` | ✅ |
| FULL HARD | `preciosgamer_full-h4rd` | ✅ |
| GAMING CITY | `preciosgamer_gaming-city` | ✅ |
| HARDCORE COMPUTACION | `preciosgamer_hardcore` | ✅ |
| RETEC | — | ⏳ no existe como source |
| COMPUFAN | — | ⏳ no existe como source |

Editar en `server/utils/config.ts`. Para sumar RETEC/COMPUFAN: poner su `source` real y `enabled: true`.

## Ver también

- [[gigabyte-aterrizaje/arquitectura|arquitectura]] · [[gigabyte-aterrizaje/gigabyte-aterrizaje|gigabyte-aterrizaje]]
