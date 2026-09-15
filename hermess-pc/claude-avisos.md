# Claude Code — avisos de atención en Ghostty

Sistema para darse cuenta, de un vistazo y desde otra ventana, qué está haciendo cada sesión de Claude Code: **emoji de estado en el título de la pestaña** + **notificación de escritorio** + **sonido**. Armado el 2026-09-15 porque con ~17 sesiones abiertas era imposible saber cuál estaba esperando una respuesta.

---

## Estados

| Emoji | Significado | Hook que lo dispara |
|---|---|---|
| 🟡 | Claude espera una respuesta (permiso o pregunta) | `Notification` |
| 🟢 | Terminó la tarea y todavía no miré la pestaña | `Stop` |
| 🔵 | Terminó y ya la vi / sesión inactiva | watcher de foco, o `SessionStart` |
| 🙃🫠🤐🤨… | Trabajando — rota 34 caritas cada 1,5 s | `UserPromptSubmit` y `PostToolUse` |

Además: 🟡 y 🟢 mandan notificación de escritorio (`notify-send`, el amarillo con urgencia *critical* para que quede pegada) y sonido (`paplay` con sonidos de `freedesktop`), y Ghostty resalta la ventana con borde.

---

## Piezas

| Archivo | Para qué |
|---|---|
| `~/.claude/notify-atencion.sh` | Todo el motor: estados, notificación, sonido, rotador, watcher de foco, comando de títulos |
| `~/.claude/settings.json` | Los hooks que lo invocan, y `preferredNotifChannel: "terminal_bell"` |
| `~/.claude/nombres-pestanas.conf` | Nombre propio por carpeta (`ruta=NOMBRE`), para que el emoji anteceda *mi* nombre y no el de la carpeta |
| `~/.local/bin/titulo` | Wrapper corto para nombrar la pestaña |
| `~/.config/ghostty/config` | `bell-features` y los keybinds |

Hooks registrados (todos `async: true`): `Notification`→atencion, `Stop`→listo, `UserPromptSubmit`/`PostToolUse`→trabajando, `SessionStart`→visto, `SessionEnd`→apagar.

---

## Cómo funciona por dentro

**Escribir el título desde un hook.** El hook no tiene `/dev/tty` (stdin va a `/dev/null` y stdout a un archivo), así que no se puede escribir al terminal por la vía obvia. El script sube por `/proc/<pid>/fd` desde `$PPID` hasta encontrar un ancestro con `/dev/pts/N` —- el proceso `claude` —- y le escribe la secuencia OSC 0 directo a esa pts. Una secuencia OSC no imprime nada visible, así que es seguro incluso con la TUI en fullscreen pintando.

**Detectar que miré la pestaña (🟢 → 🔵).** Al entrar en verde lanza un watcher con `setsid` que cada 2 s lee `xprop -root _NET_ACTIVE_WINDOW` y compara `_NET_WM_NAME` contra la marca `🟢 <nombre>`. Ghostty publica ahí el título de la **pestaña activa**, así que si coincide es porque la estoy mirando. Se rinde a la hora. **Depende de X11** (la sesión es x11, no Wayland).

**Un solo proceso de fondo por pestaña.** El pidfile es `$XDG_RUNTIME_DIR/claude-estado/<N>.pid` (numerado por pts, no por `session_id`): así el fast-path de `PostToolUse` puede chequear con `kill -0` si el rotador ya está vivo **antes** de invocar `jq`, y sale sin hacer nada. Sin eso, cada llamada a herramienta lanzaría un proceso nuevo.

---

## Nombrar pestañas

`Ctrl+Shift+T` ejecuta `titulo`, que abre un cuadrito **zenity** con el nombre actual precargado. Vacío = vuelve al nombre de la carpeta; Cancelar = no toca nada. También a mano: `titulo LASET` / `titulo -` (resetear).

El nombre se guarda por carpeta en `nombres-pestanas.conf`, así que sobrevive a cerrar y reabrir la sesión.

Otros modos del script: `--marcar-todas` (pone 🔵 en toda pestaña con sesión de Claude, salteando las que tienen estado propio), `--aprender` (lee por `xprop` el título que le puse a mano a la pestaña actual y lo registra en el conf).

---

## Gotchas (todos costaron un rato)

1. **Un título fijado a mano bloquea todo.** Si la pestaña tiene título puesto con `prompt_surface_title` (el diálogo de Ghostty), Ghostty **ignora las secuencias OSC** y el emoji nunca aparece. Se libera abriendo el diálogo y dejándolo **en blanco** (la doc de `title` dice que un valor vacío devuelve el control al programa); si no, cerrando y reabriendo la pestaña. Por eso `prompt_surface_title` se movió a `Ctrl+Shift+Alt+T` y quedó reservado para pestañas sin Claude.
2. **`\n` no envía, `\r` sí.** En el keybind `text:`, un `\n` **inserta un salto de línea** en el prompt de Claude Code (es justo lo que hace `shift+enter`); para que el comando se ejecute hay que mandar `\r`. Mismo problema, al revés, que el de [[hermess-pc/ghostty|Shift+Enter en 1.2.2]].
3. **`bell-features` es un set de flags que parte de los defaults.** Listar sólo los que quiero **no apaga** el resto: para sacar la campanita del título hay que escribir `no-title` explícito. Verificar siempre con `ghostty +show-config | grep bell-features`, que puede diferir de lo que dice el archivo.
4. **El hook corre sin `DISPLAY`.** Zenity no abría desde el comando. El script ahora lo saca del entorno del proceso de Ghostty (`/proc/<pid>/environ`).
5. **La `Notification` de sesión ociosa hay que filtrarla.** Claude Code la dispara no sólo para permisos, sino también cuando el prompt queda idle ~60 s ("waiting for your input"). Tomada como 🟡 quedaba **pegada para siempre**, porque el watcher que pasa a 🔵 sólo se arma en 🟢. El script la ignora entera, y el filtro va **antes** de matar el proceso de fondo —- si no, cortaba el watcher. Los mensajes se loguean en `$XDG_RUNTIME_DIR/claude-estado/notif.log` por si hay que afinar el patrón.
6. **El hook `Stop` también dispara** con `/clear`, `/compact` y al retomar sesión.
7. **Los avisos salen de cualquiera de las sesiones abiertas.** Con muchas sesiones puede volverse ruidoso; si molesta, dejar notificación sólo para el 🟡.

---

## Operar

```bash
~/.claude/notify-atencion.sh --marcar-todas    # resetear títulos de todas las pestañas
ls $XDG_RUNTIME_DIR/claude-estado/             # procesos de fondo vivos (uno por pestaña)
jq '.hooks' ~/.claude/settings.json            # ver los hooks registrados
```

Los cambios al script aplican al instante en todas las sesiones (se lee en cada ejecución). Los cambios a `settings.json` los toman las sesiones vivas sin reiniciar. Para desactivar todo: borrar el bloque `hooks` del settings.json.

---

## Ver también

- [[hermess-pc/ghostty|Ghostty — terminal (config + fixes)]] — la config de la terminal donde corre esto
- [[hermess-pc/changelog|Changelog]]
- [[hermess-pc/hermess-pc|Índice hermess-pc]]
