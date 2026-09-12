# Changelog

## 2026-09-09

- research: Investigación profunda de hardware para terminal de bolsillo tipo cyberdeck
  (deep-research, 102 agentes, 5 ángulos de búsqueda + verificación adversarial).
- Verificado con fuente oficial: [[hardware-placa|SBC Raspberry Pi Zero 2 W]] y
  [[hardware-pantalla|pantalla Waveshare 2.8" DPI]].
- Refutado: Luckfox Pico Pi NO trae WiFi onboard → descartada para el requisito WiFi.
- Sin verificar por rate-limit (conocimiento general): [[hardware-teclado|teclados]],
  [[hardware-energia|batería]] y [[proyectos-referencia]].
- Hallazgo clave: existe el **Beepy** de SQFMI, producto DIY casi idéntico a la idea.

## 2026-09-10

- research: teclados con flechas físicas → confirmado que ningún teclado de pulgar
  QWERTY las tiene; [[hardware-teclado]] actualizada (ZitaoTech Q20 vs 8BitDo TKL).
- research: construir teclado slider tipo Motorola Droid desde cero → nueva nota
  [[construccion-teclado-droid]]. Hallazgo estrella: **Zero Terminal v3 (NODE)** ya hace
  un slider casero con PCB de Bobricius + SAMD21 + soportes 3D. La cruceta del Droid da
  las flechas físicas que no se consiguen comprando.

## 2026-09-12

- 🏆 **PIVOTE del proyecto:** de "construir con Raspberry Pi" a **flashear un Motorola
  Droid 4 (XT894) con postmarketOS**. Nueva nota [[flashear-droid4-postmarketos]] y
  [[caminos]] (flashear / reshell / construir).
- research: reshell (vaciar Droid, meter Pi) → verificado que se puede reusar teclado
  (flex→Pico auto-scan) y slider; pantalla original casi seguro se reemplaza.
- research: postmarketOS en Droid 4 → teclado + WiFi + consola framebuffer funcionan
  (bash real). Gráfico roto en pmOS pero OK en Maemo Leste. Flasheo por `droid4-kexecboot`.
- research: Droid X → **descartado** (sin teclado + bootloader eFuse). Ver [[modelos-droid]].
- research: cursor dorado → es el **Droid original A855** (D-pad físico dorado); el Droid 4
  no lo tiene pero sí flechas dedicadas. [[modelos-droid]].
- research: comparativa de teclados para construir → [[teclado-comparativa]]
  (uConsole 74 teclas vs Bobricius mini(Pi)QWERTY $28 vs teclado Droid 4 salvado).
- Nuevos [[render|renders]] de alta calidad del dispositivo (hero 2400×1800, estilo Droid).

## 2026-09-12 (tarde)

- research: dónde comprar Droid 4 en buen estado → Swappa/eBay; **la aduana argentina
  (courier) prohíbe usados** → traer en equipaje. Batería EB41 no removible. Actualizada
  [[flashear-droid4-postmarketos]].
- research: BOM completa de construcción → nueva [[bom-construccion]] (~$108–160 núcleo;
  DPI ≤10 cm ⇒ Pi en la mitad pantalla; Bobricius $28.72 es solo PCB; Zero Terminal v3 no robusto).
- render: ficha del build con piezas verificadas (`blu-terminal-build.png`).
- research: pantallas wide 4–4.3" → **corrección: la Zero 2 W no tiene DSI** (premisa mía
  refutada 0-3). Ganadora HyperPixel 4.0 (68% del ancho). Nueva [[pantallas-wide]]; build re-renderizado.
- planos: lámina de 7 vistas con cotas en mm (`blu-terminal-planos.png`).
- render 3D: 4 vistas isométricas con mini motor SVG (`blu-terminal-iso.png`).
- análisis de grosor: v1 34 mm → **variante slim ~24 mm** (header bajo, vidrio al ras,
  switches 5 mm, LiPo 505060). No llega a 13.7. Nueva [[grosor-y-medidas]]; planos e iso
  regenerados en slim, v1 guardada como `*-v1-34mm.png`. [[render]] reescrita.

