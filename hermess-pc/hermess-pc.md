# hermess-pc

Base de conocimiento de la PC personal de hermess: configuración del sistema, red, monitores, extensiones GNOME, servicios, scripts y optimizaciones.

Última sincronización: 2026-05-20

---

## Notas

- [[hermess-pc/arquitectura|Arquitectura del sistema]]
- [[hermess-pc/red|Red — UniFi dual WAN failover]]
- [[hermess-pc/earlyoom|earlyoom — protección OOM]]
- [[hermess-pc/monitores|Configuración de monitores]]
- [[hermess-pc/sync-curls|Servicio sync-curls]]
- [[hermess-pc/changelog|Changelog]]
- [[hermess-pc/memoria|Memoria de Claude]]

---

## Skills locales

- [[hermess-pc/skills/skills|Skills de Claude Code]] — skills instalados en `~/.claude/skills/` en este equipo

---

## Proyectos

### musica
Descargador de playlists de YouTube a MP3 organizado en `Artista/Álbum/`.
- [[hermess-pc/musica/musica|musica]] — Índice del proyecto
- [[hermess-pc/musica/arquitectura|Arquitectura]] — Flujo del script
- [[hermess-pc/musica/stack|Stack]] — yt-dlp, ffmpeg, Python 3
- [[hermess-pc/musica/changelog|Changelog]] — Historial de cambios
- [[hermess-pc/musica/contexto|Contexto]] — Biblioteca descargada y entorno

---

## Resumen del sistema

- **OS:** Ubuntu (GNOME)
- **RAM:** 32 GB
- **Monitores:** 3 (Gigabyte 1440p centro, BenQ portrait izq, LG portrait der)
- **Red:** USG-3P dual WAN — Telecom (primary) + Telecentro (failover)
- **Servicios activos:** earlyoom, sync-curls, Docker, libvirt/QEMU, MySQL, Apache2
- **Entorno de trabajo:** VMs (libvirt/QEMU), contenedores Docker, apps Electron (Slack, Warp)

---

## Ver también

- [[hermess-pc/arquitectura]]
- [[hermess-pc/red]]
- [[hermess-pc/changelog]]
