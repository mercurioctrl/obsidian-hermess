# Intimación AGIP — Percepciones IIBB CABA

> Análisis de la intimación de AGIP/ARCIBA a **NB DISTRIBUIDORA MAYORISTA SRL** (CUIT 30-70924663-8, agente de recaudación 14862-6) por aplicar mal la alícuota de percepción de Ingresos Brutos CABA (Res. 352-AGIP-2022).

**Fecha análisis:** 2026-07-09
**Fuente:** 27 anexos de intimación (`intimacion/*.pdf`) + los 27 padrones reales `ARDJU008MMYYYY` bajados de agip.gob.ar.
**Entregable:** `intimacion/Intimaciones_AGIP_percepciones.xlsx` (Resumen + 27 hojas mensuales).

---

## Regla que gobierna el análisis

> **Si el sujeto NO figura en el "Padrón de Regímenes Generales", NO corresponde percibir (alícuota 0).**

Esta es la regla operativa. El padrón publicado por AGIP (`ARDJU008`, mensual, alícuota por CUIT) es la **única** fuente que un agente de recaudación puede consultar para saber a quién percibir y a qué alícuota.

## Conclusión ejecutiva

AGIP reclama **$73.103.974,46** en total (ene-2024 → may-2026, 27 periodos, 260 CUIT únicos, 694 líneas). Al cruzar cada CUIT intimado contra el padrón AGIP real de su mes, aparecen **dos bloques distintos, con consecuencias opuestas**:

| Bloque | Periodos | ¿CUIT en padrón? | Qué hizo el sistema | Interpretación | Saldo | % |
|---|---|---|---|---|---|---|
| **A** | 2024/01 → 2025/05 | **SÍ (100%)** | Aplicó **menos** que lo asignado | **Error real → rectificar** | ~$6,4M | 9% |
| **B** | 2025/06 → 2026/05 | **NO (verificado)** | Aplicó **0%** | **Correcto → intimación CONTESTABLE** | ~$66,7M | **91%** |

**El grueso de la deuda ($66,7M = 91%) es el bloque defendible:** esos CUIT no estaban en el padrón, así que aplicar 0% fue lo correcto según la regla. El quiebre arranca en **may-2025** (30/49) y desde **jun-2025** los CUIT intimados dejan de figurar en el padrón, coincidiendo con la explosión del saldo mensual (de <$1M a $4–12M/mes) y con un salto en la cantidad de sujetos intimados por mes (de ~15 a ~50).

---

## Prueba de que `ARDJU008` es el padrón correcto

En el **Bloque A**, donde los CUIT intimados figuran en el padrón, la alícuota del padrón **coincide EXACTO** con la que reclama la intimación:

> **235 de 235 casos coinciden, 0 difieren.**

Esto confirma que el padrón de **Regímenes Generales (`ARDJU008`)** es exactamente el que usa AGIP para intimar, y valida la metodología del cruce.

---

## La contradicción del Bloque B (el 91% de la deuda)

La carta de AGIP afirma, textualmente:

> *"...la alícuota por sujeto asignada en el **'Padrón de Regímenes Generales'**... Las alícuotas aplicadas a contribuyentes **que forman parte de este padrón**... es incorrecta..."*

**Pero es falso:** los CUIT intimados en el Bloque B **NO figuran** en el padrón `ARDJU008` publicado por AGIP para esos meses. Verificación decisiva (búsqueda cruda `grep -a`, sin parsear, sobre los archivos completos de 1,57M líneas):

- Los CUIT intimados de 2025/06 aparecen **0 veces** en los padrones de 06, 07 **y** 08-2025.
- Controles positivos OK: el CUIT propio de NB (30709246638) y un CUIT del Bloque A **sí** aparecen (1 vez cada uno).
- Cruce completo de los 27 meses: 2025/06=0/50, 2025/07=0/47, 2025/08=0/43, 2025/09=0/31, 2025/11=0/27, 2026/03=0/48, 2026/05=0/52 (ver tabla abajo).

**Conclusión:** aplicar 0% a esos sujetos fue **correcto** según la regla. AGIP no puede sostener que "forman parte de este padrón" cuando su propio padrón publicado no los contiene. El Bloque B ($66,7M) es **contestable**, y el Excel — que marca "NO figura en padrón" fila por fila — es la prueba a favor de NB.

---

## Lo que sí es error real: Bloque A (~$6,4M)

En 2024/01→2025/05 los sujetos **sí** estaban en el padrón y el sistema aplicó una alícuota **menor** a la asignada. Esto es una omisión genuina de percepción y corresponde rectificar. El origen técnico: el cálculo del cobro usa `clientes.percepcion` con `ISNULL(...,0)` y **sin chequear `percepcion_vencimiento`** (ver `api-rest-cobros/app/src/Repository/{PendingCharges,Liquidation,Tradable}Repository.php`), y el pipeline que actualiza esa columna (`percepciones_nb/`, repo aparte) quedó desactualizado / sin correr por cron.

---

## Detalle por periodo

Leyenda: **enPad/tot** = CUIT intimados que figuran en el padrón / total intimados ese mes. **coinc** = de los que figuran, cuántos coinciden con la alícuota reclamada.

| Periodo | enPad/tot | coinc | Saldo $ |
|---|---|---|---|
| 2024/01 | 10/10 | 10/10 | 162.390,84 |
| 2024/02 | 13/13 | 13/13 | 133.364,53 |
| 2024/03 | 11/11 | 11/11 | 348.471,70 |
| 2024/05 | 17/17 | 17/17 | 235.795,07 |
| 2024/06 | 18/18 | 18/18 | 132.747,55 |
| 2024/07 | 13/13 | 13/13 | 127.051,16 |
| 2024/08 | 18/18 | 18/18 | 259.939,47 |
| 2024/09 | 13/13 | 13/13 | 226.677,17 |
| 2024/10 | 9/9 | 9/9 | 54.881,00 |
| 2024/11 | 12/12 | 12/12 | 139.551,65 |
| 2024/12 | 12/12 | 12/12 | 107.697,67 |
| 2025/01 | 13/13 | 13/13 | 1.005.935,38 |
| 2025/02 | 12/12 | 12/12 | 296.290,30 |
| 2025/03 | 19/19 | 19/19 | 617.728,07 |
| 2025/04 | 14/15 | 14/14 | 1.068.115,16 |
| **2025/05** | **30/49** | 30/30 | 1.022.822,82 |
| **2025/06** | **0/50** | — | **12.588.965,10** |
| 2025/07 | 0/47 | — | 7.982.833,47 |
| 2025/08 | 0/43 | — | 9.037.516,84 |
| 2025/09 | 0/31 | — | 4.670.421,44 |
| 2025/10 | 1/31 | 1/1 | 4.645.407,19 |
| 2025/11 | 0/27 | — | 1.468.761,76 |
| 2025/12 | 1/28 | 1/1 | 3.085.841,90 |
| 2026/01 | 1/33 | 1/1 | 3.655.837,21 |
| 2026/02 | 1/46 | 1/1 | 4.445.018,84 |
| 2026/03 | 0/48 | — | 6.226.470,76 |
| 2026/05 | 0/52 | — | 9.357.440,41 |
| **TOTAL** | | | **73.103.974,46** |

---

## Focos secundarios (cruce DB, solo lectura — valores ACTUALES, no históricos)

- De 260 CUIT, solo **11 con `excluirPercepcion=1`** y **9 con `clientLo`** (LibreOpción) — no explican el grueso, pero si están excluidos/LO **y** fueron intimados, la exclusión está mal cargada.
- **35 CUIT con filas duplicadas** en `clientes` (13 con fila `niva=3`, que el task saltea por `WHERE niva<>3`) → ventas pueden caer en la fila sin percepción.

> ⚠️ Los valores de `clientes.percepcion` / `excluirPercepcion` consultados son **actuales**, no reconstruyen el estado histórico. La fuente histórica del "cómo lo presenté" es la columna **ALICUOTA APLICADA** de cada anexo.

---

## Postura para el estudio contable

La evidencia sostiene una defensa fuerte para el Bloque B:

1. **Regla:** sujeto no incluido en el padrón ⇒ no se percibe.
2. **Hecho verificado:** los CUIT del Bloque B no figuran en el padrón `ARDJU008` publicado por AGIP de esos meses (grep crudo sobre los archivos completos, controles positivos OK).
3. **Contradicción de AGIP:** la intimación afirma que "forman parte de este padrón", lo cual el propio padrón publicado desmiente.

→ **Contestar el Bloque B ($66,7M)** aportando el padrón publicado como prueba de que esos sujetos no estaban incluidos. La carga de probar lo contrario queda en AGIP.

→ **Reconocer/rectificar el Bloque A ($6,4M)**, donde sí hubo omisión (sujetos en padrón, alícuota aplicada menor a la asignada).

**Punto a chequear con el estudio:** por qué AGIP intima esos sujetos como "parte del padrón" si no están publicados — si existe un padrón interno/de riesgo no publicado, o si es un error de la intimación masiva. No se encontró otro padrón AGIP publicado (solo `ARDJU008`); la landing de padrones no lista un padrón de "alto riesgo" separado.

---

## Artefactos del análisis

Todos en `/var/www/nb/cobros/intimacion/`:

- `Intimaciones_AGIP_percepciones.xlsx` — entregable final (Resumen + 27 hojas).
- `anexos_consolidado.csv` — 694 líneas parseadas de los PDF.
- `padron_por_periodo.csv` — cruce CUIT×periodo contra el padrón real.
- `bajar_cruzar_padrones.py` — descarga + cruce de los padrones AGIP.
- `armar_excel.py` — genera el Excel.
- URLs de padrones reconstruibles vía `POST agip.gob.ar/api/pages/byPath` con `path` = `/agentes/agentes-de-recaudacion/ib-agentes-recaudacion/padrones/Padrón-de-Regímenes-Generales`.

## Ver también

- [[contexto]] — bugs conocidos y reglas de negocio
- [[arquitectura]] — repos y flujos
- [[cobros]] — índice
