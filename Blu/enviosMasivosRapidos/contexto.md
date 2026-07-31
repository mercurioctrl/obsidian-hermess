# Contexto

Ver índice: [[enviosMasivosRapidos]] · Arquitectura: [[arquitectura]]

## Campaña actual: Fontaine Bleau — Avance de Obra Julio 2026

- Asunto: `Avance de Obra – Julio 2026 | Bleau Ugarte · Fontaine Bleau`
- Imágenes: 4 segmentos en `envios/fb4Julio/` (HEADER, CONTENIDO, INFO, FOOTER) que apilados forman la muestra completa `FB_Newsletter_julio copia.jpg` (957×2073px).
- Los segmentos se optimizaron con ImageMagick (q82, strip, interlace): el email pasó de ~1.76 MB a **~442 KB**. Originales sin optimizar respaldados en `envios/fb4Julio/_orig/`.
- Preview navegable: `envios/fb4Julio/index.html`.
- Los ALT y el asunto reflejan el texto real de las imágenes.

## Reglas de negocio / decisiones del usuario

- **Rate limit obligatorio** — mantener los delays entre envíos para cuidar reputación del dominio.
- **Confirmar destinatarios antes de enviar** — el usuario pide ver la lista y confirmar antes de cada envío real.
- **Cambio de dominio (2026-07-31):** `@blu.inc` → `@blustudioinc.com` en todas las listas (`emails_testing.txt`, `emails_fb_produ.txt`, `emails_produ.txt`).
- **hbranda@vpodesta.com:** inicialmente marcado "no enviar todavía" y excluido; luego el usuario corrigió → sí debía recibir el envío de julio y quedar agregado en `emails_fb_produ.txt` para próximos envíos. Ya recibió y quedó en la lista (19 destinatarios FB).

## Envíos realizados (2026-07-31)

- Prueba a `emails_testing.txt`: 8/8 OK.
- Producción FB `emails_fb_produ.txt`: 18/18 OK + 1 (hbranda) = 19 total OK.

## Pendientes

- 10 contactos de la lista de Julio quedaron **sin dirección de email** (MARTIN SETTIMIO, MANENTI PABLO, ENRIQUE LOPEZ, CAMILA Y MARTINA DI LAUDO, VECCHI, GASTON GAUDIO, FERRARO, GROISMAN, CAMILA BOZO, LILIANA TENENBAUM). Pendiente conseguir los mails para agregarlos.

## Nota de seguridad

Las contraseñas SMTP están hardcodeadas en los scripts (`const`). Tratar `enviar.php` y `enviarFB.php` como archivos con secretos vivos.

## Ver también

- [[changelog]]
- [[arquitectura]]
