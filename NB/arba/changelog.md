# Changelog

## 2026-08-06

**Presentación DDJJ percepciones julio 2026 (período 2026070, D7)**

- Generado el lote de julio (`ARBA_PERCEPTIONS_202607.txt`, 769 percepciones, todas con fecha de julio → período `2026070`).
- ARBA observó operaciones por *"La alícuota ingresada difiere de las alícuotas del contribuyente"*.
- Diagnóstico: las alícuotas del sistema contable no coincidían con el **padrón de julio**. 5 líneas mal cargadas.
- **Nuevo script `corregir_padron.py`**: cruza las percepciones contra el padrón oficial, reemplaza alícuotas y recalcula percepción (redondeo comercial HALF_UP). Validación: 764/764 líneas ya correctas dieron recálculo idéntico → 0 diferencias.
- Correcciones aplicadas: CUIT `33-71664195-9` 4,00→1,60% · `30-71645720-2` 1,75→3,00% · `30-71910026-7` 0,01→2,50% · `30-71621186-6` (0% en padrón) → **2 líneas quitadas**.
- Regenerado como **LOTE2** (767 percepciones) listo para subir.

**Mejoras a `generar_lote_arba.py`**

- fix: `validar_archivo` ahora elimina **todas** las líneas vacías finales (`while` en vez de `if`) — evitaba falso rechazo con 2+ líneas en blanco.
- feat: validación de **formato numérico** de imponible/alícuota/percepción (regex `^-?\d+,\d{2}$`, acepta negativos de NC).

Archivos principales: `corregir_padron.py`, `generar_lote_arba.py`

## 2026-08-09

**Documentación y memoria**

- `CLAUDE.md`: documentado `corregir_padron.py`, agregadas las **posiciones de campo 0-indexed verificadas** + fórmula de percepción (HALF_UP), y sección completa "Corrección por padrón".
- Memoria de Claude: `referencia_padron` (ubicación en disco del padrón) y `estado_presentaciones` (historial de DDJJ).
- Bóveda `NB/arba` creada y sincronizada con 6 notas.

## 2026-09-07

**Presentación DDJJ percepciones agosto 2026 (período 2026080, D7)**

- Archivo fuente `ARBA_PERCEPTIONS_202609.txt` (707 líneas), pero **todas las fechas internas eran 08/2026** → período real **agosto `2026080`**, no septiembre. Caso concreto de la regla "el nombre del archivo no define el período".
- Validación previa: 707/707 percepciones con cálculo correcto (HALF_UP), formato OK, sin líneas al 0%. Generado LOTE1.
- ARBA observó 2 operaciones por *"la alícuota difiere de las del contribuyente"*:
  - Línea 501 — CUIT `30-71929695-1`: 1,20% → **0% en padrón de agosto → línea quitada**.
  - Línea 652 — CUIT `30-71833023-4`: 6,00% → **0,50%** (percepción $14.318,79 → $1.193,23).
- Corregido con `corregir_padron.py` contra `PadronRGSPer082026.TXT` (control: 705/705 líneas ya correctas recalcularon idénticas). Quedaron **706 líneas**.
- Generado **LOTE2** `AR-30709246638-2026080-D7-LOTE2_7c86ed64d09b80c43508f5c49c96e272.zip` — pendiente de subir. **No usar el LOTE1.**
- **Total DDJJ agosto = $21.878.962,25** (el LOTE2 reemplaza al LOTE1; NO se suman lotes).

## Ver también

- [[arba]]
- [[proceso-correccion-padron]]
