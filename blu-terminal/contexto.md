# Contexto

## Requisitos del usuario
- Es una **terminal**, no un celular: shell de bash real corriendo Linux.
- Conexión por **WiFi**.
- Portátil, cabe en el bolsillo (tamaño tipo celular).
- **Pantalla LCD** (posiblemente cristal líquido).
- **Teclado físico QWERTY**.

## 🏆 Decisión principal (pivote 2026-09-12)
El proyecto pasó de "construir con Raspberry Pi" a **comprar un Motorola Droid 4 (XT894)
y flashear postmarketOS**. Cumple todos los requisitos sin construir nada: bash real,
WiFi, teclado slider QWERTY con flechas, tamaño de bolsillo. Ver
[[flashear-droid4-postmarketos]] y [[caminos]]. La vía Raspberry Pi queda como plan B.

## Decisión de arquitectura clave (vía construir, plan B)
Una pantalla **DPI se come casi todos los pines GPIO** de la Pi. Por eso el teclado
**no puede ir por GPIO** — debe ir por **USB o I2C** (solo 2 pines). Esto define todo
el diseño. El [[proyectos-referencia|Beepy]] resuelve esto usando Sharp Memory LCD
(deja pines libres) + teclado I2C.

## Estado de verificación del research
El research (2026-09-09) verificó con fuente oficial la [[hardware-placa|placa]] y la
[[hardware-pantalla|pantalla]]. Las secciones de [[hardware-teclado|teclado]],
[[hardware-energia|batería]] y [[proyectos-referencia]] no completaron verificación
adversarial por límite de tasa de la API — datos de conocimiento general, **verificar
stock y precio antes de comprar**.

## Preguntas abiertas
- Confirmar stock y precio actual del Beepy y del teclado Solder Party en 2026.
- Decidir pantalla: **DPI color** (bonita, se come el GPIO) vs **Sharp Memory**
  (deja pines para teclado I2C, mejor batería, estética terminal).
- Madurez del soporte Linux/drivers en las SBC RISC-V (Milk-V Duo S, Luckfox) vs Zero 2 W.

## Ver también
- [[blu-terminal]]
- [[lista-compra]]
