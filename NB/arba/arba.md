# ARBA Percepciones

Automatización de la presentación de **DDJJ de percepciones de IIBB** ante ARBA (Provincia de Buenos Aires) para el agente de recaudación **NB DISTRIBUIDORA MAYORISTA** — CUIT `30-70924663-8`.

Reemplaza el utilitario Windows `GenHash.exe`: toma el `.txt` de percepciones, lo valida, lo renombra con la nomenclatura ARBA, lo comprime y le agrega el hash MD5 — dejándolo listo para subir al portal.

## Stack

- **Python 3** (solo librería estándar: `argparse`, `hashlib`, `zipfile`, `re`, `decimal`, `pathlib`)
- Sin dependencias externas
- Ubicación: `/var/www/arba/`

## Scripts

| Script | Qué hace |
|---|---|
| `generar_lote_arba.py` | Valida, renombra, comprime y genera el hash MD5 del lote |
| `corregir_padron.py` | Cruza las percepciones contra el padrón oficial y corrige alícuotas rechazadas |

## Notas del proyecto

- [[arquitectura]] — Formato de registro, nomenclatura y estructura de los scripts
- [[proceso-correccion-padron]] — Flujo mensual para arreglar alícuotas rechazadas
- [[contexto]] — Reglas de negocio y decisiones
- [[changelog]] — Registro de lo trabajado
- [[memoria]] — Memoria consolidada del proyecto

---
*Última sincronización: 2026-08-09*
