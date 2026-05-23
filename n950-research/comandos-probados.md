# Comandos probados — Tabla exhaustiva

Resultados de todos los comandos fastboot/OEM/USB-raw probados en el N950.

> **Fuente canónica:** `/Users/hermess/www/ml/n950-research/COMMANDS_TESTED.md` (más detalle). Esta nota es resumen.

## fastboot getvar — Variables expuestas

### Existen y dan info útil

| Variable | Valor |
|---|---|
| `product` | `bengal` |
| `variant` | `QCM EMMC` |
| `hw-revision` | `10000` |
| `serialno` | `NCD100037318` |
| `secure` | `yes` |
| `unlocked` | `no` |
| `kernel` | `uefi` |
| `max-download-size` | `399505408` (~381 MB) |
| `abl-version` | `59` |
| `xbl-version` | `56` |
| `off-mode-charge` | `1` |
| `logical-block-size` | `0x200` |
| `erase-block-size` | `0x200` |
| `battery-soc-ok` | `yes` |

### NO existen (todas devuelven `Variable Not found`)

- Variables custom Newland/MercadoPago/POS (todos los prefijos `nl_*`, `mp_*`, `newland_*`)
- `is_unlocked`, `slot-count`, `current-slot`, `board`, `platform`
- `secure-boot`, `vbmeta-state`, `soc-id`, `chipid`
- `boot-mode`, `current-bootmode`, `carrier-id`, `project-id`, `product-id`
- Decenas más confirmadas en fuzz masivo

## fastboot oem — Comandos existentes

**Whitelist completa (solo 3 + 1):**

| Comando | Args | Resultado |
|---|---|---|
| `oem off-mode-charge` | `0` / `1` | ✅ OKAY (cambia estado) |
| `oem off-mode-charge` | args inválidos | ⚠️ `Invalid input entered` — validador estricto, NO vulnerable |
| `oem select-display-panel` | — | ✅ OKAY (con o sin args, args ignorados) |
| `oem enable-charger-screen` | — | ✅ OKAY (idem) |
| `oem device-info` | — | ✅ retorna Verity/unlocked/critical-unlocked/charger-screen states |

## fastboot flash / stage / boot

| Comando | Resultado |
|---|---|
| `fastboot stage <file>` | ✅ OKAY — carga arbitraria en RAM (hasta 381 MB) |
| `fastboot boot <file>` | ❌ `Booting FAILED (unknown command)` — subcomando NO implementado |
| `fastboot flash <partition> <img>` | 🔒 rechazado por device locked |
| `fastboot flash '<X>:' <img>` con colon trick | 🟡 verify err uniforme — ver [[verify-pipeline]] |

## fastboot reboot

| Target | Resultado |
|---|---|
| `reboot bootloader` | ✅ funciona |
| `reboot edl` / `reboot-edl` / `reboot dload` / etc. | ❌ cliente fastboot v37 rechaza con `unknown reboot target` |

## fastboot flashing

| Comando | Resultado |
|---|---|
| `flashing unlock` | 🟡 se cuelga sin mostrar prompt en pantalla (bootloader ignora) |
| `flashing get_unlock_ability` | ✅ retorna `0` — unlock DISABLED a nivel firmware |

## USB raw (pyusb, bypass cliente)

Script: `/tmp/edl/raw_reboot_edl.py`

| Comando enviado | Respuesta |
|---|---|
| `reboot-edl` | ✅ `OKAY` — bootloader **ACEPTA**, device se desconecta, **PERO reboota a Android normal**, NO a EDL 9008. Neutralizado por Newland |
| Otros reboot variants raw | No llegan — device ya se desconectó del primer aceptado |

Ver [[stack#Lecciones técnicas (gotchas)]] para detalle del bypass.

## Fuzz raw masivo (5.701 strings, sesión 2026-05-22)

| Categoría | Cmds | Hits reales | Conclusión |
|---|---|---|---|
| `getvar:*` custom (NL/MP/POS/estándar) | 583 | **0** | Todas → `Variable Not found` |
| `oem` dev/engineer/factory/rma/service/debug | 360 | **0** | Todas → `unknown command` |
| `oem` chinos transliterados | 48 | **0** | Sin pinyin namespace |
| `oem` numéricos / hex IDs | 16 | **0** | No usan command-by-ID |
| Top-level no-`oem` | 70 | **0** | Solo verbos estándar fastboot |
| `oem` POS específico (EMV/PIN/DUKPT/RKL/TMS/NFC/magstripe/printer/ica) | 4.624 | **0** | Lógica payment en app Android, no bootloader |
| **TOTAL** | **5.701** | **0** | Command surface vacía |

## Análisis del verify pipeline (sesión 2026-05-23)

5 experimentos de `flash 'aboot:'` con imágenes generadas localmente. Todos retornaron `image verify err` independientemente del input. Ver [[verify-pipeline]] para detalle completo.

## Inspección USB descriptors (sesión 2026-05-23)

Vía `/tmp/edl/usb_descriptors.py` con pyusb directo. Endpoints/interfaces completos del device en fastboot:

| Campo | Valor |
|---|---|
| VID:PID | `0x18D1:0xD00D` |
| bcdUSB / bcdDevice | `0x0210` / `0x0100` |
| bNumConfigurations | **1** |
| Config 1 → Interfaces | **1** |
| Interface 0.0 class/sub/proto | `0xFF / 0x42 / 0x03` (Google fastboot) |
| iInterface | `'fastboot'` |
| Endpoints | `ep 0x81 IN BULK` 512B + `ep 0x01 OUT BULK` 512B |
| Strings | `Google`, `Android`, `ncd100037318`, `fastboot` |
| MS OS string desc (0xEE) | ❌ pipe error (sin WebUSB) |
| BOS desc | ✅ USB 2.0 ext + SuperSpeed + container ID (boilerplate Qualcomm) |

**Conclusión:** sin interfaces Sahara/Firehose/Diag/DM/NMEA expuestas. El N950 en fastboot habla 100% protocolo fastboot estándar Google. Para acceder a protocolos Qualcomm de servicio → solo por hardware (forzar EDL 9008 desde test points).

## fastboot continue

✅ `Resuming boot OKAY`. Sale del bootloader, arranca Android, termina en welcome screen MercadoPago. **USB cliente disabled** en runtime — ni fastboot ni adb.

## Ver también

- [[verify-pipeline]] — análisis profundo del verify
- [[arquitectura]] — contexto hardware
- [[vectores]] — qué no se probó aún
- [[stack]] — herramientas usadas
