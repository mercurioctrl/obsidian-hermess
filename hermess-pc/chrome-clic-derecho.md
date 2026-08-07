# Chrome — clic derecho no abre menú (extensión) + Slack colgado

Dos síntomas que aparecieron juntos el 2026-08-06 ("de pronto Slack se colgó y en Chrome el clic derecho no abre ningún menú"). Resultaron ser **dos problemas distintos, ninguno de GPU**.

---

## Síntoma

- **Chrome:** clic derecho sobre cualquier página no abre el menú contextual (no aparece nada).
- **Slack:** queda gris / "«Slack» no responde" (diálogo de Forzar salida / Esperar), quemando CPU.

---

## Problema 1 — Chrome: el menú contextual lo rompe una extensión

**Causa:** una de las ~31 extensiones instaladas hace `preventDefault` sobre el evento `contextmenu` en todas las páginas, anulando el menú entero.

**Cómo se confirmó (aislamiento):**

```bash
# Perfil limpio, sin extensiones → clic derecho SÍ funciona
google-chrome --user-data-dir=/tmp/chrome-test --new-window https://example.com
# Perfil real con extensiones desactivadas → clic derecho SÍ funciona
google-chrome --disable-extensions --restore-last-session
```

Con el perfil normal (extensiones activas) el clic derecho se rompe → **es una extensión**, no Chrome.

**Cómo encontrar la culpable:** bisección en `chrome://extensions` — desactivar la mitad, probar clic derecho, repetir partiendo el grupo sospechoso (4–5 pasos).

**Sospechosas top** (inyectan en todas las URLs):
- **Awesome Screen Recorder & Screenshot** ← #1 (herramientas de captura ponen su propio menú/overlay). *Ya figuraba como extensión a revisar en [[hermess-pc/chrome-keyring|chrome-keyring]].*
- Surfshark VPN, NordVPN
- Stylebot
- Un userscript de **Tampermonkey** que haga `preventDefault` en `contextmenu`

> El análisis estático de los content scripts no la pinpointeó (puede actuar vía service worker o userscript). La bisección en runtime es el método fiable.

## Problema 2 — Slack: cuelgue por presión de memoria

**Causa:** apretón de RAM/swap (~10:29 del 2026-08-06, swap libre bajó a ~16%). El equipo corría una **VM QEMU/KVM Lubuntu de 4 GB** + muchas apps Electron (Termius, Azure Data Studio, VS Code, Slack, Chrome+31 ext) → swap thrash → Slack queda tildado.

**Fix:** Forzar la salida de Slack y reabrir. **Prevención:** cerrar la VM/apps cuando no se usan o ampliar swap. Ver [[hermess-pc/earlyoom|earlyoom]] (configurado para sacrificar Chrome/Slack primero; esta vez la RAM se recuperó sola y no llegó a matar nada).

---

## Hipótesis descartadas (no repetir)

- **NO era la versión de Chrome:** rollback 151 → 150 (+ `apt-mark hold`) **no sirvió**, volvió a pasar.
- **NO era la GPU:** con `--disable-gpu` en Chrome el clic derecho seguía roto.
- **Driver NVIDIA 580 sano:** sin errores Xid/NVRM en `dmesg` (no se cae a nivel kernel).
- El log `vaapi_wrapper.cc: Could not get a valid VA display` es **inofensivo** (VA-API no disponible en NVIDIA, no afecta nada).
- El crash real de GPU de Chromium vs RTX 5070 sí existe, pero es **otro caso** (Termius, resuelto con `--disable-gpu` en su `.desktop`).

## Estado final (revertido a pedido del usuario)

- Chrome de vuelta en la última versión (**151.0.7922.75**, sin `hold`).
- `hardware_acceleration_mode.enabled = true` (aceleración reactivada).
- Borrado el override `~/.local/share/applications/google-chrome.desktop`.
- Quitado `--disable-gpu` del override de Slack.
- **Pendiente:** cazar la extensión culpable por bisección.

---

## Ver también

- [[hermess-pc/chrome-keyring|Chrome — deslogueo por keyring roto]]
- [[hermess-pc/earlyoom|earlyoom — presión de RAM]]
- [[hermess-pc/hermess-pc|Índice hermess-pc]]
