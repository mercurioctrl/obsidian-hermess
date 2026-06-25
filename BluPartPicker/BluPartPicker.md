# BluPartPicker

Catálogo unificado de tecnología argentina. API REST que consolida mayoristas y resellers en una sola DB SQLite con historial de precios, conversión de moneda en tiempo real y **matching de productos** (`oracular_sku`) con consola de curación web.

**Última sync:** 2026-06-25 · **Commit:** `44c858d` · **Rama activa:** `feat/api-auth` (auth + Swagger)

## Stack

- Python 3 · SQLite (WAL) · FastAPI · uvicorn · systemd · cron
- Playwright (solo Ceven, por Akamai)
- dolarapi.com (tipos de cambio, sin auth)
- Frontend de curación: HTML + vanilla JS (sin build), servido en `/ui`

## Fuentes — 5 mayoristas (USD) + ~37 resellers (ARS)

| Source | Tipo | Moneda |
|--------|------|--------|
| `invid` · `ceven` · `stylus` · `nb` · `air` | Mayoristas (`distribuidor=1`) | USD |
| `preciosgamer_{slug}` (~37) | Resellers (`distribuidor=0`) | ARS |

## API — http://10.10.10.7:4444 · consola `/ui` · docs `/docs`

```bash
# Catálogo
GET /items?categoria=MOUSE&fabricante=Logitech&distribuidor=0   # incluye oracular_sku
GET /items?distribuidor=1&moneda_out=ARS&tc=mayorista&sort_by=precio
GET /items?tendencia=1                                          # señal suba/baja de precio
GET /exchange-rates  |  GET /categorias  |  GET /fabricantes
GET /sources  |  GET /sync/log
# Matching / comparador
GET  /groups?solo_cruzados=1&sort_by=ahorro                     # productos canónicos
GET  /groups/{oracular_sku}                                     # comparador (mismo producto, N fuentes)
GET  /candidates  |  POST /match                                # curación
# Admin (requiere X-Api-Key: <ADMIN_KEY>)
POST  /admin/keys                    # crear key para usuario
GET   /admin/keys                    # listar todas
PATCH /admin/keys/{key}             # activar/desactivar
GET   /admin/keys/{key}/usage       # consumo por endpoint
```

**Auth:** header `X-Api-Key`. `AUTH_REQUIRED=0` (default, API pública) / `AUTH_REQUIRED=1` (activa validación). Ver [[contexto#Decisiones recientes]].

## Notas

- [[arquitectura]] — schema DB completo, endpoints, índices, conversión de precios, pipeline de matching
- [[matching-productos]] — `oracular_sku`: pipeline por niveles, tablas, loop de curación, consola `/ui`
- [[resellers]] — auth, formatos y gotchas por fuente (Invid, Ceven, Stylus, NB, Air, PreciosGamer)
- [[stack]] — dependencias y versiones
- [[contexto]] — decisiones de diseño y casos de uso
- [[changelog]] — historial de lo implementado sesión a sesión
- [[memoria]] — gotchas activos, próximos pasos, credenciales

## Crawlers

- [[BluPartPicker/crawlers/fullh4rd|Scraper — Full H4rd]] — scraper de Full H4rd
