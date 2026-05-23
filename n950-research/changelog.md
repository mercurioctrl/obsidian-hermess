# Changelog — N950 Research

Registro cronológico de sesiones de investigación.

## 2026-05-23 (sesión 2 — breakthrough SoC + búsqueda asiática/inglesa)

**SoC del N950 identificado: Qualcomm QCM2290 (codename `scuba`, familia Bengal).**

### Identificación del SoC y loader EDL conseguido

- Cruce de Qualcomm device-finder + cn.newlandnpt + DTSI AOSP confirmó **QCM2290** (no QCM2150 ni SDM429 como se conjeturaba)
- Codename `scuba`, familia Bengal, MSM_ID `0x001860e1`, OEM_PK_HASH `d9357db88795b5a8`, kernel msm-bramble 4.19, board scuba-qrd
- **Loader Firehose firmado bajado a `loaders/qcm2290/001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf`** (589 KB, sha256 31bfaa2f..., ELF aarch64)
- Origen: bkerler/Loaders. Está en `model_generic/` → probable PK del reference Qualcomm genérico, no específico Newland. Aplicabilidad real solo verificable probando en EDL 9008

### Investigación FCC — fotos PCB del N910 (predecesor) bajadas

- FCC del N950 (NA950 y NA950S): Internal Photos / Schematics / Block Diagrams bajo **confidencialidad permanente**. Solo Test Reports / SAR / Antenna Specs son públicos
- FCC del N910 (predecesor) sí publica Internal Photos → bajadas 6 PDFs a `fcc/n910/int/`. Confirmado: N910 = Qualcomm **MSM8909** dentro de módulo **Quectel SC20-A** (Cortex-A7 quad @ 1.1 GHz)
- Datasheet Quectel SC20 (133 pp) bajado a `fcc/datasheets/`. Pinout debug UART: UART2 = pines 94 TX / 93 RX. "Emergency download interface" documentado por Quectel
- **N910 ≠ N950 arquitectónicamente** — sirve solo como baseline de familia, no como mapa de pinout

### Búsqueda asiática profunda (CSDN, 52pojie, Baidu Tieba, Bilibili, Zhihu, Qiita, 5ch)

- Términos en chino: `新大陆 N950 刷机/root/拆机/EDL/9008/工厂模式`. Japonés: `ニューランド N950 ルート化`
- **0 hits útiles.** Modelo demasiado nuevo (Android 12, ~2023). Newland mantiene cadena de service cerrada via app **YPOS** (técnicos autorizados)
- Codes especulativos del modelo ME50 (no garantizados): mgmt password `159951`, admin `112233`

### Búsqueda inglesa profunda — vector nuevo encontrado

- **Writeup hhj4ck "Full-chain exploit of unfused Qualcomm device" (DEF CON 33 ago 2025)** sobre POS Qualcomm **QCM2150** unfused (familia hermana de QCM2290). Técnica: SBL1 firmado como segundo-loader con keys auto-generadas. URL: https://hhj4ck.github.io/qualcomm/secboot-off-qcm2150.html
- Quectel SC200E (módulo industrial QCM2290) tiene build env Android 12 — pero **NO público**, requiere NDA Quectel
- **PostmarketOS NO tiene port scuba/bengal** — verificado
- **Voltage glitching de bajo costo (PicoGlitcher SySS ~150 USD)** como vector nuevo hardware
- Correcciones: Moto E20/E22 NO es QCM2290 (Unisoc T606); realme C20A NO es QCM2290 (Helio G35)

### Documentación creada/actualizada

- Nuevas notas Obsidian: [[n950-hardware-soc-edl]], [[n910-hardware-reference]]
- Memorias Claude nuevas: `reference_n950_n910_hardware`, `reference_n950_soc_edl`, `reference_n950_top_vectors`, `feedback_webfetch_fccid_alucina`
- ARCHITECTURE.md sección Chipset rehecha con QCM2290 confirmado
- VECTORS.md sección "🎯 Lo más prometedor" rehecha con top 3 priorizados
- README.md actualizado con directorios `fcc/` y `loaders/`

### Lecciones técnicas

- **WebFetch alucina nombres de documentos en fccid.io.** Para listar docs reales usar página `/amp` + scraping de `<a href="document.php?id=N">`. Descargar via `pdf.php?id=N`
- Existe loader único QCM2290 en bkerler/Loaders (no múltiples variantes). Saber si carga requiere probar en EDL real

---

## 2026-05-23 (sesión 1 — verify pipeline + USB descriptors)

**Caracterización completa del verify pipeline del bootloader.**

- Generación de `fake_boot.img` válido con header Android v0 (script `make_fake_boot.py`)
- **Test inicial:** `fastboot flash 'aboot:' fake_boot.img` → `image verify err`. Bootloader llegó a verify sin colgar el handle (mejora vs sesión anterior con bytes random)
- **Test B (magic incorrecto):** mismo input con magic `BORKED!!` → `image verify err` idéntico. Magic no afecta output
- **Test A (fuzz 40 partition names):** todos los nombres (`boot:`, `super:`, `vbmeta:`, `nlFirmware:`, `:`, `::`, `../aboot:`, `:aboot`, sin colon `aboot`, etc.) → TODOS `image verify err`. **Hallazgo clave:** guard centralizado único
- **Test D (kernel/ramdisk random + magic OK):** `image verify err`. No hay parser estructural pre-verify
- **Test C (imagen 300 MB):** `image verify err` después de 5.2s. Hash completo ~58 MB/s, sin early-exit

**Conclusión:** verify pipeline blindado por encima del estándar Qualcomm. CVE-2023-4818 colon trick definitivamente muerto. Próximos vectores: hardware o firmware firmado.

**Documentación actualizada:** `COMMANDS_TESTED.md` (sección verify pipeline), `VECTORS.md` (cleanup), `project_n950_challenge.md` (memoria), nota Obsidian.

**Scripts creados:**
- `/tmp/edl/make_fake_boot.py` — generador de Android boot.img v0
- `/tmp/edl/fuzz_partitions.sh` — fuzz de partition names via flash

### Inspección USB descriptors profunda

Vía `/tmp/edl/usb_descriptors.py` con pyusb. Enumeración completa del device en modo fastboot:

- **1 configuración / 1 interface / 2 endpoints bulk** (IN 0x81, OUT 0x01, 512B)
- Interface class/sub/proto = `0xFF / 0x42 / 0x03` con `iInterface = 'fastboot'` (Google fastboot estándar)
- Strings: `Google`, `Android`, `ncd100037318`, `fastboot`
- BOS descriptor presente (USB 2.0 ext + SuperSpeed + container ID — boilerplate Qualcomm)
- MS OS string descriptor (0xEE) → pipe error (no WebUSB, no advertising vendor)

**Conclusión:** no hay interfaces alternativas Sahara/Firehose/Diag/DM/NMEA expuestas. Para acceder a protocolos Qualcomm de servicio hay que **forzar EDL 9008 por hardware** (test points / fuerza desde reset). Vector residual #2 cerrado.

**Scripts creados:**
- `/tmp/edl/usb_descriptors.py` — enumeración USB completa via pyusb

---

## 2026-05-22

**Sesión inicial + fuzz raw masivo + configuración bóveda.**

### Identificación del device
- Device conectado por USB → identificado como **Newland N950** (MercadoPago Point Smart 2)
- Chipset Qualcomm `bengal` confirmado via `getvar product`
- 4 modos de boot identificados (normal, download, recovery, factory implícito)

### Búsqueda exhaustiva de firmware
- Foros AR/BR/RU/CN/EN (5+ idiomas, 10+ comunidades): firmware N950 NO disponible públicamente
- Payment Product Tools v2.3.4 chino: NO soporta N950 (solo serie vieja NL8xxx/NLGPxxx/SPxx/ME31S)
- Comunidad 3DGames AR: estancada hace meses en el mismo punto

### Exploitación fastboot
- `flashing get_unlock_ability` → `0` (disabled a nivel firmware)
- Whitelist OEM extrema confirmada (3 comandos custom)
- CVE-2023-4818 colon trick: name check pasa pero verify rechaza
- CVE-2023-42134 PAX: no aplica (no compartió código)
- Exploit GBL 2026: no aplica (chipset entry-level sin etapa GBL)

### USB raw bypass del cliente fastboot
- Script `raw_reboot_edl.py` con pyusb directo al bulk endpoint
- `reboot-edl` raw: aceptado con `OKAY` pero **neutralizado internamente** (rebootea a Android normal, no a EDL 9008)
- Lección documentada: cliente fastboot v37 filtra strings, pyusb permite bypass

### Fuzz raw masivo
- Script `fuzz_oem.py` con diccionario combinatorio de 8.829 comandos
- Pasada efectiva: 5.701 cmds (blacklist de strings que rebootean)
- Categorías probadas: getvar custom, oem dev/engineer/factory/rma, chinos transliterados, numéricos, top-level, oem POS (EMV/PIN/DUKPT/RKL/TMS/NFC)
- **Resultado: 0 hits**. Sin comandos custom escondidos

### Configuración base de conocimiento
- Pivot del proyecto: utilitario → desafío personal de hacking
- Documentación completa creada en `/Users/hermess/www/ml/n950-research/` (7 docs)
- 6 memorias Claude persistentes creadas
- Bóveda Obsidian `n950-research/` vinculada
- Project CLAUDE.md con config Obsidian

---

## Ver también

- [[arquitectura]] — análisis hardware y boot chain
- [[n950-hardware-soc-edl]] — SoC QCM2290 + loader EDL
- [[n910-hardware-reference]] — predecesor N910 (baseline)
- [[comandos-probados]] — tabla exhaustiva
- [[verify-pipeline]] — análisis del verify centralizado
- [[vectores]] — qué queda por probar
