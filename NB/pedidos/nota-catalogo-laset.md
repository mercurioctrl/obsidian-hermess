# Pedido a Catálogo — Alta de 39 SKUs para Laset (companyCode = 11)

**Fecha:** 2026-05-15
**De:** Equipo Pedidos / Migración Laset
**Para:** Equipo Catálogo
**Asunto:** Alta de 39 artículos faltantes para la empresa Laset (companyCode = 11)

---

## Qué necesitamos

Dar de alta en la tabla `articulo` **39 SKUs** con **`companyCode = 11`** (Laset).

Hoy estos SKUs existen únicamente como artículo de **NB (companyCode = 4)**.
**No se pueden reutilizar** los artículos de NB: Laset necesita su propio
`ID_ARTICULO` con `companyCode = 11`, igual que el resto de las empresas del
grupo. Mientras falten, **48 líneas de compra + 48 líneas de venta** de Laset
quedan trabadas y no se pueden completar (remitos + stock).

## Por qué

Estamos migrando la operación histórica FOB de Laset desde la planilla al ERP.
Cada producto que Laset compró/vendió tiene que existir como artículo propio de
Laset (comp=11). Estos 39 nunca se dieron de alta para Laset — solo están en NB.

## Qué NO hacer

- **No** cambiar el `companyCode` del artículo NB existente.
- **No** reutilizar el `ID_ARTICULO` de NB para Laset.
- Crear un artículo **nuevo**, con `companyCode = 11`, conservando el mismo
  `ID_PRODUCTO` (SKU) que figura abajo.

## Prioridad

Ordenados por impacto (cantidad de líneas Laset bloqueadas). El más urgente es
**`100-100001973WOF`** (8 líneas).

| # | SKU (ID_PRODUCTO) | ID_ARTICULO NB (solo referencia, NO reutilizar) | Líneas bloqueadas |
|--:|---|---|--:|
| 1 | `100-100001973WOF` | 122551 | 8 |
| 2 | `B550 AORUS ELITE AX V2` | 114549 | 4 |
| 3 | `B650M AORUS ELITE AX` | 119875 | 4 |
| 4 | `BX8071512700` | 117137 | 4 |
| 5 | `GV-N5070GAMING OC-12GD` | 120372 | 4 |
| 6 | `PRIME B550M-K` | 104775 | 4 |
| 7 | `TUF GAMING B650EM-PLUS WIFI` | 121651 | 4 |
| 8 | `AD5S560016G-S` | 119123 | 2 |
| 9 | `AD5S560032G-S` | 119433 | 2 |
| 10 | `AD5U480032G-S` | 117833 | 2 |
| 11 | `ASU650SS-1TT-R` | 121572 | 2 |
| 12 | `B650 EAGLE AX` | 120264 | 2 |
| 13 | `B850 EAGLE WIFI6E` | 120273 | 2 |
| 14 | `B850M GAMING X WF6E` | 120271 | 2 |
| 15 | `GV-N506TEAGLE OC-16GD` | 120481 | 2 |
| 16 | `GV-N5070AERO OC-12GD` | 120370 | 2 |
| 17 | `GV-N5070AORUS M-12GD` | 121690 | 2 |
| 18 | `GV-N5070WF3OC-12GD` | 120479 | 2 |
| 19 | `GV-N507TAERO OC-16GD` | 120283 | 2 |
| 20 | `GV-N5090AORUS M-32GD` | 120367 | 2 |
| 21 | `GV-R9070XTAORUS E-16GD` | 120169 | 2 |
| 22 | `HDWG82AXZSTA` | 122550 | 2 |
| 23 | `MO27Q2` | 121215 | 2 |
| 24 | `PRIME A520M-A II` | 115799 | 2 |
| 25 | `PRIME B550M-K ARGB` | 121686 | 2 |
| 26 | `PRIME B650EM-A` | 122529 | 2 |
| 27 | `PRIME B650EM-A WIFI` | 121302 | 2 |
| 28 | `PRIME B850M-A WIFI` | 121653 | 2 |
| 29 | `PRIME B850M-K` | 121654 | 2 |
| 30 | `PRIME H510M-F R3.0` | 121656 | 2 |
| 31 | `ROG STRIX B650E-F GAMING WIFI` | 118494 | 2 |
| 32 | `TUF GAMING A620AM-PLUS` | 122525 | 2 |
| 33 | `TUF GAMING A620AM-PLUS WIFI` | 122515 | 2 |
| 34 | `TUF GAMING B550M-PLUS` | 109245 | 2 |
| 35 | `TUF GAMING B850-E WIFI` | 121655 | 2 |
| 36 | `TUF GAMING X870-PLUS WIFI` | 119735 | 2 |
| 37 | `X870E AERO X WOOD` | 122574 | 2 |
| 38 | `Z790 AORUS ELITE AX` | 118103 | 2 |
| 39 | `Z790 EAGLE AX` | 119246 | 2 |

> CSV con los mismos datos para procesar en bloque:
> `docs/laset_fasec_skus_sin_comp11.csv`

## Una vez dados de alta

Avisennos. Nosotros re-vinculamos las líneas de Laset a los nuevos artículos
comp=11 y completamos la migración (remitos + stock). No hace falta que hagan
nada más del lado de ustedes.

Gracias.
