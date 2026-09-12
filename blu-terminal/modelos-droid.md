# Modelos Droid — cuál sirve y cuál no

Research verificado: 2026-09-11/12.

## Cuadro comparativo
| Modelo | Teclado | Cursor dorado | Soporte Linux | Veredicto |
|---|---|---|---|---|
| **Droid 4 (XT894)** | ✅ Slider QWERTY 5 filas + flechas dedicadas | ❌ No | ✅ **El mejor** (postmarketOS mainline + Maemo Leste) | 🏆 **El elegido** |
| Droid original (A855 / Milestone) | ✅ Slider QWERTY | ✅ **Sí, D-pad dorado** de 5 vías (físico, no trackpad) | ❌ Sin puerto documentado (OMAP3430) | Lindo pero sin Linux |
| Droid 2 (A955) | ✅ Slider QWERTY | ❌ Quitó el D-pad | limitado | — |
| **Droid X (MB810) / X2 (MB870)** | ❌ **Sin teclado** (slab táctil) | ❌ No | ❌ Bootloader eFuse bloqueado, sin página pmOS | ❌ **NO sirve** |

## El cursor dorado (lo que el usuario recordaba)
Es el **D-pad dorado de 5 vías** del **Motorola Droid original A855** (2009/Milestone).
Es un pad direccional **físico**, no un trackpad óptico. Exclusivo de ese modelo; el
Droid 2 lo eliminó y el Droid 4 no lo tiene.

## El trade-off resuelto
- El **A855** tiene el cursor dorado icónico, pero **no tiene puerto Linux** → inútil como terminal.
- El **Droid 4** no tiene el d-pad dorado, **pero tiene teclas de flecha dedicadas** y el
  mejor soporte Linux. → Para la terminal, gana el Droid 4: no perdés las flechas, solo
  el look dorado (que en el [[render]] se conserva como guiño estético).

## Droid X — por qué NO (confirmado 3-0)
- Es un **teléfono táctil "slab" sin teclado físico** ni slider → falla el requisito central.
- **Bootloader bloqueado con eFuse** (escándalo Motorola) → instalar otro OS muy difícil.
- Ni el X ni el X2 tienen página en la wiki de postmarketOS.

## Ver también
- [[blu-terminal]]
- [[flashear-droid4-postmarketos]] — el camino ganador con el Droid 4
- [[render]]
