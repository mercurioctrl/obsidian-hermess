# Stack — Herramientas y entorno

## Entorno

- **Host:** macOS Sequoia 25.3 (Darwin), Apple Silicon M-series (T8132)
- **Shell:** zsh
- **Python:** 3.x con venv en `/tmp/edl/venv`

## Herramientas instaladas

| Tool | Path | Uso |
|---|---|---|
| `fastboot` | `/opt/homebrew/bin/fastboot` (v37) | Cliente Android Platform Tools |
| `adb` | `/opt/homebrew/bin/adb` | Android Debug Bridge |
| `pyusb` | venv `/tmp/edl/venv` | Comunicación raw USB |

## Repos clonados (en `/tmp/edl/`)

| Repo | URL | Para qué |
|---|---|---|
| `bkerler/edl` | https://github.com/bkerler/edl | Toolkit Qualcomm EDL/Sahara/Firehose |
| `bkerler/Loaders` | https://github.com/bkerler/Loaders | Loaders firehose por chipset (sin N950) |
| `qualcomm_gbl_exploit_poc` | https://github.com/hicode002/qualcomm_gbl_exploit_poc | PoC exploit GBL 2026 (no aplicable) |

⚠️ `/tmp/` se borra al rebootar la Mac. Re-clonar si faltan.

## Scripts custom (en `/tmp/edl/`)

| Script | Propósito |
|---|---|
| `raw_reboot_edl.py` | Comunicación pyusb directa al bulk endpoint (bypass cliente fastboot) |
| `fuzz_oem.py` | Fuzzer raw masivo con diccionario combinatorio (NL/MP/POS/chinos/dev/numéricos/top) |
| `make_fake_boot.py` | Generador de Android boot.img v0 con header válido |
| `fuzz_partitions.sh` | Fuzz de partition names via flash con colon trick |

## Lecciones técnicas (gotchas)

### Cliente fastboot v37 filtra strings antes de mandarlas

Comandos como `reboot edl` son **rechazados por el cliente** antes de comunicarse con el device. Usar pyusb raw al bulk endpoint para bypasear esa restricción. Ver memoria `feedback_pyusb_raw_bypass` o este patrón en `/tmp/edl/raw_reboot_edl.py`.

### macOS Sequoia + fastboot v37 cuelga el handle USB

Después de un comando que se cuelga (`flash` con archivo dummy inválido, `flashing unlock`), el handle USB queda trabado:
- `fastboot devices` sigue listando OK
- Pero todo bidireccional se cuelga

**Solución:** `pkill -9 fastboot`, reconectar cable, o power-cycle del POS completo (Power 10s + Power+VolAbajo).

### Stage funciona, boot no

`fastboot stage <file>` acepta cualquier blob hasta `max-download-size` (~381 MB). Pero `fastboot boot` retorna `unknown command` — no podemos ejecutar payloads en RAM.

## Ver también

- [[arquitectura]] — hardware del N950
- [[changelog]] — sesiones donde se usaron estas herramientas
- [[memoria]] — feedback técnico persistente
