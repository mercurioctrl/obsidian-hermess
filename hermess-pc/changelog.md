# Changelog

Registro de cambios y configuraciones aplicadas al sistema.

---

## 2026-05-15

### Notificaciones de escritorio para earlyoom — verificadas ✓

- Confirmado funcionamiento con SIGTERM (urgency normal) y SIGKILL (urgency critical)
- Probado con procesos `chrome` y `slack`
- Comando de prueba: `sudo EARLYOOM_PID=X EARLYOOM_NAME="proc" EARLYOOM_SIGNAL="SIGKILL" /usr/local/bin/earlyoom-notify.sh`

### Notificaciones de escritorio para earlyoom

- Agregado script `/usr/local/bin/earlyoom-notify.sh` llamado con `-N` en earlyoom
- SIGTERM → notificación normal, SIGKILL → notificación critical
- Usa `su -c` con socket D-Bus explícito `/run/user/1000/bus` (`sudo -u` no funciona desde servicio de sistema)

Archivos modificados:
- `/etc/default/earlyoom` (agregado `-N /usr/local/bin/earlyoom-notify.sh`)
- `/usr/local/bin/earlyoom-notify.sh` (nuevo)

### Protección contra OOM con [[hermess-pc/earlyoom|earlyoom]]

- Instalado `earlyoom` para prevenir congelamientos cuando la RAM se llena
- Configurados umbrales: SIGTERM en RAM < 5% / swap < 10%, SIGKILL en RAM < 2.5% / swap < 5%
- `--prefer` Chrome, Slack, Thunderbird, Java (primeros en ser sacrificados)
- `--avoid` GNOME Shell, terminales, MySQL, Docker, QEMU, containerd, libvirtd

**Protección de VMs y contenedores (doble capa):**
- `qemu-system` y `containerd*` en `--avoid` de earlyoom
- Drop-ins systemd con `OOMScoreAdjust=-1000` para docker, containerd y libvirtd
- Resultado: containerd-shim (procesos de contenedores) heredan oom_score_adj=-999

Archivos modificados:
- `/etc/default/earlyoom`
- `/etc/systemd/system/docker.service.d/oom.conf`
- `/etc/systemd/system/containerd.service.d/oom.conf`
- `/etc/systemd/system/libvirtd.service.d/oom.conf`
---

## 2026-05-16

### Dual WAN failover — Telecentro como WAN2 ✓

- Configurado eth2 (Port 3) del USG-3P como WAN secundaria con Telecentro
- Modem Telecentro en modo router (DHCP activo, da IP 10.131.202.19/24 al USG)
- Load Balancing: Failover Only (Telecentro solo activa si Telecom cae)
- Ambas WANs en estado **Active** confirmado desde el controller

**Problemas resueltos:**
- eth2 tenía `disable` en config.boot → removido por SSH con sed
- Reglas NAT 6004-6006 stale (network-group) bloqueaban el provision → eliminadas
- USG-3P no soporta `load-balancing wan-load-balance` → removido de config.gateway.json

Archivos modificados:
- `/var/www/hermess/unifi/config/data/sites/default/config.gateway.json` (solo eth2)
- `/config/config.boot` en USG (eth2 habilitado con DHCP, NAT rules limpiadas)

---

## 2026-06-30

### Documentada VPN CASA (L2TP/IPSec) y migración a Ubuntu

- Identificada VPN nativa de la Mac: **VPN CASA**, tipo L2TP/IPSec, server `db-nb-dev.blu.net.ar`, usuario `hermess87`
- Aclarado que NO es OpenVPN ni WireGuard (protocolos incompatibles) → en Ubuntu requiere cliente L2TP/IPSec
- Generado keyfile `vpn-casa.nmconnection` (UUID `db921be1-16c1-4511-9a50-110c02efb26d`) para importar en NetworkManager
- Documentado flujo de extracción de secretos del System Keychain de la Mac y la instalación del keyfile

Ver [[hermess-pc/vpn-casa|VPN CASA]]. Archivos generados en la Mac: `~/vpn-casa.nmconnection`, `~/vpn-casa-README.md`.
