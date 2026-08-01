# 08 — Home Assistant + Teclas Tuya (LocalTuya)

Servidor de domótica del hogar. Corre en **Docker** en `hermess-desktop` (`10.10.10.7:8123`). No confundir con el controlador UniFi, que está en la misma IP pero en `:8443` (ver [[Red]]).

## Datos del servidor

- **Cómo corre:** contenedor Docker `home-assistant` (imagen oficial `ghcr.io/home-assistant/home-assistant:stable`), **HA 2025.12.5**.
- **Config (en el host):** `/home/hermess/homeassistant/config` → montado en `/config`. Dueño root:root, escribible con sudo. Proceso adentro: `python3 -m homeassistant --config /config` como root.
- **Location** "Casa", TZ `America/Buenos_Aires`.
- **Reiniciar:** `sudo docker restart home-assistant` (esperar con `curl --retry ... --retry-connrefused`; el `sleep` en foreground está bloqueado en este entorno).

## Acceso por API REST (token)

User del propio HA: `hermess` / clave en gestor de contraseñas. La API REST necesita **Bearer token**, que se saca por el flujo de login en 3 pasos (token dura 30 min, `client_id = http://10.10.10.7:8123/`):

1. `POST /auth/login_flow` `{client_id, handler:["homeassistant",null], redirect_uri}` → `flow_id`
2. `POST /auth/login_flow/{flow_id}` `{client_id, username, password}` → `result` (código)
3. `POST /auth/token` (form) `grant_type=authorization_code&code=<result>&client_id=<cid>` → `access_token`

Después: `GET /api/states`, `POST /api/services/<dom>/<srv>`, config flows en `/api/config/config_entries/flow` y `/options/flow`, etc. Para uso frecuente conviene un **Long-Lived Access Token** (Perfil en la UI web) guardado en un config.env 600.

## Entidades

- **10 luces WiZ** RGBW (JARDIN x5, PATIO x4, una `fa33ac` unavailable) — OUI `6c:29:90:6d:xx`, integración `wiz`.
- **13 teclas Tuya/Macroled** (ver abajo) → **24 entidades `switch`**, control local.
- **6 escenas Tuya** (escalera/vestidor), TV `media_player.samsung_q70_85_tv` (dlna), `weather.forecast_casa`, `todo.lista_de_la_compra`, `person.hermess`, TTS, 15 sensores.

## Teclas Tuya/Macroled por LocalTuya (control local, sin nube) ✅

Las teclas inteligentes de las luces (marca Macroled = chip Tuya) se integraron con **control 100% local por LAN** (puerto 6668), sin depender de la nube ni de internet. Están en la red IoT `nexus-lot` (ver [[Red]]).

**LocalTuya:** fork mantenido `xZetsubou/hass-localtuya` v2026.07.0, instalado en `config/custom_components/localtuya`. Config entry con credenciales cloud (region `us` = Western America, client_id `hfw3rnhvfrrkvcasvge7`, user_id `az178561179392196nB3`).

### El proceso que funcionó (para repetir/sumar teclas)

1. **Proyecto Tuya IoT gratis** en iot.tuya.com. ⚠️ **Data Center = Western America** (Argentina va ahí, aunque la cuenta diga "Argentina"; no hay DC "Argentina"). Hubo que **habilitar ese DC en el proyecto** y **linkear la app SmartLife por QR** con **Western America seleccionado arriba a la derecha** del modal. El QR expira en ~1-2 min: escanear y confirmar rápido. La cuenta IoT (nueva, vacía) ≠ la cuenta SmartLife del celular (donde viven las teclas) — el QR "trae" la del celu.
2. **`tinytuya` 1.20.0** (venv `/home/hermess/scripts/tuya-tools/venv`): con client_id/secret/region baja **id + local_key** de cada tecla (`c.getdevices()`). `tinytuya.deviceScan()` mapea id→IP+versión de protocolo. Scripts en `/tmp/tuya_*.py`, datos en `/tmp/tuya_full.json`.
3. **Agregar a HA:** config flow de LocalTuya → paso `user` (region/client_id/client_secret/user_id) → options → `add_device` con **`mass_configure=true`** (auto-detecta DPs y entidades). Agregó 11 de 13.
4. Las **2 de protocolo v3.5** (`balcón lavadero` .103, `Lavadero frente` .93) fallaron el DP-query por timing; se **inyectaron a mano** en `.storage/core.config_entries` **con HA detenido**, copiando la plantilla de un device ya configurado y cambiando device_id/host/local_key/protocol_version/friendly_name. Backup: `.storage/core.config_entries.bak_pre_lavadero`.

### Las 13 teclas (switches `kg` multi-gang)

| Tecla | IP | Teclas | Proto |
|---|---|---|---|
| Luces de calle | 10.10.10.46 | 2 | 3.3 |
| Galería B | 10.10.10.35 | 2 | 3.4 |
| luces y cámara jardín | 10.10.10.36 | 2 | 3.4 |
| GALERIA VENTANA A | 10.10.10.37 | 1 | 3.4 |
| Galería ventana A | 10.10.10.42 | 1 | 3.4 |
| Luces Comedor | 10.10.10.33 | 3 | 3.4 |
| Vestidor (arriba) | 10.10.10.22 | 2 | 3.4 |
| ESCALERA / VESTIDOR (abajo) | 10.10.10.24 | 2 | 3.4 |
| habitación | 10.10.10.25 | 2 | 3.4 |
| Patio | 10.10.10.26 | 2 | 3.4 |
| OFICINA | 10.10.10.18 | 2 | 3.4 |
| balcón lavadero | 10.10.10.103 | 1 | 3.5 |
| Lavadero frente | 10.10.10.93 | 2 | 3.5 |

Cada gang = `switch.<nombre>_switch_N` + entidades extra (timer/number DP 7-9, power-on/select DP 14, modo relay/select DP 15). DPs: 1/2/3 = teclas.

### Notas

- El **proyecto Tuya IoT ya no se usa** — se puede borrar, las keys quedan locales en HA. Si se resetea/re-empareja una tecla, cambia su key y hay que re-extraer.
- Hay **2 dispositivos Tuya extra** en la red (`10.10.10.27`, `10.10.10.219`) que **NO** están en la cuenta SmartLife — sin identificar, no tocados.

## Ver también

- [[Red]] — infraestructura de red hogareña (domótica Tuya/WiZ en `nexus-lot`)
- [[02-camaras]] · [[04-dvr-dahua]] · [[07-timbre-vto-telegram]]
