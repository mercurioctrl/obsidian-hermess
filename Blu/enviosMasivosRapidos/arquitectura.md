# Arquitectura

Ver índice: [[enviosMasivosRapidos]] · Stack: [[stack]]

## Modelo general

Proyecto **CLI-only**. Cada campaña (`enviar*.php`) es un script autocontenido que sigue el mismo pipeline fijo. Los dos scripts existentes (`enviar.php` y `enviarFB.php`) son copias que difieren solo en config SMTP, asunto, cuerpo HTML y archivo de lista.

## Pipeline de envío (5 pasos)

1. **Config SMTP** — `const` hardcodeadas al inicio (`SMTP_HOST`, `SMTP_USER`, `SMTP_PASS`, `FROM_*`, `REPLY_TO`). Host `box.lio.red`, puerto 465 (SSL); 587 cambia a STARTTLS automáticamente.
2. **Rate limiting** — `$baseDelay` (mín 6 s) entre envíos + pausa larga `$burstRest` (60 s) cada `$burstMax` (20) mensajes, con jitter aleatorio. Existe para cuidar reputación/deliverability; **no quitar** al editar el loop.
3. **Cuerpo HTML** — heredoc `$htmlTop` con markup de tablas e inline-styles para compatibilidad con clientes de email (condicionales MSO, hints dark-mode, contenedor 600px).
4. **Carga de destinatarios** — lee un `.txt` (uno por línea), extrae emails con regex, los pasa a minúscula y deduplica.
5. **Loop de envío** — una instancia `PHPMailer` nueva por destinatario, con try/catch para que un fallo no aborte la corrida. Imprime `[OK]`/`[ERR]` por destinatario y un resumen final.

## Decisión clave: imágenes embebidas (CID) vs remotas (URL)

- **`enviarFB.php` (Julio 2026)** usa **imágenes locales embebidas por CID** (`AddEmbeddedImage`). Los 4 segmentos viven en `envios/fb4Julio/` y viajan **dentro** de cada correo (base64). No dependen de hosting externo; por eso cada email pesa ~442 KB.
- **`enviar.php`** también usa CID (una sola imagen `plantilla.jpg`).
- Versiones anteriores de FB usaban **URLs remotas** (imgur). Se puede volver a ese modo cambiando los `src="cid:..."` por URLs y quitando los `AddEmbeddedImage`.
- **Por qué CID:** el cliente entregó las imágenes como archivos locales y no había CDN; CID garantiza que se vean sin depender de un servidor externo.

## Selección de lista por entorno

`enviarFB.php` lee la lista vía `getenv('SEND_LIST')` con default `emails_fb_produ.txt`:
- Producción real: `php enviarFB.php`
- Prueba: `SEND_LIST=emails_testing.txt php enviarFB.php`
- Envío puntual a un solo mail: lista temporal de una línea + `SEND_LIST`.

El default apunta a producción a propósito, para que una corrida normal nunca use por error la lista de prueba.

## Listas de destinatarios

- `emails_fb_produ.txt` — producción Fontaine Bleau
- `emails_produ.txt` — producción NBElectric (~200)
- `emails_testing.txt` — lista corta de prueba

## Ver también

- [[stack]]
- [[contexto]]
