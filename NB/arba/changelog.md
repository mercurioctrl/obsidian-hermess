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

## Ver también

- [[arba]]
- [[proceso-correccion-padron]]
