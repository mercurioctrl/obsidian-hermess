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


---

## 2026-07-17

### Arreglado deslogueo masivo de Chrome (keyring GNOME roto)

- Chrome deslogueaba de todos los sitios a la vez (Google, GitHub, X), intermitente y casi a diario, sin cerrar el navegador.
- Descartado: hackeo, limpiadores/cron/políticas, borrado de cookies (persistían cifradas `v11`), VPN.
- Causa: `~/.local/share/keyrings/default.keyring` corrupto + faltaba el puntero `default` → con Chrome crasheando, en cada reinicio no obtenía la llave del keyring y no podía desencriptar las cookies → logout masivo.
- Fix: backup en `~/keyrings-backup-20260717-145137`, `default` → `login`, eliminado el `default.keyring` corrupto.

Ver [[hermess-pc/chrome-keyring|Chrome — keyring roto]]. Pendiente: investigar por qué crashea Chrome.

---

## 2026-07-25

### VM Windows 7 (libvirt/QEMU) — carpeta compartida y runtime faltante

- VM `win7` en `qemu:///system` (IP `192.168.122.20`, hostname `hermess-PC`, disco `/var/lib/libvirt/images/vol.qcow2`). Comparte carpeta **desde el guest** por SMB: recurso **`RecordDownload`** → accesible en `smb://192.168.122.20/RecordDownload`. Correr un cliente Hikvision (descarga de grabaciones).
- **No** es compartición del host (no hay virtiofs/9p ni Samba activo en el host). Win7 habla hasta **SMB 2.1** (montar con `vers=2.1`, no 3.0).
- **Error al instalar componente Hikvision** (`LocalServiceControl.exe`): falta `api-ms-win-crt-runtime-l1-1-0.dll` = **Universal C Runtime**. Windows Update no sirve (error **80072EFE** — Win7 ya no negocia TLS/SHA-2 con los servidores MS).
- **Solución (offline):** instalar `VC_redist.x64.exe` 2015-2019 (VS2019 14.29, compatible Win7 — las versiones 14.40+ ya no soportan Win7) o el KB **`windows6.1-kb2999226-x64.msu`**. Traen el UCRT y colocan el DLL faltante.
- **Estado:** DLL diagnosticado y `VC_redist.x64.exe` bajado a `/tmp` del host. Transferencia por SMB falló (`NT_STATUS_LOGON_FAILURE` — cuenta sin pass o pass distinta). Alternativas para pasar el archivo: server web temporal (`python3 -m http.server 8000` → `http://192.168.122.1:8000/`) o adjuntar como ISO con `virsh attach-disk`. **Pendiente:** completar la instalación dentro del Win7.

### Cámara PUERTA PTZ — cron de loop del patrullaje

- Agregado `~/.local/bin/ptz-puerta-loop.sh` + cron (`* * * * *`): relanza el patrullaje (OneTimePatrol) de la cámara PTZ `10.10.10.64` cuando queda `stopped`, porque este modelo hace **una sola pasada y no loopea** nativamente. Log en `/tmp/ptz_puerta_loop.log`.
- Detalle completo de la cámara y su API en [[Red/02-camaras#Cámara PUERTA PTZ — DS-2CV1F23G2-LIDWF|PUERTA PTZ]] (nota de [[Red/Red|Red]]).

---

## 2026-08-06

### Chrome — clic derecho no abre menú contextual: es una extensión (no GPU ni versión)

- Síntoma: el clic derecho en Chrome dejó de abrir el menú en todas las páginas, junto con Slack colgado.
- **Causa:** una de las ~31 extensiones intercepta `contextmenu` con `preventDefault`. Confirmado: con perfil limpio (`--user-data-dir`) y con `--disable-extensions` el clic derecho anda; con extensiones activas se rompe.
- **Descartado con datos:** versión de Chrome (rollback 151→150 no sirvió), GPU (`--disable-gpu` no lo arregló), driver NVIDIA 580 sano (sin Xid en dmesg). El error `vaapi_wrapper: Could not get a valid VA display` es inofensivo.
- **Pendiente:** aislar la extensión por bisección en `chrome://extensions`. Sospechosa #1: **Awesome Screen Recorder** (también listada en [[hermess-pc/chrome-keyring|chrome-keyring]]).

### Slack "no responde" — cuelgue por presión de memoria

- Apretón de RAM/swap (~10:29, swap libre ~16%) con la VM QEMU de 4 GB + apps Electron corriendo → Slack tildado. Fix: forzar salida y reabrir. Ver [[hermess-pc/earlyoom|earlyoom]].

Detalle completo en [[hermess-pc/chrome-clic-derecho|Chrome — clic derecho (extensión)]].
