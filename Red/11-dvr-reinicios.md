# 11 — DVR: se reinicia solo (diagnóstico 2026-09-16)

Diagnóstico de los reinicios espontáneos del [[04-dvr-dahua|DVR Dahua HCVR]] (`10.10.10.101`) y el monitor que se dejó para medirlos. **Test A/B en curso — ver [[#Estado: test A/B en curso]].**

## Los dos tipos de reinicio

El DVR loguea `System.ShutDown` + `System.StartUp`, y el campo **`Flag` del StartUp es el que distingue todo**:

| Flag | Qué es | Cuándo | Fuera de línea |
|---|---|---|---|
| **0** | Reinicio **programado** (auto-mantenimiento) | Todos los días **05:00** | ~50 s |
| **1** | Arranque **anormal** | A cualquier hora | ~50 s o ~3 min 50 s |

El programado sale de la config `AutoMaintain`, que venía de fábrica:

```json
{"AutoRebootDay": 7, "AutoRebootHour": 5, "AutoRebootMinute": 0}
```

`AutoRebootDay: 7` = **todos los días**. Se cambia por RPC2 con `configManager.setConfig {"name":"AutoMaintain"}`. No es una falla; conviene dejarlo (le limpia la memoria a un equipo de 2016).

## Los anormales: cuándo empezaron

Del **18-ago al 8-sep no hubo ninguno** (solo los de las 05:00). Arrancaron el **2026-09-09 19:56** y siguieron:

```
09-09 19:56  (3m49s)      09-14 09:15  (50s)
09-10 00:54  (49s)        09-15 00:09  (48s)
09-10 15:55  (52s)        09-15 22:24  (3m52s)
09-12 22:30  (51s)        09-16 12:45  (51s)
09-14 01:11  (3m49s)      09-16 13:45  (3m48s)
09-14 02:23  (51s)
```

**11 en 7 días**, ~1,6 por día, a cualquier hora.

## NO es corte de energía — es cuelgue de firmware (watchdog)

La primera hipótesis fue la fuente 12V. **Es incorrecta**, por tres pruebas:

1. **El reloj no se pierde.** La pila RTC de la placa está agotada: en los cortes de luz reales (**09-03 16:09** y **09-07 09:37**, donde la PC también reinició) el DVR volvió con fecha `2000-01-01` hasta que NTP lo corrigió — queda en el log como `System.SetCurrentTime` con `Before: 2000-01-01`. En los **11 reinicios recientes el reloj vuelve correcto** → la placa nunca perdió alimentación.
2. **Un segundo después del cuelgue el DVR contesta `Connection refused`** (RST), o sea que el stack de red sigue vivo: se murió la aplicación, no la corriente. Recién después vienen los timeouts (reboot real) y otra vez refused mientras bootea:

```
12:45:26  último heartbeat del DVR
12:45:27  RemoteDisconnected
12:45:27  [Errno 111] Connection refused   ← la placa está energizada
12:45:40  connect timeout                  ← acá reinicia la red
12:45:55  Connection refused               ← booteando, puerto cerrado
12:46:17  System.StartUp Flag:1
```

3. **Nada más se cae** en esas ventanas: ni los APs/USG (log del controlador UniFi), ni la PC (uptime continuo), ni las cámaras IP — en el log del DVR las cámaras `.64 .65 .192 .102 .216` vuelven a `Online` recién *después* del boot, nunca se caen antes.

El delta de ~3m50s se explica solo: el equipo **queda tildado ~3 minutos** y recién ahí el watchdog lo resetea (el `Time` del `ShutDown` es el último heartbeat que alcanzó a escribir en flash). Los de ~50 s son cuelgues que el watchdog agarró enseguida — 50 s es lo que tarda en bootear.

**Calor:** descartado como disparador principal. Hay cuelgues a las **00:09, 01:11 y 02:23**, las horas más frescas. Además este modelo **no expone sensor de temperatura** (`magicBox.getTemperature` devuelve `result:false`), así que no hay forma de medirlo por API. Puede sumar margen —equipo de 2016, con disco, 24/7— pero no explica el patrón.

## Sospechoso principal: la carga del poller

```
2026-09-08 20:50   se instala y arranca frente-captura.service
2026-09-09 19:56   primer cuelgue
(3 semanas previas: cero cuelgues)
```

[[10-frente-captura]] pollea `snapshot.cgi` cada **1,5 s × 2 canales** ≈ **115.000 requests HTTP por día** contra un HCVR con firmware build **2016-04-27**. Y ya venía dando señales: **40 a 400 warnings de snapshot fallado por día**, muchos fuera de las ventanas de reinicio. El propio código lo advierte: *"el HCVR OEM maneja mal las conexiones concurrentes/nuevas"* (por eso usa sesión keep-alive + lock).

## Estado: test A/B en curso

**Desde 2026-09-16 15:01**, `frente-captura` está **parado y deshabilitado**:

```bash
sudo systemctl stop frente-captura
sudo systemctl disable frente-captura     # para que un reboot de la PC no lo levante
```

Se deshabilitó además de pararlo porque la PC reinició dos veces esta semana y un `Restart=always` habría invalidado el test en silencio.

- **Ventana:** hasta el **2026-09-18 ~15:00** (48 h).
- **Esperado si el poller es la causa:** cero `Flag:1`. Al ritmo previo deberían aparecer ~3.
- **Verificar:** `python3 ~/scripts/dvr-reinicios.py 3`
- **Revertir:** `sudo systemctl enable --now frente-captura`

> ⚠️ Mientras dura el test **no llegan los avisos de movimiento del frente** a Telegram. El timbre ([[07-timbre-vto-telegram]]) y la PTZ siguen andando: apuntan a `.102` y `.64`, no tocan el DVR.

**Si el test da positivo** (cero cuelgues), dos arreglos posibles para [[10-frente-captura]]:

1. **Rápido:** subir `POLL_INTERVAL` de 1,5 s a 4-5 s (un tercio de la carga; se pierde algo de sensibilidad con `MOTION_CONSEC=2`).
2. **Bien:** pasar a **una conexión RTSP persistente** por canal en vez de polling HTTP — una sesión abierta en lugar de 115 mil conexiones nuevas por día. Es lo que mejor tolera este DVR viejo.

**Si da negativo** (se sigue colgando sin el poller), el poller queda descartado y toca hardware: limpieza de rejillas/ventilación, fuente 12V y pila RTC.

## Servicio `dvr-monitor` (avisos de reinicio a Telegram)

Monitor dejado corriendo el **2026-09-16 15:07** para medir el test sin estar mirando el log a mano.

`/home/hermess/scripts/dvr-monitor/`:

- `dvr_monitor.py` — loop principal.
- `config.env` (perms 600) — `DVR_HOST/USER/PASS`, `CHECK_INTERVAL=30`, `FAILS_TO_DOWN=2`, `STILL_DOWN_SEC=300`, `NOTIFY_SCHEDULED=1`, `NOTIFY_START=1`, `DRY_RUN`.
- `/etc/systemd/system/dvr-monitor.service` — `enabled`, `User=hermess`.

**Cómo funciona (y por qué así):** sonda **TCP al puerto 80 cada 30 s** — un handshake, **sin login**. Es deliberado: el monitor no puede sumar carga al DVR, que es justamente la hipótesis bajo prueba. Recién cuando lo ve **caer y volver**, hace **un** login RPC2 y lee el log para saber el `Flag` del arranque:

- `Flag:0` → 🔁 **PROGRAMADO** (05:00). Llega uno por día y sirve de latido del monitor.
- `Flag:1` → 🚨 **ANORMAL**, con tiempo fuera de línea y las horas exactas del log.
- Si se cae y **no vuelve en 5 min** → ⚠️ aviso aparte.

Espera 15-20 s antes de leer el log (el DVR abre el 80 antes de aceptar RPC) y reintenta 3 veces.

**Telegram:** mismo esquema que [[10-frente-captura]] y el [[07-timbre-vto-telegram|timbre]] — el `.service` carga **dos** `EnvironmentFile`: primero `vto-timbre/config.env` (credenciales del bot) y luego el propio.

**Gestión:**

```bash
journalctl -u dvr-monitor -f              # en vivo
sudo systemctl restart dvr-monitor        # tras cambios en config.env
# NOTIFY_SCHEDULED=0 en config.env = no avisar el reinicio diario de las 05:00
```

## Script `dvr-reinicios.py`

`~/scripts/dvr-reinicios.py [dias]` (default 7) — lista los reinicios separando **programados (`Flag:0`)** de **anormales (`Flag:1`)**, con hora de caída y de vuelta. Es la forma rápida de ver el resultado del test.

## Cómo leer los logs del DVR por RPC2

```
log.startFind {"condition":{"Type":"All","StartTime":"...","EndTime":"..."}}  → token
log.doFind    {"token":..., "count":100}    en loop hasta que devuelva vacío
log.stopFind  {"token":...}
```

⚠️ Tres trampas que costaron:

- Devuelve **en orden cronológico desde el inicio de la ventana**, no los más nuevos primero. Para ver lo último hay que **acotar la ventana**, no paginar desde atrás.
- El DVR **corta la conexión** (`RemoteDisconnected`) si se le piden muchos miles de registros seguidos → consultar **de a un día**.
- `doFind` puede devolver **menos de `count`** y seguir teniendo datos: cortar solo con **lista vacía**, nunca con `len(items) < count`.
- Los `Account.LogIn`/`LogOut` del poller **tapan el log**: el 7-8 de septiembre hubo ~8.400 entradas en 6 h y no dejaban ver nada más.

## ⚠️ Pendientes

- [ ] **2026-09-18 ~15:00 — leer el resultado del test A/B** (`python3 ~/scripts/dvr-reinicios.py 3`) y decidir: bajar carga del poller o ir por hardware
- [ ] Volver a habilitar [[10-frente-captura]] cuando termine el test (con `POLL_INTERVAL` más alto o con RTSP persistente)
- [ ] **Pila RTC de la placa agotada** — cada corte de luz real le borra la hora hasta que engancha NTP. Cambiar la CR2032 cuando se abra el equipo
- [ ] Limpieza física de rejillas/ventilación (equipo de 2016, 24/7, con disco)

## Ver también

- [[04-dvr-dahua]] — el DVR: datos, API RPC2 y mapeo de canales
- [[10-frente-captura]] — el servicio bajo sospecha (parado durante el test)
- [[07-timbre-vto-telegram]] — mismo esquema de avisos a Telegram (y de ahí salen las credenciales del bot)
- [[Red]] — Infraestructura de red hogareña
