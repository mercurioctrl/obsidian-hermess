# Módulo: Reclamo de Evidencias (POEs)

Desde el detalle de cada **Envío**, permite disparar **a mano** un mail a cada partner
reclamándole las **POEs** (Pruebas de Ejecución) de la campaña, con **link/botón para
cargarlas** directo, **copia oculta** a marketing, **contador** de reclamos y **directorio
de contactos** por empresa. Vive dentro de [[modulos/envios|Envíos]] (`/envios/{campania}`).

> **Historia:** el proyecto arrancó como un sistema más ambicioso (flujo Google-native que
> copiaba/verificaba el Slides, wizard de carga, réplica del deck PDF). El usuario lo
> **simplificó**: se descartó todo eso (commit `elimina Google-native, wizard y deck`) y
> quedó solo el reclamo desde Envíos. Ver [[changelog#2026-09-01]].

## Flujo

1. En la tabla de destinatarios de un envío, cada fila tiene **🔔 Reclamar**.
2. Abre un modal con: **Para (emails)** (multi-email, precargado del directorio, editable),
   **Vencimiento** (autocompletado desde el correo original de la campaña), **Asunto**,
   **Mensaje** (prellenado) y **Vista previa** del HTML tal cual llega.
3. Al enviar: el mail sale desde **mktgigabyte@blustudioinc.com** (casilla de marketing) a
   todos los contactos, con **BCC** a `giga-forwarding@blustudioinc.com` (siempre, oculto).
4. La 🔔 se pinta naranja con **(N)** = veces reclamado; el modal lista fechas.
5. El mail trae un **botón "Cargar Pruebas de Ejecución"** → página pública por token donde
   el partner sube archivos (PDF/imágenes/Office/ZIP). Quedan **enlazados** al reclamo
   (empresa/email/campaña/IP = quién subió). El chip **📎 POE (N)** en la fila y la lista de
   archivos en el modal muestran lo cargado.

## Backend

`RecordatorioEvidenciaController` (rutas `/api/recordatorios-evidencia/*`):
- **Público (por token, sin login):** `GET/POST /subir/{token}` (página + carga de archivos),
  `preview` (HTML del mail). Un token inválido/de ejemplo muestra una **página amable**
  (`reclamos/subir-invalido.blade`), no un 404 crudo.
- **Admin:** `reclamar` (envía + registra), `reclamos?campania=` (conteo/fechas/archivos por
  destinatario), `contactos?empresa=` (emails guardados), `config`.

Mail `RecordatorioEvidenciaMail` + vista `emails/recordatorio-evidencia.blade` — estética del
**correo original** de campaña (wordmark, "CAMPAÑA {nombre}", cuadro crema de vencimiento con
la fecha en naranja, botón de carga, link a la **Plantilla Reporte** de Google Slides `/copy`).

**Remitente propio:** mailer `reclamos` en `config/mail.php` (mismo SMTP, casilla de marketing,
credenciales por env `MAIL_RECLAMOS_*`). El resto de los mails del ERP siguen desde Contenido.

## Datos

- `reclamos_evidencia` (mig 0102) — un registro por reclamo enviado. `clave` = `empresa|lista|email`
  (identidad de la fila; la calcula el front), `token` (link de subida), `email_destino`, etc.
- `reclamo_evidencia_archivos` (mig 0103) — archivos (POEs) subidos, FK al reclamo.
- `partner_contactos` (mig 0104) — directorio de emails por empresa; se arma solo al enviar y
  precarga el "Para" la próxima vez. Soporta **varios emails por empresa**.

## Fechas y correos (de la plataforma de Envíos)

La **fecha límite** se toma del correo archivado original (`GET /envios/campanias/{id}/fecha-limite`),
única por campaña, formato `DD-MM-YY`. La API de Envíos **no expone los emails** de la mayoría de
los destinatarios (solo la empresa) → por eso el directorio `partner_contactos` los va cargando.

## Deploy / prod (env necesarias)

```
MAIL_RECLAMOS_USERNAME=mktgigabyte@blustudioinc.com
MAIL_RECLAMOS_PASSWORD=***
MAIL_RECLAMOS_FROM_ADDRESS=mktgigabyte@blustudioinc.com
MAIL_RECLAMOS_FROM_NAME="GIGABYTE Marketing"
REPORTES_FORWARDING_EMAIL=giga-forwarding@blustudioinc.com
REPORTES_PLANTILLA_SLIDES_URL=.../presentation/d/1zLQk6.../copy
```
La **página de subida** usa fetch con URL **relativa** (hereda esquema/host) — con `url()` salía
`http://` detrás del proxy y el navegador bloqueaba el POST por mixed content (fix `970d71a`).

## Ver también

- [[modulos/envios]] — donde vive el reclamo (detalle de campaña)
- [[modulos/campanas]] · [[modulos/clientes]] — partners = clientes/resellers
- [[changelog]] · [[troubleshooting]]
