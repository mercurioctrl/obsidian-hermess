# Memoria de Claude — hermess-pc

Contexto y preferencias guardadas por Claude para este proyecto. Sincronizado: 2026-06-30.

---

## Sobre el usuario

- Trabaja con múltiples entornos en simultáneo: VMs (libvirt/QEMU), contenedores Docker, apps Electron
- PC personal con 32GB RAM, Ubuntu GNOME, 3 monitores
- Usa Warp Terminal, Chrome, Slack, Thunderbird, Java habitualmente
- Tiene conocimiento técnico de Linux/sysadmin

---

## Configuraciones del sistema

### Red
Ver [[hermess-pc/red]] para detalle completo.
- USG-3P con dual WAN: Telecom (primary, Port 1) + Telecentro (failover, Port 3)
- Controller UniFi en Docker, config override en `config.gateway.json`
- Telecentro modem en modo router (DHCP activo, da 10.131.202.19/24)
- Ambas WANs Active, modo Failover Only

### VPN
Ver [[hermess-pc/vpn-casa]] para detalle completo.
- VPN CASA: **L2TP/IPSec** hacia `db-nb-dev.blu.net.ar`, usuario `hermess87`, auth por Pre-Shared Key
- Origen en la Mac (VPN nativa de macOS); migrable a Ubuntu con `network-manager-l2tp` + keyfile `.nmconnection`
- NO es OpenVPN ni WireGuard (incompatibles); secretos cifrados en System Keychain de la Mac

### Monitores
Ver [[hermess-pc/monitores]] para detalle completo.
- 3 monitores: Gigabyte (primario, centro), BenQ portrait (izq), LG portrait (der)
- Script `force-primary-monitor.py` previene que ventanas se abran en monitores secundarios
- TilingShell con autotiling desactivado

### Protección de memoria
Ver [[hermess-pc/earlyoom]] para detalle completo.
- earlyoom instalado con protección de VMs y contenedores
- OOMScoreAdjust=-1000 en docker, containerd, libvirtd
- Prefiere matar Chrome/Slack/Thunderbird/Java antes que infraestructura

### Sincronización periódica
Ver [[hermess-pc/sync-curls]] para detalle completo.
- sync-curls.service ejecuta 5 endpoints cada hora
- Solo notifica errores, éxitos van al log

---

## Referencia Obsidian

- **API:** `https://localhost:27124/`
- **Carpeta del proyecto:** `hermess-pc/`
- **Token:** en `obsidian.md` de la memoria de Claude

---

## Ver también

- [[hermess-pc/arquitectura]]
- [[hermess-pc/red]]
- [[hermess-pc/vpn-casa]]
- [[hermess-pc/changelog]]
- [[hermess-pc/hermess-pc|Índice]]
