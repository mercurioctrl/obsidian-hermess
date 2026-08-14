	# Intimación AGIP — Percepciones IIBB CABA

> Análisis de la intimación de AGIP/ARCIBA a **NB DISTRIBUIDORA MAYORISTA SRL** (CUIT 30-70924663-8, agente de recaudación 14862-6) por aplicar mal la alícuota de percepción de Ingresos Brutos CABA (Res. 352-AGIP-2022).

**Fecha análisis:** 2026-07-09
**Fuente:** 27 anexos de intimación (`intimacion/*.pdf`) + los 27 padrones reales `ARDJU008MMYYYY` bajados de agip.gob.ar.
**Entregable:** `intimacion/Intimaciones_AGIP_percepciones.xlsx` (Resumen + 27 hojas mensuales).

---

## ⭐ ESTADO RECTIFICATIVAS (2026-08-14, act.) — lo más actual

Doc completo: `intimacion/ESTADO_RECTIFICATIVAS.md`. Alcance: **19 meses intimados**.

- **17 PRESENTADOS en e-Arciba** ✅ (2024/01,02,03,05,08,09,10,11,12; 2025/01,02,03,04,05,12; 2026/01,02) + 2025/10 de yapa. **FALTAN SOLO 2024/06 y 2024/07** (Convenio Multilateral).
- **⭐ 11 REGLAS DE VALIDACIÓN AL IMPORTAR** (todas descubiertas importando de verdad; ARCIBA rechaza fila por fila): (1) `BASE=MONTO−OTROS−IVA`; (2) `PERCEP=BASE×ALIC` redondeo **HALF-UP**; (3) `PERCEP==TOTAL`; (4) alícuota en grilla; (5) **sitIVA=3→IVA=0**; (6) sitIVA solo {1,3,4}; (7) tipoDoc de empresa (CUIT 30/33)=`3`, no CUIL; (8) CUIT dígito verificador (DNI relleno no sirve); (9) **razón social no vacía**; (10) sin acentos; (11) **letra B→IVA=0**. Reparador que cubre casi todo: `generador/reparar_arciba.py` (Decimal HALF-UP).
- **MÉTODO escalar-a-target** (`generador/escalar_a_target.py`): para meses de reconstrucción, escalar BASE/IVA/OTROS por `factor=target/percep`, con `target=presentado + Saldo a rectificar` → Diferencia=Intimado exacto. Es el ancla-e-Arciba, ahora aplicado también a los 4 AFIP.
- **⭐ CRITERIO FLOR DEFINITIVO:** `Saldo a rectificar = Total intimado − SOLO las líneas "aplicada 0 → ajustada 6"` (todo lo demás se rectifica, incluidas CONTESTAR que no son 0→6). En el Excel: columna **Diferencia (rect−presentado) debe = columna Intimado/Saldo a rectificar** (Cumple SI). Flor lo lee columna por columna.
- **4 meses RE-rectificados** (2025/04,05,12; 2026/02): tenían líneas CONTESTAR-no-0→6 que se excluían de más → re-escalados al Saldo a rectificar de Flor. **HAY QUE RE-PRESENTARLOS (Rectificativa 2).**
- **REGLA DURA: los meses ya presentados NO se tocan** (verificar en e-Arciba, lista "Rectificativa - Por importación", antes de modificar cualquier TXT).
- **Por qué faltan 2024/06,07:** Convenio Multilateral (+176/+47 comprobantes de más). Intimación chica ($225.596). Pendiente aplicar escalar-a-target.


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

## Por qué AGIP pudo intimar: el disparador fue "declarar en cero" (confirmado 2026-08-03)

No percibir estuvo bien; el problema fue **de forma**: NB **declaraba esas operaciones en la DDJJ de percepciones CABA con alícuota 0** (bloque *"PADRÓN REGÍMENES GENERALES - 0%"* de la presentación ARCIBA), en vez de **no incluirlas**. Al declararlas, AGIP las tenía en su radar, las cruzó contra su padrón y les aplicó la alícuota que creía correspondiente. Si esos sujetos (provincia Bs.As. / ARBA) no hubieran entrado en la DDJJ CABA, no habría nada contra qué cruzar.

**Prueba (cruce agregado DDJJ presentada vs anexos de intimación):** las presentaciones reales `intimacion/presentaciones/2025-0{6,7,8}.pdf` traen la línea *"PADRÓN REGÍMENES GENERALES - 0%"*, y **el 100% de las líneas intimadas del Bloque B tienen alícuota aplicada = 0**. La base intimada es un **subconjunto** (siempre ≤) de la base declarada al 0% de cada mes:

| Período | DDJJ 0% (registros / base) | Anexo intimado (líneas / base) |
|---|---|---|
| 2025/06 | 183 / $256.556.932 | 50 / $209.816.091 |
| 2025/07 | 169 / $139.427.318 | 47 / $133.047.234 |
| 2025/08 | 163 / $159.008.670 | 43 / $150.625.290 |

AGIP eligió las de mayor monto (jul/ago ~95% de la base 0% del mes en ~45 CUITs). *Caveat: cruce a nivel registros+base total; el borrador PDF de la DDJJ solo trae resumen por alícuota, no detalle nominal — para prueba 1-a-1 hace falta el TXT importado a ARCIBA.*

## Causa raíz en el código + fix aplicado

El TXT de percepciones CABA se genera en `GET /perceptioniibb?type=CABA`. El filtro por jurisdicción en `PerceptionRepository::setFilters()` comparaba contra `'AGIP'`, pero el endpoint **solo recibe `'CABA'` o `'ARBA'`** (el front solo ofrece esas dos opciones) → la rama `'AGIP'` era **código muerto**, así que el reporte CABA **nunca** aplicaba `AND MSR.IMPPERCEP_CABA > 0` y colaba las filas con CABA en 0/NULL.

**Fix (`api-rest-cobros`, rama `fix/perception-caba-cero`, PRs #940 → `blu-dev-staff`, #941 → `Development`):**
```diff
-  if(strtoupper($filters['type']) == 'AGIP'){
+  if(strtoupper($filters['type']) == 'CABA'){
       $filter .= " AND MSR.IMPPERCEP_CABA > 0";
   }
```
`> 0` excluye **tanto NULL como 0** (`NULL > 0` → UNKNOWN, `0 > 0` → false). Queda simétrico con ARBA.

**Verificación con datos reales (corrida 2026-08, datos de jul-2025):** los TXT generados `CABA_PERCEPTIONS_202608.txt` (1.208 filas) y `ARBA_PERCEPTIONS_202608.txt` (268 filas) tienen **0 filas con alícuota o importe de percepción en cero**. Antes del fix, CABA arrastraba ~180 filas en 0. Volúmenes normales de ARBA (reusando la query real): jun-2025 = 303, jul-2025 = 268 — ARBA es de forma estable ~20-25% de CABA (solo se percibe a los sujetos del padrón ARBA, que son pocos).

---

## Qué tienen en común los CUIT del Bloque B (patrón encontrado)

Cruce de los 147 CUIT del Bloque B contra `clientes` (solo lectura). El eje que los separa del Bloque A es **la jurisdicción**:

| Atributo | Bloque B (NO en padrón) | Bloque A (en padrón) |
|---|---|---|
| **Provincia = Buenos Aires** (`ID_PROVINCIA=2`) | **96%** (141/147) | 40% |
| Provincia = CABA (`ID_PROVINCIA=1`) | 3% (4) | 55% |
| **Tienen `percepcion_arba` > 0** | **92%** (135) | 64% |
| Tienen `percepcion` (CABA) > 0 | **3%** (5) | 96% |
| Personas físicas (CUIT 20/23/27) | 83% | 51% |
| Solapamiento de CUIT entre bloques | **0** (conjuntos disjuntos) | — |

**Denominador común = jurisdicción.** El Bloque B son clientes **domiciliados en provincia de Buenos Aires, sujetos a percepción de ARBA, no de AGIP/CABA**. Por eso:

1. No figuran en el padrón de Regímenes Generales de AGIP (son contribuyentes de provincia, no de CABA).
2. El sistema les aplica (correctamente) percepción **ARBA**, y CABA en 0.
3. **AGIP los intima igual reclamando 6% de percepción CABA** → tiene toda la pinta de un **error de jurisdicción de la intimación**: AGIP reclama percepción de Capital Federal sobre sujetos de provincia de Buenos Aires.

El resto de atributos (LibreOpción, `excluirPercepcion`, condición IVA, inactivo, año de alta, IIBB propio) **no diferencian** los bloques. Refuerza la postura de contestar el Bloque B.

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

**Hipótesis con más fuerza (error de jurisdicción):** el 96% de los CUIT del Bloque B son de **provincia de Buenos Aires** y el 92% tienen percepción **ARBA** cargada, no CABA. AGIP estaría reclamando percepción de Capital Federal sobre sujetos de provincia — que ni corresponden a su padrón ni a su jurisdicción. Argumento adicional para contestar: aportar el domicilio/jurisdicción de esos clientes. No se encontró otro padrón AGIP publicado (solo `ARDJU008`); la landing de padrones no lista un padrón de "alto riesgo" separado.

---

## Artefactos del análisis

Todos en `/var/www/nb/cobros/intimacion/`:

- `Intimaciones_AGIP_percepciones.xlsx` — entregable final (Resumen + 27 hojas).
- `anexos_consolidado.csv` — 694 líneas parseadas de los PDF.
- `padron_por_periodo.csv` — cruce CUIT×periodo contra el padrón real.
- `bajar_cruzar_padrones.py` — descarga + cruce de los padrones AGIP.
- `armar_excel.py` — genera el Excel.
- URLs de padrones reconstruibles vía `POST agip.gob.ar/api/pages/byPath` con `path` = `/agentes/agentes-de-recaudacion/ib-agentes-recaudacion/padrones/Padrón-de-Regímenes-Generales`.

---

## Actualización 2026-08-12 — Rectificativas (respuesta a la intimación)

**Cómo se rectifica:** en e-Arciba se re-importa la DDJJ completa del mes con nueva secuencia (F.5225 + intereses). Cada rectificativa debe cumplir el criterio del estudio: **`rectificativa = presentado + intimación_rectificable`**.

**El DB de hoy NO reproduce lo presentado** (reprocesó base + rate + `ImportePercepCLi` juntos). Se descartaron todas las vías de reconstrucción (generador con-padrón, saftel/descargarAGIP en vivo, campos "congelados"). **Única fuente fiel = el TXT que efectivamente se presentó cada mes.**

**Regla de armado (confirmada por el dueño), quirúrgica desde el presentado real:**
1. CUIT intimados **que SÍ están en el padrón** → suben a su alícuota del padrón.
2. **Todo lo que se mandó en 0% se saca, salvo el punto 1** — incluye los intimados-por-error (Bloque B, no en padrón, "nos los intimaron por error porque no deberíamos haberlos mandado").
3. El resto, intacto.

**Estado: 7 de 18 meses listos** (`intimacion/PARA_PRESENTAR/`):
- **Exactas** (base = e-Arciba al centavo): 2025/10, 2026/01.
- **Dif mínima** (<0,05%): 2024/08, 09, 10, 11, 2025/02.
- **Faltan 11** (sin TXT presentado original): 2024/01, 02, 03, 05, 12; 2025/01, 03, 04, 05, 12; 2026/02.

**Recuperación de presentados:** los archivos del sistema viejo se llaman `PERCEPCIONES_AFIP_<timestamp>.txt/.docx` (no `CABA_PERCEPTIONS`). Buscar en disco **por contenido** (líneas que empiezan `2029`+fecha). Algunos guardados como `.docx` de Word (extraer XML + `html.unescape`).

**e-Arciba API:** `GET cc/rest/ddjjs` (con sesión) da el total presentado OFICIAL de cada DDJJ (`liqImpuesto.totalOperaciones`) → `presentado_earciba_oficial.csv`.

**Consulta abierta con el estudio:** la columna INTIMACIÓN de la planilla de Flor da más baja que sus propios PDF de intimación (nuestra corrección coincide al centavo con el PDF). Mail enviado 2026-08-12.

Doc maestro para retomar: `intimacion/ESTADO_RECTIFICATIVAS.md`.


## Ver también

- [[contexto]] — bugs conocidos y reglas de negocio
- [[arquitectura]] — repos y flujos
- [[cobros]] — índice

---

## Rectificativas reconstruidas — los 20 meses (2026-08-07)

Se generaron los TXT de rectificativa de **los 20 meses con líneas de Bloque A** (2024/01-03,05-12; 2025/01-05,10,12; 2026/01-02).

**El problema:** no existían los TXT originales presentados, y **ninguna fuente los reproduce**: el endpoint `/perceptioniibb` da 0 para meses previos a 2025-05-14 (no existía la tabla `MS_REMITO_PERCEPCIONES`); el sistema viejo *saftel* recalcula con el padrón actual; e-Arciba solo entrega el **resumen** por alícuota (no el detalle por comprobante de DDJJ importadas). La DB de hoy fue reprocesada y no reproduce las bases declaradas.

**El método (validado):**
```
Rectificativa = facturas FP (base real, congelada)
              × alícuota del padrón histórico ARDJU008 de ese mes (por CUIT)
              + regla "0% no va" (no en padrón o padrón=0 → excluir)
```
Como la alícuota del padrón **es** la correcta, la reconstrucción autocorrige el Bloque A y saca los no-padrón en un solo paso, sin depender de ARCIBA ni de archivos guardados.

**Validación (POC mayo-2025 contra el TXT presentado real):** 99% alícuotas idénticas, 94% bases idénticas, percepción $24,61M vs $24,80M (**99,2%**).

**Entregables:**
- `intimacion/recon/RECON_YYYY-MM.txt` — 20 meses, **18.864 líneas, $522,9M** percep, formato ARCIBA 215-char.
- `intimacion/Rectificativas_reconstruidas.xlsx` — legible, 1 hoja por mes + Resumen; **1.166 correcciones (Bloque A) resaltadas** con antes→después; **408 excluidos** ("0% no van").

**Caveats (para el estudio):** universo = clientes percibidos (`ImportePercepCLi>0`), no incluye los de padrón cobrados a 0; es DDJJ "fresca correcta" (recalcula todos), no edición quirúrgica; las bases de la intimación estaban infladas → posible defensa adicional. Ver [[changelog]] y [[mail-estudio-contable]].

### Veredicto (2026-08-09): la reconstrucción no reconcilia

Al comparar `recon/RECON_*.txt` contra los **presentados reales de ARCIBA** (`intimacion/presentado_arciba.csv`, bajados de e-Arciba), la reconstrucción se desvía del objetivo (presentado + intimación) **entre −$2,3M y +$16M**, en ambas direcciones. Dos causas: (1) el universo `ImportePercepCLi>0` **mezcla percepción ARBA con CABA** (ej. 2024/06: presentado $18,7M vs recon $34,9M, +$16M); (2) la **base de la DB driftó** (tipos de cambio mal grabados, facturas reprocesadas a 0).

**Conclusión:** sin los TXT originales presentados (solo tenemos mayo, el `(38)`), **no se puede reconstruir un TXT por comprobante fiel** — ni la DB ni ARCIBA (que solo da el resumen) tienen el detalle. Lo firme: el **objetivo por mes = presentado (ARCIBA) + intimación**. El resto es decisión del estudio contable (rectificativa por diferencias / recuperar originales / contestar Bloque B). Detalle completo en `intimacion/ESTADO_RECTIFICATIVAS.md`. Ver [[changelog]].