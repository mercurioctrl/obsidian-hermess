# Changelog

Ver índice: [[enviosMasivosRapidos]]

## 2026-07-31

- **feat:** Newsletter Fontaine Bleau "Avance de Obra – Julio 2026". Se armó la plantilla a partir de los 4 segmentos de `envios/fb4Julio/` (HEADER, CONTENIDO, INFO, FOOTER), reemplazando las imágenes remotas (imgur) por imágenes locales embebidas por CID en `enviarFB.php`.
- **feat:** Nueva plantilla de preview navegable `envios/fb4Julio/index.html`.
- **perf:** Optimización de los JPG con ImageMagick (q82, strip, interlace). Email de ~1.76 MB → ~442 KB. Originales respaldados en `envios/fb4Julio/_orig/`.
- **feat:** `enviarFB.php` ahora selecciona la lista con `getenv('SEND_LIST')` (default `emails_fb_produ.txt`), permitiendo pruebas sin editar el script.
- **chore:** Actualizado asunto, preheader y ALT de las imágenes con el texto real de los segmentos.
- **data:** Cambio de dominio `@blu.inc` → `@blustudioinc.com` en las 3 listas de emails.
- **data:** `hbranda@vpodesta.com` agregado a `emails_fb_produ.txt` (19 destinatarios).
- **send:** Prueba a `emails_testing.txt` (8/8 OK) y envío de producción FB (19/19 OK).
- **docs:** Creado `CLAUDE.md` inicial del repo (init) + sección Obsidian.

Archivos principales: `enviarFB.php`, `envios/fb4Julio/`, `emails_fb_produ.txt`, `emails_testing.txt`, `emails_produ.txt`, `CLAUDE.md`
