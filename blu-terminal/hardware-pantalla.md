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

## Enlaces
- Waveshare 2.8" DPI: https://www.waveshare.com/2.8inch-dpi-lcd.htm

## Ver también
- [[blu-terminal]]
- [[hardware-placa]]
- [[hardware-teclado]]
