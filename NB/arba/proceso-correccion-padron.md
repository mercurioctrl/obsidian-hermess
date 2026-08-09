# Proceso de corrección por padrón

Flujo **mensual recurrente**. Cuando ARBA rechaza operaciones con el mensaje:

> **"La alícuota ingresada difiere de las alícuotas del contribuyente"**

NO es un error del script ni del ZIP: la alícuota que exporta el sistema contable no coincide con la que ARBA tiene registrada para ese CUIT en su **padrón de percepciones** del mes. ARBA cruza cada percepción contra la tasa registrada del contribuyente.

## Pasos

1. **Bajar el padrón del mes** desde el portal ARBA (`Agentes → Agentes de Recaudación → Padrones → Regímenes Generales`, período `MMAAAA`). Viene en un ZIP con:
   - `PadronRGSPer{MMAAAA}.TXT` → **Percepciones** (el que se usa; puede venir renombrado `padroARBARegimenesGenerales.txt`)
   - `PadronRGSRet{MMAAAA}.TXT` → Retenciones (NO usar)
2. **Correr `corregir_padron.py`**:
   ```bash
   python3 corregir_padron.py \
     --archivo ARBA_PERCEPTIONS_AAAAMM.txt \
     --padron "/ruta/PadronRGSPer{MMAAAA}.TXT" \
     --salida ARBA_PERCEPTIONS_AAAAMM_corregido.txt
   ```
   Reemplaza cada alícuota por la del padrón y recalcula percepción = imponible × alícuota (redondeo comercial HALF_UP). **Control de calidad:** el reporte muestra `redondeo N ok / 0 difieren` — debe dar **0 diferencias** en las líneas cuya alícuota ya era correcta (confirma posiciones de campo y redondeo).
3. **Quitar las líneas de CUIT que el padrón marca a 0%** (alícuota `00,00`) — ARBA rechaza operaciones en importe 0. Precedente confirmado (junio 2026): los lotes corregidos no llevan líneas al 0%. El reintegro al cliente se maneja por contabilidad aparte.
4. **Regenerar con `generar_lote_arba.py` como LOTE siguiente** (LOTE2, LOTE3...) con el **archivo completo corregido**, no solo las operaciones observadas. Criterio histórico: se resube el lote entero corregido como nuevo número de lote.

## Formato del padrón

Separado por `;`, un contribuyente por línea:

```
P;25062026;01072026;31072026;20000033481;D;N;N;0,00;01;
```

| Campo | Contenido |
|---|---|
| 1 | Régimen (`P` = Percepción) |
| 2 | Fecha de publicación (ddMMyyyy) |
| 3-4 | Vigencia desde / hasta |
| 5 | **CUIT** (11 díg, sin guiones) |
| 6 | Tipo (`D`=Directo, `C`=Convenio Multilateral) |
| 8 | `S` si la alícuota cambió ese mes |
| **9** | **Alícuota** (`N,NN`, coma decimal) |
| 10 | Grupo ARBA |

## Ver también

- [[arba]]
- [[arquitectura]]
- [[changelog]]
