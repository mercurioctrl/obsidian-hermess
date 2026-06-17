# Contexto

## Por qué este proyecto

**Brevo le pidió a New Bytes limpiar la base de contactos** para no perder reputación
de envío (rebotes/quejas pueden derivar en suspensión). La base son ~231k contactos
exportados de Brevo (CSV `;`, columna `EMAIL`, ~40 columnas con datos del contacto).

## Decisiones del usuario (importantes)

1. **No corregir emails.** Todo lo que está mal desde el origen (typos como `gmial.com`,
   `hotmial.com`) se entrega **en su forma original** en una lista aparte, para que el
   usuario la importe a Brevo y bloquee/elimine esos contactos. No quiere correcciones
   automáticas: corregir dejaba duplicados fantasma en Brevo.

2. **Incluir los `sin_mx` (a_only) en el bloqueo.** Los 1.741 dominios que existen pero
   no tienen MX se sumaron a la lista de bloqueo (total 5.114).

## Flujo operativo en Brevo

- Importar `bloquear_solo_emails.csv` a la **lista negra / blocklist** de Brevo
  (los emails están en forma original = match exacto con lo guardado en Brevo).
- Mantener `validos.csv` (226.113) como la base limpia.

## Gotchas

- **Variación entre corridas:** cientos de dominios pueden caer en `a_only`/`no_dns`
  por timeouts transitorios de DNS, desplazándose entre valid/risky. Pendiente:
  reintento de reconfirmación para estabilizar.
- **~5 filas malformadas** del CSV original (semicolons extra en campos de texto) las
  saltea el parser (0,002%).
- La validación es a nivel **dominio** (existe y acepta correo), no a nivel buzón
  individual (eso requeriría SMTP, que Brevo desaconseja).

## Ver también
- [[arquitectura]] · [[memoria]] · [[limpieza-contactos-brevo]]
