# Intimación AGIP — Percepciones IIBB CABA

> Análisis de la intimación de AGIP/ARCIBA a **NB DISTRIBUIDORA MAYORISTA SRL** (CUIT 30-70924663-8, agente de recaudación 14862-6) por aplicar mal la alícuota de percepción de Ingresos Brutos CABA (Res. 352-AGIP-2022).

**Fecha análisis:** 2026-07-09
**Fuente:** 27 anexos de intimación (`intimacion/*.pdf`) + los 27 padrones reales `ARDJU008MMYYYY` bajados de agip.gob.ar.
**Entregable:** `intimacion/Intimaciones_AGIP_percepciones.xlsx` (Resumen + 27 hojas mensuales).

---

## Conclusión ejecutiva

AGIP reclama **$73.103.974,46** en total (ene-2024 → may-2026, 27 periodos, 260 CUIT únicos, 694 líneas). Al cruzar cada CUIT intimado contra el padrón AGIP real de su mes, aparecen **dos bloques claramente distintos**:

| Bloque | Periodos | ¿CUIT en padrón? | Qué pasó | Saldo | % del total |
|---|---|---|---|---|---|
| **A** | 2024/01 → 2025/05 | **SÍ (100%)** | Se aplicó una alícuota **menor** a la del padrón vigente | ~$6,4M | 9% |
| **B** | 2025/06 → 2026/05 | **NO (≈0%)** | AGIP exige **6%** (máxima), el sistema aplicó **0%** | ~$66,7M | **91%** |

El quiebre arranca en **may-2025** (30/49 en padrón) y desde **jun-2025** los CUIT intimados dejan de figurar en el padrón, coincidiendo con la explosión del saldo mensual (de <$1M a $4–12M/mes).

---

## Prueba de que `ARDJU008` es el padrón correcto

En el **Bloque A**, donde los CUIT intimados figuran en el padrón, la alícuota del padrón **coincide EXACTO** con la que reclama la intimación:

> **235 de 235 casos coinciden, 0 difieren.**

Esto descarta la duda de "¿AGIP usa otro padrón?". El padrón de **Regímenes Generales (`ARDJU008`)** es exactamente el que usa AGIP para intimar.

---

## Causa raíz del Bloque B (el 91% de la deuda)

Cuando un CUIT **no está** en el padrón, la regla ARCIBA es percibir a la **alícuota máxima (6%)**. El sistema, en cambio, aplica **0%**. El desglose es contundente:

- **Lo que AGIP dice que debías aplicar:** 433 filas a **6%** + 4 a 5%.
- **Lo que el sistema realmente aplicó:** 432 filas a **0%** + 5 a 3%.

Es exactamente el bug de `percepciones_nb/guardarPercepcion_task.php`:

```php
$alicuota = $DATOS ? (float) $DATOS["ALICUOTA_PERCEPCION"] : 0;
```

Cuando el CUIT **no aparece** en el padrón (`$DATOS` vacío), el sistema pone **0 en lugar de 6%**.

A esto se suma que el cálculo del cobro usa `clientes.percepcion` directo con `ISNULL(...,0)` y **sin chequear `percepcion_vencimiento`** (ver `api-rest-cobros/app/src/Repository/{PendingCharges,Liquidation,Tradable}Repository.php`), y que el pipeline que actualiza esa columna (`percepciones_nb/`, repo aparte) **no corría por cron** — `aplicarPercepciones.log` aplicó 0 el 01-jun y 01-jul (staging vacío).

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

## Pregunta para el estudio contable

La duda ya **no** es "¿es el padrón correcto?" (lo es, probado 235/235). La pregunta es:

> **¿Confirman que la regla de "sujeto no incluido en padrón ⇒ 6% obligatorio" aplica?**

Si la respuesta es sí, el **Bloque B ($66,7M, 91% de la deuda) es indefendible** y el fix técnico es que el pipeline aplique **6% (no 0)** cuando el CUIT no está en el padrón.

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
