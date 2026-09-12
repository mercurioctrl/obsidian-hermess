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

### Si las flechas físicas son requisito duro (salir del formato BlackBerry)
- **M5Stack Cardputer** — teclado QWERTY completo, verificar cluster de flechas.
- Teclados mini QWERTY USB/BT con fila de flechas (AliExpress, Rii, teclados de handheld).
- Teclados de teclas mecánicas compactas con fila de flechas.

> Research enfocado en teclados con flechas físicas lanzado 2026-09-10 — pendiente de
> completar y actualizar esta sección con enlaces/precios verificados.

## Enlaces
- Solder Party (Tindie): https://www.tindie.com/stores/arturo182/ — buscar "BB Q20 Keyboard"
- Solder Party shop: https://www.solder.party/

## Ver también
- [[blu-terminal]]
- [[hardware-pantalla]]
- [[proyectos-referencia]]
