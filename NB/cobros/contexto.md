# Contexto — CashBox Cobros

## Reglas de negocio importantes

### Sistema de cajas
- Cada usuario tiene una caja identificada por `USU_IDENTIFICACION`
- Los saldos de caja se almacenan en `MC_SALDOS_CAJA` por forma de pago
- Las formas de pago principales: 1=Dólares, 2=Pesos

### Cuenta corriente de clientes
- `MC_CCORRIENTES_MOVIMIENTOS`: cada movimiento tiene TR_CODIGO que indica el tipo
  - TR=30: Créditos varios (solo al prestar capital)
  - TR=42: Cobro efectivo (aparece en log de caja)
- `CC_IMPORTEUSD` es siempre en dólares; positivo = crédito al cliente, negativo = cobro

### Cotización
- Todas las cuentas guardan valores en dólares
- El importe en pesos se deriva: `monto_usd * cotizacion`
- La cotización del día se obtiene de `MC_FORMAS_PAGO.FP_COTIZACION`

### Préstamos de capital (`MC_PRESTAMOS_CAPITAL`)
- `TIPO=P`: préstamo otorgado al cliente
- `TIPO=C`: cobro/pago recibido del cliente
- El saldo = SUM(P.MONTO_TOTAL_USD) - SUM(C.MONTO_TOTAL_USD)
- Los pagos son parciales y libres — no están atados a un préstamo específico
- **Al prestar**: impacta CC (TR=30 positivo), NO impacta caja
- **Al cobrar**: NO impacta CC, SÍ impacta caja (log + saldo)

### Visibilidad de montos en el modal de capital
- Por defecto los montos aparecen ocultos (••••)
- El ícono de ojo en el footer alterna la visibilidad
- Si el usuario no tiene `ver_capital=1`, el ojito muestra error y no revela

### Total en pesos en el modal de capital
- No es `totalUsd × cotización actual`
- Es la suma fila a fila de `amountUsd × quote` de cada movimiento individual

### Dashboard de Impuestos (carga impositiva mensual)
- **IVA a pagar** = IVA débito (ventas, `TOTIVAS_EnviadoAFIP`) − IVA crédito (compras, `AfipComprobantesRecibidos.total_iva`). Negativo = saldo técnico a favor.
- **Carga impositiva total** del mes = IVA a pagar + percepciones IIBB + retenciones IIBB + retenciones ganancias + **impuestos internos** (agregado 2026-09-15, ver [[impuestos-internos]]).
- **Jurisdicciones** (`FP_Provincias.Id_Provincia`): AGIP = 1 (Capital Federal), ARBA = 2 (Buenos Aires), resto = "Otras".
- **Retenciones IIBB**: jurisdicción exacta (cada registro tiene `provinceId`).
- **Percepciones IIBB**: NO tienen jurisdicción a nivel factura → se aproximan por la provincia registrada del cliente (`clientes.ID_PROVINCIA`). Es aproximado (cliente multi-jurisdicción puede no ser fiel) pero reconcilia con el total.
- La tabla `NEW_BYTES.dbo.ganancias` (retenciones ganancias) está **vacía** hoy → esa categoría muestra 0 hasta que se carguen datos.
- ~~`MS_REMITO_PERCEPCIONES.IMPPERCEP_ARBA/CABA` NO sirve para desglosar percepciones: cubre solo remitos (miles vs millones), no reconcilia con `ImportePercepCLi`.~~ **CORREGIDO 2026-09-15:** sí reconcilia — `ImportePercepCLi` = `IMPPERCEP_CABA + IMPPERCEP_ARBA` **exacto** (verificado en 5/5 facturas, join `MSR.REMITO_FP = FP.CNUMALB` agrupando con `MAX`). La impresión de "miles vs millones" venía de dos cosas: MSR **arranca el 2025-05-14** (antes no hay filas) y la comparación mezclaba monedas. MSR es la **única fuente que separa CABA de ARBA** y es la que usan el reporte de percepciones y el xlsx de ventas. El dashboard sigue aproximando por provincia del cliente — se puede mejorar migrándolo a MSR (pendiente, solo para fechas ≥ 2025-05-14).

### Monedas: qué columna está en qué moneda

Descubierto el 2026-09-15. **~92% de los comprobantes se factura en DOL**, así que confundir esto
sub-reporta por un factor de ~15.

| Fuente | Moneda | Conversión |
|---|---|---|
| `FP_FactWebCliEncabezado.TOTIVAS_EnviadoAFIP` (IVA débito) | moneda del comprobante | `* NVALDIV` |
| `FP_FactWebCliEncabezado.ImportePercepCLi` (percepciones) | moneda del comprobante | `* NVALDIV` |
| `FP_FactWebCliEncabezado.internalTax` (imp. internos) | moneda del comprobante | `* NVALDIV` |
| `MS_REMITO_PERCEPCIONES.IMPPERCEP_CABA/ARBA` | moneda del comprobante | `* NVALDIV` |
| `AfipComprobantesRecibidos.total_iva` (IVA crédito) | moneda original (`moneda` + `tipo_cambio`) | `* tipo_cambio` (ver caveat) |
| `retentionIIBB.amountPaid` (retenciones IIBB) | **PESOS** | **ninguna — no tocar** |

- **`retentionIIBB.quotation` NO es un multiplicador**, es la cotización de referencia del día.
  Si se aplicara, una retención individual daría $80.278.962. `amountPaid` ya viene en pesos.
  Es la trampa principal al corregir el bug.
- **Evidencia (3 vías independientes)** de que las columnas FP están en la moneda del comprobante:
  (1) el recálculo desde `FP_FactWebCliDetalle` (`Σ NCANENT*NPREUNIT` por `NIVA` × tasa) coincide
  **al centavo** con `TOTIVAS_EnviadoAFIP` sin cotización en 8/8 facturas DOL; (2) el PDF imprime
  "IVA 21%: **DOL** 60,95 / IVA 10.5%: **DOL** 40,65" y la base guarda `101.61`; (3) no existe
  columna alternativa en pesos en el encabezado.
- **Caveat Allianz (sin resolver):** de 383 comprobantes de compra en USD de jun-ago 2026, **250 son
  todos de ALLIANZ ARGENTINA CIA DE SEGUROS con `tipo_cambio` entre 36 y 135,80** y fecha 2026
  (implausible), aportando 354.488 USD de IVA. O están en pesos y la importación marcó
  `moneda=USD` mal (→ excluirlos de la conversión), o son USD reales con `tipo_cambio` erróneo
  (→ ~$531M al IVA crédito). **No se puede distinguir desde la base**: hace falta un PDF de Allianz
  de julio 2026 (`imp_total 1117,90`, `total_iva 183,12`, 2026-07-14). Los otros 133 (tc > 1000)
  son sanos: $82.571.670.

### Intimación AGIP percepciones IIBB CABA (jul-2026)
AGIP intimó a NB por $73,1M en percepciones IIBB CABA mal aplicadas (Res. 352-AGIP-2022), 27 períodos ene-2024→may-2026. Análisis completo en [[intimacion-agip-percepciones]].
- **Regla de negocio clave:** si un CUIT **no figura** en el padrón de Regímenes Generales de AGIP (`ARDJU008` mensual), **no corresponde percibirle** (alícuota 0). El padrón publicado es la única fuente que el agente puede consultar.
- **Dos bloques:** A (2024/01–2025/05, ~$6,4M) sujetos EN padrón, se aplicó menos → error real. B (2025/06–2026/05, ~$66,7M = 91%) sujetos NO en padrón → 0% correcto → contestable.
- **Patrón del Bloque B:** 96% son clientes de **provincia de Buenos Aires** (`ID_PROVINCIA=2`, ARBA) y 92% tienen `percepcion_arba`>0, no percepción CABA → probable error de jurisdicción (AGIP reclama percepción de Capital sobre sujetos de provincia). Coincide con el mapeo documentado arriba (1=AGIP/CABA, 2=ARBA/Bs.As.).
- **Causa técnica secundaria (Bloque A):** el cálculo usa `clientes.percepcion` con `ISNULL(...,0)` sin chequear `percepcion_vencimiento`; el pipeline que actualiza esa columna (`percepciones_nb/`, repo aparte) quedó desactualizado/sin cron.

## Decisiones tomadas

### Fix OpenSSL para SQL Server (dev)
- ODBC Driver 18 + OpenSSL 3.0 necesita `SECLEVEL=0` y legacy provider en `/etc/ssl/openssl.cnf`

### display_errors = Off
- PHP 8.2 emite E_DEPRECATED por static trait methods → contamina respuestas JSON
- Solución: `display_errors=Off` + `error_reporting = E_ALL & ~E_DEPRECATED`

### AuthService::user() — mapeo manual
- El endpoint `/user` construye el array de permisos manualmente
- **Cualquier permiso nuevo en AuthRepository debe agregarse también en AuthService::user()**
- Error detectado: `verCapital` llegaba en el token del login pero no del refresh

### payCapitalDebt — sin impacto en CC
- Se intentó doble movimiento (TR=30 + TR=42 negativos) para neto 0 en CC, pero restaba doble
- Decisión final: el cobro de capital no toca CC; solo impacta caja

### Columnas de nombre en clientes
- `NewBytes_DBF.dbo.clientes`: nombre = `cnomcli`, razón social = `cnomcom`, CUIT = `cdnicif`
- No usar `capeage`/`cnbrape`/`cnombre` (son columnas de agentes/otra tabla)

## Bugs conocidos (preexistentes, no del feature)
1. **Búsqueda por CUIT**: `C.ccodcli = {stringFilter}` sin comillas → falla si el input tiene `-`
2. **companyCode = "null"**: el frontend envía el string literal `"null"` cuando no hay companyCode
3. **`/heartbeat` da 500 aunque la base esté OK**: `Repository/Health/HeartbeatRepository` arma su propio PDO **sin** `Encrypt=0; TrustServerCertificate=1`, entonces el ODBC Driver 18 falla la verificación del certificado self-signed. La conexión real (`src/App/Database.php`) sí los incluye y funciona. No confiar en el heartbeat para saber si la base está viva.
4. **DB host en `app/.env`** (gitignored): server alcanzable = `190.210.23.97:4444` (DB `NB_WEB`). Traía `190.210.23.108:1433` que da login timeout. Si el front no carga datos, revisar `DB_HOST`/`DB_PORT`.

5. **Dashboard de Impuestos mezcla USD con pesos** (detectado 2026-09-15, **ABIERTO**): `TaxesStatisticsRepository` suma `TOTIVAS_EnviadoAFIP` e `ImportePercepCLi` sin `NVALDIV`. Impacto jun-ago 2026: IVA débito muestra $64.398.072 cuando son **$1.061.689.169** (×16,5); percepciones muestra $13.734.460 cuando son **$186.341.180** (×13,6). El fix son dos `* NVALDIV`, **sin tocar retenciones** (ya están en pesos). Ver [[contexto#Monedas: qué columna está en qué moneda]].
6. **`monthsBetween()` se come el último mes si el rango corta a mitad** (detectado 2026-09-15, **ABIERTO**): calcula el límite como el día 1 del mes de `endExcl` con `while ($cursor < $limit)`, así que con `01-06-2026_15-09-2026` devuelve jun/jul/ago y **septiembre desaparece** — no se lista ni se suma, aunque las queries SQL sí traen los datos. No se nota en uso normal porque el menú linkea con `.endOf('month')`. Archivo: `src/Domain/Statistics/Taxes/Repositories/TaxesStatisticsRepository.php:338`.
7. **`internalTax` significa dos cosas**: importe en `FP_FactWebCliEncabezado`, alícuota (%) en `FP_FactWebCliDetalle` y en `articulo`. Ver [[impuestos-internos]].

## Convención de ramas (importante)

La rama de integración tiene distinta capitalización en cada repo:
- `api-rest-cobros` → **`Development`** (D mayúscula), staging `Gamma`, prod `main`
- `cobros-web-app-v1` → **`development`** (minúscula), staging `gamma`, prod `main`

Ramas de trabajo con prefijos de ticket Jira: `COB-<n>-...`, `API-COB-...`, `APP-COB-...`, `PED-...`.

## TODOs / próximos pasos
- ✅ ALTERs ejecutados en prod: `prestar_capital`, `cobrar_capital`, `ver_capital`
- ✅ Permisos asignados: agentes 27 y 66 → `cobrar_capital=1`; agente 12 → los 3 permisos
- ✅ `feature/prestamos-capital` integrado en `Development`/`development` (2026-07-02)
- Fix bug CUIT search en `Client.php:441`
- Fix bug companyCode null en `Client.php:331`
- ✅ `feature/reporte-ventas-empresa` (Dashboard Impuestos + reporte de ventas xlsx) mergeado en `Development`/`development` (2026-09-15)
- ✅ Impuestos internos agregados al Dashboard de Impuestos, sumados al total (2026-09-15)
- **Decidir fix del bug de monedas** del dashboard (dos `* NVALDIV`) — queda a la espera de la decisión del usuario
- **Decidir fix de `monthsBetween`** (mes parcial perdido)
- **Pendiente de evidencia:** PDF de factura Allianz de julio 2026 para resolver el caveat del IVA crédito
- Evaluar migrar el desglose por jurisdicción de percepciones del dashboard a `MS_REMITO_PERCEPCIONES` (exacto, pero solo ≥ 2025-05-14)
- Revisar el maestro `articulo`: 10,50 vs 10,51 en monitores (una está mal) y 3 artículos mal marcados (TOMACORRIENTE/TECLA al 25%, un MONITOR al 23,46%)

## Ver también
- [[arquitectura]] · [[stack]] · [[changelog]] · [[memoria]] · [[impuestos-internos]]