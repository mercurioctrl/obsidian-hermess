# Grosor y medidas del build (planos + variante slim)

Análisis 2026-09-12 a partir de las piezas verificadas. Ver los planos y vistas 3D en [[render]].

## Medidas generales
- Cuerpo: **127 × 67 mm** (huella tipo Droid). Abierto: **122 mm** (recorrido 55*, solape 12*).
- Pantalla HyperPixel 4.0: área activa 86.4×51.8, módulo 97×58.5. Bisel izq 34.6*, der 6*.
- Teclado Bobricius 107×65, bloque de teclas 29.6* mm de alto; flechas en **T invertida**
  dentro del PCB (a la derecha de enter) — en 107 mm no entra un cluster aparte.
- Bajo el teclado: LiPo 50×60 + PowerBoost 23×45 lado a lado. 4 tornillos M2, guías del slider.
- Pi Zero 2 W (65×30) **detrás de la pantalla**: 65 + 86 > 127, no entran lado a lado.

`*` = cota derivada (supuesto de diseño); el resto, del fabricante.

## v1 — apilado directo: **~34 mm** cerrado
| Mitad | Capas | Total |
|---|---|---|
| Pantalla | pared 1.2 + HyperPixel (vidrio+PCB+header estándar) 12 + PCB Pi 1.4 + holgura 0.2 + pared 1.2 | **16** |
| Teclado | pared 1.2 + Bobricius (switches 7 mm) 8 + LiPo Adafruit 7.3 + holgura 0.3 + pared 1.2 | **18** |

## Variante slim: **~24 mm** cerrado
| Cambio | Ahorro |
|---|---|
| Header de perfil bajo / soldar la HyperPixel (solo ~3 mm de luz sobre el SoC) | −4 a −5 |
| Vidrio **al ras** de la carcasa (sin pared encima) | −1.2 |
| Switches de **5 mm** en el fork del PCB | −2 |
| LiPo **505060** (50×60×5, ~2000–2500 mAh) | −2.3 |

| Mitad | Capas | Total |
|---|---|---|
| Pantalla | vidrio 2 + PCB HP 1.6 + luz 3 + PCB Pi 1.4 + holgura 0.4 + pared 1.2 | **9.6** |
| Teclado | pared 1.2 + teclas 6.6 + LiPo 5 + holgura 0.3 + pared 1.2 | **14.3** |

## Por qué no llega a los 13.7 del Droid
Un slider apila dos cuerpos; cada mitad debería medir ~7 mm y la Pi sola ya mide 5. Motorola
lo logró con PCB de 1 mm, componentes a medida y batería custom. **Piso realista con piezas
de hobby: ~22–24 mm** (≈ GBA SP cerrada; el N900 medía 18).

## ⚠️ Sin verificar en la slim
Luz de 3 mm sobre la Zero (medir blindaje/SoC), dimensiones de la celda 505060, switches de
5 mm (cambian el tacto). Opción más agresiva (Pi en la mitad del teclado, pantalla en ~7 mm)
depende de pasar DPI por un flex de ~70 mm — **no verificado**, no recomendada como base.

## Decisiones derivadas
- **Energía por PowerBoost + LiPo** (no PiSugar): la LiPo va a la mitad del teclado con 2
  cables por el slider; el PiSugar obligaría a apilarla bajo la Pi (+7 mm en la pantalla).

## Ver también
- [[blu-terminal]] · [[render]] · [[bom-construccion]] · [[pantallas-wide]] · [[caminos]]
