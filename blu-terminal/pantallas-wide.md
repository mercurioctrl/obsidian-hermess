# Pantallas wide (4–4.3") para la Zero 2 W — y la corrección DSI

Research verificado: 2026-09-12 (101 agentes). Objetivo: una pantalla apaisada que llene
el frente de un cuerpo de 127×67 mm (la Waveshare 3.5" 4:3 dejaba 44% de bisel).

## 🚨 Premisa corregida
**La Raspberry Pi Zero 2 W NO tiene puerto DSI.** Su conector de 22 pines es **CSI
(cámara)**. Salidas de video: **mini-HDMI** o **DPI por GPIO**. → Ninguna pantalla "MIPI
DSI para Raspberry Pi" (Waveshare 4.3" DSI, 4" DSI, 43H-800480, Elecrow) funciona con la
Zero. Los claims que lo asumían fueron refutados 0-3.

## Ranking (cuerpo 127×67, con Zero 2 W)
| # | Pantalla | Área activa | Ancho | Interfaz | Precio | Cabe |
|---|---|---|---|---|---|---|
| 🥇 | **Pimoroni HyperPixel 4.0** | 86.4×51.8 | **68%** | DPI (header 40) | £31.50–37.50 | ✅ módulo 97×58.5, **Zero compatible declarada** |
| 🥈 | Waveshare 4" HDMI (H) | 86.4×51.8 | 68% | **HDMI nativo** | $42.99 | ⚠️ panel cabe, PCB 76.5 mm alto → reubicar controladora. Táctil resistivo |
| — | Waveshare 3.5" DPI | 71×53 | 56% | DPI | $29.99 | ✅ |

**Solo si se cambia a CM4/CM5/Pi 5 (que sí tienen DSI):** Waveshare 43H-800480-IPS 4.3"
95×53.9 (75%), $24.99, panel 105.42×67.07 → 0.07 mm sobre el límite. Elecrow 4.3" DSI $29.90.

**Techo real:** ninguna verificada llena los ~110 mm; el máximo es **95 mm (4.3")** y exige
DSI. Con Zero 2 W el máximo es **86 mm (68%)**.

## Otras conclusiones
- **HDMI sí cruza el slider** con cinta FFC "DIY HDMI" de Adafruit (10–50 cm, $1.50–9.95)
  → vía práctica para poner la Pi en la mitad del teclado, si se usa la 4" HDMI.
- Cables DSI largos existen (20–50 cm) pero solo desde host con DSI real.
- **Legibilidad:** ppi casi idéntico (214–235). La ganancia de la wide es de **columnas**
  (100 vs 80 con fuente 8×16), no de nitidez.
- El "límite de 10 cm del DPI" **no quedó firmemente probado** (refutado 1-2).

## Decisión
**Con Zero 2 W → HyperPixel 4.0.** Pi detrás de la pantalla (DPI por header).

## Ver también
- [[blu-terminal]] · [[hardware-pantalla]] · [[bom-construccion]] · [[grosor-y-medidas]] · [[render]]
