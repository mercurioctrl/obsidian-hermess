# Sync Curls — Proceso de sincronización periódica

## Descripción

Script bash que corre en loop infinito ejecutando curls de sincronización contra la API local cada ~1 hora. Notifica via `notify-send` tanto los errores (urgencia crítica) como los éxitos (urgencia baja, con el body de respuesta).

**Script:** `/var/www/sync_curls.sh`  
**Log:** `/tmp/sync_curls_history.json` (últimos 500 registros)  
**API local:** `http://localhost:8097` (Docker, container en `172.24.0.4:80`)

## Estado actual (2026-05-08)

- Corriendo como proceso bash suelto (PID 8945, levantado may06)
- **Pendiente:** convertir a systemd service con `Restart=always`
- Unit file preparado en `/tmp/sync-curls.service`

## Secuencia de curls por ciclo

| Orden | Método | Endpoint | Intervalo post-ejecución |
|---|---|---|---|
| 1 | POST | `/v4/syncUp/items` | 5 min |
| 2 | PATCH | `/v4/syncUp/items` | 5 min |
| 3 | PATCH | `/v4/syncUp/resellers` | 5 min |
| 4 | PATCH | `/v4/syncUp/rankingVendedores` | 5 min |
| 5 | PATCH | `/v4/syncUp/itemsRanking` | 35 min (completa la hora) |

Ciclo total: ~60 minutos.

El PATCH de items sincroniza los campos: `price`, `freeShipping`, `instantFlash`, `discount`, `sellerName`, `sellerId`, `description`, `image`, `keywords`, `brandId`.

## Notificaciones

- **Error:** `notify-send` urgencia crítica — título del error o código HTTP
- **Éxito:** `notify-send` urgencia baja — JSON del `data.summary` (truncado a 200 chars)
- Usa `DISPLAY=:0` para funcionar desde systemd sin sesión gráfica

## Conversión a systemd

```bash
sudo kill 8945
sudo cp /tmp/sync-curls.service /etc/systemd/system/sync-curls.service
sudo systemctl daemon-reload
sudo systemctl enable --now sync-curls
sudo systemctl status sync-curls
```

Contenido del unit:

```ini
[Unit]
Description=Sync Curls Libre Opción
After=network.target docker.service
Requires=docker.service

[Service]
Type=simple
ExecStart=/bin/bash /var/www/sync_curls.sh
Restart=always
RestartSec=10
User=hermess
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

## Ver también

- [[stack|Stack]]
- [[arquitectura|Arquitectura]]
