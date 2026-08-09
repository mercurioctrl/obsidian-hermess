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

## Ver también

- [[arba]]
- [[contexto]]
- [[changelog]]
