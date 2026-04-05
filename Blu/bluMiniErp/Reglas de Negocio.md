# Reglas de Negocio

Comportamientos de dominio criticos que no son obvios del codigo.

## Cuenta Corriente vs Gastos

Son dos modulos separados con propositos distintos:

| | Cuenta Corriente (`movimientos_cuenta`) | Gastos (`gastos`) |
|-|----------------------------------------|-------------------|
| Que representa | Debe/haber entre empresa y cliente | Salida real de dinero |
| Quien genera | Sistema automatico (aprobacion presupuesto) | Usuario manual |
| Banco/Caja | No involucra | Obligatorio |
| Saldo negativo | Cliente pago mas (credito a favor) | N/A |

Ver tablas en [[Base de Datos#movimientos_cuenta]] y [[Base de Datos#gastos]].

## Presupuestos - Flujo de estados

```
BORRADOR -> ENVIADO -> APROBADO -> FACTURADO
                    \-> RECHAZADO -> (puede volver a BORRADOR)
CANCELADO (accesible desde cualquier estado)
APROBADO / FACTURADO -> COBRADO
```

- Editable en cualquier estado excepto **COBRADO** y **FACTURADO**
- Solo eliminable en estado **BORRADOR**
- Al editar en APROBADO o ENVIADO: advertencia de confirmacion en [[Frontend]]
- Al guardar, los movimientos de cuenta corriente se actualizan automaticamente
- Al pasar a **APROBADO**: crea MovimientoCuenta tipo CARGO
- Al pasar a **COBRADO**: requiere credenciales admin. Ver [[#Operaciones que requieren credenciales admin]]

Modelo en [[Backend - Modelos#Presupuesto]]. Endpoints en [[Backend - API#Presupuestos]].

## IVA en Presupuestos

El IVA es **por item**, no global:

```
Item.subtotal = cantidad x precio_unitario
Item.iva_monto = subtotal x iva_porcentaje / 100
iva_porcentaje valores validos: 0, 10.5, 21

Presupuesto.iva_monto = SUM(items.iva_monto)
Presupuesto.total = (subtotal_neto - descuento) + iva_monto
```

Siempre llamar `presupuesto->recalcularTotales()` despues de editar items.

## IVA en Gastos

Mismo patron que items de presupuesto:

```
subtotal  = precio_unitario x cantidad
iva_monto = subtotal x iva_porcentaje / 100
monto     = subtotal + iva_monto   <- impacta saldo banco/caja
```

- `iva_porcentaje` valores: 0, 10.5, 21, 27
- Default: 0 (gastos antes de migracion 0047 quedan sin IVA)
- El [[Backend - API#Gastos|controller]] calcula `monto`, nunca viene del frontend

## Bancos y Cajas - Saldo automatico

El `saldo_actual` se ajusta automaticamente:

| Evento | Efecto |
|--------|--------|
| `POST /gastos` | `BancoCaja->restarSaldo(monto)` |
| `DELETE /gastos` | `BancoCaja->sumarSaldo(monto)` |
| `PUT /gastos` (mismo banco) | ajusta diferencia |
| `PUT /gastos` (banco distinto) | devuelve al anterior + resta del nuevo |
| `POST /empleados/{id}/pagos` | `BancoCaja->restarSaldo(monto)` |
| `DELETE /empleados/{id}/pagos/{id}` | `BancoCaja->sumarSaldo(monto)` |
| `POST /bancos-cajas/{id}/ajuste` | suma o resta segun monto |

Ver [[Backend - Modelos#BancoCaja]] y [[Modulo Personal#Comportamiento de pagos y saldo]].

## Gastos - Campo realizado

Indica si el pago al acreedor fue efectivamente cancelado.

- Toggle: `PATCH /api/gastos/{id}/realizado`
- Marcar: cualquier usuario, sin confirmacion
- Desmarcar: requiere credenciales admin. Ver [[#Operaciones que requieren credenciales admin]]
- En proyecto: checkbox en tabla de gastos, filas no realizadas con `opacity-50`

## Operaciones que requieren credenciales admin

```php
$data = $request->validate(['email' => 'required|email', 'password' => 'required|string']);
$admin = Usuario::where('email', $data['email'])->where('activo', true)->first();
if (!$admin || !Hash::check($data['password'], $admin->password)) abort(401);
if (!$admin->esAdmin()) abort(403);
```

Operaciones que usan este patron:
- Eliminar banco/caja
- Ajuste manual de saldo de banco/caja
- Desmarcar gasto como `realizado`
- Transicion de presupuesto a COBRADO

## Gastos - Proteccion por estado de presupuesto

Los gastos de un proyecto **no se pueden editar ni eliminar** si el presupuesto esta COBRADO o FACTURADO.

- Backend: `GastoController` valida con `validarNoProtegido()`. Retorna 422.
- Frontend: campo `editable` en GastoResource controla visibilidad de botones.
- Gastos sin proyecto (OPERATIVO, RETIRO) siempre son editables.

## Activaciones - Copiar entre proyectos

- Proyectos deben ser del mismo cliente
- Se copia estructura (hitos con categoria, actividad, descripcion, QC)
- Datos de ejecucion (QE, QB, fecha, estado, Jira) se dejan vacios

## Etiquetas de Presupuestos

- Se gestionan en Configuracion (paleta de 11 colores)
- Relacion many-to-many via pivot `presupuesto_etiqueta`
- Asignables desde presupuesto **y desde proyecto** (mismo endpoint)
- Filtrable en listados de presupuestos (`?etiqueta_id=`) y proyectos

Ver [[Base de Datos#etiquetas]] y [[Backend - API#Etiquetas]].

## Orden de listados - Ultima actividad

Presupuestos y proyectos: `updated_at DESC`. Se toca al modificar hijos:
- Presupuesto: al crear/editar/eliminar items (`$touches`), al sync etiquetas
- Proyecto: al crear/editar/eliminar gastos, empleados, adjuntos, Jira boards, activaciones, hitos

## Personal - Asignacion a Proyectos

Ver [[Modulo Personal]] para detalle completo.

- Relacion N:M via tabla `proyecto_empleado`
- Unique constraint en (proyecto_id, empleado_id)
- Se usa `syncWithoutDetaching`

## Autoria (created_by)

Presupuestos y proyectos registran `created_by` -> FK a usuarios.
Se guarda con `auth()->id()` al crear.

## Monedas y Tipo de Cambio

Cotizacion en gastos: se auto-obtiene del BCRA (dolarapi.com). Editable por el usuario.
Rentabilidad de proyectos: convierte gastos a la moneda del presupuesto usando tasa_cambio.

Conversion automatica al cobrar con [[Medios de Pago]]:
- USD -> ARS: monto x tipo de cambio
- ARS -> USD: monto / tipo de cambio

## Eliminacion suave

No hay `SoftDeletes` de Laravel. Se usa `activo = false` para clientes, usuarios y empleados.
BancoCaja y Gasto: eliminacion fisica (con validaciones).

---

## Ver tambien

- [[Base de Datos]] - Esquema de tablas referenciadas
- [[Backend - API]] - Endpoints que implementan estas reglas
- [[Backend - Modelos]] - Modelos con metodos de negocio
- [[Medios de Pago]] - Conversion de monedas al cobrar
- [[Modulo Personal]] - Reglas de empleados
- [[Errores Comunes]] - Bugs por no respetar estas reglas
