# Los 3 caminos para tener la terminal

Resumen de las opciones evaluadas en la sesión (research 2026-09-09 → 09-12).

| Camino | Estética Droid | Esfuerzo | Teclado | Veredicto |
|---|---|---|---|---|
| **Flashear Droid 4 (postmarketOS)** | ✅ Es un Droid real | 🟢 Bajo (solo flashear) | ✅ Funciona | **🏆 Recomendado** |
| Reshell (vaciar Droid, meter Pi) | ✅ Idéntica | 🔴🔴 Alto | ⚠️ Reingeniería del flex | Solo si el Droid 4 no arranca |
| Construir de cero (Pi + slider 3D) | 🟡 Aproximada | 🔴🔴🔴 Muy alto | ⚠️ Diseñarlo | Proyecto "maker" aparte |

## 1. Flashear el Droid 4 → [[flashear-droid4-postmarketos]]
Comprás un Droid 4 usado y le ponés postmarketOS. Bash + WiFi + teclado slider sin
construir nada. **El camino ganador.**

## 2. Reshell (donor-phone cyberdeck)
Vaciás un Droid y le metés una [[hardware-placa|Pi Zero 2 W]], conservando carcasa y
slider. Verificado que es posible:
- **Teclado:** se reutiliza haciendo ingeniería inversa del flex (FPC) → enchufás el flex
  a un breakout con **Raspberry Pi Pico** que **auto-detecta la matriz** (sin multímetro).
  Refs: método de Frank Adams (laptop→USB), proyecto **Nokia N97 Cyberdeck Resurrection**.
- **Pantalla:** la original casi seguro NO se reusa (panel paralelo/DSI propietario) →
  reemplazo por panel chico HDMI/DSI (Pi Hut 3.5" 640×480 ~£42, Waveshare 4.3" DSI).
- **Slider:** se puede conservar al vaciar el teléfono (iFixit muestra el mecanismo).

## 3. Construir de cero → [[construccion-teclado-droid]]
Diseñás matriz + RP2040 + QMK/KMK, slider impreso 3D estilo **Zero Terminal v3** (NODE),
partiendo del PCB open-source de Bobricius. Para el teclado ver [[teclado-comparativa]].

## Ver también
- [[blu-terminal]]
- [[modelos-droid]]
- [[render]]
