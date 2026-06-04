# BluPartPicker

Catálogo unificado de tecnología argentina. API REST que consolida mayoristas y resellers en una sola DB SQLite con historial de precios.

**Última sync:** 2026-06-04

## Stack

- Python 3 · SQLite · FastAPI · uvicorn · systemd · cron
- Playwright (solo Ceven, por Akamai)

## Fuentes

| Source | Tipo | Productos | Moneda |
|--------|------|-----------|--------|
| `invid` | Mayorista | ~1.195 | USD |
| `ceven` | Mayorista | ~464 | USD |
| `stylus` | Mayorista | ~906 | USD |
| `preciosgamer_*` (37) | Resellers | ~145.108 | ARS |

## API — http://10.10.10.7:4444

```bash
GET /items?categoria=MOUSE&fabricante=Logitech&distribuidor=0
GET /categorias?distribuidor=0
GET /fabricantes?categoria=MOUSE&distribuidor=1
GET /items/{source}/{codigo}/historia
GET /sources  |  GET /sync/log
```

## Notas

- [[arquitectura]] — schema DB, endpoints, inferencia de categoría/marca
- [[resellers]] — auth, formatos y gotchas por fuente
- [[stack]] — dependencias y versiones
- [[contexto]] — decisiones de diseño y casos de uso
- [[changelog]] — historial de lo implementado
- [[memoria]] — próximos pasos y gotchas de sesión