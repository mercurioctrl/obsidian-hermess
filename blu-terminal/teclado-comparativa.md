# Comparativa de teclados para construir (similitud al Droid 4)

Research verificado: 2026-09-12. Objetivo: si se construye la terminal, qué teclado se
parece más al del Droid 4 en **tamaño y comodidad**.

| Teclado | Teclas | Tamaño | Comodidad | Conexión a la Pi | Precio |
|---|---|---|---|---|---|
| **ClockworkPi uConsole** | **74**, retroiluminado | landscape handheld | 🥇 La mejor (más teclas, buen tacto) | ⚠️ pines **POGO USB** internos (STM32) → hay que adaptarlos a USB | módulo repuesto |
| **Bobricius mini (Pi)QWERTY** | 36–56 táctiles | 107×65×20mm (8mm sin base) | 🥉 El creador admite *"nadie puede decir que es cómodo… solo escritura corta"* | ✅ **USB HID plug-and-play** (micro-USB + header 4-pin + I2C) | **$28.72** Tindie |
| Droid 4 (teclado salvado) | 5 filas | ~ancho del teléfono | 🏆 Referencia (el más cómodo) | Reingeniería del flex | — |

## Veredicto
- 🥇 **Máxima comodidad tipo Droid → teclado del ClockworkPi uConsole.** El más cercano
  (74 teclas, retroiluminado). Costo: se conecta por pines POGO USB al mainboard, hay que
  exponerlos como USB para la Pi. Es "USB por dentro", factible.
- ⚡ **Integración inmediata → Bobricius mini (Pi)QWERTY.** USB HID plug-and-play, $28,
  fácil de montar. Costo: es de pulgar y táctil, cómodo NO es.
- 🏆 **Fidelidad total → salvar el teclado del Droid 4** (ver [[caminos|reshell]]).

## ⚠️ Sin verificar (rate-limit)
Dimensiones exactas del teclado del Droid 4, "King of the QWERTY", venta como repuesto,
Beepy/BBQ20 y MutantC → no confirmados en esta ronda.

## Nota irónica
Si lo que se busca es *de verdad* el tacto del Droid 4, el propio
[[flashear-droid4-postmarketos|Droid 4 flasheado]] lo da sin construir nada. Replicar un
teclado igual de cómodo es la parte más difícil.

## Enlaces
- ClockworkPi uConsole: https://www.clockworkpi.com/uconsole
- Bobricius mini (Pi)QWERTY: https://www.tindie.com/products/bobricius/mini-piqwerty-usb-wired-mechanical-thumb-keyboard/
- Hackaday 158454: https://hackaday.io/project/158454

## Ver también
- [[blu-terminal]]
- [[hardware-teclado]]
- [[construccion-teclado-droid]]
- [[caminos]]
