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
| Dmz-server | 10.30.30.1/24 (VLAN 30) | — | Servidores |
| VPN-Casa | 10.10.20.1/24 | — | VPN L2TP remota |

## Domótica

- **Tuya/Smartlife** (switches): ~12 dispositivos en `nexus-lot`, OUI Tuya Smart Inc.
- **WiZ/Macroled** (luces): ~10 dispositivos en `nexus-lot`, prefijo hostname `wiz_`
- **Ezviz Cam**: 10.10.10.43, MAC `98:f1:12:3f:f0:a6` → asignada a [[AP Galeria]]

## Cámaras

- [[02-camaras]] — Inventario, diagnóstico y tareas pendientes

## ⚠️ Tareas pendientes

- [ ] **Reemplazar cable del pasillo** — cámara PASILLO-C (10.10.10.192) negoció 10Mbps half-duplex, causa de los cortes de imagen
- [ ] **Pinear Ezviz a AP Galeria** — crear SSID `nexus-cam` solo en AP Galeria y reconectar la cámara

## Historial

- [[01-cambios-2025-05]] — Sesión de diagnóstico y optimización (mayo 2025)

## Notas

- El controlador corre en `hermess-desktop` (10.10.10.7), no en el USG
- El modem/ISP upstream está en `192.168.0.1`, red `192.168.0.x`
- WAN usa DHCP desde el modem (actualmente `192.168.0.125`)
