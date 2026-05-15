# Arquitectura del sistema

Visión general de los componentes, servicios y decisiones de configuración del sistema hermess-pc.

---

## Hardware

| Componente | Detalle |
|-----------|---------|
| RAM | 32 GB |
| Monitores | 3 (ver [[hermess-pc/monitores]]) |
| GPU | Conectores DP-0, DP-3, HDMI-0 |

---

## Stack de servicios

```
┌─────────────────────────────────────────────────────┐
│  GNOME Shell (desktop)                              │
│  ├── TilingShell (autotiling: OFF)                  │
│  └── force-primary-monitor.py (autostart)           │
├─────────────────────────────────────────────────────┤
│  Servicios del sistema                              │
│  ├── earlyoom          ← protección RAM             │
│  ├── dockerd           ← contenedores               │
│  ├── containerd        ← runtime de contenedores    │
│  ├── libvirtd          ← VMs (QEMU/KVM)             │
│  ├── mysqld            ← base de datos              │
│  └── apache2           ← web local (sync-dashboard) │
├─────────────────────────────────────────────────────┤
│  Servicios de usuario                               │
│  └── sync-curls.service  ← sincronización horaria   │
└─────────────────────────────────────────────────────┘
```

---

## Protección de memoria

Ver [[hermess-pc/earlyoom]] para detalle completo.

- **earlyoom** actúa cuando RAM < 5%, antes que el kernel OOM killer
- VMs y contenedores protegidos con doble capa (regex + OOMScoreAdjust=-1000)
- Procesos más pesados habitualmente: QEMU (VMs), Chrome, Slack, Thunderbird, Java

---

## Monitores

Ver [[hermess-pc/monitores]] para detalle completo.

| Monitor | Conector | Posición | Rol |
|---------|----------|----------|-----|
| Gigabyte G27QC A | DP-0 | Centro | **Primario** (2560x1440) |
| BenQ GW2780 | DP-3 | Izquierda | Portrait |
| LG IPS FULLHD | HDMI-0 | Derecha | Portrait |

**Problema resuelto:** apps se abrían en BenQ por dimensiones guardadas en dconf.
**Fix:** TilingShell autotiling OFF + script `force-primary-monitor.py`.

---

## Sincronización de datos

Ver [[hermess-pc/sync-curls]] para detalle completo.

- Servicio systemd de usuario que ejecuta 5 endpoints cada hora
- Target: API Laravel en `localhost:8097` (contenedor Docker)
- Dashboard: `http://localhost/sync-dashboard/`

---

## Decisiones de configuración

| Decisión | Por qué |
|---------|---------|
| earlyoom en vez de kernel OOM | Actúa antes del congelamiento |
| OOMScoreAdjust=-1000 en docker/containerd/libvirtd | VMs y contenedores nunca son sacrificados |
| TilingShell autotiling=false | Causaba redimensionado que rompía posición de ventanas |
| sync-curls como servicio de usuario | No requiere root, se integra con `journalctl --user` |

---

## Ver también

- [[hermess-pc/earlyoom]]
- [[hermess-pc/monitores]]
- [[hermess-pc/sync-curls]]
- [[hermess-pc/changelog]]
