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

## Enlaces
- Solder Party (Tindie): https://www.tindie.com/stores/arturo182/ — buscar "BB Q20 Keyboard"
- Solder Party shop: https://www.solder.party/

## Ver también
- [[blu-terminal]]
- [[hardware-pantalla]]
- [[proyectos-referencia]]
