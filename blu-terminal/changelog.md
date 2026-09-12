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
