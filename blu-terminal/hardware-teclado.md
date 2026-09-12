# Hardware — Teclado QWERTY físico

⚠️ **No completó verificación adversarial** (rate-limit). Datos de conocimiento general —
verificar stock y precio antes de comprar.

Lo que hace única a la terminal. Debe conectarse por **USB o I2C** (no GPIO), ver
[[hardware-pantalla]].

| Teclado | Precio aprox. | Conexión | Nota |
|---|---|---|---|
| **Solder Party BB Q20** (teclado BlackBerry + trackpad) | ~$30–40 | USB HID e I2C (RP2040 a bordo) | El mejor. Trackpad integrado. |
| Solder Party BB Q10 | ~$30 | USB / I2C / PMOD | Sin trackpad, más barato. |
| M5Stack CardKB | ~$12 | I2C | Mini, plano, teclas de goma. |

Usan teclados físicos reciclados de BlackBerry sobre un breakout con chip RP2040 → se
presentan como teclado USB estándar, Linux los reconoce sin driver raro.

## ⚠️ El tema de las flechas (importante para una terminal)
Los teclados BlackBerry **NO tienen teclas de flecha dedicadas** (son teclados de
smartphone). Para una terminal esto pesa: navegar historial de bash, mover el cursor y
editar dependen de las flechas. Se resuelven de dos formas:

1. **Combinación de firmware** — modificador (`alt`/símbolo) + tecla → ↑↓←→. Funciona
   pero es menos cómodo.
2. **Trackpad óptico** — solo en el modelo **Q20** (BlackBerry *Classic*), que trae la
   franja táctil. El **Q10 NO tiene trackpad**.

| Teclado | Trackpad | Flechas físicas |
|---|---|---|
| BB Q20 / BBQ20 (Classic) | ✅ Sí | ❌ No (cursor por trackpad + combos) |
| BB Q10 / BBQ10 | ❌ No | ❌ No (solo combos) |

El **Beepy** usa teclado tipo Q20 → tiene trackpad, pero **no flechas físicas reales**.

### Conclusión del research de flechas (2026-09-10) ✅ verificado
**No existe un teclado de pulgar QWERTY ultracompacto con flechas físicas dedicadas.**
Todos los "de bolsillo" resuelven flechas por firmware (Fn/capas) o trackpad óptico.

#### Formato bolsillo — SIN flechas físicas
| Teclado | Conexión a la Pi | Flechas | Nota |
|---|---|---|---|
| Beepy / BBQ20 (Solder Party) | I2C | ❌ firmware/trackpad | Trackpad óptico como cursor |
| **ZitaoTech Q20** | ✅ USB-C, HID teclado+ratón | ❌ firmware/trackpad | BBQ20 modificado +2 botones de hombro. **Mejor para la Pi**: es USB HID directo, remapeás flechas en QMK/Vial |
| HackberryPi Cyberdeck | integrado | ❌ capa 3 | Trackpad necesita shim evdev en TTY |
| M5Stack CardKB | ❌ solo I2C 0x5F | ❌ Fn | NO es USB HID ni BT — no plug-and-play |
| M5Stack Cardputer | ❌ no es periférico | ❌ Fn | Es un ESP32-S3 autónomo con pantalla propia; USB-C solo carga/programa |

#### Con flechas físicas reales — más grandes, ya no de bolsillo
| Teclado | Conexión | Precio | Nota |
|---|---|---|---|
| **8BitDo Retro Mechanical Keyboard** | BT / 2.4G / USB-C | ~$100 | TKL 87 teclas, cluster de flechas real, hot-swap. Mejor opción confirmada con flechas físicas |
| Mecánicos 60%/62 teclas (MonkeyKing / pc-100) | USB-C cableado | varía | Cluster de flechas dedicado, más chico que TKL pero no de pulgar |

#### El trade-off
- **Bolsillo real** → aceptás flechas por combo/trackpad → **ZitaoTech Q20** (recomendado).
- **Flechas físicas innegociables** → subís a 60%/TKL → **8BitDo**, deja de ser de bolsillo.

Enlaces:
- ZitaoTech Q20 (Tindie): https://www.tindie.com/products/zitaotech/q20-usb-keyboard-with-trackpad/
- 8BitDo Retro Mechanical: https://www.amazon.com/dp/B0CCP8KYGG

## Enlaces
- Solder Party (Tindie): https://www.tindie.com/stores/arturo182/ — buscar "BB Q20 Keyboard"
- Solder Party shop: https://www.solder.party/

## Ver también
- [[blu-terminal]]
- [[hardware-pantalla]]
- [[proyectos-referencia]]
- [[teclado-comparativa]] — comparativa de teclados por tamaño/comodidad vs Droid 4
- [[caminos]] · [[flashear-droid4-postmarketos]] — recordá: el Droid 4 real ya trae el teclado
