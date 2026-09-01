---
cliente: NBE
tipo: minuta
fecha: 2026-08-28
---

# Minuta — NBE · Circuito de compras, pagos y recepción

**Fecha:** 2026-08-28 · 16:32 h (GMT-03:00)
**Modalidad:** Reunión virtual (videollamada) · ~24 min
**Participantes:** Juan · Darío · PM / Gerentes de Producto · Equipo Sistemas (hr Mercurio / Blu)
**Referencia externa:** Órdenes de compra · Depósito / Recepción · Dropshipping
**Documento formal:** `Minuta_Reunion_2026-08-28_NBE.pdf` (hoja membretada Blu, en `/var/www/minutas/nb/`)

## Objetivo

Definir el circuito de compras, pagos y recepción de mercadería: acordar qué información necesita ver Depósito y en qué estado ("pagada" / "pendiente de recepción") debe figurar cada orden de compra, contemplar las excepciones operativas y definir el esquema de cargo por dropshipping, para luego comunicar las definiciones finales a Sistemas para su implementación.

## Temas tratados

- **Circuito de pagos y recepción.** Se analizó qué información debe ver Depósito y en qué momento una orden de compra tiene que figurar como "pagada" o "pendiente de recepción", de modo que el estado de la OC refleje con precisión la operatoria real.
- **Excepciones operativas.** Se contemplaron los casos que se apartan del flujo estándar: mercadería recibida antes del pago, compras en cuenta corriente y situaciones similares que el circuito debe soportar.
- **Cargo de dropshipping.** Se discutió el esquema de cobro (2,5%, monto fijo, esquema mixto y/o con topes), quedando pendiente la definición de la regla comercial final.
- **Carga y responsabilidad de las órdenes de compra.** Se acordó que la carga completa de las OC —de inicio a fin— y la correcta especificación de productos, modelos y especificaciones recae en los PM / Gerentes de Producto.
- **Alcance y condiciones para Sistemas.** Se estableció que Sistemas no avanzará con el desarrollo del indicador de pago ni de la lógica de dropshipping hasta contar con las definiciones comerciales, y que no se modificarán los circuitos operativos sin consenso previo entre las áreas involucradas.

## Próximos pasos y responsables

**Juan + Darío**
- Definir circuito de pagos/recepción: acordar qué información necesita ver Depósito y cuándo una OC debe figurar como "pagada / pendiente de recepción".
- Contemplar excepciones: mercadería recibida antes del pago, compras en cuenta corriente, etc.
- Definir cargo de dropshipping: decidir si será 2,5%, monto fijo, esquema mixto y/o con topes.
- Comunicar las definiciones finales a Sistemas para su implementación.

**PM / Gerentes de Producto**
- Cargar las órdenes de compra completas, de inicio a fin.
- Responsabilizarse por la correcta carga de productos, modelos y especificaciones.

**Sistemas / Mercurio**
- Indicador de pago: esperar definición de Juan + Darío antes de desarrollar.
- Dropshipping: implementar la lógica una vez definida la regla comercial.
- No modificar circuitos operativos hasta que exista consenso entre las áreas involucradas.

## Ver también

- [[nbe]] — índice de minutas del cliente NBE
- [[minutas]] — índice de minutas de Blu
