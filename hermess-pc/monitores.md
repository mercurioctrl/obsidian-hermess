# Configuración de monitores

Tres monitores conectados, con Gigabyte como primario y los otros dos en portrait.

---

## Layout físico

```
[BenQ portrait] [Gigabyte 1440p — PRIMARIO] [LG portrait]
   izquierda            centro                 derecha
```

## Tabla de monitores

| Monitor | Conector | Posición X | Resolución | Orientación | Rol |
|---------|----------|-----------|-----------|-------------|-----|
| Gigabyte G27QC A | DP-0 | x=1080 | 2560×1440 | Normal | **Primario** |
| BenQ GW2780 | DP-3 | x=0 | 1920×1080 | Portrait (right) | Izquierda |
| LG IPS FULLHD | HDMI-0 | x=3640 | 1920×1080 | Portrait (left) | Derecha |

## Rangos X totales

| Monitor | Rango X |
|---------|---------|
| BenQ | 0 — 1080 |
| Gigabyte | 1080 — 3640 |
| LG | 3640 — 4720 |

---

## Problema resuelto: ventanas abriéndose en BenQ

**Causa:** TilingShell con autotiling redimensionaba ventanas a ~1900px de alto (dimensión del BenQ portrait). GNOME recordaba ese tamaño y al relanzar colocaba las apps en el BenQ.

**Solución aplicada:**

1. Desactivar autotiling de TilingShell:
   ```bash
   dconf write /org/gnome/shell/extensions/tilingshell/enable-autotiling false
   ```

2. Script Python que fuerza ventanas nuevas al Gigabyte:
   - `~/.local/bin/force-primary-monitor.py`
   - Autostart: `~/.config/autostart/force-primary-monitor.desktop`
   - Usa python3 + Wnck (disponible por defecto en Ubuntu)

3. Reset de estado guardado de apps afectadas (por app):
   ```bash
   dconf reset -f /org/gnome/NOMBRE-APP/window-state/
   ```

---

## Ver también

- [[hermess-pc/arquitectura]]
- [[hermess-pc/hermess-pc|Índice]]
