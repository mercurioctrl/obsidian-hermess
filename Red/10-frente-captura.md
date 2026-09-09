# 10 — FRENTE (CCTV) → Telegram

Servicio que **manda una foto a Telegram por detección de movimiento** en las dos cámaras analógicas del frente. Mismo esquema que el [[07-timbre-vto-telegram|timbre]] y el [[02-camaras#Avisos a Telegram en cada reposo (servicio `ptz-captura`, 2026-08-15)|ptz-captura]]. **Agregado 2026-09-08.**

## Qué cámaras son

**FRENTE DER** y **FRENTE IZQ** son las **analógicas CH1 y CH2 del [[04-dvr-dahua|DVR Dahua HCVR]]** (`10.10.10.101`), **no** cámaras IP con dirección propia. Se leen por el DVR:

- Snapshot: `GET /cgi-bin/snapshot.cgi?channel=1` (FRENTE DER) / `channel=2` (FRENTE IZQ) — auth **digest**, user `herrmess87`.
- Resolución: **352×240**. El OSD de CH2 tiene el typo **"FRENE IZQ"**.
- Encuadre: CH1 mayormente la vereda; CH2 la entrada/pared izquierda + algo de calle.

## Cómo detecta (OpenCV del lado del server)

El HCVR OEM viejo **no publica `VideoMotion` por `eventManager.cgi`** (probado: ni siquiera manda heartbeat con `codes=[All]`), aunque `MotionDetect[0]/[1].Enable=true`. Igual que el VTO. Por eso la detección se hace **por polling + OpenCV**, un hilo por cámara:

- Baja snapshot cada `POLL_INTERVAL`=**1.5 s**, frame-diff (GaussianBlur + absdiff + threshold 25 + dilate + contours).
- Umbral `MOTION_MIN_AREA`=**500 px** (referencia 352×240), `MOTION_CONSEC`=**2** frames consecutivos, `DEBOUNCE_SEC`=**30 s** entre avisos de la misma cámara.
- **ROI por cámara** soportado (campo `roi` en `CAMERAS`), pero **arranca vacío = toda la imagen**. ⚠️ Pendiente afinar ROI si de día el tráfico de la calle genera falsos positivos (como se hizo en el timbre).

## Ubicación y archivos

`/home/hermess/scripts/frente-captura/`:

- `frente_telegram.py` — un hilo `motion_loop` por cámara.
- `config.env` (perms 600) — `DVR_HOST/USER/PASS`, `CAMERAS` (JSON), umbrales, `DRY_RUN`.
- `frente-captura.service` — systemd, `enabled`, `User=hermess`.

**Telegram:** reusa `TG_TOKEN` / `TG_CHAT_ID` del timbre — el `.service` carga **dos** `EnvironmentFile`: primero `vto-timbre/config.env` (credenciales del bot) y luego el propio `frente-captura/config.env`.

## Detalles clave (costaron)

- ⚠️ **El HCVR cierra conexiones** (`RemoteDisconnected`) si dos hilos abren conexión nueva cada vez → se usa **una `requests.Session` compartida (keep-alive) + un lock global que serializa** los pedidos al DVR. Sin eso fallaba casi todo snapshot.
- ⚠️ **`CAMERAS` en `config.env` va entre comillas simples** (`CAMERAS='[{"channel":"1",...}]'`): sin comillas, `source` en bash se come las comillas dobles y el JSON queda inválido. systemd lo parsea OK igual.
- `DRY_RUN=1` = no manda a Telegram, solo loguea (para calibrar umbrales). Producción = `DRY_RUN=0`.

## Gestión

- Ver en vivo: `journalctl -u frente-captura -f`
- Reiniciar tras cambios: `sudo systemctl restart frente-captura`
- Deps: `cv2` + `requests` (ya instalados, los usan también el timbre y ptz-captura).

Probado end-to-end el 2026-09-08: foto de prueba llegó a Telegram, detección OK sin errores de conexión.

## Ver también

- [[04-dvr-dahua]] — DVR donde están las analógicas CH1/CH2
- [[07-timbre-vto-telegram]] — mismo esquema (y de ahí salen las credenciales del bot)
- [[02-camaras#Avisos a Telegram en cada reposo (servicio `ptz-captura`, 2026-08-15)|ptz-captura]] — el otro servicio de fotos por movimiento
- [[Red]] — Infraestructura de red hogareña
