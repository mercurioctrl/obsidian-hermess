# earlyoom — Protección contra OOM

Daemon que previene congelamientos del sistema actuando antes que el kernel OOM killer, cuando la RAM se acerca al límite.

Instalado: 2026-05-15

---

## Por qué earlyoom

El kernel OOM killer actúa demasiado tarde — para cuando interviene, el sistema ya lleva segundos o minutos congelado. earlyoom monitorea la memoria constantemente y mata el proceso más pesado cuando todavía hay margen de respuesta.

---

## Configuración

**Archivo:** `/etc/default/earlyoom`

```bash
EARLYOOM_ARGS="-m 5 -s 10 -r 60 \
  --prefer '(chrome|chromium|slack|thunderbird|java)' \
  --avoid '(gnome-shell|bash|zsh|fish|sshd|systemd|warp-terminal|mysqld|dockerd|qemu-system|containerd|libvirtd)'"
```

### Umbrales

| Condición | Acción |
|-----------|--------|
| RAM libre < 5% **o** swap libre < 10% | SIGTERM (cierre graceful) |
| RAM libre < 2.5% **o** swap libre < 5% | SIGKILL (fuerza) |

### Prioridades

- **Prefiere matar primero:** Chrome, Chromium, Slack, Thunderbird, Java
- **Nunca mata:** GNOME Shell, bash/zsh/fish, sshd, systemd, Warp Terminal, MySQL, Docker, QEMU, containerd, libvirtd

---

## Protección de VMs y contenedores Docker

Protección en dos capas para que earlyoom **y** el kernel nunca maten VMs ni contenedores:

### Capa 1 — earlyoom `--avoid` (regex por nombre de proceso)

earlyoom skipea explícitamente: `qemu-system`, `containerd`, `libvirtd`, `dockerd`

### Capa 2 — OOMScoreAdjust=-1000 vía systemd drop-ins

Los servicios tienen score -1000 (inmune para el kernel OOM killer).
Los procesos hijos heredan el score:

| Proceso | oom_score_adj | Fuente |
|---------|--------------|--------|
| dockerd | -1000 | drop-in docker.service |
| containerd | -1000 | drop-in containerd.service |
| containerd-shim | -999 | heredado de containerd |
| libvirtd | -1000 | drop-in libvirtd.service |
| qemu-system | 0 | default de libvirt (cubierto por capa 1) |

**Drop-ins en:** `/etc/systemd/system/{docker,containerd,libvirtd}.service.d/oom.conf`

---

## Comandos útiles

```bash
# Ver logs en tiempo real (qué mató y cuándo)
journalctl -u earlyoom -f

# Ver estado del servicio
systemctl status earlyoom

# Verificar oom_score_adj de un proceso
cat /proc/$(pgrep dockerd)/oom_score_adj

# Reiniciar si se cambia config
sudo systemctl restart earlyoom
```

---

## Ver también

- [[hermess-pc/arquitectura|Arquitectura del sistema]]
- [[hermess-pc/hermess-pc|Índice]]
