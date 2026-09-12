# Hardware — Pantalla

✅ **Verificado con fuente oficial** (Waveshare 2.8" DPI).

Regla de oro: **evitar pantallas SPI baratas** (lentas, ~10-20fps, malas para terminal
con scroll). Preferir **DPI o DSI**.

| Pantalla | Precio | Interfaz | Nota |
|---|---|---|---|
| **Waveshare 2.8" DPI LCD 480×640 IPS táctil** | ~$35 | DPI666 (GPIO paralelo), hasta 60Hz | Escritorio Linux fluido. |
| Sharp Memory LCD 2.7" 400×240 (la del [[proyectos-referencia|Beepy]]) | ~$45 | SPI especial, monocromo, ultra bajo consumo | Estética terminal retro, excelente batería. |

## ⚠️ Conflicto clave (definitorio del diseño)
Una pantalla **DPI se come casi todos los pines GPIO**. Por eso el [[hardware-teclado|teclado]]
**no puede ir por GPIO** → debe ir por **USB o I2C**. Ver [[contexto]].

## 🚨 Corrección (2026-09-12): la Zero 2 W NO tiene DSI
Su conector de 22 pines es CSI (cámara). Solo mini-HDMI o DPI. Las pantallas "DSI para Pi"
no sirven con la Zero. Para el build, la ganadora es la **Pimoroni HyperPixel 4.0** (DPI,
86.4×51.8, 68% del ancho). Ranking completo y alternativas HDMI en [[pantallas-wide]].

## Enlaces
- Waveshare 2.8" DPI: https://www.waveshare.com/2.8inch-dpi-lcd.htm

## Ver también
- [[blu-terminal]]
- [[hardware-placa]]
- [[hardware-teclado]]
