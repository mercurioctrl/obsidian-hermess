# Memoria del proyecto

Consolidado de la memoria de Claude para este proyecto (`~/.claude/projects/-var-www-arba/memory/`).

## Usuario y rol

Agente de recaudación de ARBA (IIBB, Provincia de Buenos Aires). Razón social **NB DISTRIBUIDORA MAYORISTA**, CUIT `30-70924663-8`. Presenta DDJJ de percepciones por la vía web, método devengado mensual (D7). Genera los lotes (`.txt` → `.zip` + hash MD5) para cargar en el portal.

## Proyecto

Automatiza la preparación del lote para presentar DDJJ de percepciones de IIBB, reemplazando el utilitario Windows `GenHash.exe` (el usuario trabaja desde Linux/servidor). Ver [[arquitectura]].

## Feedback / preferencias

- **El nombre del archivo fuente no define el período.** El sistema contable exporta con el mes de exportación, no el del contenido. Verificar siempre las fechas dentro del archivo. Ver [[contexto]].

## Proceso recurrente

- **Corrección por padrón**: flujo mensual para arreglar alícuotas rechazadas cruzando contra el padrón de ARBA. Ver [[proceso-correccion-padron]].

## Referencia

- **Ubicación del padrón**: `~/Descargas/percepciones {mes}/PadronRGS{MMAAAA}.zip`. Usar `PadronRGSPer{MMAAAA}.TXT` (Percepciones), NO el `...Ret...` (Retenciones). Ver [[proceso-correccion-padron]].

## Estado de presentaciones

- **Agosto 2026** (`2026080`, D7): **LOTE2 pendiente de subir** al 2026-09-07. Fuente `ARBA_PERCEPTIONS_202609.txt` pero contenido de agosto (regla del período). LOTE1 observado (2 alícuotas ≠ padrón) → corregido → **LOTE2** (706 percepciones). **Total DDJJ = $21.878.962,25.** No usar el LOTE1.
- **Julio 2026** (`2026070`, D7): LOTE1 observado → corregido por padrón → **LOTE2** generado (767 percepciones). No usar el LOTE1.
- **Junio 2026** (`2026060`): presentado con corrección por padrón. Meses previos (abril, mayo): presentados.
- Ver [[changelog]].

Nota de negocio: cuando un lote es observado, se resube el **archivo completo corregido como nuevo lote** (LOTE2, LOTE3…) — el lote nuevo **reemplaza** al anterior, los lotes **no se suman** para el total de la DDJJ.

## Ver también

- [[arba]]
- [[contexto]]
- [[changelog]]
