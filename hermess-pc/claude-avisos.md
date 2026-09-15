# Claude Code — avisos de atención en Ghostty

Sistema para darse cuenta, de un vistazo y desde otra ventana, qué está haciendo cada sesión de Claude Code: **emoji de estado en el título de la pestaña** + **notificación de escritorio** + **sonido**. Armado el 2026-09-15 porque con ~17 sesiones abiertas era imposible saber cuál estaba esperando una respuesta.

---

## Estados

| Emoji | Significado | Qué lo dispara |
|---|---|---|
| caritas | Trabajando — rota 34 caritas cada 1,5 s | `UserPromptSubmit`, `PostToolUse`, `PostCompact` |
| 🟡 | Espera una respuesta (permiso o pregunta) | `PermissionRequest`, `Notification` |
| 🟢 | Terminó y todavía no miré la pestaña | `Stop` |
| 🔴 | Terminó **con error**, y no lo miré | `StopFailure` |
| 🔵 | Terminó y ya la vi / sesión inactiva | el mantenedor al detectar que miré; `SessionStart` |
| 😵 | Una herramienta falló (vuelve solo a los 6 s) | `PostToolUseFailure` |
| ⛔ | Denegué un permiso (vuelve solo a los 6 s) | `PermissionDenied` |
| 🗜️ | Compactando el contexto | `PreCompact` |
| 🤖 | Hay subagentes trabajando | `SubagentStart` / `SubagentStop` |
| ⚙️ | Hay tareas en background | `TaskCreated` / `TaskCompleted` |

Además: 🟡, 🟢 y 🔴 mandan notificación de escritorio (`notify-send`, el amarillo y el rojo con urgencia *critical* para que queden pegados; el rojo con sonido de error) y sonido (`paplay` con sonidos de `freedesktop`), y Ghostty resalta la ventana con borde.

---

## Piezas

| Archivo | Para qué |
|---|---|
| `~/.claude/notify-atencion.sh` | Todo el motor: hooks, mantenedor de título, notificación, sonido, comando de nombres |
| `~/.claude/settings.json` | Los hooks que lo invocan, y `preferredNotifChannel: "terminal_bell"` |
| `~/.claude/nombres-pestanas.conf` | Nombre propio por carpeta (`ruta=NOMBRE`), para que el emoji anteceda *mi* nombre y no el de la carpeta |
| `~/.local/bin/titulo` | Wrapper corto para nombrar la pestaña |
| `~/.config/ghostty/config` | `bell-features` y los keybinds |
| `~/.tmux.conf` | `set-titles on`, si no tmux no le pasa el título a Ghostty |
| `$XDG_RUNTIME_DIR/claude-estado/<pts>.estado` | Estado de cada pestaña (`estado\|nombre\|expira`) — lo escriben los hooks, lo lee el mantenedor |
| `$XDG_RUNTIME_DIR/claude-estado/<pts>.cuenta` | Contadores de subagentes y tareas en background |
| `$XDG_RUNTIME_DIR/claude-estado/<pts>.pid` | PID del mantenedor de esa pestaña |

Hooks registrados (16, todos `async: true`): `UserPromptSubmit`/`PostToolUse`/`PostCompact`→trabajando · `Notification`→atencion · `PermissionRequest`→espera · `PermissionDenied`→denegado · `Stop`→listo · `StopFailure`→fallo · `PostToolUseFailure`→error · `PreCompact`→compactando · `SubagentStart`/`SubagentStop`→subagente± · `TaskCreated`/`TaskCompleted`→tarea± · `SessionStart`→visto · `SessionEnd`→apagar.

**Estados transitorios.** 😵 y ⛔ se escriben con una marca de expiración en el tercer campo del archivo de estado (`estado|nombre|expira`); el mantenedor los devuelve solos a `trabajando` a los 6 s. Igual, si mientras tanto corre otra herramienta, `PostToolUse` ya los limpia antes.

**Contadores.** 🤖 y ⚙️ no son estados sino contadores en `<pts>.cuenta` (`subagentes tareas`), porque puede haber varios a la vez. Los hooks `Subagent*`/`Task*` sólo suman o restan ahí —- ni siquiera invocan `jq` —- y el mantenedor los mira cuando el estado es `trabajando`. Se resetean a `0 0` al terminar el turno, para que un evento desbalanceado no deje el 🤖 pegado.

**Prioridad:** un estado explícito (🟡 🟢 🔴 🔵 😵 ⛔ 🗜️) siempre gana; los contadores sólo pintan cuando el estado es `trabajando`.

---

## Cómo funciona por dentro

**Escribir el título desde un hook.** El hook no tiene `/dev/tty` (stdin va a `/dev/null` y stdout a un archivo), así que no se puede escribir al terminal por la vía obvia. El script sube por `/proc/<pid>/fd` desde `$PPID` hasta encontrar un ancestro con `/dev/pts/N` —- el proceso `claude` —- y le escribe la secuencia OSC 0 directo a esa pts. Una secuencia OSC no imprime nada visible, así que es seguro incluso con la TUI en fullscreen pintando.

**El título lo mantiene un proceso, no los eventos.** Claude Code **también** escribe el título del terminal —- el tema auto-generado de la conversación, con `✳` adelante (`✳ Review APIs and…`) —- y no hay setting para apagarlo, así que pisaba nuestro emoji cada vez que la sesión terminaba. Por eso el diseño final es **un mantenedor por pestaña**: un proceso `setsid` que cada 1,5 s reescribe el título según el estado. Siempre gana el nuestro.

Los hooks entonces **no escriben el título**: sólo dejan el estado en `$XDG_RUNTIME_DIR/claude-estado/<pts>.estado`, con formato `estado|nombre`. El mantenedor lo lee en cada vuelta, así que un cambio de estado se ve en ≤1,5 s. Muere solo cuando el pts desaparece (pestaña cerrada) o cuando el estado pasa a `apagado`.

**Fast-path de `PostToolUse`.** Ese hook dispara en *cada* llamada a herramienta. Si el estado ya es `trabajando`, el script sale en las primeras líneas —- lee el archivo de estado y listo, sin invocar `jq` ni lanzar nada.

**Detectar que miré la pestaña (🟢 → 🔵).** Lo hace el propio mantenedor, sólo mientras el estado es verde y cada 2 vueltas (para no abusar de `xprop`): lee `xprop -root _NET_ACTIVE_WINDOW` y compara `_NET_WM_NAME` contra la marca `🟢 <nombre>`. Ghostty publica ahí el título de la **pestaña activa**, así que si coincide es porque la estoy mirando. **Depende de X11** (la sesión es x11, no Wayland).

---

## Nombrar pestañas

`Ctrl+Shift+T` ejecuta `titulo`, que abre un cuadrito **zenity** con el nombre actual precargado. Vacío = vuelve al nombre de la carpeta; Cancelar = no toca nada. También a mano: `titulo LASET` / `titulo -` (resetear).

El nombre se guarda por carpeta en `nombres-pestanas.conf`, así que sobrevive a cerrar y reabrir la sesión.

**De dónde sale el nombre** (`nombre_base`): 1) entrada exacta en el conf; 2) si la carpeta tiene nombre **genérico** (`app`, `src`, `dist`, `public`, `frontend`…) sube hasta 3 niveles buscando uno significativo; 3) una entrada del conf que sea carpeta **padre** gana si es igual o más específica; 4) nombre de la carpeta. `$HOME` nunca cuenta como carpeta padre.

El cwd sale del JSON del hook: es el **actual**, no el de arranque —- por eso una sesión que hacía `cd app/` pasaba a llamarse `app`. `titulo` guarda el nombre para la raíz del repo git, así no depende de dónde estés parado al ponerlo.

> **Lo que NO funcionó:** resolver el nombre por la raíz del repo git. La bóveda entera es un repo, así que `obsidian-hermess/jira` y `obsidian-hermess/Blu` quedaban las dos como `obsidian-hermess`. Por eso la regla final mira nombres genéricos, no repos.

Otros modos del script: `--marcar-todas` (pone 🔵 en toda pestaña con sesión de Claude, salteando las que tienen estado propio), `--aprender` (lee por `xprop` el título que le puse a mano a la pestaña actual y lo registra en el conf).

---

## Gotchas (todos costaron un rato)

1. **Un título fijado a mano bloquea todo.** Si la pestaña tiene título puesto con `prompt_surface_title` (el diálogo de Ghostty), Ghostty **ignora las secuencias OSC** y el emoji nunca aparece. Se libera abriendo el diálogo y dejándolo **en blanco** (la doc de `title` dice que un valor vacío devuelve el control al programa); si no, cerrando y reabriendo la pestaña. Por eso `prompt_surface_title` se movió a `Ctrl+Shift+Alt+T` y quedó reservado para pestañas sin Claude.
2. **`\n` no envía, `\r` sí.** En el keybind `text:`, un `\n` **inserta un salto de línea** en el prompt de Claude Code (es justo lo que hace `shift+enter`); para que el comando se ejecute hay que mandar `\r`. Mismo problema, al revés, que el de [[hermess-pc/ghostty|Shift+Enter en 1.2.2]].
3. **`bell-features` es un set de flags que parte de los defaults.** Listar sólo los que quiero **no apaga** el resto: para sacar la campanita del título hay que escribir `no-title` explícito. Verificar siempre con `ghostty +show-config | grep bell-features`, que puede diferir de lo que dice el archivo.
4. **El hook corre sin `DISPLAY`.** Zenity no abría desde el comando. El script ahora lo saca del entorno del proceso de Ghostty (`/proc/<pid>/environ`).
5. **La `Notification` de sesión ociosa hay que filtrarla.** Claude Code la dispara no sólo para permisos, sino también cuando el prompt queda idle ~60 s ("waiting for your input"). Tomada como 🟡 quedaba **pegada para siempre**, porque el watcher que pasa a 🔵 sólo se arma en 🟢. El script la ignora entera —- ni título, ni notificación, ni tocar el estado —- así el 🟢 sigue esperando a que la mire. Los mensajes se loguean en `$XDG_RUNTIME_DIR/claude-estado/notif.log` por si hay que afinar el patrón.
6. **tmux se come el título.** Dentro de tmux el pty del proceso `claude` es el del *pane*: la secuencia OSC la captura tmux (queda en `pane_title`) y **no llega a Ghostty**, porque `set-titles` viene en `off` por default. Síntoma: la pestaña se queda con el comando (`tmux new -t cobrosNB`) y nunca muestra emoji. Fix en `~/.tmux.conf`:
   ```
   set -g set-titles on
   set -g set-titles-string "#{?#{==:#{pane_title},#{host}},#S,#{pane_title}}"
   ```
   El condicional hace que un pane sin título propio (donde `pane_title` es el hostname) muestre el nombre de la sesión tmux en lugar de `hermess-desktop`. Recargar con `tmux source-file ~/.tmux.conf`. Para diagnosticar: `tmux list-panes -a -F "#{session_name} '#{pane_title}' #{pane_tty}"`.
7. **El hook `Stop` también dispara** con `/clear`, `/compact` y al retomar sesión.
8. **Los avisos salen de cualquiera de las sesiones abiertas.** Con muchas sesiones puede volverse ruidoso; si molesta, dejar notificación sólo para el 🟡.

---

## Operar

```bash
~/.claude/notify-atencion.sh --marcar-todas    # resetear todas las pestañas a 🔵 y levantar mantenedores
cat $XDG_RUNTIME_DIR/claude-estado/*.estado    # en qué estado está cada pestaña
pgrep -fc -- --mantener                        # cuántos mantenedores vivos (uno por pestaña)
tail $XDG_RUNTIME_DIR/claude-estado/notif.log  # qué notificaciones llegaron
jq '.hooks' ~/.claude/settings.json            # ver los hooks registrados
```

Los cambios al script aplican al instante en todas las sesiones (se lee en cada ejecución). Los cambios a `settings.json` los toman las sesiones vivas sin reiniciar. Para desactivar todo: borrar el bloque `hooks` del settings.json.

---

## Ver también

- [[hermess-pc/ghostty|Ghostty — terminal (config + fixes)]] — la config de la terminal donde corre esto
- [[hermess-pc/changelog|Changelog]]
- [[hermess-pc/hermess-pc|Índice hermess-pc]]
