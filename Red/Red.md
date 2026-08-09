# Red — Infraestructura de Red Hogareña

Documentación de la red UniFi del hogar: dispositivos, configuración, cambios y domótica.

## Dispositivos

| Dispositivo | Modelo | IP | Rol |
|---|---|---|---|
| USG-3P | UGW3 | LAN: 10.10.10.1 / WAN: 192.168.0.125 | Router/Gateway |
| Controlador UniFi | Software | 10.10.10.7:8443 | Controlador (en hermess-desktop) |
| AP Oficina | U7Pro Gen2 | 10.10.10.15 | AP principal, zona oficina |
| AP Galeria | U7Pro Gen2 | 10.10.10.13 | AP galería/living |
| AP Vestidor | U7Pro Gen2 | 10.10.10.12 | AP vestidor/dormitorios |

## Redes (SSIDs / VLANs)

| Red | Subred | Banda | Uso |
|---|---|---|---|
| nexus | 10.10.10.1/24 | 5GHz only | Dispositivos principales |
| nexus-lot | 10.10.10.1/24 | 2.4GHz only | IoT / domótica |
| nexus-invitados | 10.10.10.1/24 | 2.4GHz + 5GHz | Invitados |
| nexus-printers | 10.10.10.1/24 | 2.4GHz only | Impresora P1102w (11v/11r/PMF/steering OFF) |
| Dmz-server | 10.30.30.1/24 (VLAN 30) | — | Servidores |
| VPN-Casa | 10.10.20.1/24 | — | VPN L2TP remota |

> Nota: el **NVR Hikvision** ([[05-nvr-hikvision]]) emite además su **propia WiFi** `NVRFM7479611` para las cámaras de su kit — es una red aislada, no gestionada por UniFi.

## Domótica

- **[[08-home-assistant|Home Assistant]]** — servidor de domótica en Docker (`10.10.10.7:8123`). Orquesta luces WiZ + las 13 teclas Tuya (control local por LocalTuya), escenas, TV, sensores.
- **Tuya/Smartlife** (switches/teclas): 13 teclas Macroled en `nexus-lot`, OUI Tuya (`38:1f:8d`, `00:33:7a`), puerto local 6668. Integradas a HA por **LocalTuya** (control local, sin nube) → ver [[08-home-assistant]].
- **WiZ/Macroled** (luces): ~10 dispositivos en `nexus-lot`, prefijo hostname `wiz_`. En HA vía integración `wiz`.
- **Ezviz Cam**: 10.10.10.43, MAC `98:f1:12:3f:f0:a6` → asignada a [[AP Galeria]]
- **Wabee** (medidor de energía): `10.10.10.44`, MAC `5c:cf:7f:66:2e:cc` (Espressif/ESP). **Solo-nube** (todos los puertos TCP cerrados, sin API local): mide y sube a la nube Wabee, los datos se ven en su app. NO integrable localmente a HA; sí habría opción vía su API/nube o MQTT (a evaluar). Descubierto 2026-08-02.

## Cámaras

- [[02-camaras]] — Inventario, diagnóstico y tareas pendientes
- [[02-camaras#Cámara PUERTA PTZ — DS-2CV1F23G2-LIDWF|PUERTA PTZ]] — WiFi PT motorizada (10.10.10.64), patrullaje "enfoque B" vía ISAPI JSON

## Grabadores (DVR / NVR)

- [[04-dvr-dahua]] — **DVR Dahua HCVR** (10.10.10.101): grabador principal, híbrido 4 analógicas + IP. Se opera por API RPC2. Mapeo de canales y cómo operarlo.
- [[05-nvr-hikvision]] — **NVR Hikvision** kit WiFi (10.10.10.105): headless, gestión **solo por Hik-Connect**. Emite su propia WiFi para las cámaras del kit. La clave/SSID del AP **no se puede cambiar en remoto** (investigación 2026-07-27).

## Portero / Timbre

- [[07-timbre-vto-telegram]] — **Timbre Dahua VTO2101E** (10.10.10.102, portero PoE): servicio `vto-timbre` en hermess-desktop que manda **foto a Telegram** ante movimiento (polling OpenCV, el VTO no publica `VideoMotion`) y ante el botón de llamada. Es el mismo equipo que graba como CH6 "PORTERO" en el [[04-dvr-dahua|DVR]].

## Impresoras

- [[03-impresora-p1102w]] — HP LaserJet P1102w: config (driver hplip+plugin, SSID `nexus-printers`, IP fija 10.10.10.189) y diagnóstico

## ⚠️ Tareas pendientes

- [ ] **Reemplazar cable del pasillo** — cámara PASILLO-C (10.10.10.192) negoció 10Mbps half-duplex, causa de los cortes de imagen
- [ ] **Pinear Ezviz a AP Galeria** — crear SSID `nexus-cam` solo en AP Galeria y reconectar la cámara
- [ ] **NVR Hikvision** — reservar IP fija en el USG y evaluar bloqueo de salida a WAN (ver [[05-nvr-hikvision#⚠️ Pendientes]])
- [x] **Sticky client / roaming** — RESUELTO 2026-08-09: `nexus` a doble banda + Min RSSI -78 en ambas bandas + canales 5GHz no-DFS (ver [[06-sticky-client-roaming#Resolución definitiva (2026-08-09)]])
- [ ] **Timbre VTO** — fijar IP en el USG (hoy DHCP) y evaluar bloqueo a WAN; capturar el código del botón (ver [[07-timbre-vto-telegram#⚠️ Pendientes]])
- [ ] **2 Tuya sin identificar** — `10.10.10.27` y `10.10.10.219` responden en puerto Tuya 6668 pero NO están en la cuenta SmartLife (ver [[08-home-assistant#Notas]])
- [ ] **Wabee** (medidor energía, `10.10.10.44`) — reservar IP fija en el USG; evaluar llevar el consumo a HA vía su nube/API
- [ ] **Telecentro (WAN2)** — venía caída, recuperó 2026-08-02 pero con flapping previo; vigilar estabilidad y verificar seed `wan-mon` con la IP nueva (ver [[Monitoreo_WAN#Incidente Telecentro caída (2026-07/08)]])

## Historial

- [[01-cambios-2025-05]] — Sesión de diagnóstico y optimización (mayo 2025)
- [[03-impresora-p1102w#Sesión de diagnóstico (2026-07-12)]] — Puesta a punto de la impresora P1102w (julio 2026)
- [[02-camaras#Sesión de configuración (2026-07-25) — patrullaje "enfoque B"]] — Config del patrullaje de la cámara PUERTA PTZ (julio 2026)
- [[04-dvr-dahua#Sesión de reordenamiento (2026-07-26)]] — Reordenamiento de canales del DVR Dahua: PTZ movida CH11→CH9 (julio 2026)
- [[05-nvr-hikvision]] — Conexión del NVR Hikvision kit WiFi (10.10.10.105) e investigación del cambio de clave de su WiFi (julio 2026)
- [[06-sticky-client-roaming]] — Sticky client 5GHz RESUELTO (agosto 2026): `nexus` a doble banda + Min RSSI -78 en ambas bandas + canales no-DFS (Vestidor 40/Oficina 149/Galeria 161). Incluye runbook de la API UniFi y script `scripts/unifi_diag.py`. Registra también el intento fallido de julio (Min RSSI en 5GHz con nexus solo-5GHz rompió la conexión + incidente DFS)
- [[07-timbre-vto-telegram]] — Timbre Dahua VTO2101E → Telegram: servicio con detección de movimiento server-side (OpenCV, ROI a la vereda) + aviso de botón; ajuste de sensibilidad y arquitectura pull/push (agosto 2025)
- [[08-home-assistant]] — Integración de las 13 teclas Tuya/Macroled a Home Assistant por **LocalTuya** (control local sin nube): proyecto Tuya IoT + extracción de local keys con tinytuya + mass_configure e inyección manual de las v3.5 (agosto 2025)
- [[08-home-assistant#Rutinas / iluminación automática]] — Dashboard "Casa" (con sección propia "Calle") + rutinas de iluminación exterior (atardecer→amanecer calle/terraza; jardín y patio WiZ→medianoche), **avisos por Telegram** de cada rutina (reusa el bot del timbre vía `rest_command`), lectura de nombres por gang desde la app (`shadow/properties`) y regla dura: los switches de **jardín/cámara y patio** van SIEMPRE ON (alimentan WiZ/cámara); **conmutación escalera/vestidor** por mirror bidireccional (prender abajo/apagar arriba) reemplazando 6 escenas Tuya (agosto 2025)
- [[Monitoreo_WAN#Incidente Telecentro caída (2026-07/08)]] — diagnóstico de Telecentro caída (WAN2 con IP `0.0.0.0`) desde la LAN vía egress Cloudflare + controlador UniFi; recuperó 2026-08-02 17:28 con IP nueva. Descubierto el **Wabee** (medidor de energía, `10.10.10.44`, solo-nube). Confirmado que el switch de la calle NO alimenta las WiZ del jardín (prueba controlada) → las WiZ se prendían por un horario de la app WiZ; se dejó HA como único cerebro (agosto 2025)

## Notas

- El controlador corre en `hermess-desktop` (10.10.10.7), no en el USG
- El modem/ISP upstream está en `192.168.0.1`, red `192.168.0.x`
- WAN usa DHCP desde el modem (actualmente `192.168.0.125`)
