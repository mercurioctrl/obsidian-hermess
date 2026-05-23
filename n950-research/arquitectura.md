# Arquitectura — Newland N950

## Identidad del dispositivo

| Campo | Valor |
|---|---|
| Marca | Newland Payment Technology (NPT) |
| Modelo comercial | N950 (a.k.a. MercadoPago **Point Smart 2** en Argentina) |
| Año de generación | 2022+ (Android 12 stock) |
| Producto en bootloader | `bengal` |
| Variant | `QCM EMMC` |
| Hw revision | `10000` |
| Serial example | `ncd100037318` (prefijo `ncd` = Newland) |
| Vendor USB | `0x18D1` (Google — VID estándar Android) |
| Product USB (fastboot) | `0xD00D` (custom Newland) |

## Chipset

**Qualcomm QCM2290** — confirmado 2026-05-23. Cruzado entre Qualcomm device-finder (lista N950 y N950S bajo QCM2290) y specs Newland (A53 quad @ 2.0 GHz). La página china marketea "octa-core" pero el chip es quad-A53 — posiblemente cuenta cores del modem/security separados.

| Campo | Valor | Fuente |
|---|---|---|
| SoC | Qualcomm QCM2290 | Qualcomm device-finder |
| Codename board | `scuba` (familia Bengal) | AOSP `scuba.dtsi` |
| Arquitectura | ARMv8-A, Cortex-A53 quad @ 2.0 GHz | Newland specs |
| MSM_ID (Sahara) | `0x001860e1` | bkerler/Loaders filename |
| OEM_PK_HASH | `d9357db88795b5a8` | bkerler/Loaders filename |
| Kernel base AOSP | msm-bramble 4.19, Android 11/12 | AOSP devicetree |
| Reference board | `scuba-qrd` | Qualcomm RB |
| Security core | ARMv7-M @ 192 MHz (TrustZone SCM) | Newland specs |

**Loader EDL firmado disponible** — `loaders/qcm2290/001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf` (589 KB, sha256 `31bfaa2f66db4b72...`). Es un Firehose programmer DDR genérico Qualcomm, no model-specific Newland. Si Newland fused el SoC con OEM_PK propia (típico POS PCI), la PBL lo rechazará; pero hay que probarlo si conseguimos modo 9008.

Refs verificados:
- Loader: https://github.com/bkerler/Loaders/tree/main/qualcomm/model_generic/qcm2290
- DTSI scuba: https://android.googlesource.com/kernel/msm-extra/devicetree/+/refs/heads/android-msm-bramble-4.19-android11-qpr1/qcom/scuba.dtsi
- Geekbench (bot 403, abrir en browser): https://browser.geekbench.com/v4/cpu/17170434

Chipset secundario: "CPU de seguridad dedicada" mencionada en página oficial china — probablemente un Secure Element separado para procesar pagos (irrelevante para nuestro objetivo).

## Cadena de boot

```
PBL (ROM, Qualcomm)
  → SBL/XBL (Qualcomm Secondary Bootloader, version 56)
    → ABL (Application Bootloader, version 59)
      → UEFI/EDK2 (kernel: uefi reportado por fastboot)
        → boot.img (Android 12)
          → Android userspace (welcome screen waiting for MP activation)
```

**NOTA:** el N950 NO tiene la etapa **GBL (Generic Boot Loader)** que sí tienen los Snapdragon 8 Elite Gen 5. Por eso el exploit GBL de 2026 no aplica.

## Estado de seguridad (fastboot getvar)

```
secure: yes                              # Secure Boot activo
unlocked: no                             # Bootloader bloqueado
get_unlock_ability: 0                    # Unlock DISABLED a nivel firmware
Verity mode: true                        # dm-verity activo
Device unlocked: false
Device critical unlocked: false
abl-version: 59
xbl-version: 56
max-download-size: 399505408             # ~381MB (stage en RAM)
kernel: uefi
```

## Partition layout

Particiones detectadas vía `fastboot getvar all`:

**Estándar Android:**
- `boot` (96 MB) — kernel + ramdisk
- `recovery` (48 MB)
- `system` (parte de super)
- `super` (2.1 GB) — A/B dynamic partitions
- `userdata` (10.7 GB)
- `cache` (256 MB)
- `metadata` (16 MB)
- `vbmeta`, `vbmeta_system` (64 KB cada una)
- `dtbo` (10 MB)
- `misc` (1 MB)

**Qualcomm bengal específicas:**
- `abl` (1 MB) — Application Bootloader
- `fsc` (128 KB)
- `secdata` (25 KB)
- `multiimgqti` (32 KB)
- `mdcompress` (20 MB)
- `cateloader`, `catefv`, `catecontentfv` — Carrier/Authentication (Qualcomm)
- `uefivarstore` (512 KB) — UEFI variable store
- `toolsfv` (1 MB) — UEFI Tools Firmware Volume
- `splash` (33 MB)
- `spunvm` — secure processing unit non-volatile

**Newland custom (prefijo `nl`):**
- `nlFirmware` (200 MB) — firmware propietario Newland
- `nlconfigdata` (1 MB) — config Newland
- `privdata1`, `privdata2` (100 MB cada una) — datos privados
- `nvdata1`, `nvdata2` (1.5 MB cada una) — NV data
- `parameter` (50 MB)
- `hardwareCfg` (50 MB)
- `logdump` (64 MB)
- `limits` (4 KB)

## Whitelist OEM commands (descubierta por fuzz)

Solo **3 comandos OEM** existen en este bootloader (de 80+ probados):

| Comando | Args | Comportamiento |
|---|---|---|
| `oem off-mode-charge` | `0` o `1` (estricto) | Valida estrictamente. Rechaza args extras con `Invalid input entered`. **NO vulnerable a inyección** |
| `oem select-display-panel` | cualquier cosa | Acepta args silenciosamente. No los procesa (estado no cambia). |
| `oem enable-charger-screen` | cualquier cosa | Idem. |

**Comandos NO existentes** (todos retornan `unknown command`):
- Todos los OEM unlock variants
- Todos los Carlo Maragno's 35 (Pixel 3 reversed)
- Comandos vulnerables conocidos: `set-gpu-preemption[-value]`, `set-hw-fence-value`, `paxassert`
- Comandos de debug: `dmesg`, `ramdump`, `dump-chipid`
- Comandos de control USB raw: `reboot-edl`, `oem reboot-edl`, `reboot-dload`

## Comandos fastboot base

| Comando | Resultado |
|---|---|
| `fastboot getvar all` | Funciona, lista ~100 vars |
| `fastboot stage <file>` | **Funciona** — carga arbitraria en RAM |
| `fastboot boot <file>` | `unknown command` — no implementado |
| `fastboot flash <partition> <img>` | Rechazado con device locked |
| `fastboot flash 'aboot:' <img>` | **Pasa check inicial** (CVE-2023-4818 colon trick funcional) — pero requiere imagen firmada |
| `fastboot continue` | Funciona — boot a Android (welcome screen MP, USB cliente disabled en runtime) |
| `fastboot reboot bootloader` | Funciona |
| `fastboot reboot edl` | Cliente rechaza |
| Raw USB `reboot-edl` (via pyusb) | Aceptado con OKAY pero **neutralizado** — reboot a Android normal, NO a EDL 9008 |

## Hardening observado

Newland aplicó **endurecimiento por encima del estándar Qualcomm**:

1. **Whitelist OEM extrema** (3 commands vs ~35 típicos en bootloader Qualcomm de referencia)
2. **El único OEM con args validados** (off-mode-charge) sanitiza estrictamente — no vulnerable a inyección cmdline tipo GBL
3. **fastboot boot deshabilitado** (no se puede ejecutar payload staged)
4. **`reboot-edl` aceptado pero neutralizado** — saben que pyusb raw puede mandar comandos bloqueados por cliente, y los capturaron al nivel del bootloader
5. **USB cliente disabled en runtime normal** (post-`continue` el USB no se enumera)
6. **OEM unlock disabled a nivel firmware** (`get_unlock_ability: 0` — no flag toggleable)
7. **Secure Boot + dm-verity + Verified Boot activos**

## Modo download (USB)

El POS expone modo download por defecto cuando se enciende con `Power + Vol Abajo` desde apagado. En ese modo:
- VID: `0x18D1` (Google)
- PID: `0xD00D` (Newland custom — NO es 0xD001/D002 estándar fastboot)
- Interface class: `0xFF` (Vendor Specific), subclass `0x42`, protocol `0x3` → identifica como **fastboot estándar**
- Endpoints: Bulk IN `0x81` (512 bytes), Bulk OUT `0x01` (512 bytes)

Visualmente: pantalla negra con flecha de descarga blanca centrada.

## Modos confirmados no accesibles

- **EDL mode (9008)**: comando `reboot-edl` neutralizado. Sin acceso software. Solo accesible (potencialmente) via test points hardware.
- **Recovery mode**: combos botones no responden ni con dispositivo encendido.
- **Sideload mode**: nunca arranca a un Android que pueda exponer ADB.

## Anti-tamper hardware

POS de procesadoras de pago tienen Secure Element con anti-tamper físico:
- Apertura de carcasa borra claves criptográficas del SE (definitivo)
- Esto **no debería brickear** el dispositivo según diseño Qualcomm, pero algunos firmwares interpretan tamper como señal de bloqueo total
- En el N950 específicamente, **no hay reportes confirmados** de uno u otro caso

Para nuestro objetivo (impresora/utility, no pagos) el tamper del SE es irrelevante — perdemos capacidad de pago, pero esa nunca fue nuestra meta.
