---
title: N910 Hardware Reference (predecesor del N950)
tags: [n910, n950, hardware, reverse-engineering, fcc]
fecha: 2026-05-23
---

# N910 — Hardware Reference

El N910 es el **predecesor del N950** y comparte fabricante/familia. La FCC publicó las fotos internas del N910 (a diferencia del N950 que está bajo confidencialidad permanente). Esto nos da un baseline arquitectónico.

> [!warning] El N950 NO es N910
> El N950 usa **A53 quad @ 2.0GHz + 4GB RAM + 64GB**.
> El N910 usa **A7 quad @ 1.1GHz + 1GB RAM + 8GB**.
> **Son SoCs distintos** — el N950 NO usa Quectel SC20-A. Estos hallazgos sirven como referencia de **familia**, no como mapa exacto.

## SoC del N910 (confirmado por fotos FCC)

- **SoC:** Qualcomm **MSM8909** (Snapdragon 210) — visible en foto "2G&3G&4G Chip View"
- **Módulo contenedor:** **Quectel SC20-A**
- **RAM:** SK hynix LPDDR3 1GB (PoP sobre SoC)
- **Storage:** 8GB eMMC (default según datasheet SC20)
- **Arquitectura:** ARM Cortex-A7 quad @ 1.1 GHz, 512KB L2

## Quectel SC20-A — interfaces relevantes para reverse engineering

Datasheet bajado en `n950-research/fcc/datasheets/quectel-sc20-hardware-design-v3.pdf` (133 páginas).

| Interfaz | Pines | Uso |
|----------|-------|-----|
| **UART1** | 34 TX / 35 RX / 36 CTS / 37 RTS | 4-wire, HW flow control, hasta 4 Mbps |
| **UART2** | 94 TX / 93 RX | **Debug UART** (2-wire) — *este es el target* |
| USB | 13 DM / 14 DP / 15 GND / 16 ID | AT cmds, data, **software debug**, firmware upgrade |
| RESET_N | (PMIC) | Reset hardware |
| PWRKEY | (PMIC) | Power on |
| **Emergency Download** | (sec 3.x) | Modo EDL — interface documentado |

## Layout del PCB (N910)

Visible en FCC internal photos (`fcc/n910/int/`):
- **Main Board Top View:** SIM slots, conector cámara, antenas conectorizadas (u.FL)
- **Main Board Unshielded Bottom View:** SoC MSM8909 + RAM PoP expuestos cuando se retira la lata de blindaje
- **Antenas separadas en PCBs auxiliares:** 2G/3G/4G, WiFi, GPS, NFC — cada una con etiqueta `ZTX-N910-XXX-ANT-R-V1.0`

## Implicancias para el ataque

### Lo que sí transfiere al N950 (high confidence)
- **Modo EDL existe** — Qualcomm-wide feature. El N950 también lo tiene; lo que cambia es el chipset (loader distinto)
- **Debug UART probablemente exista** — Newland reusó el bare-board del N910 (mismo form-factor handheld), y el form-factor del N950 es similar
- **Storage es eMMC** (no UFS) — chip-off es viable con un programmer eMMC común

### Lo que NO transfiere (sin verificar)
- Pinout específico de los test points — el módulo del N950 NO es SC20 (A53 quad @ 2GHz vs A7 quad @ 1.1GHz)
- Loader EDL del MSM8909 NO funciona en el SoC del N950
- Layout del PCB es diferente (el N950 tiene 4× la RAM y 8× el storage)

## Próximos pasos

1. **Abrir un N950 físicamente** para:
   - Confirmar el módulo (etiqueta Quectel/Fibocom/Newland)
   - Ubicar el debug UART (probable: 3 pads pequeños cerca del SoC, con .1" spacing)
   - Buscar test point de EDL (un único pad cortocircuitable a GND)
2. **Una vez confirmado el SoC del N950**, buscar:
   - Loader EDL firmado para ese SoC en `bkerler/edl/Loaders/`
   - Datasheet del módulo Quectel correspondiente
3. **Comprar N950 barato** (eBay/MercadoLibre) para sacrificio — el actual queda como target final

## Referencias

- FCC ID N910: `2AM6U-N910` — https://fccid.io/2AM6U-N910
- FCC ID N950 (portable): `2AM6U-NA950` — https://fccid.io/2AM6U-NA950 (Int Photos confidenciales)
- FCC ID N950S (counter): `2AM6U-NA950S` — https://fccid.io/2AM6U-NA950S (Int Photos confidenciales)
- Archivos locales:
  - `n950-research/fcc/n910/int/` — 6 PDFs Internal Photos del N910
  - `n950-research/fcc/n910/ext/` — Ext Photos
  - `n950-research/fcc/n910/setup/` — Setup Photos
  - `n950-research/fcc/datasheets/quectel-sc20-hardware-design-v*.pdf` — pinout SC20

## Wikilinks

- Padre: [[n950-research]]
- Relacionado: [[vectores-ataque]], [[exploits-edl]]
