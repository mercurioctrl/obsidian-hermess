# 05 — NVR Hikvision (kit WiFi)

Grabador **aparte** del [[04-dvr-dahua|DVR Dahua]]. Es un **kit WiFi headless gestionado 100% por Hik-Connect** (nube), sin salida de video ni gestión local práctica. Conectado a la LAN el 2026-07-25.

## Datos

- **Modelo:** Hikvision **DS-7104NI-S1/W/KIT** (4 canales digitales, kit con cámaras WiFi)
- **IP:** `10.10.10.105` **por DHCP** — MAC `dc:07:f8:7d:eb:4e`, máscara `255.255.255.0`, gw `10.10.10.1`. NO quedó en rango de fábrica (`192.168.1.64`).
- **Firmware:** `V4.32.202 build 240813` · DSP `V5.0 build 240430`
- **SN (etiqueta):** `FM7479611` · **SN largo:** `DS-7104NI-S1/W/KIT0120240826CCRRFM7479611WCU`
- **Verification Code:** `DSIFNQ` (etiqueta) — para agregar a Hik-Connect / resets
- **Hik-Connect (nube):** ENCENDIDO (`HCPlatformEnable:true`) — ya llama a servidores Hikvision
- Credenciales admin: (ver gestor de contraseñas)

## Headless — sin monitor ni web local

Este equipo **NO tiene HDMI ni puerto USB para mouse**: se administra solo desde la **app Hik-Connect**. En la LAN **solo responde ping, SADP (UDP 37020) y los puertos P2P de Hik-Connect (`9020`/`30960`)**. El **web (80) y el SDK (8000) están cerrados/deshabilitados** — no hay gestión local por navegador ni por iVMS-4200 sobre LAN.

## Su propia WiFi (para las cámaras del kit)

El modelo `/W` **emite su propia red WiFi** donde se conectan las cámaras del kit, aislada de la red UniFi:

- **SSID:** `NVRFM7479611` (= `NVR` + serial), **WPA2** — confirmado por escaneo de aire
- Las cámaras vienen **pre-emparejadas de fábrica**; NO cuelgan de la WiFi UniFi ni aparecen en el controlador. Solo el NVR aparece en la LAN.
- Las cámaras IP existentes del hogar (Ezviz `.43`, PASILLO-C `.192`, PTZ `.64`) son **equipos aparte**, no las del kit.

## Descubrimiento vía SADP

Al no exponer web, se descubre con el protocolo propio de Hikvision **SADP** (multicast UDP `37020`). Script en el host: `/tmp/sadp_probe.py` (resumen) y `/tmp/sadp_raw.py` (XML crudo). Devuelve modelo, SN, FW, IP, DHCP, `DeviceLock`, puertos.

## Estado (2026-07-25 → 27)

- Al conectarlo respondía ping+SADP pero **todos los puertos TCP cerrados** con `DeviceLock:true` (bloqueo por login fallido o de arranque).
- Tras **reboot** (12V): sigue igual — web/SDK cerrados, solo P2P (`9020`/`30960`) + ping + SADP. El reboot no reabrió la gestión local.

## Cambiar la clave/SSID de la WiFi del NVR — investigación profunda (2026-07-27)

**Conclusión: NO existe vía remota/nube documentada para cambiar el SSID o la clave del AP WiFi del NVR.** Solo se edita desde el **menú local en pantalla** (monitor + mouse) o desde su **web/SDK local** — y este equipo no tiene ni lo uno (headless) ni lo otro (80/8000 cerrados). Verificado con 20 fuentes y votación adversarial:

- **App móvil Hik-Connect → NO.** Su "Remote Configuration" solo expone 7 grupos (info, hora, contraseña, grabación, eventos normales/inteligentes, medición térmica); **sin sección Wi-Fi/WLAN**. Su "Wi-Fi Settings" es un **generador de QR** para que una cámara se una a un router existente, no edita el AP del NVR.
- **iVMS-4200 vía Cloud P2P → NO.** Oficial Hikvision (art. 17000129955): la config remota *"only works when the device is added via IP/Domain, it will not work via HikConnect P2P"*. Además en **firmware 4.x se quitó por diseño**. El workaround de re-agregar por IP local usa el **puerto 8000 → cerrado acá**, así que tampoco.
- **Portal hik-connect.com → NO.** Misma limitación que la app.
- **Habilitar web/ISAPI/SDK en remoto → sin procedimiento oficial** documentado.

**Clave por defecto del AP:** la regla "últimos 8 caracteres del serial de la etiqueta" es oficial **solo para cámaras WiFi Hikvision**, no para el AP de un NVR (aplica por analogía). Candidato literal con `FM7479611` → **`M7479611`** (no verificado).

**Opciones reales:**
1. **No tocarlo** — es una red interna cerrada y pre-emparejada; no hace falta la clave para uso normal.
2. **Factory reset** (botón físico / flujo SADP) → restaura servicios locales por defecto (web puerto 80) y ahí sí, por navegador `http://10.10.10.105` → *Network → WiFi*. Costo: se pierde config y hay que re-emparejar cámaras.
3. **Hipótesis no documentada (técnica):** `PUT` autenticado a `/ISAPI/System/Network/wireless` por el túnel P2P — pero primero ISAPI tendría que responder (hoy 80 cerrado). Incógnita abierta.

> ⚠️ Si se cambia la WiFi del NVR, las cámaras del kit **pierden el enlace** y hay que reconfigurarlas (web de cada cámara o re-cablearlas al NVR para que reempuje credenciales).

## ⚠️ Pendientes

- [ ] Reservar **IP fija** en el USG (mismo criterio que la impresora [[03-impresora-p1102w]], la Ezviz, etc.)
- [ ] Evaluar **bloqueo de salida a WAN** en el USG para aislarlo de la nube Hikvision (Hik-Connect + historial de CVEs). Ojo: bloquear WAN mata el acceso remoto por Hik-Connect (solo quedaría vista local en el mismo WiFi).

## Ver también

- [[04-dvr-dahua]] — DVR Dahua HCVR (grabador principal, equipo aparte)
- [[02-camaras]] — Cámaras IP del hogar (equipos aparte del kit)
- [[Red]] — Infraestructura de red hogareña
