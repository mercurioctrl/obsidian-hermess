# 07 — Timbre / Portero Dahua VTO → Telegram

Portero de villa (doorbell) Dahua con cámara. Detecta movimiento y avisos de llamada, y manda una **foto a Telegram** mediante un servicio propio en `hermess-desktop`. Es el mismo equipo que figura como **CH6 "PORTERO"** en el [[04-dvr-dahua|DVR Dahua]].

## Datos del equipo

- **Modelo:** Dahua **DHI-VTO2101E-P-S1** (portero PoE, cámara 352×288, chip HI3516CV200)
- **Firmware:** 4.400 (2019-10-19)
- **IP:** `10.10.10.102` (hoy por **DHCP** — pendiente fijar en el USG)
- **MAC:** `6c:1c:71:f1:28:28`
- **Usuario:** `admin` · pass en gestor de contraseñas
- **API:** CGI con **digest auth** (`snapshot.cgi`, `eventManager.cgi`, `configManager.cgi`) + RPC2

## Capacidades relevadas (agosto 2025)

- Detección de movimiento **activada** (grilla completa 24/7, Level 6), pero **el equipo NO tiene SMTP/Email** (tabla Email = *Bad Request*) ni ranura SD → no puede mandar mail nativo. FTP sería posible vía tabla NAS.
- **Snapshot funciona en `channel=1`** (channel=0 da HTTP 400).
- ⚠️ **El VTO NO publica el movimiento por evento.** Aunque `MotionDetect.Enable=true`, **no emite `VideoMotion`** por `eventManager.cgi` (confirmado con minutos de escucha: solo salen `TimeChange` y `SIPRegisterResult`). Por eso el movimiento **se detecta del lado del server** (polling + OpenCV), no por suscripción.

## Solución implementada (Opción B — servicio systemd)

Servicio `vto-timbre` en `hermess-desktop`: `/home/hermess/scripts/vto-timbre/` (`vto_telegram.py`, `config.env` con perms 600, unit systemd `enabled`+`active`, User=hermess). **Dos hilos en paralelo:**

### Hilo MOVIMIENTO (plan B — pull con OpenCV)
- El **script sondea** al VTO (pull): `GET snapshot.cgi?channel=1` (800×480) cada `POLL_INTERVAL`=**1.5s** (~40 fotos/min, ~2400/h, JPEG chico, tráfico solo LAN). El VTO es **pasivo**.
- Compara frames (GaussianBlur + absdiff + threshold 25 + dilate + contours). Umbral `MOTION_MIN_AREA`=1500 px (ruido en reposo ~82px).
- **99.9% de las fotos se descartan al instante**; solo va a Telegram la del momento con movimiento.
- **Dos filtros anti-falsos** (se agregaron porque tomaba autos de la calle a toda velocidad):
  - `MOTION_CONSEC`=2 → exige 2 frames consecutivos con movimiento (filtra autos rápidos, que aparecen en un solo frame).
  - `MOTION_ROI` → polígono que vigila **solo la vereda de adelante** e ignora la calle con tráfico y los árboles. Encuadre: columna de ladrillo + puerta a la izq, vereda abajo (zona vigilada), calle al medio/derecha (ignorada). Coords de referencia 800×480, se auto-escala.

### Hilo EVENTOS (botón del timbre — push)
- Al revés que el movimiento: el **VTO empuja** por el stream `eventManager.cgi?action=attach&codes=[All]` y el script queda escuchando.
- Dispara ante cualquier evento no listado en `IGNORE_CODES` (ruido: TimeChange, SIPRegisterResult, NTPAdjustTime…) con `action != Stop`. Sirve para el botón de llamada.
- ⚠️ El stream llega en **bytes**: hay que decodificar antes de `startswith` (bug arreglado).

## ¿Dónde se configura la "zona muerta" del movimiento?

**No está en el front del VTO ni en el NVR/DVR.** Es el polígono `MOTION_ROI` en `config.env`. No hay UI ni heatmap visual.

- **Cambiarla:** editar `MOTION_ROI` en `/home/hermess/scripts/vto-timbre/config.env` → `sudo systemctl restart vto-timbre`.
- Valor actual: `[[0,480],[0,345],[260,320],[560,400],[800,470],[800,480]]`.
- Para verla gráficamente se regenera un frame con el polígono dibujado (tipo `frame_roi_propuesta.jpg`).

## Telegram

- Bot `@Nmedina87bot` (id 8949822424) · `TG_CHAT_ID=1019202411`. Token y chat_id en `config.env` (perms 600).
- Ante movimiento o botón → `sendPhoto` con la foto del momento; si no hay imagen, `sendMessage`.
- `DEBOUNCE_SEC`=30 por vía para no spammear.

## Disparo de llamada por API (no logrado)

Con RPC2 (login digest MD5) se ve que `VideoTalkPeer.invite` **existe** (da "Invalid Request", es factory service) pero reconstruir sus params de sesión VideoTalk es un pozo. **No se logró hacer sonar el timbre por API** — el botón físico sigue siendo la prueba real.

## Gestión

- Ver logs: `journalctl -u vto-timbre -f`
- Reiniciar: `sudo systemctl restart vto-timbre` — **NO** usar `pkill -f eventManager.cgi` (mata la propia shell).
- Probado end-to-end: llega la foto. ROI probado OK por el usuario (agosto 2025).

## ⚠️ Pendientes

- [ ] Confirmar el **código exacto del botón** (capturar en vivo un toque real) para asignarle la etiqueta "Llaman al timbre" (hoy cae en genérico).
- [ ] **Fijar IP** en el USG (hoy DHCP) y evaluar **bloqueo de salida a WAN** (como el resto de cámaras/grabadores).
- [ ] Opcional: explorar email nativo vía el servicio RPC `SmtpClient` (sin explorar).

## Ver también

- [[04-dvr-dahua]] — el VTO se graba como CH6 "PORTERO"
- [[02-camaras]] — inventario de cámaras IP del hogar
- [[Red]] — infraestructura de red hogareña
