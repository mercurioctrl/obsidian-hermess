# Memoria — Consolidación

Snapshot de las memorias persistentes Claude del proyecto. Path: `~/.claude/projects/-Users-hermess-www-ml/memory/`.

## 👤 Usuario

**hermess (Catriel Mercurio)** — Argentino, maker/dev, español rioplatense. Cómodo con CLI, fastboot, ADB, lectura de PoCs en C y Python (pyusb). Entiende Secure Boot, dm-verity, bootloader chain, USB descriptors, EDL/Sahara/Firehose. Trabaja en Mac (Sequoia M-series).

**Restricciones globales (de `~/.claude/CLAUDE.md`):**
- ❌ NUNCA agregar `Co-Authored-By` en commits
- ❌ NUNCA modificar autorías de git

**Estilo:** iterar rápido, simplicidad sobre complejidad, acepta veredictos honestos sobre infactibilidad, pero quiere agotar opciones técnicas antes de tirar la toalla. Pide explicaciones con detalle del "por qué".

## 🎯 Proyecto

**N950 Challenge** — Reverse engineering del Newland N950 (MercadoPago Point Smart 2).

**Why:** Originalmente uso utilitario (escuelita), pivoteado 2026-05-22 a desafío personal de hacking hobby.

**Estado (2026-05-23 sesión 2):** SoC del N950 confirmado **Qualcomm QCM2290** (codename `scuba`, familia Bengal). Loader Firehose firmado bajado local (`loaders/qcm2290/...`). Vector EDL **reabierto** si conseguimos modo 9008.
- Fuzz raw masivo fastboot 5.701 cmds → 0 hits (cerrado)
- Verify pipeline completamente caracterizado y blindado (cerrado)
- Próximos vectores: writeup hhj4ck QCM2150, probar loader QCM2290 en EDL, voltage glitching PicoGlitcher

**Cómo aplicar:** Al volver al proyecto, leer en orden:
1. [[n950-research]] (índice)
2. [[n950-hardware-soc-edl]] (SoC y EDL — hallazgo más reciente)
3. [[vectores]] (top 3 priorizados)
4. [[comandos-probados]] (no repetir)
5. [[verify-pipeline]] (caracterización del guard)

## 🔧 Hardware confirmado

- **SoC:** Qualcomm QCM2290 (codename `scuba`, familia Bengal)
- **MSM_ID Sahara:** `0x001860e1`
- **OEM_PK_HASH:** `d9357db88795b5a8` (probable reference Qualcomm genérico, no específico Newland — verificable solo en EDL real)
- **Kernel base AOSP:** msm-bramble 4.19, board `scuba-qrd`
- **CPU:** ARMv8-A, Cortex-A53 quad @ 2.0 GHz + ARMv7-M security core @ 192 MHz

## 📚 Hardware reference del predecesor N910

- **SoC:** Qualcomm MSM8909 (Snapdragon 210), Cortex-A7 quad @ 1.1 GHz
- **Módulo:** Quectel SC20-A (datasheet 133pp en `fcc/datasheets/`)
- **Pinout debug:** UART2 = pines 94 TX / 93 RX del SC20 (referencia conceptual, NO mapea al N950)
- Fotos PCB públicas en FCC (`fcc/n910/`)

## 💬 Feedback / lecciones técnicas

### Cliente fastboot v37 filtra comandos antes de mandarlos

Si `fastboot reboot <X>` falla con `unknown reboot target` o `usage:`, **NO significa que el bootloader no lo soporte**. El cliente filtra strings antes de comunicarse con el device. Bypass: pyusb directo al bulk endpoint.

**Patrón:** ver `/tmp/edl/raw_reboot_edl.py`. Endpoints en N950: Bulk IN `0x81`, Bulk OUT `0x01`, max packet 512.

### macOS Sequoia + fastboot v37 cuelga el handle USB

Después de un comando colgado (especialmente `flashing unlock` esperando prompt en pantalla, o `flash partition:` con archivo inválido), el handle queda trabado: `fastboot devices` sigue OK pero todo bidireccional se cuelga.

**Solución:** `pkill -9 fastboot adb` + reconectar cable + power-cycle POS.

### WebFetch alucina nombres de documentos en fccid.io

WebFetch sobre páginas índice de fccid.io inventa nombres de categorías (puede decir "Internal Photos APP #3 → ID 6598160" cuando el ID 6598160 en realidad es "Label & Label Location"). Newland tiene confidencialidad permanente sobre Internal Photos del N950 — esos docs NO existen públicamente, pero WebFetch los inventa.

**Solución:**
```bash
curl -sL "https://fccid.io/<FCCID>/amp" | \
  grep -oE '<a[^>]*href="https://fccid\.io/document\.php\?id=[0-9]+"[^>]*>[^<]+</a>' | \
  sed 's/.*id=\([0-9]*\)">/\1\t/; s|</a>||' | sort -u
```

Descargar PDFs vía `pdf.php?id=N` (URL directo al binario, no la página HTML).

**Regla general:** cuando uses WebFetch para enumerar contenido tipo índice, verificar contra HTML/AMP crudo antes de prometer URLs al usuario.

## 🔗 Refs principales (sesión 2026-05-23)

- Writeup hhj4ck QCM2150 unfused (DEF CON 33): https://hhj4ck.github.io/qualcomm/secboot-off-qcm2150.html
- Loader QCM2290 bkerler: https://github.com/bkerler/Loaders/tree/main/qualcomm/model_generic/qcm2290
- scuba-qrd.dtsi AOSP: https://android.googlesource.com/kernel/msm-extra/devicetree/+/refs/heads/android-msm-bramble-4.19-android11-qpr1/qcom/scuba-qrd.dtsi
- PicoGlitcher SySS (voltage glitching ~150 USD): https://blog.syss.com/posts/voltage-glitching-with-picoglitcher-and-findus/
- Quarkslab — Qualcomm Secure Boot chains: https://blog.quarkslab.com/analysis-of-qualcomm-secure-boot-chains.html

## Ver también

- [[n950-research]] — índice del proyecto
- [[n950-hardware-soc-edl]] — SoC QCM2290 + loader EDL
- [[n910-hardware-reference]] — predecesor MSM8909 + Quectel SC20-A
- [[arquitectura]] — espejo de ARCHITECTURE.md local
- [[vectores]] — top 3 priorizados
- [[changelog]] — historial sesiones
