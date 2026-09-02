# Changelog — Tarjetas

> [[Tarjetas]]

## 2026-08-29

- **Nuevo origen de datos: API del home banking.** Los movimientos del período en curso se pueden traer de `POST /obp-servicios/bff/cards/cards/{cardId}/movements` (payload con `accountId`, `accountNumber`, `cardId`, `cardData`). El token JWT dura **10 minutos**, así que hay que copiar el cURL desde DevTools y correrlo enseguida.
  - Visa: `accountNumber` 1103119048 · Amex: `accountNumber` 110315238.
  - Devuelve `paymentsAndBonifications` + un array `cards` (titular y adicional) con cada movimiento, su `installment`/`totalInstallments` e `isPending`.
  - **No trae** intereses, IVA, percepciones RG 5617 ni IIBB: eso se liquida al cierre y solo aparece en el PDF.
- Creadas [[Visa 2026-09]] y [[Amex 2026-09]] — período en curso (cierre 27-Ago-26), marcadas como **preliminares**.
- [[Cuotas Activas]] **reconstruida desde los movimientos reales** en vez de la proyección oficial del banco: 26 planes en Visa + 12 en Amex, con proyección mes a mes hasta Mayo/28.
- [[Índice Resúmenes]] y [[Tarjetas]]: agregado el período en curso.

### Dato de la sesión

- Consumos del período: **$10.105.876,83** (Visa 4,32M + Amex 5,79M) + **U$S 593,96**. Pagos aplicados: **$11.608.796,53**.
- Se iniciaron **14 planes nuevos en cuotas** ($1.086.383,90/mes) contra 8 que terminan ($848.182,52/mes) → **+$238.201,38/mes** de cuota fija. Va en contra de la regla 6 de [[contexto]].
- Cuota fija comprometida para Set/26: **$2.767.722,35**.

## 2026-08-18

- **Pago extra a Amex:** $1.000.000 más. Total pagado a Amex: **$6.100.000**. Baja el saldo financiado a **$7.815.144,63** y el pendiente del resumen de agosto a **$7.274.170,39**. Actualizados [[Proyección de Pago]], [[contexto]] y [[memoria]].

## 2026-08-14

- **Pago extra a Amex:** $900.000 (tarjeta ****-34375). Total pagado a Amex: $5.100.000. Saldo pendiente del resumen de agosto: $8.274.170,39 (vto 10-ago ya pasó → financiándose). Actualizados [[Proyección de Pago]] y [[memoria]].

## 2026-08-09

- Procesados los **16 resúmenes** (Visa + Amex, Ene–Ago 2026) → 16 notas fieles con cada movimiento transcripto textualmente del PDF.
- Notas de análisis creadas: [[Índice Resúmenes]], [[Cuotas Activas]], [[Gastos por Comercio]], [[Pagos e Intereses]].
- Dashboard [[Panorama de Gastos]] con gráficos (Mermaid + imágenes de líneas y área apilada por categoría).
- [[Proyección de Pago]] — escenarios para desarmar el saldo financiado + cálculo de interés pagando solo el mínimo.
- Recategorización de comercios con datos aportados por el usuario: "Otros" bajó de 43% → 20% (ver [[contexto]]).
- Gráficos generados como **SVG+PNG** (matplotlib bloqueado por PEP 668).
- `Home.md` de la bóveda: agregada la sección **💳 Finanzas**.
- Scripts y documentación técnica persistidos en el repo `/var/www/Tarjetas` (`scripts/`, `docs/PIPELINE.md`, `CLAUDE.md`).

### Dato de la sesión
- El usuario **pagó $5.500.000 a Visa el 2026-08-08** y decidió pagar Amex por el mínimo.
- **2026-08-09:** pagos parciales a **Amex** (tarjeta ****-34375): $1.000.000 + $2.400.000 + $800.000 = **$4.200.000,00** → cubre el mínimo ($4.198.210). Saldo pendiente del resumen Amex de agosto: $9.174.170,39 (vto 10-ago). Plan: pagar el resto durante la semana.
