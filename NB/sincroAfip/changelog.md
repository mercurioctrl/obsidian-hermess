# Changelog

## 2026-04-22

- **feat:** Bootstrap completo del proyecto sincroAfip.
  - Scraper Playwright: login en AFIP, navegación hasta Mis Comprobantes, selección de CUIT representado, descarga de CSV de Recibidos.
  - Loader pymssql: parseo CSV → staging temp → MERGE idempotente contra `NewBytes_DBF.dbo.AfipComprobantesRecibidos`.
  - Dockerización con imagen base `mcr.microsoft.com/playwright/python:v1.48.0-jammy`.
  - CLI `sincro.py` con flags `--desde`, `--hasta`, `--ultimos-dias`, `--cuit`, `--skip-db`, `--skip-scrape`, `--headful`, `--debug`.
  - Config vía `.env` + `cuits.yaml`.
  - Sesión persistente por CUIT en `storage/sessions/<cuit>.json`.
  - Log rotado en `storage/logs/sincro.log`.
- **data:** Creación de tabla `AfipComprobantesRecibidos` con índice único `UX_AfipRec_natural` para dedup. Ver [[migracion]].
- **docs:** `README.md`, `CLAUDE.md`, `docs/ARQUITECTURA.md`, `docs/DESPLIEGUE.md`, `docs/MIGRACION.md`, `docs/TABLA.md`.
- **test:** Validado end-to-end con 77 comprobantes reales de NB DISTRIBUIDORA MAYORISTA (30-70924663-8). Re-corrida del mismo rango → 0 insertados / 77 duplicados (idempotencia OK).

**Archivos principales:** `sincro.py`, `afip/config.py`, `afip/scraper.py`, `afip/db.py`, `cuits.yaml`, `Dockerfile`, `docker-compose.yml`.

## Ver también

- [[sincroAfip]]
- [[contexto]] — estado y pendientes.


## 2026-04-22 (tarde)

- **data:** Backfill de abril 2026 completo para NB DISTRIBUIDORA (30-70924663-8) contra DB **producción** (`190.210.23.97:4444`). Procesado en chunks de 7 días (01-07, 08-14, 15-21) dada la posible carga por rango. Total: 120 comprobantes nuevos (+ 77 que ya estaban del rango 15-22).
- **config:** Cambiado `DB_HOST` a `190.210.23.97` y `DB_PORT` a `4444`. Default del contenedor pasado de `--ultimos-dias 1` a `--ultimos-dias 5` (tolerancia mayor para retries).
- **fix:** `cae VARCHAR(14)` pasado a `NULL` — los `tipo_comprobante = 81` (Tique Factura de controladores fiscales) usan CAI/COE, no CAE, y llegan vacíos. Ajustado:
  - `ALTER TABLE` ejecutado en prod.
  - `CREATE TABLE #staging` en `afip/db.py` actualizado (`cae` NULL).
  - Actualizado `docs/MIGRACION.md` y [[migracion]] con la regla.
  - Actualizado `docs/TABLA.md` y [[tabla-referencia]].

## 2026-08-14

- **fix (login roto por captcha de AFIP):** El 2026-08-06 AFIP agregó un captcha de texto en el login de Clave Fiscal, que rompió el scraper. El cron falló en cada corrida desde las 16:15 de ese día con `Login fallo: seguimos en la pagina de login`.
  - **Diagnóstico:** el login llegaba hasta "Ingresando clave..." y quedaba en la página de login. El screenshot post-login mostró el captcha nuevo (`img[alt='Captcha']`, JPEG en base64) + input `#F1:captchaSolutionInput`. También la clave fiscal había cambiado (se actualizó `AFIP_PASS`), pero eso solo no alcanzaba.
  - **Caminos evaluados:** OCR local con tesseract (descartado — 0/6 en captchas reales, ni con preprocesado agresivo); modelo local CRNN (descartado — juntar el dataset implicaba pegarle mucho al login = riesgo de bloqueo de la cuenta); **servicio 2Captcha** (elegido — ~99% al primer intento, sin riesgo de bloqueo, ~EUR 0.05-0.10/día).
  - **Solución:** nuevo módulo `afip/captcha.py` (`resolver_captcha_dataurl`) que terceriza a 2Captcha vía `twocaptcha`. `_login` completa el captcha y reintenta con uno nuevo hasta `LOGIN_INTENTOS` veces (`_reiniciar_login`).
- **config:** nueva var `CAPTCHA_API_KEY` en `.env` (obligatoria, validada en `config.load_settings()`). Dep `2captcha-python==1.5.1` agregada; tesseract/Pillow descartados.
- **hallazgo:** AFIP **no persiste la sesión** entre corridas (histórico: 2486 logins completos, 0 reusos de `storage_state`). Se hace login + captcha en **cada** ejecución del cron → cada corrida consume un captcha de 2Captcha.
- **test:** login OK al primer intento; flujo completo hasta CSV con 37 filas reales.
- **docs:** actualizados `ARQUITECTURA.md`, `DESPLIEGUE.md` (troubleshooting de saldo/captcha), `README.md`, `.env.example`, `CLAUDE.md` (gotcha #9).

**Archivos principales:** `afip/captcha.py` (nuevo), `afip/scraper.py`, `afip/config.py`, `requirements.txt`, `.env.example`.
