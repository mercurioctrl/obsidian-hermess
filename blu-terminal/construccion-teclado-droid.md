# Construcción — Teclado slider tipo Motorola Droid/Milestone

Plan para **construir desde cero** el teclado QWERTY deslizable con D-pad/cruceta real
(flechas físicas), presentándose como teclado **USB HID** a la [[hardware-placa|Pi Zero 2 W]].
Resuelve el problema de [[hardware-teclado|las flechas]] que ningún teclado comprado tiene.

Research verificado: 2026-09-10.

## ⭐ Proyecto de referencia clave: Zero Terminal v3 (NODE)
Terminal Linux de bolsillo con **teclado slider casero**. La receta exacta:
- Usa el PCB open-source **"mini (Pi)QWERTY" de Bobricius** (~56 switches táctiles).
- Chip **SAMD21** (USB nativo) → lo convierte en teclado USB HID para la Pi.
- **El slider = soportes impresos en 3D + tornillos** sobre el PCB plano (no es mecanismo exótico).
- https://n-o-d-e.net/zeroterminal3.html
- PCB Bobricius: https://hackaday.io/project/158454

**Estrategia recomendada:** no diseñar PCB de cero → **forkear el PCB de Bobricius**,
agregarle la cruceta al layout, fabricar, y hacer el slider con impresión 3D.

## Electrónica de la matriz (verificado en docs QMK)
- Switches en **filas y columnas** (matriz) — no un cable por tecla.
- **1 diodo 1N4148 por tecla** en la pata de la fila → evita ghosting (Columna→Fila).
- El micro escanea columna por columna y lee todas las filas a la vez.
- Se expone como **USB HID** → la Pi lo ve como teclado normal, sin drivers.
- https://docs.qmk.fm/hand_wire · https://docs.qmk.fm/how_a_matrix_works

## Firmware — dos caminos
| Firmware | Lenguaje | Micro | Para quién |
|---|---|---|---|
| **QMK / VIAL** | C (config visual VIAL) | Pro Micro, Proton C, RP2040 | HID robusto, remapeo fácil de flechas/D-pad |
| **KMK** | **Python (CircuitPython)** | **RP2040 / Pi Pico** | Principiantes, arrancás en una tarde |
- KMK: https://github.com/KMKfw/kmk_firmware (nota: "limited life support" pero RP2040 sigue vigente)

## BOM aproximado (precios sin verificar — orientativos)
| Componente | Qué es | Aprox. |
|---|---|---|
| Switches | Kailh Choc low-profile / botones táctiles 6mm / domos silicona | ~$0.30 c/u × ~45 |
| Diodos 1N4148 | 1 por tecla | ~$2 el lote |
| Microcontrolador | RP2040 (Pi Pico) o Pro Micro | ~$4-8 |
| PCB | Diseñada en KiCad, fabricada en JLCPCB | ~$5-15 el lote |
| Cruceta/D-pad | 4 switches en cruz + tapa impresa 3D | — |
| Carcasa + slider | Impresión 3D | filamento |

## Otras referencias (canibalización, mismo Pi Zero 2 W)
- **Hackberry-Pi Zero** — reutiliza teclado BlackBerry Q10/Q20 vía breakout con MCU,
  remapeo por VIAL: https://github.com/ZitaoTech/Hackberry-Pi_Zero
- **Zepir FLIP** — Pi Zero 2 W con matriz real de 70 teclas.

## ⚠️ No verificado / advertencias
- **Canibalizar el flex del Droid/Milestone real**: NO se confirmó que nadie lo lograra.
  El flex es propietario y sin pinout público → usar el Droid como **molde estético**, no
  como electrónica.
- Precios exactos de Kailh Choc y costos JLCPCB no verificados (rate-limit).
- No se confirmó una plantilla KiCad lista para RP2040.

## Sugerencia de fases
1. **v1 candybar** (sin slider): matriz plana landscape + cruceta, RP2040 + KMK, USB HID.
   No pelear mecánica y electrónica a la vez.
2. **v2 slider**: agregar rieles/soportes 3D + resorte estilo Zero Terminal v3.

## Herramientas necesarias
- **KiCad** (diseño PCB, gratis) — la curva de aprendizaje más grande.
- **KMK o QMK/VIAL** (firmware).
- **Impresora 3D** (o servicio) para carcasa, tapas, slider.
- Soldadura básica.

## Ver también
- [[blu-terminal]]
- [[hardware-teclado]] — por qué ningún teclado comprado tiene flechas físicas
- [[hardware-placa]]
- [[proyectos-referencia]]
- [[lista-compra]]
