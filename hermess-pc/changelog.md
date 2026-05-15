# Changelog

Registro de cambios y configuraciones aplicadas al sistema.

---

## 2026-05-15

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
