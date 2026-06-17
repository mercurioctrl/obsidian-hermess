# Arquitectura

Script único `validar_emails.py` que ejecuta un pipeline lineal sobre el CSV de Brevo.

## Pipeline

1. **Backup** del CSV original a `salida/backup_*`.
2. **Carga** (`pandas`, `sep=';'`, `dtype=str`) preservando las ~40 columnas.
3. **Normaliza**: minúsculas + trim sobre `email_norm`; elimina vacíos y duplicados.
4. **Sintaxis** con `email-validator` → flag `formato_valido` + extrae `dominio`.
5. **Descartables**: `dominio in disposable-email-domains` → flag `disposable`.
6. **Typos**: `is_typo_domain()` → flag `typo_domain` (MARCA, no corrige).
7. **DNS** (MX→A) de cada dominio único, en paralelo (`ThreadPoolExecutor`, caché
   por dominio, resolvers públicos 8.8.8.8/1.1.1.1). Solo dominios con formato OK,
   no descartables y no typo.
8. **Clasifica** por `motivo` → genera salidas.

## Decisión central: detectar, NO corregir

La herramienta **no reescribe ningún email**. Todo lo que está mal desde el origen
(typos incluidos) se entrega en su forma original en la lista de bloqueo.

**Por qué** (ver [[contexto]]):
- Corregir y reimportar dejaba contactos "fantasma" duplicados en Brevo.
- Un corrector difuso agresivo escondía descartables (ej. `yopmail.com` → `hotmail.com`).

## Detección de typos (`is_typo_domain`)

- Lista blanca `LEGIT_PROVIDER_DOMAINS` (incluye ccTLD reales: `yahoo.com.ar`,
  `hotmail.es`, etc.) → nunca se marcan.
- Distancia Damerau-Levenshtein contra stems de proveedores (gmail, hotmail, yahoo,
  outlook, icloud) con umbrales 1-2.
- **Guarda anti-falsos-positivos:** el typo debe empezar con la MISMA letra que el
  proveedor. Evita `yopmail`→hotmail, `uolmail`→hotmail, `mail.x`→gmail.
- Substring `gmail` incrustado (ej. `2001gmail.com`, `webgmail.info`) → typo.

## Clasificación por motivo

Prioridad: `formato_invalido` > `dominio_typo` > `email_temporal` > DNS
(`dominio_inexistente`/`sin_dns`/`sin_mx`) > `ok`.

- **valid** = `ok` (MX válido, entregable)
- **risky** = `sin_mx` (a_only: dominio existe pero sin servidor de correo)
- **bloquear** = formato_invalido, dominio_typo, email_temporal, dominio_inexistente, sin_dns

## Ver también
- [[stack]] · [[contexto]] · [[limpieza-contactos-brevo]]
