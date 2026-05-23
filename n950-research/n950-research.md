# n950-research

Base de conocimiento del **desafío personal de reverse engineering del Newland N950** (a.k.a. MercadoPago Point Smart 2).

## Estado actual (actualizado 2026-05-23, sesión 2)

**Breakthrough:** SoC confirmado **Qualcomm QCM2290** (codename `scuba`, familia Bengal). Loader Firehose firmado bajado local. Vector EDL **reabierto** si conseguimos modo 9008. Vector software fastboot sigue cerrado.

## Notas del proyecto

### Índice y overview
- [[arquitectura]] — Hardware, boot chain, partitions, features de seguridad (con QCM2290 confirmado)
- [[verify-pipeline]] — Análisis de los 5 experimentos del verify (sesión 2026-05-23 parte 1)
- [[comandos-probados]] — Tabla exhaustiva de comandos fastboot/OEM/USB-raw con resultados
- [[vectores]] — Agotados vs residuales, top 3 priorizados al cierre
- [[contexto]] — Origen del proyecto, restricciones, decisiones
- [[stack]] — Herramientas, scripts custom, lecciones técnicas (gotchas)
- [[memoria]] — Consolidación de memorias persistentes Claude
- [[changelog]] — Historial cronológico de sesiones

### Hardware reference
- [[n950-hardware-soc-edl]] — **SoC QCM2290 confirmado**, MSM_ID + OEM_PK, loader Firehose bajado, refs verificadas
- [[n910-hardware-reference]] — Predecesor N910 con MSM8909 + Quectel SC20-A (baseline arquitectónico de FCC)

## Resumen rápido

### Hardware (confirmado 2026-05-23)

- **Modelo:** Newland N950 / MercadoPago Point Smart 2
- **SoC:** Qualcomm **QCM2290** (codename `scuba`, familia Bengal)
- **MSM_ID Sahara:** `0x001860e1` | **OEM_PK_HASH:** `d9357db88795b5a8`
- **Kernel base AOSP:** msm-bramble 4.19, reference board `scuba-qrd`
- **CPU:** ARMv8-A, Cortex-A53 quad @ 2.0 GHz + ARMv7-M security core @ 192 MHz
- **RAM/Storage:** 4 GB LPDDR / 64 GB eMMC
- **OS:** Android 12 stock
- **Bootloader:** UEFI/EDK2-based, Secure Boot activo, ABL v59 / XBL v56
- **USB en download mode:** VID `0x18D1` PID `0xD00D` (custom Newland)

### Hallazgos clave acumulados

1. Whitelist OEM extrema (solo 3 comandos custom, ninguno inyectable)
2. CVE-2023-4818 colon trick funcional en name check **pero verify centralizado** sin early-exit
3. Exploit GBL 2026 no aplica (Bengal entry-level sin etapa GBL)
4. `reboot-edl` raw aceptado pero **neutralizado** deliberadamente
5. USB cliente disabled en runtime — no se puede meter ADB
6. **Fuzz raw masivo 5.701 cmds (2026-05-22):** 0 hits
7. **Verify pipeline caracterizado (2026-05-23 parte 1):** guard centralizado único, hash completo sin early-exit
8. **USB descriptors:** solo fastboot Google estándar, sin Sahara/Firehose/Diag expuestos
9. **SoC identificado y loader EDL conseguido (2026-05-23 parte 2):** Qualcomm QCM2290 + Firehose firmado bajado
10. **Búsqueda asiática + inglesa profunda (2026-05-23 parte 2):** 0 hits en CSDN/52pojie/Baidu/Bilibili/Zhihu/Qiita/5ch. En inglés se encontró writeup hhj4ck (DEF CON 33) sobre QCM2150 unfused — familia hermana

## Top 3 vectores priorizados (próxima sesión)

1. **Leer writeup hhj4ck (QCM2150 unfused, DEF CON 33 ago 2025)** — https://hhj4ck.github.io/qualcomm/secboot-off-qcm2150.html — describe cadena Sahara→SBL1→XBL→ABL para Bengal-family
2. **Probar el loader QCM2290** apenas se logre entrar a EDL 9008 (path: `loaders/qcm2290/001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf`)
3. **Voltage glitching con PicoGlitcher (~150 USD)** para saltear la instrucción que neutraliza `reboot-edl`

## Para próxima sesión

Leer en orden:
1. Esta nota (overview + estado actual)
2. [[n950-hardware-soc-edl]] (SoC y EDL — el hallazgo más reciente)
3. [[vectores]] (top 3 priorizados)
4. [[comandos-probados]] (no repetir lo probado)
5. [[verify-pipeline]] (caracterización del guard centralizado)
6. Decidir: hardware (test points / glitching) o seguir buscando firmware firmado

## Docs técnicos locales

Path: `/Users/hermess/www/ml/n950-research/`

- `README.md` — overview y quickstart
- `ARCHITECTURE.md` — espejo de [[arquitectura]]
- `COMMANDS_TESTED.md` — fuente canónica de [[comandos-probados]]
- `VECTORS.md` — fuente canónica de [[vectores]]
- `TOOLS.md` — espejo parcial de [[stack]]
- `SETUP.md` — modos del POS, troubleshooting
- `EXPLOITS.md` — referencias CVEs (4818, GBL 2026, 42134)
- `fcc/n910/` — Internal/External/Setup photos del N910 (predecesor)
- `fcc/datasheets/` — Quectel SC20 Hardware Design (pinout UART/debug del N910)
- `loaders/qcm2290/` — Firehose programmer firmado para QCM2290

## Herramientas custom en `/tmp/edl/`

- `raw_reboot_edl.py` — comunicación pyusb directa al bulk endpoint
- `fuzz_oem.py` — fuzzer raw masivo (NL/MP/POS/chinos/dev/numéricos/top)
- `make_fake_boot.py` — genera Android boot.img v0 con header válido
- `fuzz_partitions.sh` — fuzz partition names via flash con colon trick
- `usb_descriptors.py` — enumera config/interfaces/endpoints/strings/BOS via pyusb

⚠️ `/tmp/` se borra al rebootar la Mac. Si las herramientas no están, re-clonar bkerler/edl y re-crear scripts (versionados en esta bóveda y memorias Claude).

---

*Última sincronización: 2026-05-23 (sesión 2)*
