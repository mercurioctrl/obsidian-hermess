# optimizaciones-adb

Registro de **todos los cambios ADB** aplicados a la tablet [[fire]] el 2026-09-10 para ahorrar recursos/calor, con **cómo revertir cada uno**. Sin root — techo alcanzado en lo que Fire OS permite tocar.

ADB: `/home/hermess/Android/Sdk/platform-tools/adb`. La app de cámaras en uso, **gDMSS Plus** (`com.mm.android.direct.gdmssphone`), NO se tocó.

## 1. Pantalla
- Brillo: 236/255 (93%) → **191/255 (75%)**, modo manual.
- Revertir: `adb shell settings put system screen_brightness 236`

## 2. Animaciones (off)
- `window/transition/animator_animation_scale`: 0.5 → **0**.
- Revertir: `adb shell settings put global window_animation_scale 1` (idem transition y animator).

## 3. Verificador de apps de Play (off)
- `package_verifier_enable` 1 → **0**, `upload_apk_enable` → 0.
- Revertir: `adb shell settings put global package_verifier_enable 1`

## 4. Apps DESACTIVADAS (20) — reversibles con `pm enable`
Comando de revertir por app: `adb shell pm enable <paquete>`

**Cámaras duplicadas (5):**
- `com.mm.android.direct.gdmsspadLite`
- `com.mm.android.DMSS`
- `com.mm.android.DMSSHD`
- `com.mm.dss`
- `com.ichano.athome.camera`

**Personales sin uso (4):**
- `com.grability.rappi`
- `com.pedidosya`
- `com.sand.airmirror`
- `com.google.android.apps.chromecast.app`

**Extra (1):**
- `com.google.ar.core`

**Bloatware Amazon desactivable (10):**
- `com.amazon.client.metrics.api`
- `com.amazon.imp`
- `com.amazon.zico`
- `com.amazon.iris`
- `com.amazon.dcp`
- `com.amazon.storagemanager`
- `com.amazon.avod` (Prime Video)
- `com.amazon.cloud9` (navegador Silk)
- `com.amazon.cloud9.kids`
- `com.amazon.kindle`

## 5. Servicios Amazon PROTEGIDOS — estrangulados (no desactivables sin root)
No se pudieron desactivar, pero se mandaron a bucket restringido + background denegado:
`am set-standby-bucket <pkg> restricted` + `cmd appops set <pkg> RUN_ANY_IN_BACKGROUND ignore`

Paquetes: `client.metrics`, `device.metrics`, `device.crashmanager`, `device.logmanager`, `device.messaging`, `device.backup`, `device.sync`, `sync.service`, `securitysyncclient`, `diode`, `kindle.kso` (anuncios de pantalla), `device.software.ota`, `device.software.ota.override`, `kindle.otter.oobe.forced.ota`, `tcomm`, `tcomm.client`, `venezia` (appstore), `whisperlink.core.android`, `whisperlink.activityview.android`.

- Revertir: `adb shell cmd appops set <pkg> RUN_ANY_IN_BACKGROUND allow` + `adb shell am set-standby-bucket <pkg> active`
- Nota: algunos quedaron en bucket 5 (exentos por el sistema) → no bajan más sin root.

## Techo sin root
Amazon blinda anuncios (`kindle.kso`), telemetría exenta, appstore (`venezia`), OTA. Para más habría que **rootear** — no recomendado en producción.

## Lo de mayor impacto que queda (NO es ADB)
1. En **gDMSS**: pasar las cámaras a **substream / SD** (el decodificado de video es hoy el consumo #1).
2. Ver menos cámaras simultáneas.
3. Hardware: batería dummy + ventilación (ver [[diagnostico]]).

## Ver también
- [[fire]]
- [[diagnostico]]
- [[contexto]]
