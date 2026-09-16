# Feature: Emisor (Razón Social) en la grilla de Comprobantes

Corrige la columna **Razón Social** (emisor del comprobante) en la grilla de Comprobantes (`GET /v1/vouchers`), que salía vacía en casi todos los comprobantes y, al ser `null`, corría toda la grilla una columna.

## Regla del emisor (clave y no obvia)

El emisor se determina por **`FP_Empresas.SUCFacturaPlus = comprobante.CNUMSUC`**, **NO por el CODEMP del cliente**. NB (CODEMP 4) factura a sus clientes a través de dos entidades legales según la sucursal de la que sale el comprobante:

| CNUMSUC | Emisor (SUCFacturaPlus) | CODEMP | CUIT |
|---|---|---|---|
| `0005` | **DIGITO BINARIO SRL** | 5 | 30-70865519-4 |
| `0003` | **NB DISTRIBUIDORA MAYORISTA SRL** | 4 | 30-70924663-8 |

`FP_Empresas` tiene **1 fila por CODEMP**, pero `SUCFacturaPlus` **colisiona**: `0003` → NB(4)/NBElectric(9); `0010` → SUC10(7)/LASET(11)/LibreOpción(12).

## Bug original

El join era `FP_Empresas.SUCFacturaPlus = A.CNUMSUC AND FP_Empresas.CODEMP = clientes.CODEMP`. La condición de CODEMP **excluía al emisor cross-company** (DIGITO BINARIO es CODEMP 5, el cliente CODEMP 4) → `businessName = null`. Además el front hacía `text.length` sobre ese null → `TypeError` que **corría la fila una columna a la izquierda**. La única fila que se veía "bien" (con emisor) era la que casualmente tenía `CNUMSUC=0003`.

## Fix (rama `fix/vouchers-emisor-razon-social`, mergeado PR #1644 → Development)

- **Backend** (`VoucherRepository.php`): se reemplazó el `LEFT JOIN FP_Empresas` por un `OUTER APPLY` que resuelve el emisor por `SUCFacturaPlus = CNUMSUC` con **desempate por CODEMP del cliente** para las colisiones:
  ```sql
  OUTER APPLY (
    SELECT TOP 1 emp_e.CNOMBRE FROM FP_Empresas emp_e
    WHERE emp_e.SUCFacturaPlus = A.CNUMSUC
    ORDER BY CASE WHEN emp_e.CODEMP = clientes.CODEMP THEN 0 ELSE 1 END, emp_e.CODEMP
  ) emp
  ```
  Aplicado en query principal + conteo; referencias `FP_Empresas.CNOMBRE` → `emp.CNOMBRE` en SELECT, GROUP BY y buscador. **Path UY (companyCode 11) sin cambios** (joinea solo por CODEMP; su tabla `_Uy` no tiene CNUMSUC).
- **Frontend** (`pages/vouchers.vue`): guard `v-if="text && text.length > 0"` en el slot `businessName`.

## Verificación

Serie `0005` → **DIGITO BINARIO SRL** (coincide con el PDF), sin duplicar filas, conteo (23.569) y path UY/LASET (1.329) intactos, buscador por razón social OK. El `VoucherDto` existe pero **no se aplica** en `GetVouchers` (devuelve filas crudas del repo).

## Ver también

- [[feature-nota-credito-debito]] — otra feature sobre comprobantes/cta cte tocada en paralelo
- [[relacion-companycode|companyCode por tabla]]
- [[feature-pdf-fiscal-por-empresa|PDF fiscal por empresa]] — también usa `FP_Empresas` como emisor
- [[changelog#2026-09-15 — Fix emisor (Razón Social) en grilla de Comprobantes]]
