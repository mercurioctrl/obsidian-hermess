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

- **Tuya/Smartlife** (switches): ~12 dispositivos en `nexus-lot`, OUI Tuya Smart Inc.
- **WiZ/Macroled** (luces): ~10 dispositivos en `nexus-lot`, prefijo hostname `wiz_`
- **Ezviz Cam**: 10.10.10.43, MAC `98:f1:12:3f:f0:a6` → asignada a [[AP Galeria]]

## Cámaras

- [[02-camaras]] — Inventario, diagnóstico y tareas pendientes
- [[02-camaras#Cámara PUERTA PTZ — DS-2CV1F23G2-LIDWF|PUERTA PTZ]] — WiFi PT motorizada (10.10.10.64), patrullaje "enfoque B" vía ISAPI JSON

## Grabadores (DVR / NVR)

- [[04-dvr-dahua]] — **DVR Dahua HCVR** (10.10.10.101): grabador principal, híbrido 4 analógicas + IP. Se opera por API RPC2. Mapeo de canales y cómo operarlo.
- [[05-nvr-hikvision]] — **NVR Hikvision** kit WiFi (10.10.10.105): headless, gestión **solo por Hik-Connect**. Emite su propia WiFi para las cámaras del kit. La clave/SSID del AP **no se puede cambiar en remoto** (investigación 2026-07-27).

## Impresoras

- [[03-impresora-p1102w]] — HP LaserJet P1102w: config (driver hplip+plugin, SSID `nexus-printers`, IP fija 10.10.10.189) y diagnóstico

## ⚠️ Tareas pendientes

- [ ] **Reemplazar cable del pasillo** — cámara PASILLO-C (10.10.10.192) negoció 10Mbps half-duplex, causa de los cortes de imagen
- [ ] **Pinear Ezviz a AP Galeria** — crear SSID `nexus-cam` solo en AP Galeria y reconectar la cámara
- [ ] **NVR Hikvision** — reservar IP fija en el USG y evaluar bloqueo de salida a WAN (ver [[05-nvr-hikvision#⚠️ Pendientes]])

## Historial

- [[01-cambios-2025-05]] — Sesión de diagnóstico y optimización (mayo 2025)
- [[03-impresora-p1102w#Sesión de diagnóstico (2026-07-12)]] — Puesta a punto de la impresora P1102w (julio 2026)
- [[02-camaras#Sesión de configuración (2026-07-25) — patrullaje "enfoque B"]] — Config del patrullaje de la cámara PUERTA PTZ (julio 2026)
- [[04-dvr-dahua#Sesión de reordenamiento (2026-07-26)]] — Reordenamiento de canales del DVR Dahua: PTZ movida CH11→CH9 (julio 2026)
- [[05-nvr-hikvision]] — Conexión del NVR Hikvision kit WiFi (10.10.10.105) e investigación del cambio de clave de su WiFi (julio 2026)

## Notas

- El controlador corre en `hermess-desktop` (10.10.10.7), no en el USG
- El modem/ISP upstream está en `192.168.0.1`, red `192.168.0.x`
- WAN usa DHCP desde el modem (actualmente `192.168.0.125`)
