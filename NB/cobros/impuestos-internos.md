# Impuestos internos (`internalTax`)

Investigado y validado el 2026-09-15 al agregar el concepto al [[arquitectura#Dashboard de Impuestos (Statistics/Taxes)|Dashboard de Impuestos]].

En el PDF del comprobante aparecen como columna **"I. Int."** por línea y como renglón **"Impuestos Internos"** del bloque *Otros Tributos* (pie del comprobante).

## Fuentes

| Tabla | Columna | Qué es |
|---|---|---|
| `NewBytes_DBF.dbo.FP_FactWebCliEncabezado` | `internalTax` | **importe total** del comprobante, en la moneda del comprobante |
| `NewBytes_DBF.dbo.FP_FactWebCliDetalle` | `internalTax` | **alícuota (%)** de la línea |
| `NewBytes_DBF.dbo.articulo` | `internalTax` | **alícuota (%)** del artículo (maestro) + flags `nimpintc`/`nimpintv` (compra/venta) |

> [!warning] Misma columna, dos significados
> `internalTax` es **importe** en el encabezado y **alícuota** en el detalle y en `articulo`.
> Es la trampa más fácil de este tema. Ver [[contexto#Bugs conocidos (preexistentes, no del feature)]].

**Para pesos:** `internalTax * NVALDIV` — el importe está en la moneda del comprobante (~92% DOL).
Ver [[contexto#Monedas: qué columna está en qué moneda]].

Solo **93 artículos de 26.415** tienen alícuota > 0 en el maestro.

## Validación

Factura A 0006-00020829 (`enc 612190`, DOL, `NVALDIV` 1530):

```
detalle: base 2 × 98,6648 = 197,3296 × 10,51% = 20,74
encabezado: internalTax = 20,74
PDF: "Impuestos Internos 20,74" / "Importe Otros Tributos: DOL 20,74"   ✓
```

Factura A 0006-00019978 (`enc 609530`, DOL, `NVALDIV` 1520): `internalTax` = 9,32 → **$14.166,40**.
Control de cotización: `TOTIMP 135,56 × 1520 = $206.051,20`, idéntico al total que imprime el PDF.

### Redondeo: usar siempre el encabezado
El encabezado guarda el importe **ya redondeado a centavos de USD**; al multiplicar por ~1500 ese
redondeo se amplifica hasta **~$7,60 por comprobante** (0,005 × cotización). Con ~300 comprobantes
mensuales son ~$2.000 contra ~$20M → irrelevante, pero explica micro-diferencias contra un recálculo
por línea (en la 00019978: 14.166,40 del encabezado vs 14.172,96 exacto del detalle, $6,56).

**Criterio adoptado:** el encabezado es el importe efectivamente consignado en el comprobante y
declarado a AFIP. Para un dashboard impositivo vale lo declarado, no un recálculo teórico. Es el mismo
criterio que ya usaba el xlsx del [[changelog|reporte de ventas]].

## Alícuotas: son cuatro, no una

**10,50 / 10,51 / 23,46 / 25,00** (hubo 23,30 en 2024). **Nunca asumir 10,5%.**

La composición se dio vuelta entre años (líneas de `FP_FactWebCliDetalle`):

| Alícuota | 2024 | 2025 | 2026 (ene-sep) |
|---|---|---|---|
| 23,46 % | 247 | 852 | 32 |
| 23,30 % | 3 | 1 | — |
| 10,51 % | — | 1.611 | 1.853 |
| 10,50 % | — | 99 | 841 |
| 25,00 % | — | 11 | 2 |

En **2024 el 100% tributaba 23,3/23,46%**; el 10,5% aparece en 2025. **El mismo monitor cambió de
tasa**: en 2025 hubo 719 líneas de MONITOR al 23,46%, en 2026 casi todas al 10,5x.

> [!important] La tasa del artículo NO es estable en el tiempo
> No validar períodos viejos usando la alícuota actual del maestro. Para cualquier verificación
> histórica, usar el importe del comprobante.

## Qué productos tributan

**2026 (ene-sep), 2.728 líneas:**

| Producto | Alícuota | Líneas |
|---|---|---|
| MONITOR | 10,51 % | 1.853 |
| MONITOR | 10,50 % | 840 |
| HIKVISION (DVR/NVR) | 23,46 % | 28 |
| XVR | 23,46 % | 3 |
| SAMSUNG | 10,50 % | 1 |
| MONITOR | 23,46 % | 1 |
| TOMACORRIENTE | 25,00 % | 1 |
| TECLA | 25,00 % | 1 |

**Monitores = 2.694 de 2.728 (98,7%).** El resto es casi todo equipamiento de CCTV (grabadoras
Hikvision `NVR-104MH-D`/`NVR-108MH-D`/`DVR 4-CH 1080P` y XVR). En 2025 también aparecían
**PARLANTE** (24 líneas) y **ACCESORIOS** (11) al 23,46%.

### Dos cosas que conviene mirar en el maestro
1. **10,50 vs 10,51 conviven en monitores** y el 10,50 gana terreno mes a mes durante 2026
   (ene 19 vs 171 → ago 177 vs 198). Sale de `articulo`, no del comprobante → alguien está
   reclasificando artículo por artículo sin terminar. **Una de las dos tasas está mal.**
2. **Tres casos que parecen error de carga:** TOMACORRIENTE y TECLA al 25% (no son bienes
   alcanzados) y un MONITOR al 23,46% (tiene la tasa de los grabadoras). Son 3 líneas sobre
   2.728 → en plata no mueven nada, pero son los candidatos si alguien corrige el maestro.

## Cobertura histórica

El dato arranca en **2024-11**. Antes, `FP_FactWebCliDetalle.internalTax` es **NULL en las 80.383
líneas anteriores**: el campo no se poblaba, no es que no se facturara.

> [!caution] El $0 de meses anteriores a 2024-11 es falso
> El dashboard va a mostrar cero para esos meses. No compararlo contra períodos históricos.

En el encabezado, desde 2024-11 **no hay ni un NULL** en los 4.554 comprobantes con impuestos
internos (221 en 2024, 2.134 en 2025, 2.199 en 2026).

## Volumen

~**$15–28M por mes** en 2026, sobre 150–310 comprobantes. Mismo orden de magnitud que las
percepciones IIBB, así que no es un concepto menor.

```
2026-01  $12.642.722     2026-06  $14.739.348
2026-02  $28.479.166     2026-07  $22.739.783
2026-03  $14.393.582     2026-08  $22.350.074
2026-04  $16.606.513     2026-09  $ 6.754.762 (parcial)
2026-05  $28.456.351
```

## Ver también

- [[arquitectura#Dashboard de Impuestos (Statistics/Taxes)]] — dónde vive el código
- [[contexto#Monedas: qué columna está en qué moneda]] — el bug de moneda del dashboard
- [[changelog]] · [[cobros]] · [[memoria]]
