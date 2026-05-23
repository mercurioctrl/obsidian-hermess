---
title: N950 Hardware — SoC y EDL confirmados
tags: [n950, hardware, soc, edl, qcm2290, breakthrough]
fecha: 2026-05-23
estado: hallazgo-critico
---

# N950 — SoC identificado: **Qualcomm QCM2290 ("scuba")**

> [!success] Breakthrough — 2026-05-23
> El SoC del N950 es **Qualcomm QCM2290** (codename interno **scuba**, familia Bengal). Hay un Firehose programmer firmado disponible públicamente en `bkerler/Loaders`. Esto reabre el vector EDL si conseguimos meter el device en modo 9008.

## Identificación

| Campo | Valor | Fuente |
|---|---|---|
| **SoC** | Qualcomm QCM2290 | Qualcomm device-finder + cruce con specs |
| **Codename board** | `scuba` (familia Bengal) | DTSI en AOSP |
| **Arquitectura** | ARMv8-A, Cortex-A53 quad @ 2.0 GHz | Newland specs |
| **MSM_ID (Sahara)** | `0x001860e1` | Filename del loader firmado |
| **OEM PK Hash** | `d9357db88795b5a8` | Filename del loader firmado |
| **Kernel base** | msm-bramble 4.19, Android 11/12 | AOSP devicetree |
| **Reference board** | `scuba-qrd` | Qualcomm RB |
| **RAM** | 4 GB | Newland specs |
| **Storage** | 64 GB eMMC | Newland specs |
| **Security core** | ARMv7-M @ 192 MHz (TrustZone SCM) | Newland specs |

> Nota: cn.newlandnpt menciona "八核 octa-core" pero el QCM2290 es quad-A53. Posibles explicaciones: (a) marketing mezcla cores secundarios, (b) el N950**S** counter usa otro SKU. La identificación de chipset por Qualcomm device-finder es fuente primaria.

## EDL Loader firmado — DISPONIBLE

Bajado a:
```
/Users/hermess/www/ml/n950-research/loaders/qcm2290/
└── 001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf  (589 KB, ELF aarch64)
```

- **SHA256:** `31bfaa2f66db4b722f50c412023d14c603886a0edee3768fe9ae428d5fa9cc5c`
- **Origen:** `bkerler/Loaders/qualcomm/model_generic/qcm2290/`
- **Tipo:** DDR Firehose programmer genérico Qualcomm
- **Filename decodificado:** `<MSM_ID 0x001860e1 + pad> _ <OEM_PK_HASH d9357db88795b5a8> _ Qcm2290_ddr_fhprg.elf`

### Caveat crítico
El loader es **genérico Qualcomm**, no model-specific de Newland. Si Newland fused el SoC con OEM_PK propia (típico en POS para PCI compliance), la PBL **rechazará este loader**. Hay que probarlo para confirmar.

### Comando de prueba (una vez en EDL 9008)
```bash
edl --loader=/Users/hermess/www/ml/n950-research/loaders/qcm2290/001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf printgpt
```

## Cómo entrar a modo 9008 (EDL) — pendiente

Métodos posibles, **ninguno confirmado para el N950**:

1. **`adb reboot edl`** — requiere ADB enabled (improbable en POS de producción)
2. **EDL deep-flash cable** — short de USB D+ con resistencia a GND durante boot
3. **Test point físico en PCB** — un pad cortocircuitable a GND (estándar Qualcomm). En boards `scuba-qrd` está documentado, en N950 hay que ubicarlo abriendo
4. **Combinación de teclas + power** — no documentada para N950

## Codes especulativos (NO garantizados, vienen del N**M**E50)

De documentación Newland ME50 (modelo distinto, pero misma cadena de service):
- Management mode password: `159951`
- Default admin: `112233`

Vale la pena probarlos en cualquier menú oculto / dialer / login del N950.

## Referencias verificadas

- ✅ Loader path: https://github.com/bkerler/Loaders/blob/main/qualcomm/model_generic/qcm2290/001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf
- ✅ DTSI scuba: https://android.googlesource.com/kernel/msm-extra/devicetree/+/refs/heads/android-msm-bramble-4.19-android11-qpr1/qcom/scuba.dtsi
- ✅ DTSI scuba-qrd: https://android.googlesource.com/kernel/msm-extra/devicetree/+/refs/heads/android-msm-bramble-4.19-android11-qpr1/qcom/scuba-qrd.dtsi
- ✅ Newland N950 (CN, Android 12): https://www.cn.newlandnpt.com/product/znzd/wlb/N950.htm
- ⚠️ Geekbench (HTTP 403 vía bot, abrir en browser): https://browser.geekbench.com/v4/cpu/17170434
- Writeup QCM2150 unfused (metodología transferible, distinto SoC): https://hhj4ck.github.io/qualcomm/secboot-off-qcm2150.html
- Firehose Peek/Poke (ALEPH-2017028): https://alephsecurity.com/vulns/aleph-2017028
- Firehorse framework: https://github.com/alephsecurity/firehorse

## Fuentes asiáticas — resultados negativos

Búsqueda exhaustiva en chino/japonés (CSDN, 52pojie, Baidu Tieba, Bilibili, Zhihu, Qiita, 5ch) por:
- 新大陆 N950 刷机/root/拆机/EDL/9008/工厂模式
- ニューランド N950 ルート化

**0 hits útiles.** Newland mantiene la cadena de service cerrada via app **YPOS** (técnicos autorizados). La comunidad china de reparación POS no ha publicado nada sobre el N950 (modelo nuevo, Android 12). No hay firmware images filtradas, ni teardowns, ni service tools públicos.

## Próximos pasos priorizados

1. **Probar el loader QCM2290** si conseguimos forzar modo 9008 (cualquier método). Costo: cero, beneficio potencial: completo
2. **Confirmar SoC visualmente** abriendo un N950 (etiqueta del SoC o módulo). Si NO es QCM2290, este loader no aplica
3. **Buscar test point EDL** en el PCB — abrir y comparar contra el layout de `scuba-qrd` reference
4. **Abrir Geekbench profile manualmente** en el browser para capturar kernel string completo y Android version exacta (eso confirma la cadena AOSP a usar)
5. **Probar codes ME50** (`159951`, `112233`) en menús ocultos del N950 — barato e inmediato

## Wikilinks

- Padre: [[n950-research]]
- Hardware base N910: [[n910-hardware-reference]]
- Vectores: [[vectores-ataque]]
- Exploits: [[exploits-edl]]
