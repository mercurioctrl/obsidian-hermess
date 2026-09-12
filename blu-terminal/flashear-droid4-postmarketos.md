# 🏆 Camino ganador — Flashear un Motorola Droid 4 con postmarketOS

Research verificado: 2026-09-11/12.

**La idea que resolvió el proyecto:** en vez de construir o vaciar un teléfono, se
compra un **Motorola Droid 4 (XT894)** original y se le flashea **Linux (postmarketOS)**.
El teléfono ya tiene pantalla + teclado slider QWERTY + WiFi + batería. Solo se cambia
Android por Linux → shell de bash real con teclado físico. Cero soldadura, cero
canibalización. Es literalmente [[blu-terminal|el proyecto]] terminado.

## Por qué el Droid 4 (XT894)
- **Teclado slider QWERTY de 5 filas** con fila numérica y **teclas de flecha dedicadas**
  (driver `omap4-keypad` en mainline, matriz 8×8). Un mantenedor del kernel lo compró
  justamente porque "no hay teléfono más nuevo con un teclado de hardware decente".
- Codename postmarketOS: **`motorola-maserati`**. SoC OMAP4430 (dual Cortex-A9).

## Qué funciona (verificado, voto 3-0)
| Componente | postmarketOS | Maemo Leste |
|---|---|---|
| Teclado físico slider | ✅ | ✅ |
| WiFi | ✅ | ✅ |
| Consola framebuffer (bash) | ✅ | ✅ |
| Pantalla | ✅ | ✅ |
| Entorno gráfico (Xorg/Wayland) | ❌ roto (segfault) | ✅ |
| Aceleración 3D (GPU SGX540) | ❌ | ✅ |
| BT / audio / USB | parcial | ✅ |

🔑 **Clave para una terminal:** no hace falta Wayland ni GPU. Con **bash en la consola
framebuffer + teclado + WiFi** ya tenés la terminal → y eso es exactamente lo que
funciona en postmarketOS. Si quisieras escritorio gráfico completo → **Maemo Leste**.

## Cómo se flashea
- Método **`droid4-kexecboot`** (github.com/tmlind/droid4-kexecboot): se graba a la eMMC
  **sin modificar hardware** ni desbloquear el bootloader (Android actúa de "bootloader
  gigante" vía kexec). Se flashea a la partición `mmcblk1p13` y se configura con `utagboot`.

## Enlaces
- Wiki postmarketOS Droid 4: https://wiki.postmarketos.org/wiki/Motorola_Droid_4_(motorola-maserati)
- Maemo Leste Droid 4: https://leste.maemo.org/Motorola_Droid_4
- droid4-kexecboot: https://github.com/tmlind/droid4-kexecboot

## Dónde comprar (⚠️ precios sin verificar en 2026)
- **Swappa** (swappa.com) — usados verificados, mejor estado.
- **eBay** — mayor oferta de "Motorola Droid 4 XT894".
- **Back Market** — refurbished con garantía (si aparece).
- Referencia histórica ~$60–300 USD usado. Es de Verizon USA → hay que importar.
- **Uso como terminal:** WiFi-only sin línea celular → debería andar sin activar Verizon.
- **Argentina:** Decreto 604/2026 unificó correo/courier; revisar franquicia USD 400 y
  tema ENACOM/homologación antes de importar (no verificado).

## Ver también
- [[blu-terminal]]
- [[modelos-droid]] — por qué el Droid 4 y no el X o el A855
- [[caminos]] — comparación flashear vs reshell vs construir
- [[hardware-teclado]]
