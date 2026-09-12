# BOM de construcción (plan B: construirlo con Raspberry Pi)

Research verificado: 2026-09-12 (100 agentes, 0 errores). Lista de materiales para la
réplica DIY tipo Droid con [[hardware-placa|Pi Zero 2 W]]. Complementa [[caminos]] y
[[construccion-teclado-droid]].

## 🔑 Restricción de arquitectura (verificada 3-0)
**El cable de una pantalla DPI no puede extenderse más de ~10 cm** (Waveshare: señales
paralelas → jitter, parpadeo, pantalla negra). Consecuencia: **la Pi vive en la mitad de
la pantalla** y a la mitad del teclado solo pasa **USB** (pogo pins), no un flex de 40 vías.
Para poner la Pi en la mitad del teclado haría falta HDMI (ver [[pantallas-wide]]).

## BOM núcleo verificada (USD, sin envío ni aduana)
| Pieza | Elección | Precio | Nota |
|---|---|---|---|
| Cerebro | Raspberry Pi Zero 2 W | ~$15 | dato de contexto |
| **Pantalla** | **Pimoroni HyperPixel 4.0** 800×480 IPS, DPI | £31.50–37.50 | ganadora para la Zero, ver [[pantallas-wide]]. Alternativa verificada: Waveshare 3.5" DPI 640×480 $29.99 (4:3, deja biseles) |
| **Teclado** ⚠️ | Bobricius mini PiQWERTY | **$28.72 = solo 3 PCBs desnudos** | sin componentes. Armado ~$72.92 y **agotado**. 107×65×20 (8 sin placa inf.). USB HID por Pi Pico (RP2040) |
| Energía A | PiSugar 3 (Zero) | $39.99 | 1200 mAh, apagado seguro, RTC, pogo. Obliga a apilar bajo la Pi |
| Energía B | Waveshare UPS HAT (C) | $23.99 | 1000 mAh, INA219 I2C, sin corte por software |
| **Energía C** (elegida) | PowerBoost 1000C + LiPo | $19.95 + $14.95 | única con 2000–3000 mAh; la LiPo puede ir en la mitad del teclado. Sin apagado seguro |

**Subtotal núcleo: ~$108–160.** Aduana argentina puede duplicarlo.

## Dato de diseño
LiPo 7.3–8 mm + Pi 5 mm = 12.3–13 mm → **no se pueden apilar** en un cuerpo fino; van
lado a lado o en mitades distintas. Ver [[grosor-y-medidas]].

## Slider (lo más honesto del research)
El **Zero Terminal v3** (única referencia verificada) usa **soportes 3D + tornillos** y su
autor admite que "necesita más trabajo para ser robusto"; el teclado **no funcionaba** al
publicarse (2020) y **no hay BOM publicada**. → Referencia de arquitectura, no diseño probado.

## Dificultad por etapa
| Etapa | Dificultad |
|---|---|
| Pantalla DPI (config.txt + header 40 pines) | 🟢 baja-media |
| Energía PiSugar/UPS HAT | 🟢 baja |
| Energía PowerBoost + LiPo | 🟡 media |
| Teclado desde PCB desnudo (soldar + flashear .uf2) | 🔴 alta |
| Slider impreso 3D | 🔴 alta (sin diseño probado) |

## ❌ Sin verificar (huecos)
Mecanismos slider comprados (rieles AliExpress), cables FPC para deslizamiento, carcasa y
**servicios de impresión 3D en Argentina**, tornillos, herramientas, MutantC/Hackberry/PicoCalc.

## Ver también
- [[blu-terminal]] · [[caminos]] · [[pantallas-wide]] · [[grosor-y-medidas]]
- [[construccion-teclado-droid]] · [[teclado-comparativa]] · [[hardware-energia]]
- [[render]] — ficha visual del build con estas piezas
