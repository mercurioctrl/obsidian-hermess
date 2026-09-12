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

## Dónde comprar en buen estado (research 2026-09-12)
⚠️ El research **no pudo verificar stock ni precios 2026** (modelo de 2012, poca data pública).
- **Swappa** — la mejor para "buen estado": *grading* Mint/Good/Fair, IMEI verificado, sin robados.
- **eBay** — la mayor oferta de "Motorola Droid 4 XT894". Vendedor con reputación, fotos reales.
- Back Market / Amazon Renewed — poco probable para un modelo tan viejo.
- Referencia histórica ~$60–150 usado (no confirmado).

### Versión correcta
**XT894** (codename *maserati*). No confundir con **Droid 3** (XT862/XT860, el anterior) ni
**Droid MAXX/RAZR** (el sucesor, sin teclado).

### Qué revisar (teléfono de ~14 años)
1. 🔋 **Batería = riesgo #1.** LiPo interna **no removible** de 1785 mAh; se degrada/hincha.
   Reemplazo OEM **Motorola EB41** (SNN5905A/B, 3.8 V ~1735 mAh) existe, pero cambiarla
   **no es trivial** (abrir con Torx T5 + spudger, adhesivo fuerte, iFixit 4/10). Stock/precio 2026 sin confirmar.
2. Slider y teclado: que deslice firme y respondan las teclas.
3. Pantalla sin burn-in.
4. Pedir **IMEI**; sin bloqueo Google/FRP ni reporte de robo. (Aunque esté *blacklisteado* en
   Verizon, el WiFi funciona y Linux ni corre el firmware que lo chequea.)

### Uso técnico
Verizon CDMA, pero como terminal **WiFi-only con Linux** no necesita red celular. ✅

### 🚨 Importación a Argentina (verificado 3-0)
El **régimen courier** (Decreto 604/2026 + RG 5884/2026: franquicia USD 400 FOB, 5 envíos/año,
IVA 21%) **prohíbe importar "artículos usados"** → **no entra un Droid 4 usado por
Aerobox/courier puerta a puerta.** Es el obstáculo central.
Workarounds (confirmar caso por caso): traerlo **en equipaje** con alguien que viaje desde
USA (la vía más limpia); intermediarios (TiendaMIA, Grabr), que suelen rechazar usados;
buscar uno vendido como "refurbished" (zona gris). Tema ENACOM/homologación sin verificar.

## Ver también
- [[blu-terminal]]
- [[modelos-droid]] — por qué el Droid 4 y no el X o el A855
- [[caminos]] — comparación flashear vs reshell vs construir
- [[hardware-teclado]]
