# Módulo Contabilidad

Sección `/contabilidad`: **liquidación de impuestos del mes** y descarga del **Libro IVA** en Excel
(hojas **Ventas** y **Compras**), calcado del export de *Mis Comprobantes* de ARCA que ya usaba el contador.

Mergeado en **PR #34 + #35** (2026-08-21). Ver también [[Reglas de Negocio]], [[Modulo Permisos]] y [[Medios de Pago]].

## Qué entra y qué no

| | Entra | No entra |
|---|---|---|
| **Ventas** | Comprobantes AFIP emitidos por BLU (`comprobantes_afip`, estado `EMITIDA` o `ACREDITADA`): facturas **y** notas de crédito | Invoices de **Mercury** (no son comprobantes argentinos), presupuestos `FACTURADO` sin comprobante, movimientos de cuenta corriente, cobros MP/Stripe |
| **Compras** | Gastos con **IVA discriminado** (`iva_monto > 0`) = facturas de compra con crédito fiscal | Gastos sin factura (propinas, viáticos sin respaldo), sueldos (van por F.931), retiros, percepciones/retenciones sufridas (→ van por [[#Retenciones sufridas (migración 0117)]], no son crédito fiscal) |

⚠️ **Una factura acreditada se declara igual.** `estado = ACREDITADA` es semántica del ERP, no
"no declarar": la factura y su NC van las dos y netean entre sí. Excluirlas descuadra contra lo que
ARCA ya tiene registrado con CAE.

## Backend

- **`ContabilidadService`**
  - `liquidacion($desde,$hasta)` — todo en **ARS** (convierte DOL/USD con la cotización de cada
    comprobante/gasto): IVA débito − crédito, Ganancias, IIBB. Es la **única** fuente del cálculo:
    `DashboardService::impuestosResumen()` delega acá para que Dashboard y Contabilidad no se
    desincronicen.
  - `libroVentas()` / `libroCompras()` — filas del libro, orden cronológico (factura antes que su NC).
  - Desglose por alícuota: sale de `comprobantes_afip.request_json → Iva.AlicIva` (ids AFIP
    3=0%, 9=2,5%, 8=5%, 4=10,5%, 5=21%, 6=27%). Si falta, deduce una sola alícuota de la relación IVA/neto.
- **`LibroIvaExcelService`** — escribe el `.xlsx` a mano (ZIP + OOXML mínimo) usando **`ext-zip`**
  (el container ya lo tiene). **Sin dependencias nuevas, sin rebuild.** Layout de columnas en
  `HEADERS_VENTAS` / `HEADERS_COMPRAS`; ⚠️ en **Compras el bloque de alícuotas arranca 2 columnas
  más a la derecha** que en Ventas.
- **`ContabilidadController`** — `index()` (resumen + libros + serie 12 meses) y `libroIva()` (descarga).

### Rutas
```
GET /api/contabilidad?anio=&mes=            (o desde=&hasta= para rango libre; default: mes actual)
GET /api/contabilidad/libro-iva?anio=&mes=&token=   (fuera de auth, token en query — descarga .xlsx)
```

### Convenciones del archivo (decisiones, no accidentes)
- **Importes en moneda de origen** con la cotización en su columna, como los exporta ARCA. La
  liquidación en pantalla, en cambio, va toda pesificada.
- **Notas de crédito en positivo**: el signo lo da el tipo de comprobante (1 = Factura A, 3 = NC A).
- **"Número de CAI"** se llena con el **CAE** (todos los comprobantes son electrónicos).
- **Provincia IIBB** fija en `CABA` (const `PROVINCIA_IIBB`).
- Razón social del cliente = `clientes.empresa ?: clientes.nombre` (igual que Facturación). ⚠️ No hay
  campo dedicado de razón social: si `empresa` tiene el nombre comercial y no el legal, el libro sale con ese.

## Datos fiscales del gasto (migración 0101)

`gastos` sumó las columnas que AFIP pide por línea en el libro de compras — todas **opcionales**
(`0101_add_datos_comprobante_to_gastos`):

| Campo | Uso |
|---|---|
| `proveedor_nombre` / `proveedor_cuit` | Razón social y CUIT del proveedor |
| `comprobante_tipo` | Código AFIP (1 Fac A, 6 Fac B, 11 Fac C, 3/8/13 NC…) |
| `comprobante_pto_vta` / `comprobante_numero` | Numeración |
| `comprobante_fecha` | **Fecha del comprobante ≠ fecha de pago.** El libro filtra por esta cuando está cargada; si no, cae a `gastos.fecha` (indexada) |
| `comprobante_cae` | CAE de la factura recibida |

Se cargan desde el componente `FacturaCompraFields.vue`, embebido en `/gastos/nuevo` y `/gastos/[id]`.
La sección se **auto-abre cuando el gasto tiene IVA > 0** (ahí es cuando va a aparecer en el libro).

### Gastos con IVA mixto — campo Exento / No gravado (migración 0104, 2026-08-24)

Una Factura A puede traer ítems con distinto tratamiento (ej: **catering 21% + propinas exentas**). El
gasto tenía un solo `iva_porcentaje`, así que no se podía cargar bien. Se agregó **`gastos.monto_exento`**
(decimal 12,2):

- El gasto lleva una parte **gravada** (`precio_unitario × cantidad` → neto, × `iva_porcentaje`) y una parte
  **exenta / no gravada** (`monto_exento`). **Total = neto gravado + IVA + exento**; el banco/caja descuenta el total.
- `ContabilidadService::libroCompras()`: `neto` = sólo la parte gravada (`monto − iva − exento`),
  `exento` = `monto_exento`, `total` = `monto`. El `LibroIvaExcelService` ya leía esas claves → sin cambios.
- Forms `/gastos/nuevo` y `/gastos/[id]`: campo "Exento / No gravado" con el total recalculado en vivo.
- **⚠️ Limitación:** cubre 1 alícuota gravada + exento. NO cubre dos alícuotas gravadas distintas
  (21% + 10,5%) en la misma factura — para eso harían falta ítems por gasto. Gastos 100% exentos
  (`iva_monto = 0`) NO entran al libro (`gastosConFactura` filtra `iva_monto > 0`).
- Verificado con factura real: neto 1.440.000 @21% + exento 174.240 → IVA 302.400, total 1.916.640. **PR #38.**

### Compras incompletas (2026-08-23)

Un gasto con `iva_monto > 0` pero **sin CUIT, tipo o número** de comprobante sale al Excel con esas
columnas vacías. `ContabilidadService::libroCompras()` marca cada fila con `incompleto` (= falta
alguno de los tres) y su `gasto_id`.

El aviso ámbar de `/contabilidad` **lista cada compra incompleta** (proveedor/descripción, fecha,
monto y **qué falta** — helper `faltantesDe(c)` sobre `cuit/tipo/numero`) con botón **"Completar"** →
`/gastos/{gasto_id}`. Además resalta esas filas en la tabla Compras y les pinta el lápiz en ámbar. Al
completar el gasto y volver, el aviso desaparece.

## Frontend

- `pages/contabilidad/index.vue` — selector de mes (`<input type="month">`), botón de descarga,
  tiles (ingresos netos, gastos con factura, ganancia, IVA venta/compra, IVA a pagar, Ganancias,
  IIBB, total), `PixelBarChart` de 12 meses y tablas Ventas/Compras con preview de lo que va al Excel.
- Permiso **`VER_SECCION_CONTABILIDAD`** (frontend: sidebar + `middleware/auth.global.ts` + `usuarios`),
  igual que el resto de las secciones. Ícono `lucide:calculator`.

## Estimación de impuestos en pantalla + simulador (2026-08-23)

La misma liquidación se muestra "en vivo" en presupuesto, proyecto y dashboard. **Todos los importes
fiscales van netos de IVA** (Ganancias e IIBB se calculan sin IVA; el IVA va por su carril).

Tres números que se confunden fácil:
- **Ganancia (base fiscal)** = `ventas netas − compras netas con factura`. Es la **base imponible de
  Ganancias**, NO utilidad de bolsillo. Sin gastos con factura, `Ganancia = total − IVA`.
- **Resultado operativo** (tile de arriba en el proyecto) = `ingreso presupuestado − gastos registrados`.
- **Te queda después de impuestos** = `Ganancia − Imp. Ganancias − IIBB`. El IVA **no** se resta (neutro:
  se cobra al cliente y se remite a AFIP). Es "lo que te queda" real de la operación.

### Simulador de facturas de compra (what-if) — `proyectos/[id].vue`
Botón "Simular compras" dentro del bloque "Impuestos estimados" (pestaña Ejecución). 100% client-side
reactivo, no toca backend. Se ingresa una compra neta `P` con alícuota `a`; muestra comparativa
**Actual vs Simulado** de cada impuesto y de "Te queda después de impuestos".
- Ahorro en impuestos = `P·a + P·(gan%)` (IIBB **no** cambia: es sobre ventas).
- **Costo real de la compra** = `total desembolsado (P + P·a) − ahorro`. ⚠️ NO `P − ahorro` (bug ya
  cometido, ver [[Errores Comunes]]). El costo real = cuánto baja "Te queda después de impuestos".
- Botón "Neutralizar IVA" fija `P = IVA débito / a`; pasado ese punto el excedente es saldo a favor /
  quebranto (se traslada).

### Dashboard — Rentabilidad por Cliente
`DashboardService::rentabilidadPorCliente()` arma una tabla por cliente (facturación `CARGO` ARS, gasto
vía `proyectos.cliente_id`, ganancia bruta, **impuestos prorrateados** por facturación sobre el `total`
global de la liquidación, ganancia neta). Los impuestos por cliente son **aproximación**: la liquidación
real es global. Gateado por `VER_MONTOS_SALDOS`.

## Multi-empresa — dos razones sociales (2026-09-08)

El negocio opera con **dos empresas de contabilidades separadas**: **BLU INC S.R.L** (principal, la
única que factura por AFIP) y **DIGITO BINARIO SRL**. Algunas facturas de **compra** las emiten a
DIGITO; las **ventas** por AFIP son todas de BLU. Se agregó atribución por empresa para poder liquidar
cada una por separado. **Decisión del usuario: solo etiquetado** — AFIP sigue emitiendo bajo BLU (no se
implementó emisión electrónica bajo el CUIT de DIGITO, que exigiría su cert/PV propios).

- **Migración 0114** — tabla `empresas` (`nombre`, `cuit`, `es_principal`, `activo`). Seed: BLU
  (principal, CUIT tomado de `configuracion`) + DIGITO BINARIO SRL (`cuit` NULL, cargable después).
  Modelo `Empresa` con `principal()` / `principalId()`.
- **Migración 0115** — `empresa_id` (FK nullable) en `gastos` y `comprobantes_afip`. **Todo el histórico
  se backfilleó a BLU** para que nada quede fuera de una contabilidad.
- **Gasto:** `GastoController::store` defaultea a la principal si no viene `empresa_id`. Selector de
  empresa en `/gastos/nuevo` y `/gastos/[id]`. `GastoResource` expone `empresa_id` / `empresa_nombre`.
- **Ventas (AFIP):** `AfipComprobanteService::emitir()` setea `empresa_id = principalId()` (BLU); la NC
  hereda el `empresa_id` de su factura.
- **`ContabilidadService`** — `liquidacion()` / `libroVentas()` / `libroCompras()` (+ helpers privados
  `comprobantesVenta` / `gastosConFactura`) aceptan `?int $empresaId`. Null = consolidado (todas). Las
  filas del libro exponen `empresa_id` / `empresa_nombre` (y `comprobante_id` en ventas) para el
  selector inline.
- **Frontend `/contabilidad`:** selector global **BLU / DIGITO / Todas** que filtra liquidación, libros,
  serie de 12 meses y **la descarga del Excel**. Al entrar, el filtro **arranca en BLU** (la principal),
  no en "Todas", para que el Libro IVA baje por empresa por defecto. Además, **selector inline por fila**
  en Ventas y Compras para reasignar al toque (refetch tras el cambio). El selector solo aparece si hay
  >1 empresa.

### Rutas nuevas
```
GET   /api/empresas                          (catálogo para los selectores; JSON directo, sin wrapper)
PATCH /api/contabilidad/asignar-empresa      (body: tipo=compra|venta, id, empresa_id — reasigna una fila)
GET   /api/contabilidad?...&empresa_id=       (filtro opcional; también en /contabilidad/libro-iva)
```

**Pendiente:** no hay CRUD de empresas (catálogo fijo de 2, editable por DB); DIGITO quedó sin CUIT.

## Retenciones sufridas (migración 0117)

Lo que el agente de retención nos descuenta al pagarnos una factura, y después se computa como
**pago a cuenta** del impuesto del período. Agregado el **2026-09-17**.

**El problema que resuelve:** la liquidación sólo sabía calcular el impuesto **determinado**. En la
DDJJ real de IIBB de agosto 2026 el determinado era $93.905,15 pero se ingresaron **$5,45**, porque
$93.899,70 ya habían sido retenidos. El ERP no tenía dónde cargar los certificados que llegan en
papel. Ver [[Conciliacion Impuestos 2026-08]].

### Modelo

Tabla `retenciones`, colgada del **presupuesto** (el ancla que usa el equipo), con FK opcional al
`comprobante_afip` concreto sobre el que se retuvo — que es como viene el certificado.

| Campo | Notas |
|---|---|
| `tipo` | `GANANCIAS` · `IIBB` · `IVA` · `SUSS` · `OTRO` (enum `TipoRetencion`) |
| `jurisdiccion` | Sólo IIBB (CABA, Provincia…) |
| `agente_nombre` / `agente_cuit` | El cliente que nos paga. Se precarga del cliente del presupuesto |
| `numero_certificado`, `fecha` | **La fecha del certificado define el período** al que se imputa |
| `base_imponible`, `alicuota`, `monto` | En la UI el monto se autocompleta con base × alícuota |
| `archivo_*` | Certificado escaneado (PDF/imagen), opcional pero es el respaldo legal |
| `empresa_id` | Se hereda del comprobante del presupuesto ([[#Multi-empresa — dos razones sociales (2026-09-08)]]) |

> [!warning] Los importes van SIEMPRE en ARS
> El agente retiene en pesos aunque la factura sea en USD. No hay conversión ni cotización acá.

> [!warning] La fecha del certificado ≠ la fecha de la factura
> Suelen caer en meses distintos. Los dos certificados de Microglobal son del **09/09/2026** sobre
> facturas del **01/09**, y **no** entran en la DDJJ de agosto aunque el trabajo sea de agosto.
> `retencionesPorTipo()` filtra por `fecha`, no por la fecha del comprobante.

### Efecto en la liquidación

`ContabilidadService::liquidacion()` suma las retenciones del período y las netea. **Las claves
viejas no cambiaron de significado** — siguen siendo el impuesto determinado — para no romper a los
consumidores actuales (`DashboardService::impuestosResumen()` delega acá). Se agregaron:

- `retenciones_iva`, `retenciones_ganancias`, `retenciones_iibb`, `retenciones_otras`, `retenciones_total`
- `iva_neto`, `ganancias_neto`, `iibb_neto`, `total_neto` — lo que **realmente se ingresa**.
  **Negativo = saldo a favor** que se arrastra al período siguiente.

> [!note] El neteo de Ganancias es informativo, el de IIBB es real
> **IIBB** es un anticipo mensual: el neteo mensual es exactamente lo que se ingresa.
> **Ganancias es anual**: el "determinado" mensual del ERP es una estimación propia, así que netear
> contra él una retención puntual da un número que no corresponde a ninguna DDJJ. Leerlo como
> referencia, no como posición fiscal.

### Endpoints

```
GET    /api/presupuestos/{presupuesto}/retenciones
POST   /api/presupuestos/{presupuesto}/retenciones          (multipart: incluye `archivo`)
DELETE /api/presupuestos/{presupuesto}/retenciones/{retencion}
GET    /api/presupuestos/{presupuesto}/retenciones/{retencion}/archivo   (fuera de auth, ?token=)
```

Gate: `VER_MONTOS_SALDOS` (son plata). El `store` valida que el `comprobante_afip_id` **pertenezca
al presupuesto** — si no, la retención quedaría imputada a otra venta (422).

### Frontend

- Card **"Retenciones sufridas"** en `pages/presupuestos/[id].vue`, debajo de *Impuestos estimados*:
  alta con modal, borrado, y descarga del certificado.
- `pages/contabilidad/index.vue`: bajo cada impuesto, lo retenido y lo que queda por ingresar; el
  tile negro suma `total_neto`.

> [!tip] El certificado de Ganancias se carga UNA sola vez
> RG 830 se emite **por orden de pago**, no por factura: un certificado puede cubrir facturas de
> varios presupuestos y trae un importe no sujeto a retención. Se carga en uno solo y se aclara en
> observaciones — la liquidación suma **por período**, no por presupuesto. El modal lo avisa.

## DDJJ del estudio — «ERP vs Estudio» (migración 0118)

Lo que el estudio declara y manda a pagar cada mes, guardado **al lado** de lo que calculó el ERP.
Agregado el **2026-09-17**. No corrige la liquidación propia: son dos fuentes que deben dar parecido,
y el valor está justamente en ver la diferencia.

**El problema que resuelve:** la conciliación de agosto 2026 hubo que hacerla a mano contra los PDFs
del estudio. Ver [[Conciliacion Impuestos 2026-08]].

Tabla `declaraciones_estudio`, **una por empresa/período/impuesto** (índice único). El POST es un
**upsert**: cargar y corregir son la misma acción. `empresa_id` es obligatorio — una DDJJ pertenece a
un CUIT, así que con empresa «Todas» la sección no ofrece comparación en vez de inventar una suma.

> [!warning] Se guarda el DESGLOSE, no sólo el importe a pagar
> En agosto 2026 el total cerraba salvo **$737,10** y el hueco estaba en el **crédito fiscal**: con
> sólo el total, eso no se ve. Campos opcionales: `base_imponible`, `debito_fiscal`,
> `credito_fiscal`, `impuesto_determinado`, `retenciones`. El único obligatorio es `monto_a_pagar`.
> También `numero_formulario`, `fecha_vencimiento`, `fecha_pago`, `pagado` y la DDJJ escaneada.

### Qué se ve

Sección **"ERP vs Estudio contable"** en `/contabilidad`:

- Por impuesto (IVA / IIBB), tabla **Concepto · ERP · Estudio · Diferencia** renglón por renglón:
  débito, crédito, determinado, retenciones, a ingresar. ✓ verde si coincide, ámbar si no.
- Tabla **mes a mes** de los últimos 12 meses con lo que queda a ingresar en cada fuente.
- Botón **"Copiar lo del ERP"** en el modal: precarga el desglose para tipear sólo lo que difiere.

Con agosto 2026 cargado, el panel reproduce exactamente la conciliación manual:

```
IVA   Débito fiscal          657.343,35   657.343,35   ✓
      Crédito fiscal         438.900,00   439.637,10     737,10
      A ingresar             218.443,35   217.706,25    -737,10
IIBB  Base imponible       3.130.171,80 3.130.171,80   ✓
      Impuesto determinado    93.905,15    93.905,15   ✓
      Retenciones                  0,00    93.899,70  93.899,70
      A ingresar              93.905,15         5,45 -93.899,70
```

> [!note] Cómo leer una diferencia
> La columna **ERP es neta de las retenciones cargadas**
> ([[#Retenciones sufridas (migración 0117)]]). La fila de retenciones de IIBB de arriba muestra
> $0,00 contra $93.899,70 porque los certificados de **agosto** todavía no están cargados en el ERP
> (sólo están los de septiembre). Eso no es un error de cálculo: es el panel diciendo qué falta.
>
> Y una diferencia tampoco es necesariamente un error del ERP: puede ser un comprobante que nunca
> pasó por el sistema. Es el disparador para ir a buscarlo, no un veredicto.

### Endpoints

```
GET    /api/declaraciones-estudio?empresa_id=&anio=
POST   /api/declaraciones-estudio                        (upsert, multipart con `archivo`)
DELETE /api/declaraciones-estudio/{declaracion}
GET    /api/declaraciones-estudio/{declaracion}/archivo  (fuera de auth, ?token=)
```

Gate `VER_MONTOS_SALDOS`. `GET /api/contabilidad` suma `declaraciones` (las del período, indexadas
por impuesto) y `por_mes` trae `iva_neto`/`iibb_neto` + `iva_declarado`/`iibb_declarado`. **Todo
`null` con empresa «Todas».**

## Limitaciones conocidas
- El libro cubre **sólo lo que pasó por el sistema**. No es el Libro IVA Digital completo (eso exige
  todos los comprobantes emitidos y recibidos del período, incluidos los de afuera del ERP). Conciliar
  siempre contra *Mis Comprobantes* antes de presentar.
- **Exportación de servicios**: los invoices de Mercury (offshore USD) no generan Factura E. Si el
  servicio se presta desde Argentina al exterior, ese comprobante falta y el libro no lo muestra.
- Los gastos en USD (SaaS del exterior) entran como compra común si tienen IVA cargado, pero en
  realidad son importación de servicios y van por otro régimen.
- Las **percepciones** sufridas (distintas de las retenciones) se pueden cargar con `tipo` = el
  impuesto que corresponda, pero el modelo no las distingue de una retención. Si el estudio las
  imputa en una línea distinta del formulario, el neteo del ERP no va a coincidir con la DDJJ.

## Ver también
- [[Reglas de Negocio]] — dominio: cuenta corriente vs gastos, IVA en gastos
- [[Medios de Pago]] — Mercury/Stripe/MP (por qué no entran al Libro IVA)
- [[Modulo Permisos]] — `VER_SECCION_CONTABILIDAD`, `VER_MONTOS_SALDOS`
- [[Base de Datos]] — tabla `gastos` (columnas fiscales), `comprobantes_afip`
- [[Frontend]] — Dashboard (Rentabilidad por Cliente), proyecto (simulador de impuestos)
- [[Errores Comunes#Costo real de una compra en el simulador de impuestos (2026-08-23)]]
- [[changelog#2026-08-21]]

## Conciliaciones contra las DDJJ reales

- [[Conciliacion Impuestos 2026-08]] — cotejo de agosto 2026 contra lo que presentó el estudio. Útil para ver qué toma y qué no toma esta liquidación frente a un F.2051 real.
