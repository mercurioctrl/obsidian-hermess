# Finanzas — BLU

Temas financieros, de cobranzas y de compliance de BLU Digital Agency.

## Casos y compliance

- [[caso-mercury-acer|Caso Mercury — Origen de fondos (Acer USD 12.322)]] — verificación
  de origen de fondos ante Mercury por el pago de Acer. Deadline 2026-07-09.
- [[pagos-freelance-guillermo-avila|Pagos freelance — Guillermo Avila (QA)]] — respaldo
  Mercury de pagos salientes a colaborador freelance de QA en México, vía USDT/Binance
  (jun–ago 2026).

## Ver también

- [[Blu]]
- [[bluMiniErp/Modulo Mercury Invoicing|Mercury Invoicing (bluMiniErp)]]

## 2026-08-13 · Cambio de divisas Mercury → USDC → ARS

- Origen: Cuenta Mercury (USD)
- Monto enviado: **2,000.00 USD**
- Plataforma intermedia: [indicar si aplica, ej. Mercury <> exchange]

### Paso 1 — USD → USDC
- Monto recibido: **1,871.35509812 USDC**
- Comisión: **40.00 USD**
- Precio referencia: **1.04736937 USDC/USD**

### Paso 2 — USDC → ARS (Binance)
- Monto convertido: **2,947,665.92066592 ARS**
- Tasa de referencia: **1 ARS ≈ 0.000634734 USDC**

### Notas
- Registrar esta operación para trazabilidad entre fondos Mercury y ARS operativos.
- Verificar que el asiento contable refleje:
  - Salida de 2,000 USD de Mercury.
  - Ingreso de 1,871.35509812 USDC.
  - Gasto por comisión de 40 USD.
  - Ingreso de 2,947,665.92066592 ARS desde Binance.

### Paso 3 — Retiro a cuenta bancaria en ARS
- Origen: Binance (saldo en ARS)
- Destino: Cuenta bancaria personal (ARS)
- Monto retirado: **2,947,665.92066592 ARS**
- Comisión retiro (1%): **29,493.21 ARS**
- Monto neto acreditado: **2,918,172.71066592 ARS**

### Notas adicionales
- Registrar la comisión del 1% como gasto financiero.
- Alinear esta salida con el flujo de fondos personal vs. Blu (definir imputación contable según corresponda).

### Resumen de costo neto de la operatoria
- Monto inicial enviado: **2,000 USD** desde Mercury.
- Cashback esperado: **20 USD** (1% de 2,000 USD, cash out).
- Comisión fija de cambio: **40 USD**.
- Comisión retiro 1% (29,493.21 ARS): se asume neutralizada por el cashback del 1% sobre los 2,000 USD.

**Costo neto final estimado de toda la operación:** **20 USD**.
