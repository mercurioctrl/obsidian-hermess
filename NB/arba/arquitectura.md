# Arquitectura

Proyecto de scripts CLI en Python, sin framework ni dependencias externas. Dos scripts independientes que se encadenan cuando ARBA rechaza operaciones.

## Flujo normal

1. Exportar `ARBA_PERCEPTIONS_AAAAMM.txt` del sistema contable
2. `generar_lote_arba.py` → valida, renombra, comprime y agrega hash MD5
3. Subir el ZIP: `arba.gov.ar → Agentes → Agentes de Recaudación → Presentación de DDJJ → Presentación Web → Carga por lote`
4. Esperar ~2 h (procesamiento asincrónico)
5. Verificar sin operaciones rechazadas → cerrar y enviar DDJJ

## Flujo con rechazo (ver [[proceso-correccion-padron]])

Si ARBA observa operaciones por alícuota, se corrige contra el padrón con `corregir_padron.py` y se regenera el lote como LOTE siguiente.

## Formato del archivo fuente — Nuevo Diseño de Registro ARWeb

**71 caracteres por línea**, sin cabecera ni pie, sin líneas en blanco.

| Campo | Pos. | Long. | Notas |
|---|---|---|---|
| CUIT percibido | 1-13 | 13 | `XX-XXXXXXXX-X` |
| Fecha percepción | 14-23 | 10 | `dd/mm/aaaa` |
| Tipo comprobante | 24 | 1 | F/R/C/D/V/E/H/I |
| Letra comprobante | 25 | 1 | A/B/C o espacio |
| Nro sucursal | 26-30 | 5 | ceros a izquierda |
| Nro emisión | 31-38 | 8 | ceros a izquierda |
| Monto imponible | 39-52 | 14 | `99999999999,99`, negativo en NC |
| Alícuota | 53-57 | 5 | `99,99` |
| Importe percepción | 58-70 | 13 | `9999999999,99`, negativo en NC |
| Tipo operación | 71 | 1 | A=Alta, B=Baja, M=Modificación |

Actividad P7 quincenal: **81 chars** (agrega Fecha Emisión en pos 71-80). Las posiciones de imponible/alícuota/percepción son iguales en 71 y 81 chars.

### Posiciones para código (0-indexed, verificadas)

| Campo | slice Python | Formato |
|---|---|---|
| CUIT | `[0:13]` | `XX-XXXXXXXX-X` |
| Imponible | `[38:52]` | 14 · `NNNNNNNNNNN,NN` |
| Alícuota | `[52:57]` | 5 · `NN,NN` |
| Percepción | `[57:70]` | 13 · `NNNNNNNNNN,NN` |
| Tipo operación | `[70]` / `[80]` | 1 |

**Percepción = imponible × alícuota / 100**, redondeo comercial **HALF_UP** (`Decimal` + `ROUND_HALF_UP`). Coma decimal, no punto. Confirmado: recalcular 764/764 líneas ya correctas dio idéntico.

## Nomenclatura ARBA

```
AR-{CUIT_SIN_GUIONES}-{AAAAMMQ}-{ACTIVIDAD}-LOTE{N}_{MD5}.zip
```

- `Q`: 0=mensual devengado · 1=1ra quincena · 2=2da quincena
- `ACTIVIDAD`: D7 (devengado mensual, habitual) · P7 (percibido quincenal)
- El ZIP contiene exactamente el `.txt` con el mismo nombre base
- El hash es **MD5** sobre el ZIP completo — si se re-comprime o renombra, el hash deja de servir y ARBA lo rechaza por integridad

## Validaciones del script

`generar_lote_arba.py` valida por línea: longitud (71/81), formato de CUIT, tipo/letra de comprobante, tipo de operación, y **formato numérico de los importes** (imponible, alícuota, percepción — regex `^-?\d+,\d{2}$`, acepta negativos de NC). Elimina líneas vacías finales automáticamente.

**No valida** que la alícuota sea la correcta — eso solo lo sabe el padrón de ARBA (ver [[proceso-correccion-padron]]).

## Ver también

- [[arba]]
- [[proceso-correccion-padron]]
- [[contexto]]
