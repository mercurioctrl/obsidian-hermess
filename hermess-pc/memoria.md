# Memoria de Claude — hermess-pc

Contexto y preferencias guardadas por Claude para este proyecto. Sincronizado: 2026-05-15.

---

## Sobre el usuario

- Trabaja con múltiples entornos en simultáneo: VMs (libvirt/QEMU), contenedores Docker, apps Electron
- PC personal con 32GB RAM, Ubuntu GNOME, 3 monitores
- Usa Warp Terminal, Chrome, Slack, Thunderbird, Java habitualmente
- Tiene conocimiento técnico de Linux/sysadmin

---

## Configuraciones del sistema

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
- [[hermess-pc/changelog]]
- [[hermess-pc/hermess-pc|Índice]]
