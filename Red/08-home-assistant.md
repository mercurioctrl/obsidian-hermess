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
- **WiZ = un solo cerebro (HA):** las WiZ del jardín se prendían "solas" a horas raras por un **horario/ritmo en la app WiZ** (nube), en paralelo a las automatizaciones de HA. Se comprobó por prueba controlada que el switch de la calle NO las alimenta (son independientes) → era la app WiZ. Recomendación aplicada: **borrar los horarios de la app WiZ** y dejar HA como único controlador (evita comportamientos fantasma). También conviene poner el "power-on behavior" de las WiZ en Apagado/Último estado. La integración `wiz` de HA es **local** (no depende de la nube).
- **Wabee** (medidor de energía, `10.10.10.44`, MAC `5c:cf:7f:...`, Espressif): **solo-nube**, sin API local → NO integrable localmente como las Tuya. Eventual integración a HA sería vía su nube/API o MQTT (a evaluar). Ver [[Red#Domótica]].
- **Descubrir/integrar WiZ nuevas (método reutilizable):** censo por **UDP `getPilot` puerto 38899** (unicast a las IPs vivas; el broadcast no anda desde este host). Para saber qué WiZ cuelga de un switch: **apagar el switch → las WiZ dejan de responder** = ésas son. Agregar a HA por integración `wiz` (config flow por IP) y nombrar por WS. Así se sumaron: **Balcón atrás x2** (`fa3132 fa2fb0`) y **Comedor x9** ("Comedor 1–9": `6d723e 6d7602 6d6cd6 6d7a36 6d7a78 6d7836 6d6ca0 6d7250 6d5744`, IPs .56–.63/.242).
- **Comedor** (interior): el switch `Luces Comedor` (.33, 3 gangs) alimenta las **9 WiZ**. Están en el dashboard (sección 🍽️ Comedor, gangs marcados "⚡ Aliment."). A diferencia de jardín/patio/balcón, el switch del comedor **sigue en los apagados** (interior); si se quiere control fino por WiZ habría que dejarlo siempre-ON (decisión pendiente del usuario).

## Dashboard "Casa"

Dashboard dedicado en **modo YAML** (`config/dashboards/casa.yaml`, registrado en `configuration.yaml` bajo `lovelace: dashboards: casa-tuya`, URL `/casa-tuya`). El Overview y los demás dashboards (Oficina, Jardin, Mapa) quedaron intactos. Layout `type: sections` por ambiente (Acciones rápidas, Escenas, **Calle**, Jardín/Exterior, Patio, Galería, Comedor, Escalera/Vestidor, Habitación, Oficina, Lavadero): teclas como toggle, WiZ con slider de brillo, 6 escenas, y botones de acción (Apagar todas las luces, Apagar teclas seguro, Buenas noches). Las luces de calle tienen su propia sección "🛣️ Calle" (separada del jardín). El Patio muestra sus 4 WiZ con slider (aparecen recién desde que el switch del patio quedó siempre ON). La sección "🎬 Escenas" se **quitó** (las 6 escenas Tuya de escalera/vestidor quedaron obsoletas con la conmutación por mirror; backup `casa.yaml.bak_pre_quitar_escenas`).

> ⚠️ **Footgun del dashboard:** las tiles de los switches `Patio 1/2` y `Jardín / cámara 1/2` cortan la corriente de las WiZ (y de la cámara) si se tocan. Son alimentación, no deberían operarse. Pendiente/opción: renombrarlas ("no apagar") o sacarlas del dashboard.

## Nombres por tecla — leer de la app SmartLife y aplicar a HA

Cuando se le pone nombre a **cada gang** en la app SmartLife, ese `custom_name` **NO** sale por la API cloud común (`getfunctions`/`getstatus` dan genérico "switch 1/2"). SÍ sale por **`GET /v2.0/cloud/thing/{device_id}/shadow/properties`**. Flujo reutilizable (se irá repitiendo a medida que se bauticen más teclas), **2 comandos**:

```bash
V=/home/hermess/scripts/tuya-tools/venv/bin/python3
$V /home/hermess/scripts/tuya-tools/leer_nombres.py   # lee de la nube → tabla + /tmp/tuya_nombres.json
$V /home/hermess/scripts/tuya-tools/ha_ws.py rename    # aplica a HA en caliente (WebSocket)
```

- `leer_nombres.py` — lee el `custom_name` de cada gang (todas, o `leer_nombres.py <device_id>` para una).
- `ha_ws.py rename` — token por login flow + **WebSocket** `config/entity_registry/update`. Mapea device_id+dp → entity_id por el `unique_id` de LocalTuya, que es `local_<device_id>_<dp>`. Cambia solo el `friendly_name` (**el `entity_id` NO cambia**, no rompe dashboard/rutinas). `ha_ws.py list-localtuya` lista las 24 switch entities. Ojo: si una tile del dashboard tiene `name:` fijo, hay que editarla aparte (pisa el friendly_name).
- **Estado ago 2025:** la única bautizada por gang es **"Lavadero frente"** (.93): `switch_1` = **"Lavadero adentro"**, `switch_2` = **"Frente terraza princ"**. El resto sigue con el nombre del device.

## Rutinas / iluminación automática

Automatizaciones en `automations.yaml` + scripts en `scripts.yaml` (formato nuevo triggers/actions). Backups `*.bak_pre_*` de cada cambio.

**Modelo de exterior — prender al ATARDECER, apagar según zona:**

| Zona | Prende | Apaga |
|---|---|---|
| Luces de calle (1,2) | atardecer (sunset) | amanecer (sunrise) |
| Terraza (`lavadero_frente_switch_2` "Frente terraza princ") | atardecer | amanecer |
| **Jardín — 5 WiZ** (`3f4298`,`3f5fc4`,`6d5a5e`,`6d6eb4`,`6d72a6`) | atardecer | **medianoche (00:00)** |
| **Patio — 4 WiZ** (`afc136`,`afcbd2`,`afcdca`,`afce6a`) | atardecer | **medianoche (00:00)** |
| **Balcón (atrás lavadero) — 2 WiZ** (`fa3132`,`fa2fb0`, IP .246/.247) | atardecer | **medianoche (00:00)** |
| Switch `luces y cámara jardín` (2 gangs) | — **siempre ON 24/7** — | **nunca** |
| Switch `patio` (2 gangs) | — **siempre ON 24/7** — | **nunca** |
| Switch `balcón lavadero` (1 gang, `switch.balcon_lavadero_switch_1`) | — **siempre ON 24/7** — | **nunca** |

- `automation.exterior_prender_al_atardecer` — al sunset: calle (1,2) + jardín/cámara switch (1,2) + patio switch (1,2) + balcón switch (`balcon_lavadero_switch_1`) + terraza + las **11 WiZ** (jardín + patio + balcón).
- `automation.exterior_apagar_al_amanecer` — al sunrise: terraza + calle (1,2).
- `automation.jardin_wiz_apagar_a_medianoche` (alias "Jardin + Patio + Balcon WiZ") — 00:00: apaga las 11 WiZ de jardín, patio y balcón (los switches NO se tocan).
- `automation.apagar_todo_2_am` — 02:00: llama `script.buenas_noches` (barrido de **interior**).
- `script.buenas_noches` — apaga todas las luces + lista SEGURA de teclas. **NO** incluye calle, terraza, jardín/cámara ni patio (para no cortar el exterior ni las cámaras/WiZ). `script.apagar_teclas` (botón manual) tampoco incluye jardín/cámara ni patio.

> 🔌 **SWITCHES SIEMPRE ON (regla dura):** los switches `luces y cámara jardín` (.36, 2 gangs), `patio` (.26, 2 gangs) y `balcón lavadero` (.103, 1 gang, `switch.balcon_lavadero_switch_1`) **alimentan lámparas WiZ** (y el de jardín, además, **la cámara del jardín**). Deben estar **siempre prendidos (24/7)** — NO se apagan en ninguna rutina/script/botón. La **iluminación** de jardín/patio/balcón se maneja con las **WiZ**. Nunca agregar estos switches a un `turn_off`. (Las WiZ de patio y balcón aparecían `unavailable`/sin integrar porque su switch estaba apagado; al dejarlo siempre ON aparecieron. Las 2 del balcón se agregaron a HA por la integración `wiz` — config flow por IP; descubiertas con scan UDP `getPilot` puerto 38899.)

### Conmutación escalera / vestidor (mirror bidireccional)

Dos luces de la zona escalera se controlan desde **abajo** (`switch.escalera_vestidor_abajo_*`, .24) y **arriba** (`switch.vestidor_arriba_*`, .22). El cableado es **paralelo (OR)**: con cualquiera de los 2 gangs en ON la luz prende, así que sin sincronizar no se podía apagar desde el otro extremo. Se resolvió con 2 automatizaciones que mantienen **iguales** los 2 gangs de cada luz (conmutador real).

| Luz | Gang abajo | Gang arriba |
|---|---|---|
| **Escalera** | `escalera_vestidor_abajo_switch_1` | `vestidor_arriba_switch_1` |
| **Vestidor** | `escalera_vestidor_abajo_switch_2` | `vestidor_arriba_switch_2` |

- Automatizaciones `automation.sync_luz_escalera` y `automation.sync_luz_vestidor` (`mode: restart`, acción `switch.turn_{{ trigger.to_state.state }}` sobre ambos gangs; sin bucles). Mapeo confirmado por prueba física (encender un gang a la vez y ver qué luz prendía). Backup `automations.yaml.bak_pre_escalera`.
- Reemplazan a las 6 escenas Tuya viejas (ya sacadas del dashboard).

### Avisos por Telegram

Cada rutina de exterior avisa por Telegram al **mismo bot del timbre** (`@Nmedina87bot`, chat `1019202411`, ver [[07-timbre-vto-telegram]]). Se implementa con un `rest_command: telegram_aviso` en `configuration.yaml` (POST a la API de Telegram, `payload: '{"chat_id":1019202411,"text":"{{ mensaje }}"}'`), y cada automatización llama `rest_command.telegram_aviso` con su `mensaje`. Avisan: atardecer ON, amanecer OFF, jardín WiZ 00:00 y barrido 2 AM.

- ⚠️ `rest_command` es una **integración nueva** → hay que **reiniciar HA** (`sudo docker restart home-assistant`) para que cargue; `reload_all` no instancia integraciones nuevas.
- Probar sin encender luces: `POST /api/services/rest_command/telegram_aviso` con `{"mensaje":"..."}`.
- **Dónde ver los eventos en la UI:** Ajustes → Automatizaciones (cada una tiene "última ejecución" + Trazas), y el **Registro/Logbook** con cada cambio de estado.

## Ver también

- [[Red]] — infraestructura de red hogareña (domótica Tuya/WiZ en `nexus-lot`)
- [[02-camaras]] — la cámara del jardín se alimenta del switch Tuya `luces y cámara jardín`
- [[04-dvr-dahua]] · [[07-timbre-vto-telegram]]
