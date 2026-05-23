# Vectores de ataque — N950

## ❌ Agotados (probados y sin éxito)

### Software via fastboot
- **Exploit Qualcomm GBL 2026** (`oem set-gpu-preemption[-value]`) — chipset bengal entry-level NO tiene la etapa GBL (es de Snapdragon 8 Elite Gen 5)
- **`oem set-hw-fence-value`** — comando no existe
- **CVE-2023-4818 colon trick** — la sintaxis `'aboot:'` SÍ funciona y bypassa el name check, pero requiere imagen firmada válida que no tenemos
- **CVE-2023-42134 PAX** — `oem paxassert` no existe (Newland no compartió código con PAX)
- **`fastboot flashing unlock`** — `get_unlock_ability: 0` confirmado, deshabilitado a nivel firmware
- **`fastboot boot <unsigned>`** — subcomando "boot" no implementado en el bootloader
- **Fuzz OEM 80+ comandos manuales** — solo 3 existen, ninguno vulnerable a inyección
- **`fastboot reboot edl`** — cliente bloquea
- **USB raw `reboot-edl` via pyusb** — aceptado con OKAY pero neutralizado por Newland (rebootea a Android normal)
- **Fuzz raw masivo pyusb (5.701 strings, sesión 2026-05-22)** — 0 hits. Probado: getvars custom (NL/MP/POS/estándar), oem dev/engineer/factory/rma, oem chinos transliterados, oem numéricos, top-level no-oem, oem POS (EMV/PIN/DUKPT/RKL/TMS/NFC/magstripe/printer/ica). Conclusión: NO existen comandos custom escondidos en el bootloader. Ver `COMMANDS_TESTED.md` final.
- **Inspección USB descriptors profunda (sesión 2026-05-23)** — única configuración con una sola interface `fastboot` (class 0xFF/sub 0x42/proto 0x03) y dos endpoints bulk (IN 0x81, OUT 0x01). Sin Sahara/Firehose/Diag expuesto, sin MS OS string descriptor, sin WebUSB. **Para acceder a protocolos Qualcomm de servicio hay que forzar EDL 9008 por hardware.** Ver `COMMANDS_TESTED.md` "Inspección USB descriptors".

### Búsqueda de firmware oficial
- **Foros AR/BR/RU/CN/EN** — ningún firmware N950 disponible públicamente (5+ idiomas, 10+ comunidades, búsqueda exhaustiva)
- **Newland Payment Tools v2.3.4** (leak chino) — soporta solo serie vieja (NL8xxx, NLGPxxx, SPxx, ME31S). N950 NO está en su lista
- **Sitios "gofirmware"** — sospechosos, requieren pago, sin verificación
- **Búsqueda asiática profunda (sesión 2026-05-23)** — CSDN, 52pojie, Baidu Tieba (新大陆吧/POS吧), Bilibili, Zhihu, Qiita, 5ch con términos `新大陆 N950 刷机/root/拆机/EDL/9008/工厂模式` y `ニューランド N950 ルート化`: **0 hits útiles**. Newland mantiene cadena de service cerrada via app **YPOS** (técnicos autorizados). Modelo demasiado nuevo (Android 12, ~2023) para que la comunidad china lo haya tocado
- **FCC del N950 (NA950 y NA950S)** — Internal Photos, Schematics y Block Diagrams están bajo **confidencialidad permanente** (no expiran a los 180 días como típico). Solo hay Test Reports, SAR, Antenna Specs públicos. FCC del N910 (predecesor) sí tiene Int Photos públicas — sirven como baseline arquitectónico pero NO mapean al N950 (chipset distinto: N910 = MSM8909 quad-A7; N950 = QCM2290 quad-A53)

### Comunicación intentos
- **Foros 3DGames AR thread oficial** — comunidad estancada hace meses en el mismo punto (welcome screen waiting)

## 🟡 No probados todavía (vale la pena explorar)

### Software residual
1. ~~**Fuzz raw masivo de comandos vía pyusb**~~ — **HECHO sesión 2026-05-22, 5.701 strings, 0 hits.**
2. ~~**Fuzz raw de getvar**~~ — **HECHO mismo run, 583 variables custom, 0 hits.**
3. ~~**CVE-2023-4818 con boot.img genérico**~~ — **HECHO sesión 2026-05-23 (4 experimentos). Verify centralizado, output sanitizado uniforme, hash sobre imagen completa sin early-exit. Ver COMMANDS_TESTED.md "Análisis del verify pipeline".**
4. **Modular `bkerler/edl` para hablar al fastboot Newland** custom — el PID `0xD00D` no es estándar pero igual habla protocolo fastboot. Vale la pena ver si edl.py tiene modo "fastboot-as-transport" para mandar comandos Sahara/Firehose por encima
5. ~~**Inspección USB descriptors completa**~~ — **HECHO sesión 2026-05-23. Sin interfaces alternativas. Solo fastboot estándar Google.**
6. **Buscar firmware leakeado del N950 en darkweb / canales privados** — no en buscadores públicos, sino en canales Telegram especializados

### Hardware (requiere abrir el equipo)
1. **Test points EDL en PCB** — buscar puente que cortocircuitado durante boot fuerce EDL 9008. Algunos POS Qualcomm tienen punto soldable bien conocido. Riesgo: anti-tamper SE. **Si llegamos a EDL 9008, ya tenemos el loader Firehose firmado** (`loaders/qcm2290/001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf`, sesión 2026-05-23). Probar con `edl --loader=... printgpt`. Caveat: loader genérico Qualcomm, puede ser rechazado por PBL si Newland fused OEM_PK propia
2. **Deep-flash USB cable (no requiere abrir)** — short de D+ a GND con resistencia (típicamente 150-910Ω) durante boot. Para Qualcomm bengal/scuba hay esquemas públicos. Probar antes que test points físicos
3. **JTAG / SWD test points** — control directo del SoC via debugger HW (J-Link, Riff Box). Requiere identificar JTAG layout específico del scuba/bengal en este PCB
4. **UART debug** — algunos POS tienen UART expuesta. Si lo logramos identificar, podemos ver logs del bootloader y posiblemente interactuar pre-Android. Para referencia del N910 (mismo fabricante, módulo Quectel SC20-A con MSM8909), UART2 debug está en pines 94/93 del SC20 — pinout en `fcc/datasheets/quectel-sc20-hardware-design-v3.pdf`
5. **eMMC chip-off** — soldar fuera el eMMC, dumpear con programador. Permite leer todo el firmware sin pasar por bootloader. ~USD 300 equipment, alta dificultad (BGA fina)

### Administrativo
1. **Email a Newland Payment Argentina** — pedir firmware como ONG/desarrollador/researcher
2. **Programa "developer" oficial de Newland NPT** — newlandpayment.com → portal developer
3. **Contactar distribuidor regional** (Datalogic, Cono Sur)
4. **Pedir a MercadoPago vía AFIP / abogado** la liberación oficial del equipo donado

## 🎯 Lo más prometedor para próxima sesión

(Actualizado tras 2026-05-23 — SoC confirmado QCM2290 + búsqueda inglesa profunda)

### Top 3 priorizados

1. **Leer writeup hhj4ck (DEF CON 33, ago 2025) — "Full-chain exploit of an unfused Qualcomm device"**
   - URL: https://hhj4ck.github.io/qualcomm/secboot-off-qcm2150.html | Twitter: https://x.com/hhj4ck/status/1952965963340759512
   - QCM2150 (familia hermana de QCM2290, también Bengal-entry) unfused. Técnica: usar **SBL1 firmado como segundo-loader** con keys auto-generadas en lugar de Firehose
   - Costo: 30 min de lectura. Probable rendimiento alto — describe cadena Sahara→SBL1→XBL→ABL específica para Bengal-family
   - Caveat: si el N950 está fused (OEM_PK custom Newland), no aplica directo

2. **Probar el loader QCM2290 que ya tenemos** apenas se logre entrar a EDL 9008
   - Path: `loaders/qcm2290/001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf` (sha256 31bfaa2f...)
   - **Importante**: el PK_HASH `d9357db88795b5a8` está en `model_generic/` de bkerler/Loaders — sugiere que es el del **reference design QCM2290 genérico Qualcomm**, NO específico de Newland. Si Newland NO refused el chip con su propia OEM_PK (incierto sin probar), este loader carga
   - Comando: `edl --loader=loaders/qcm2290/001860e100000000_d9357db88795b5a8_Qcm2290_ddr_fhprg.elf printgpt`

3. **Voltage glitching de bajo costo (PicoGlitcher SySS, ~USD 150)** apuntando al instante exacto del `reboot-edl` neutralizado
   - URL kit: https://blog.syss.com/posts/voltage-glitching-with-picoglitcher-and-findus/
   - Idea: la instrucción ARM que rebootea a Android normal en lugar de EDL 9008 es **una sola decisión binaria**. Glitchear VCC en ese momento puede saltarla → EDL sin abrir el equipo ni necesitar test points
   - Tutorial general: https://www.synacktiv.com/en/publications/how-to-voltage-fault-injection

### Otros vectores residuales

4. **Buscar firmware FIRMADO del N950 en canales especializados** (Telegram POS modding, XDA semi-privados, foros invitation-only) — con `aboot.img` firmado real podríamos flashear bootloader unlocked
5. **Quectel SC200E AOSP source tree (mismo SoC QCM2290)** — Quectel tiene build env `QCM2290_Android12.0_R02_r004-SC200E_rl` con XBL/ABL/sbl1 firmados de Quectel. ⚠️ **NO es descarga pública** — requiere registro como cliente Quectel / NDA. Si se consigue, diff vs Newland puede revelar si comparten chain-of-trust
   - Forum: https://forums.quectel.com/t/compiling-a-custom-kernel-module-for-the-sc200e-platform-using-the-qcm2290-android-12-0-build-environment/38227
6. **Análisis estático de bootloader bengal de otros vendors** — devices QCM2290 conocidos (top): Nokia C20/C30 (TA-1352/TA-1359, algunas units), Wiko T10/T50, Cricket Vision 3, AT&T Calypso 2 (U319AA). **Correcciones**: Moto E20/E22 NO es QCM2290 (es Unisoc T606); realme C20A NO es QCM2290 (es Helio G35)
7. **Planificar hardware: test points EDL + osciloscopio + lupa** — vector más probable de éxito a largo plazo:
   - Abrir el POS (atención al anti-tamper SE — puede brickear)
   - Para mapear pinout del PCB, usar **scuba-qrd.dtsi público** como referencia: https://android.googlesource.com/kernel/msm-extra/devicetree/+/refs/heads/android-msm-bramble-4.19-android11-qpr1/qcom/scuba-qrd.dtsi
   - Sondear pads con multímetro y matchear contra el reference design
8. **eMMC chip-off + dumpear con programador EMMC** — bypassa el bootloader completamente. Costo ~USD 300 (rework station + programador BGA), alta dificultad técnica

### Lectura técnica de referencia

- **Quarkslab — Qualcomm Secure Boot chains**: https://blog.quarkslab.com/analysis-of-qualcomm-secure-boot-chains.html
- **Quarkslab — Attacking ARM TrustZone**: https://blog.quarkslab.com/attacking-the-arms-trustzone.html
- **tryigit.dev — Qualcomm UEFI/GBL zero-day 2026**: https://tryigit.dev/qualcomm-uefi-gbl-bootchain-zero-day-exploit/
- **Pen Test Partners — Snapdragon 660 bootloader break (metodología)**: https://www.pentestpartners.com/security-blog/breaking-the-android-bootloader-on-the-qualcomm-snapdragon-660/

### ❌ Confirmado descartado en sesión inglesa 2026-05-23

- **CVEs 2024-2026 con PoC público que afecten QCM2290/Bengal bootloader** — Qualcomm Security Bulletins revisados, solo CVEs transient DoS sin escalation
- **PostmarketOS NO tiene port scuba/bengal** — verificado vs pkgs.postmarketos.org
- **alephsecurity/firehorse abandonado desde 2018** — útil solo como referencia teórica; Firehose moderno (post-2020) tiene peek/poke deshabilitado en programmers firmados
- **Newland source code leak (aboot/u-boot)** — no encontrado en ningún índice público
- **Firmware images del N950/NA950 leak** — no encontrado en web ni Telegram público

## ⚠️ Lo que NO vale la pena reintentar

- Búsqueda en Google de "Newland N950 firmware download" — ya hecho exhaustivamente
- Probar exploits documentados para Snapdragon flagship (8 Elite, etc.) — chipset entry-level es otra arquitectura
- `fastboot oem unlock` y variantes — confirmado bloqueado a nivel firmware
- Reintentar `Payment Product Tools v2.3.4` chino — confirmado por dos fuentes que no soporta N950
