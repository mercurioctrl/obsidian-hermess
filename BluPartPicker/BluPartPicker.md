# BluPartPicker

Catálogo unificado de distribuidores mayoristas de tecnología argentina. Consolida productos, precios, stock e imágenes de múltiples distribuidores en una sola API REST con historial de cambios.

**Ruta:** `/var/www/blupartpicker`  
**API:** `http://10.10.10.7:4444`  
**Docs:** `http://10.10.10.7:4444/docs`  
**DB:** `/var/www/blupartpicker/invid.db` (SQLite)

---

## Notas

- [[BluPartPicker/arquitectura|Arquitectura]]
- [[BluPartPicker/resellers|Resellers — casos puntuales]]
- [[BluPartPicker/contexto|Contexto y motivación]]
- [[BluPartPicker/stack|Stack e infraestructura]]
- [[BluPartPicker/changelog|Changelog]]
- [[BluPartPicker/memoria|Memoria Claude]]

---

## Distribuidores activos

| Source    | Productos | Con imagen | En stock | Cron           |
|-----------|-----------|------------|----------|----------------|
| `invid`   | ~1.195    | ~3%        | ~1.195   | cada 4h (00hs) |
| `ceven`   | ~464      | ~96%       | ~442     | cada 4h (01hs) |
| `stylus`  | ~906      | ~95%       | ~811     | cada 4h (02hs) |
| **Total** | **~2.565**|            |**~2.448**|                |

---

## Quick commands

```bash
# Estado de la API
curl http://10.10.10.7:4444/sources

# Sync manual
python3 /var/www/blupartpicker/sync_invid.py
python3 /var/www/blupartpicker/sync_ceven.py
python3 /var/www/blupartpicker/sync_stylus.py

# Servicio
sudo systemctl restart blupartpicker-api
tail -f /var/www/blupartpicker/api.log
```

**Repo:** `git@github.com:BluIncStudio/bluPartPicker.git` (privado · rama `main`)

*Última sincronización: 2026-06-03*
