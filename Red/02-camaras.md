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
**Credenciales:** admin / (ver gestor de contraseñas)  
**IP:** 10.10.10.64  
**Ubicación:** apunta a la calle/vereda y a la entrada del edificio ("puerta")

Tiene **6 presets** (no renombrables), todos mirando la misma escena con distinto zoom/encuadre. Preset 6 = vista amplia de la calle (posición "park"). Es una cámara aparte del NVR (ver memoria [[memoria]]).

> 📼 También se graba en el **DVR Dahua** en **CH9** (movida desde CH11 el 2026-07-26). Ver [[04-dvr-dahua]].

### Sesión de configuración (2026-07-25) — patrullaje "enfoque B"

Configurada para quedar fija en la puerta la mayor parte del tiempo y hacer barridos cortos periódicos:

| Paso | Preset | Permanencia |
|---|---|---|
| 1 | 1 | 15 s |
| 2 | 3 | 15 s |
| 3 | 4 | 15 s |
| 4 | 5 | 15 s |
| 5 | 6 (vista amplia — park) | 180 s (3 min) |

→ Barre P1/P3/P4/P5 (~1 min) y después queda **3 min fija en el preset 6** (el barrido va primero para que el descanso quede en la vista amplia). **Auto-inicio programado 00:00 y 12:00.**

### ⚠️ OneTimePatrol = una sola pasada → cron para el loop

El patrullaje de este modelo hace **UNA pasada y se detiene** (no hace loop nativo; el schedule solo admite 2 horarios/día). Para loop continuo hay un **cron en hermess-desktop**:

- Script: `~/.local/bin/ptz-puerta-loop.sh` — cada 1 min: si `SearchOneTimePatrolStatus` = `stopped` → `StartOneTimePatrol`. Log en `/tmp/ptz_puerta_loop.log`.
- Cron: `* * * * * /home/hermess/.local/bin/ptz-puerta-loop.sh`

Sin este cron, la cámara barre una vez y se queda quieta en el preset 6.

### API de esta cámara (ISAPI JSON) — importante

Este modelo de consumo **NO** soporta el patrol clásico (`maxPatrolNum=0`, los PUT a `/patrols/1` se ignoran) ni `timeTasks` (Device Error). Su API real usa **`?format=json`** con endpoints **capitalizados**:

- `GET/PUT /ISAPI/PTZCtrl/channels/1/OneTimePatrolParam?format=json` — pasos del barrido (`presetID` / `seqSpeed` 1-7 / `delay` 15-3600 s, 2-16 pasos)
- `GET/PUT /ISAPI/PTZCtrl/channels/1/OneTimePatrolScheduleParam?format=json` — horarios de auto-inicio (máx 2)
- `PUT /ISAPI/PTZCtrl/channels/1/StartOneTimePatrol` y `/StopOneTimePatrol` (body `{"patrolID":1}`)
- `POST /ISAPI/PTZCtrl/channels/1/SearchOneTimePatrolStatus?format=json` → `{"patrolStatus":"running"}`
- Snapshot: `GET /ISAPI/Streaming/channels/101/picture`
- Auth **digest**. El schedule **no** se puede modificar con el patrullaje corriendo (`TOUR_BUSY`): hay que **Stop → PUT schedule → Start**.

### Cómo tocarlo

- **Pausar/reanudar:** botón ■/▶ del *Inspection Path* en la UI web (`10.10.10.64`), o `Stop/StartOneTimePatrol`.
- **Cambiar tiempos/presets:** Configuration → PTZ → Inspection Path, o PUT a `OneTimePatrolParam`.

### Sin seguimiento automático (auto-tracking)

Este modelo **no soporta** auto-tracking (seguir gente que pasa). El endpoint `/ISAPI/PTZCtrl/channels/1/moveAutoTracking` devuelve `notSupport` (`SW_AUTO_TRACK_SUP` / `SW_AUTO_TRACK_VMD_SUP not support`); tampoco tiene EPTZ auto-track. Para seguimiento haría falta otro modelo (PTZ con Smart Tracking de fábrica) o Master-Slave con 2 cámaras (una fija que detecta + una PTZ que sigue). Además el auto-tracking es el uso que **más desgasta** el motor PT.

## Ver también

- [[Red]] — Infraestructura de red hogareña
