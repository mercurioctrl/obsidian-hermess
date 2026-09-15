# Ghostty — terminal principal (config + fixes post-update)

Terminal principal de la PC (reemplaza a Termius/Warp para el uso diario). Config en `~/.config/ghostty/config`, tema estilo Termius (fondo `#252836`, fuente JetBrains Mono). Backup del template en `config.b5036194.bak`.

---

## Contexto (2026-09-10)

Tras actualizar Ghostty a **1.2.2** cambiaron dos comportamientos porque la config **no los fijaba explícitos** y quedaban atados al default de la versión:

## Síntoma 1 — clic derecho pega en vez de abrir menú

- **Antes:** clic derecho → menú contextual. **Después del update:** pega el portapapeles.
- **Causa:** la config nunca fijó `right-click-action`, así que seguía el default de la versión.
- **Fix:** fijarlo explícito en el config:
  ```
  right-click-action = context-menu
  ```
  Valores válidos: `context-menu`, `paste`, `copy-or-paste`, `ignore`.
- **Ojo:** el clic del **medio/rueda** SIEMPRE pega la selección en Linux y **no** se puede desactivar — no confundir con el derecho.

## Síntoma 2 — Shift+Enter manda enter en vez de salto de línea

- **Antes:** Shift+Enter insertaba un salto de línea. **Después:** manda un enter pelado (envía/submit).
- **Causa:** el keybind estaba en `text:\x1b\r` = ESC + **CR**, y `\r` (CR) es justo lo que dispara *enviar* en la mayoría de REPLs/shells.
- **Fix:** usar line feed puro:
  ```
  keybind = shift+enter=text:\n
  ```
- **Nota de diagnóstico:** en `ghostty +list-keybinds` los escapes se muestran con doble backslash (`\\n`, `\\x1b\\r`). Es solo el formato de impresión (re-escapa para mostrar), **NO** significa que el escape esté roto. No sacar conclusiones de eso.

---

## Config nueva (2026-09-15) — avisos de Claude Code

Al armar [[hermess-pc/claude-avisos|los avisos de atención de Claude Code]] se tocó la config de Ghostty:

```
bell-features = no-system,no-audio,attention,no-title,border
keybind = ctrl+shift+t=text:! titulo\r          # nombrar pestaña (abre cuadrito zenity)
keybind = ctrl+shift+alt+t=prompt_surface_title  # el diálogo nativo, movido acá
keybind = ctrl+alt+r=reload_config               # porque Ctrl+Shift+, no dispara (ver abajo)
```

- **`bell-features` es un set de flags que arranca de los defaults**: listar sólo los que quiero **no apaga** el resto. Para sacar la campanita del título hay que escribir `no-title` explícito. Verificar con `ghostty +show-config | grep bell-features`, que puede diferir del archivo.
- **Un título fijado a mano bloquea las secuencias OSC.** Con `prompt_surface_title` puesto, Ghostty ignora los títulos que manda el programa. Se libera abriendo el diálogo y dejándolo **en blanco** (la doc de `title`: un valor vacío devuelve el control al programa), o cerrando y reabriendo la pestaña.
- **En `text:`, `\n` inserta salto de línea y `\r` envía.** Es la otra cara del fix de Shift+Enter de arriba: ahí se quería insertar (`\n`), acá ejecutar (`\r`).

---

## Recargar la config — `Ctrl+Shift+,` NO anda (teclado latinoamericano)

El default `Ctrl+Shift+,` **no dispara** con teclado latinoamericano, porque `Shift+,` produce `;`. Se perdió un buen rato ahí (2026-09-15) creyendo que los cambios no se aplicaban. Alternativas:

```bash
kill -USR2 $(pgrep -x ghostty)    # Ghostty captura SIGUSR2 = recargar config
```

o el keybind propio `Ctrl+Alt+R`.

**Ojo antes de mandar señales:** verificar que el proceso la capture, mirando `SigCgt` en `/proc/<pid>/status`. Ghostty captura **SIGUSR2**, pero **NO** captura SIGUSR1 ni SIGHUP — mandar esas lo mataría con todas las pestañas abiertas.

---

## Cómo operar / diagnosticar

```bash
ghostty +version                       # versión y canal
ghostty +show-config                   # config efectiva (omite valores == default)
ghostty +show-config --default --docs  # todas las opciones + docs + defaults
ghostty +list-keybinds                 # keybinds efectivos
ghostty +list-keybinds --default       # keybinds default
ghostty +list-actions                  # acciones disponibles (text, csi, esc, ...)
ghostty +show-config 2>&1 | grep -iE "error|invalid|unknown"  # chequear parseo
```

**Aplicar cambios de config:** recargar con `Ctrl+Alt+R` o `kill -USR2 $(pgrep -x ghostty)` (el default `Ctrl+Shift+,` no anda en este teclado, ver arriba) o cerrar/reabrir Ghostty del todo (más seguro tras un update de versión, porque el instance en ejecución conserva la config vieja hasta recargar).

---

## Lección general

Después de cada **update de Ghostty**, revisar comportamientos que dependan de defaults no fijados. Fijar explícito en el config todo lo que importe (clic derecho, keybinds con escapes) para que un cambio de default de la versión no lo pise.

---

## Ver también

- [[hermess-pc/chrome-clic-derecho|Chrome — clic derecho (extensión)]] — otro caso de "clic derecho roto", pero de causa distinta (extensión, no config)
- [[hermess-pc/claude-avisos|Claude Code — avisos de atención]] — usa esta terminal para mostrar el estado de cada sesión
- [[hermess-pc/changelog|Changelog]]
- [[hermess-pc/hermess-pc|Índice hermess-pc]]
