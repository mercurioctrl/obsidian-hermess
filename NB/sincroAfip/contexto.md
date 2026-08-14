# Contexto

## Motivo

El equipo contable de [[NB]] cargaba a mano cada factura recibida. Para cada uno de los 6 CUITs del grupo, alguien entraba a AFIP, filtraba por mes, y copiaba los datos a planillas / sistema contable. Horas-persona recurrentes todos los días.

Este proyecto reemplaza esa tarea: baja automáticamente los recibidos de cada CUIT y los deja en una tabla SQL Server lista para consumir desde el ERP o reportería.

## CUITs del grupo

En `cuits.yaml`:

| CUIT             | Razón social                             | Estado    |
|------------------|------------------------------------------|-----------|
| 30-70924663-8    | NB DISTRIBUIDORA MAYORISTA S R L         | ✅ activo |
| 30-71909207-8    | BLU INC S.R.L                            | ⏸ pendiente |
| 30-71413236-5    | CONSORCIO DE COOPERACION RED DE TECNOLOGIA | ⏸ pendiente |
| 20-26239532-5    | FONTAN SEBASTIAN ANIBAL                  | ⏸ pendiente |
| 30-70881184-6    | MAYORISTA INTEGRAL DE INFORMATICA S.R.L. | ⏸ pendiente |
| 30-71917480-5    | NAEVO S.R.L.                             | ⏸ pendiente |

Todos están bajo la misma clave fiscal (20-26239532-5 / Sebastián Fontán) con permiso de "Mis Comprobantes" en el Administrador de Relaciones.

## Captcha del login (desde 2026-08-06)

AFIP agregó un captcha de texto en el login de Clave Fiscal. Se resuelve con **2Captcha**, un servicio pago **prepago**. Implicancias operativas:

- La cuenta de 2Captcha es de `hermess87@gmail.com`; la `CAPTCHA_API_KEY` va en `.env`.
- **Si el saldo se agota, el login falla y el cron deja de bajar comprobantes.** Hay que vigilar el saldo y recargar (dura meses; ~EUR 0.05-0.10/día).
- Como AFIP no persiste la sesión, cada corrida del cron gasta un captcha. Si se quiere bajar el consumo/costo, espaciar la cadencia del cron.

Ver la decisión completa en [[arquitectura#2Captcha para el captcha del login]].

## Estado actual (2026-08-14)

- Scraper funcionando end-to-end otra vez, ahora con captcha resuelto por 2Captcha: login → CUIT → Recibidos → CSV → SQL Server.
- Login OK al primer intento en las pruebas; CSV con datos reales.
- Idempotencia verificada previamente: re-corridas del mismo rango no generan duplicados.
- Docker build OK; loader pymssql funciona en Linux (no en macOS sin FreeTDS).

## Pendientes

1. **Activar los otros 5 CUITs** en `cuits.yaml` (flag `activo: true`) — ver [[despliegue]] para el flujo de alta.
2. **Programar cron diario** en el server del cliente. Comando típico: `docker compose run --rm sincro --ultimos-dias 2`.
3. **Alertas de fallo** — wrapper que notifique por Slack/mail cuando `sincro.py` devuelve exit 1. Especialmente útil ahora para avisar si 2Captcha se queda sin saldo (si no, uno se entera días después, como pasó con el captcha).
4. **Vigilar saldo de 2Captcha** — cargar antes de que se agote.
5. **(Opcional, futuro)** Agregar también Emitidos a la misma base. Reutilizaría todo el stack cambiando solo el tab en el scraper + una tabla gemela.

## Cosas que se intentaron y no funcionaron

- **URL directa a Mis Comprobantes** (`/genericos/comprobantes/cliente/default.aspx`): responde 404. La forma correcta es ir por el buscador del portal ARCA, que abre el servicio en pestaña nueva en `fes.afip.gob.ar/mcmp/`. Ver [[arquitectura]].
- **`fill()` directo en el input de fecha:** no funciona; es un daterangepicker.js. Hay que fillear los inputs internos `daterangepicker_start/end` + click `.applyBtn`.
- **Selectores `input[name*='Desde']`**: matchean con "Número desde" (filtro de número de comprobante), no con fecha. Usar XPath relativo al label "Fecha del Comprobante".
- **Guardar el download como `.csv` directo:** AFIP entrega un ZIP. Hay que desempaquetar con `zipfile` primero.
- **pymssql en macOS local sin FreeTDS:** error `symbol not found '_bcp_batch'`. Solución: `brew install freetds` o simplemente usar Docker (Linux).
- **OCR local del captcha (tesseract):** descartado — 0/6 en captchas reales, ni con preprocesado agresivo (morfología, umbrales, upscale) el techo pasa de 0. La fuente distorsionada + líneas diagonales lo derrotan.
- **Modelo local entrenado (CRNN) para el captcha:** descartado — para juntar el dataset habría que pegarle muchas veces al login de AFIP, con riesgo de bloquear la cuenta.
- **Reutilizar sesión guardada (`storage_state`) para evitar el login:** no sirve — AFIP no persiste la sesión, el form de login reaparece en cada corrida.

## Ver también

- [[sincroAfip]]
- [[arquitectura]] — internals.
- [[despliegue]] — operación.
- [[changelog]]
