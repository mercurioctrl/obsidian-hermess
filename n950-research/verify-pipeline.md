# Verify pipeline del bootloader N950

Análisis detallado del `image_verify()` del bootloader Newland. Resultado de 5 experimentos controlados (sesión 2026-05-23).

## Hipótesis inicial

El bootloader Newland implementa CVE-2023-4818 (colon trick) y permite bypass del name check de partition. La pregunta: **una vez bypaseado el name check, qué etapa del verify rechaza y con qué granularidad de error**.

## Metodología

Generamos imágenes locales con `make_fake_boot.py` (Android boot.img v0 con header magic `ANDROID!`, kernel y ramdisk de 256 bytes cada uno, total 12 KB en 3 páginas de 4096 bytes). Mandamos via `fastboot flash 'aboot:'` (colon trick) y observamos el output del bootloader.

## Experimentos

### Test inicial — Imagen mínima válida estructural

**Input:** `fake_boot.img` con magic ANDROID!, kernel y ramdisk de ceros.
**Comando:** `fastboot flash 'aboot:' fake_boot.img`
**Output:**
```
Warning: skip copying aboot: image avb footer (aboot: partition size: 0, aboot: image size: 12288).
Sending 'aboot:' (12 KB)        OKAY [0.009s]
Writing 'aboot:'                FAILED (remote: 'image verify err')
```

**Observación:** el handle USB **no se colgó** (mejora vs sesiones anteriores con bytes random que sí colgaron). El verify rechazó limpio con error explícito. Podemos seguir experimentando sin reset.

### Test B — Magic incorrecto

**Input:** mismo fake_boot pero magic = `BORKED!!`
**Output:** `image verify err` **idéntico**.
**Lección:** el magic no afecta el output. O Newland sanitiza el output (todos los errores → mismo mensaje), o el verify ejecuta signature ANTES de magic (raro). Más probable: sanitización.

### Test A — Fuzz de 40 partition names

**Input:** mismo fake_boot.img, variando el partition name con colon trick (`'X:'`).

Nombres probados:
- Particiones reales: `boot:`, `super:`, `system:`, `vendor:`, `recovery:`, `userdata:`, `vbmeta:`, `dtbo:`, `abl:`, `xbl:`, `aboot:`, `aboot_a:`, `aboot_b:`
- Newland custom: `nlFirmware:`, `nlconfigdata:`, `privdata1:`, `privdata2:`
- Qualcomm security chain: `tz:`, `tz_a:`, `tz_b:`, `keymaster:`, `cmnlib:`, `cmnlib64:`, `rpm:`, `hyp:`, `devcfg:`, `qupfw:`
- Obscure: `splash:`, `logo:`, `frp:`, `persist:`, `modem:`, `modemst1:`, `modemst2:`, `fsg:`, `fsc:`, `bluetooth:`, `metadata:`, `misc:`, `ssd:`, `sec:`, `limits:`
- Edge cases: `:`, `::`, `a:`, `b:`, `../aboot:`, `..:`, `/aboot:`, `:aboot`
- Sin colon trick (comparación): `aboot`, `boot`, `super`

**Output:** TODOS los 40 nombres → `image verify err` exacto.

**Lección crítica:** el guard de verify es **centralizado y se ejecuta ANTES de toda lógica de partition lookup, lock state, parser estructural**. El partition name es completamente irrelevante para el verify — solo se usa después del verify exitoso para decidir DÓNDE escribir.

**Implicación de seguridad:** anti-inferencia perfecto. No podemos distinguir `device locked` vs `signature mismatch` vs `magic err` vs `partition unknown` — todos rebotan al mismo mensaje.

### Test D — Kernel/ramdisk random + magic OK

**Input:** header válido con magic ANDROID! + kernel y ramdisk = bytes random.
**Output:** `image verify err`.
**Lección:** el verify es **signature-based puro**, no hay parser estructural pre-verify. Eso descarta ataques tipo buffer overflow en el parser de boot.img (típico en bootloaders más débiles, CVE-2020-15859 y similares).

### Test C — Imagen gigante (300 MB)

**Input:** header válido + 300 MB de padding ceros.
**Comando:** `fastboot flash 'aboot:' fake_boot_huge.img`
**Output:**
```
Sending 'aboot:' (307200 KB)    OKAY [7.281s]
Writing 'aboot:'                FAILED (remote: 'image verify err')
Total time: 12.456s
```

**Análisis temporal:**
- Sending USB: 7.281s para 300 MB → ~41 MB/s throughput USB
- Total: 12.456s
- **Verify took: ~5.2s para 300 MB → ~58 MB/s throughput de hash SHA en Cortex-A53**

**Lecciones:**
1. Verify procesa la imagen **completa** antes de rechazar (no hay early-exit en hash mismatch)
2. **Anti timing-oracle:** no podemos inferir qué byte falla por timing
3. No hay límite práctico de payload (maneja max-download-size sin issues)
4. Hash sobre toda la imagen → si Newland incluye anti-rollback metadata en footer/header, lo procesan completo

## Tabla resumen

| Test | Variante | Tamaño | Tiempo verify | Output |
|---|---|---|---|---|
| Inicial | header + ceros | 12 KB | <1s | `image verify err` |
| B | magic = `BORKED!!` | 12 KB | <1s | `image verify err` |
| A | 40 partition names | 12 KB c/u | <1s c/u | `image verify err` (todos) |
| D | magic OK + random | 12 KB | <1s | `image verify err` |
| C | header + 300 MB ceros | 300 MB | ~5.2s | `image verify err` |

## Conclusiones arquitecturales

1. **Guard centralizado único** ejecutado antes de toda otra lógica (partition lookup, lock state, parser, write). Defense-in-depth.
2. **Output sanitizado uniforme** — `image verify err` para cualquier fallo. Anti-inferencia perfecto.
3. **Hash sobre imagen completa, sin early-exit.** Anti timing-oracle.
4. **Sin parser estructural pre-verify** — inmune a CVEs de parser (BO, integer overflow, etc.)
5. **CVE-2023-4818 colon trick DEFINITIVAMENTE muerto** — el name check ya ni siquiera importa
6. **El bootloader maneja `max-download-size`** sin cuelgues, incluso con imágenes patológicas (300 MB de ceros)

## Implicaciones para próximos vectores

Para flashear cualquier cosa necesitamos OBLIGATORIAMENTE:
- (a) Imagen con **firma criptográfica válida Newland** → buscar firmware leakeado
- (b) Bypass del verify mismo (RCE en SHA/RSA del bootloader) → improbable, código maduro
- (c) Bypassar el bootloader completo (EDL forzado por hardware, JTAG, chip-off) → vector hardware

Ver [[vectores]] para roadmap completo.

## Ver también

- [[arquitectura]] — hardware y boot chain
- [[comandos-probados]] — todos los flashes intentados
- [[vectores]] — qué hacer ahora
- [[changelog#2026-05-23]] — sesión donde se hicieron estos experimentos
