# BluPartPicker

Catálogo unificado de tecnología argentina. API REST que consolida mayoristas y resellers en una sola DB SQLite con historial de precios y conversión de moneda en tiempo real.

**Última sync:** 2026-06-04

## Stack

- Python 3 · SQLite (WAL) · FastAPI · uvicorn · systemd · cron
- Playwright (solo Ceven, por Akamai)
- dolarapi.com (tipos de cambio, sin auth)

## Fuentes

| Source | Tipo | Productos | Moneda |
|--------|------|-----------|--------|
| `invid` | Mayorista | ~1.195 | USD |
| `ceven` | Mayorista | ~464 | USD |
| `stylus` | Mayorista | ~906 | USD |
| `preciosgamer_*` (37) | Resellers | ~145.108 | ARS |

## API — http://10.10.10.7:4444

```bash
# Filtros principales
GET /items?categoria=MOUSE&fabricante=Logitech&distribuidor=0
GET /items?distribuidor=1&moneda_out=ARS&tc=mayorista&sort_by=precio

# Conversión de precios
GET /items?moneda_out=ARS&tc=blue&precio_min=50000&precio_max=200000
GET /exchange-rates

# Navegación
GET /categorias?distribuidor=0
GET /fabricantes?categoria=MOUSE&distribuidor=1

# Detalle e historial
GET /items/{source}/{codigo}
GET /items/{source}/{codigo}/historia
GET /sources  |  GET /sync/log
```

## Notas

- [[arquitectura]] — schema DB completo, endpoints, índices, conversión de precios
- [[resellers]] — auth, formatos y gotchas por fuente (Invid, Ceven, Stylus, PreciosGamer)
- [[stack]] — dependencias y versiones
- [[contexto]] — decisiones de diseño y casos de uso
- [[changelog]] — historial de lo implementado sesión a sesión
- [[memoria]] — gotchas activos, próximos pasos, credenciales
