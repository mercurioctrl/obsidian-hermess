# Servicio sync-curls

Servicio systemd de usuario que ejecuta 5 endpoints de sincronización cada hora contra la API Laravel local en `:8097`.

---

## Archivos clave

| Archivo | Rol |
|---------|-----|
| `/var/www/sync_curls.sh` | Script bash principal |
| `~/.config/systemd/user/sync-curls.service` | Definición del servicio (user-level) |
| `/tmp/sync_curls_history.json` | Log JSON con los últimos 500 registros |
| `/var/www/html/sync-dashboard/index.php` | Dashboard web |

---

## Endpoints sincronizados (en orden)

| # | Método | Endpoint |
|---|--------|---------|
| 1 | POST | `http://localhost:8097/v4/syncUp/items` |
| 2 | PATCH | `http://localhost:8097/v4/syncUp/items` (price, freeShipping, etc.) |
| 3 | PATCH | `http://localhost:8097/v4/syncUp/resellers` |
| 4 | PATCH | `http://localhost:8097/v4/syncUp/rankingVendedores` |
| 5 | PATCH | `http://localhost:8097/v4/syncUp/itemsRanking` |

Ciclo: ~25 min de ejecución + 35 min de sleep = 1 hora.

---

## Infraestructura

- Puerto 8097 → contenedor Docker `sitio-api-rest-4.1-laravel` (Laravel v4)
- Worker: `sitio-api-rest-worker` — tuvo 152+ reinicios en algún momento, monitorear
- Apache2 en host corre el dashboard PHP

---

## Dashboard

URL: `http://localhost/sync-dashboard/` — auto-refresh cada 30 segundos.

---

## Comportamiento de notificaciones

- **Errores:** disparan `notify-send` con urgency critical
- **Éxitos:** solo al journal y al JSON (sin notificación de escritorio)

---

## Comandos útiles

```bash
# Estado
systemctl --user status sync-curls.service

# Reiniciar
systemctl --user restart sync-curls.service

# Logs en tiempo real
journalctl --user -u sync-curls.service -f

# Historial JSON (últimos 10)
cat /tmp/sync_curls_history.json | jq '.[-10:]'
```

---

## Ver también

- [[hermess-pc/arquitectura]]
- [[hermess-pc/hermess-pc|Índice]]
