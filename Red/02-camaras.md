# 02 — Cámaras IP

## Inventario

| Nombre | IP | MAC | Modelo | Conexión | AP / Puerto |
|---|---|---|---|---|---|
| Ezviz (exterior) | 10.10.10.43 | 98:f1:12:3f:f0:a6 | Ezviz (Hikvision) | WiFi | AP Galeria |
| PASILLO-C | 10.10.10.192 | 18:68:cb:d0:df:21 | DS-2CD1001-I | Cable | Switch (no administrado) |
| PUERTA PTZ | 10.10.10.64 | — | DS-2CV1F23G2-LIDWF (WiFi PT ColorVu) | WiFi | — |

---

## Cámara PASILLO-C — DS-2CD1001-I

**Modelo:** Hikvision DS-2CD1001-I (1MP, 2017)  
**Firmware:** V5.4.5 build 170208  
**Credenciales:** admin / (ver gestor de contraseñas)  
**IP:** 10.10.10.192 (estática, máscara /23)

### Problema: imagen se interrumpe cada tanto

**Causa principal — cable degradado:**
- Link negociado a **10Mbps half-duplex** en vez de 100Mbps full-duplex
- Half-duplex genera colisiones cuando hay tráfico simultáneo → cortes de imagen
- Auto-negociación habilitada pero falla por cable dañado, mal crimpado o solo 2 pares activos

**Causa secundaria — RAM al límite:**
- RAM usage: ~93-96% (solo ~2-3 MB disponibles)
- Modelo muy básico con poca RAM de base
- Con 16+ días de uptime acumula memory leaks

### Cambios aplicados

- UPnP deshabilitado (liberaba memoria innecesariamente)
- Multicast deshabilitado en ambos streams (main 101 y sub 102)
- Reboot manual realizado → RAM bajó de 96% a 93%
- **Cron diario 3:40am** configurado en hermess-desktop para reboot automático:
  ```
  40 3 * * * curl -sk --digest -u 'admin:...' -X PUT 'http://10.10.10.192/ISAPI/System/reboot'
  ```

### Configuración de streams

| Stream | Resolución | Codec | Bitrate | FPS |
|---|---|---|---|---|
| Main (101) | 1280×720 | H.264 Main | VBR 512 kbps | 25 |
| Sub (102) | 352×288 | H.264 Main | VBR 256 kbps | 25 |

### ⚠️ Tarea pendiente — reemplazar cable

El cable de red del pasillo necesita ser reemplazado o re-crimpado. Mientras no se cambie, los cortes de imagen van a persistir independientemente de cualquier otra optimización.

**Checklist para resolver:**
- [ ] Revisar el recorrido del cable en el pasillo
- [ ] Probar con un cable de reemplazo temporario para confirmar que es el cable
- [ ] Si es un patch cord: reemplazar directamente
- [ ] Si es cable de pared: re-crimpear o tirar cable nuevo
- [ ] Confirmar que el link queda en 100Mbps full-duplex luego del cambio

---

## Cámara Ezviz (exterior)

**Conexión:** WiFi — debe conectarse siempre a **AP Galeria**  
**Señal actual:** -43 dBm en AP Galeria (antes estaba en AP Oficina con -58 dBm)  
**Retries acumulados:** 387.515 (histórico antes del kick)

### ⚠️ Tarea pendiente — pinear a AP Galeria

UniFi no soporta pinear un cliente a un AP específico de forma nativa. Si la cámara vuelve a migrar a AP Oficina, opciones:

- **Opción recomendada:** crear SSID `nexus-cam` asignado solo a AP Galeria y reconectar la cámara a esa red
- **Alternativa:** kick manual desde el controlador para forzar reconexión (temporal)

---

## Cámara PUERTA PTZ — DS-2CV1F23G2-LIDWF

**Modelo:** Hikvision WiFi PT ColorVu DS-2CV1F23G2-LIDWF (pan-tilt motorizada)  
**Firmware:** V5.8.12  
**Credenciales:** admin / (ver gestor de contraseñas — el cron usa `admin:chanteclair87`)  
**IP:** 10.10.10.64  
**Ubicación:** apunta a la calle/vereda y a la entrada del edificio ("puerta")

Tiene **6 presets de hardware** (no renombrables). **Config actual (ago 2026): solo se usan 2** — preset **1 = Reposo Izquierda** (calle arriba, profundo) y preset **2 = Reposo Derecha** (vereda abajo hacia la esquina) — con barrido lento entre ambos que cubre toda la cuadra. Los presets 3/4/5/6 siguen guardados pero fuera del barrido. Es una cámara aparte del NVR (ver memoria [[memoria]]).

> 📼 También se graba en el **DVR Dahua** en **CH9** (movida desde CH11 el 2026-07-26). Ver [[04-dvr-dahua]].

### Configuración actual (2026-08-15) — barrido 2 reposos + optimización de desgaste

Rediseño total del patrullaje (a raíz de un corte de luz que dejó la cámara aparentemente "quieta"). En vez de 5 presets, ahora hay **2 posiciones de reposo + barrido lento** entre ellas:

| Paso | Preset | Encuadre | Velocidad (`seqSpeed`) | Descanso (`delay`) |
|---|---|---|---|---|
| 1 | 1 (Reposo Izquierda) | calle arriba a la izquierda, profundo | 1 (mínima) | 90 s |
| 2 | 2 (Reposo Derecha) | vereda abajo hacia la esquina | 1 (mínima) | 90 s |

→ Descansa 90s a la izquierda → **barrido lento** cruzando toda la cuadra (ahí "se ve todo") → descansa 90s a la derecha → y de vuelta. El tránsito izq↔der **ES** el barrido. Zoom abierto para que entre toda la calle. Config JSON:

```json
{"patrolList":[{"patrolID":1,"oneTimePatrolParam":[
  {"presetID":1,"seqSpeed":1,"delay":90},
  {"presetID":2,"seqSpeed":1,"delay":90}]}]}
```

**Optimización de desgaste (clave en esta cámara de consumo):** los engranajes son plásticos y **no están hechos para patrullar 24/7**. Se subió el descanso de 25s → **90s** para bajar los barridos de **~1000/día a ~350/día (≈3× menos desgaste)** sin perder cobertura (se refresca cada ~3-4 min). El factor de desgaste #1 es la cantidad de barridos/día; alargar descansos es la palanca más efectiva (más que bajar la velocidad). Con el tiempo puede aparecer juego (backlash) y los reposos correrse un poco → reposicionar con el joystick y volver a guardar.

**Cómo se guardan los reposos:** se posiciona la cámara con el **joystick de la app** (zoom abierto) y se fija la posición ACTUAL por API:
`PUT /ISAPI/PTZCtrl/channels/1/presets/{id}` con body XML `<PTZPreset><enabled>true</enabled><id>N</id><presetName>...</presetName></PTZPreset>`. **Mover el joystick NO cambia un preset**; solo lo cambia un "set preset" explícito (por eso, si un reposo quedó raro, es que se guardó sin querer).

**Límite de pan:** el recorrido hacia la izquierda es corto — al llegar al tope mecánico el `PUT /continuous` devuelve **HTTP 403**.

### Recuperación ante cortes de luz

Tras un corte, cámara y host se reinician. El barrido **se recupera solo**: el cron de relanzado (cada 1 min) lo vuelve a arrancar dentro de ~1 min de que la cámara agarra WiFi. Además se agregó un `@reboot` para adelantar el primer arranque post-boot. La duración del ciclo no importa (definido así con el usuario), por eso descansos largos y sin apuro.

### Avisos a Telegram en cada reposo (servicio `ptz-captura`, 2026-08-15)

Servicio systemd aparte que **manda una foto a Telegram cada vez que la cámara se queda quieta en un reposo** (izquierda / derecha). Reusa el **mismo bot del timbre** (ver [[07-timbre-vto-telegram#Telegram]]).

- **Ubicación:** `/home/hermess/scripts/ptz-captura/` → `ptz_captura.py`, `config.env` (perms 600), `ptz-captura.service` (systemd, `enabled`+`active`, User=hermess). Refs `ref_izq.jpg` / `ref_der.jpg`.
- **No toca el barrido** — es solo-lectura sobre la cámara (snapshots). El sweep lento sigue igual.
- **Cómo detecta el arribo:** sondea `GET /ISAPI/Streaming/channels/101/picture` cada `PTZ_POLL`=2s, compara frames (gris 320×240 + GaussianBlur + `absdiff().mean()`). **Calibrado:** quieto ≈ **1**, paneando ≈ **35–55** → umbral `PTZ_MOVE_DIFF`=**8** (enorme margen; ni un camión en la calle mueve la media). Dispara en la transición **paneando→quieto** (tras `PTZ_STILL_CONSEC`=2 frames quietos → foto sin motion-blur), una sola vez por reposo.
- **Etiqueta 👈izq / 👉der (híbrida):** compara el frame con `ref_izq.jpg` / `ref_der.jpg`; si el margen `|di-dd|` ≥ `PTZ_ANCHOR_MARGIN`=8 confía en la ref (la izquierda siempre da margen amplio), si no usa **alternancia** izq↔der (los reposos alternan siempre). Robusto ante cambios de luz día/noche.
- **Telegram:** reusa `TG_TOKEN` / `TG_CHAT_ID` del timbre — el `.service` carga **dos** `EnvironmentFile`: primero `vto-timbre/config.env` (aporta las credenciales del bot) y luego el propio `ptz-captura/config.env`.
- **⚠️ Volumen:** con descansos de 90s son **~2 fotos cada ~4 min → ~600-700/día**. Dial para bajarlo sin tocar código: `PTZ_MIN_INTERVAL` en `config.env` (segundos mínimos entre avisos; `0` = cada reposo, default).
- **Gestión:** `journalctl -u ptz-captura -f`, `sudo systemctl restart ptz-captura`. Deps: `cv2` + `requests` (ya instalados, los usa también el timbre).

### ⚠️ OneTimePatrol = una sola pasada → cron para el loop

El patrullaje de este modelo hace **UNA pasada y se detiene** (no hace loop nativo; el schedule solo admite 2 horarios/día). Para loop continuo hay un **cron en hermess-desktop**:

- Script: `~/.local/bin/ptz-puerta-loop.sh` — cada 1 min: si `SearchOneTimePatrolStatus` = `stopped` → `StartOneTimePatrol`. Log en `/tmp/ptz_puerta_loop.log`.
- Crontab:
  ```
  * * * * * /home/hermess/.local/bin/ptz-puerta-loop.sh >> /tmp/ptz_puerta_loop.log 2>&1
  @reboot sleep 90 && /home/hermess/.local/bin/ptz-puerta-loop.sh >> /tmp/ptz_puerta_loop.log 2>&1
  ```

Sin este cron, la cámara barre una vez y se queda quieta.

> 💡 Al mandar `StartOneTimePatrol`, `SearchOneTimePatrolStatus` puede reportar `stopped` un instante mientras la cámara transiciona; reconsultar a los pocos segundos confirma `running`.

### API de esta cámara (ISAPI JSON) — importante

Este modelo de consumo **NO** soporta el patrol clásico (`maxPatrolNum=0`, los PUT a `/patrols/1` se ignoran) ni `timeTasks` (Device Error). Su API real usa **`?format=json`** con endpoints **capitalizados**:

- `GET/PUT /ISAPI/PTZCtrl/channels/1/OneTimePatrolParam?format=json` — pasos del barrido (`presetID` / `seqSpeed` 1-7 / `delay` 15-3600 s, 2-16 pasos)
- `GET/PUT /ISAPI/PTZCtrl/channels/1/OneTimePatrolScheduleParam?format=json` — horarios de auto-inicio (máx 2)
- `PUT /ISAPI/PTZCtrl/channels/1/StartOneTimePatrol` y `/StopOneTimePatrol` (body `{"patrolID":1}`)
- `POST /ISAPI/PTZCtrl/channels/1/SearchOneTimePatrolStatus?format=json` → `{"patrolStatus":"running"}`
- `PUT /ISAPI/PTZCtrl/channels/1/presets/{id}/goto` — ir a un preset · `PUT /presets/{id}` (body XML) — guardar posición actual
- `PUT /ISAPI/PTZCtrl/channels/1/continuous` (body XML `<PTZData><pan>±</pan><tilt>±</tilt><zoom>±</zoom></PTZData>`) — movimiento manual; enviar con ceros para frenar. Devuelve **403** al tope de pan.
- Snapshot: `GET /ISAPI/Streaming/channels/101/picture`
- Auth **digest**. El schedule/param **no** se puede modificar con el patrullaje corriendo (`TOUR_BUSY`): hay que **Stop → PUT → Start**.

### Cómo tocarlo

- **Pausar/reanudar:** botón ■/▶ del *Inspection Path* en la UI web (`10.10.10.64`), o `Stop/StartOneTimePatrol`.
- **Cambiar tiempos/presets:** Configuration → PTZ → Inspection Path, o PUT a `OneTimePatrolParam`.
- **Reposicionar un reposo:** joystick de la app hasta la vista deseada → guardar con `PUT /presets/{id}`.

### Sesión de configuración (2026-07-25) — patrullaje "enfoque B" (histórico, reemplazado el 2026-08-15)

Configuración previa: quedaba fija en la puerta la mayor parte del tiempo y hacía barridos cortos periódicos.

| Paso | Preset | Permanencia |
|---|---|---|
| 1 | 1 | 15 s |
| 2 | 3 | 15 s |
| 3 | 4 | 15 s |
| 4 | 5 | 15 s |
| 5 | 6 (vista amplia — park) | 180 s (3 min) |

→ Barría P1/P3/P4/P5 (~1 min) y después quedaba **3 min fija en el preset 6** (el barrido iba primero para que el descanso quedara en la vista amplia). Auto-inicio programado 00:00 y 12:00. **Reemplazado** el 2026-08-15 por el esquema de 2 reposos + barrido lento (ver arriba).

### Sin seguimiento automático (auto-tracking)

Este modelo **no soporta** auto-tracking (seguir gente que pasa). El endpoint `/ISAPI/PTZCtrl/channels/1/moveAutoTracking` devuelve `notSupport` (`SW_AUTO_TRACK_SUP` / `SW_AUTO_TRACK_VMD_SUP not support`); tampoco tiene EPTZ auto-track. Para seguimiento haría falta otro modelo (PTZ con Smart Tracking de fábrica) o Master-Slave con 2 cámaras (una fija que detecta + una PTZ que sigue). Además el auto-tracking es el uso que **más desgasta** el motor PT.

## Ver también

- [[Red]] — Infraestructura de red hogareña
