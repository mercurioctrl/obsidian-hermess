# Módulo Contabilidad

Sección `/contabilidad`: **liquidación de impuestos del mes** y descarga del **Libro IVA** en Excel
(hojas **Ventas** y **Compras**), calcado del export de *Mis Comprobantes* de ARCA que ya usaba el contador.

Mergeado en **PR #34 + #35** (2026-08-21). Ver también [[Reglas de Negocio]], [[Modulo Permisos]] y [[Medios de Pago]].

## Qué entra y qué no

| | Entra | No entra |
|---|---|---|
| **Ventas** | Comprobantes AFIP emitidos por BLU (`comprobantes_afip`, estado `EMITIDA` o `ACREDITADA`): facturas **y** notas de crédito | Invoices de **Mercury** (no son comprobantes argentinos), presupuestos `FACTURADO` sin comprobante, movimientos de cuenta corriente, cobros MP/Stripe |
| **Compras** | Gastos con **IVA discriminado** (`iva_monto > 0`) = facturas de compra con crédito fiscal | Gastos sin factura (propinas, viáticos sin respaldo), sueldos (van por F.931), retiros, percepciones |

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

## Limitaciones conocidas
- El libro cubre **sólo lo que pasó por el sistema**. No es el Libro IVA Digital completo (eso exige
  todos los comprobantes emitidos y recibidos del período, incluidos los de afuera del ERP). Conciliar
  siempre contra *Mis Comprobantes* antes de presentar.
- **Exportación de servicios**: los invoices de Mercury (offshore USD) no generan Factura E. Si el
  servicio se presta desde Argentina al exterior, ese comprobante falta y el libro no lo muestra.
- Los gastos en USD (SaaS del exterior) entran como compra común si tienen IVA cargado, pero en
  realidad son importación de servicios y van por otro régimen.

## Ver también
- [[Reglas de Negocio]] — dominio: cuenta corriente vs gastos, IVA en gastos
- [[Medios de Pago]] — Mercury/Stripe/MP (por qué no entran al Libro IVA)
- [[Modulo Permisos]] — `VER_SECCION_CONTABILIDAD`, `VER_MONTOS_SALDOS`
- [[Base de Datos]] — tabla `gastos` (columnas fiscales), `comprobantes_afip`
- [[Frontend]] — Dashboard (Rentabilidad por Cliente), proyecto (simulador de impuestos)
- [[Errores Comunes#Costo real de una compra en el simulador de impuestos (2026-08-23)]]
- [[changelog#2026-08-21]]
