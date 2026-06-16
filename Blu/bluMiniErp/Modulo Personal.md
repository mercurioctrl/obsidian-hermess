# Modulo Personal (Empleados)

Gestion completa de empleados: alta, asignacion a proyectos y pagos.

## Tablas involucradas

- `empleados` - datos del empleado
- `proyecto_empleado` - pivot de asignaciones (sin timestamps)
- `pagos_personal` - historial de pagos. Cada pago genera un **gasto vinculado** que descuenta saldo de [[Base de Datos#bancos_cajas|bancos_cajas]] (migración 0057: `periodo_mes`, `periodo_anio`, `gasto_id`)

Ver columnas detalladas en [[Base de Datos#empleados]].

## Backend

### Rutas API
```
GET    /api/empleados                       <- listado (filtros: activo, q)
POST   /api/empleados                       <- crear
GET    /api/empleados/{id}                  <- detalle con proyectos y pagos
PUT    /api/empleados/{id}                  <- editar
DELETE /api/empleados/{id}                  <- desactiva (activo=false)
POST   /api/empleados/{id}/proyectos        <- asignar a proyecto
DELETE /api/empleados/{id}/proyectos/{proy} <- desasignar
GET    /api/empleados/{id}/pagos            <- historial de pagos
POST   /api/empleados/{id}/pagos            <- registrar pago -> crea gasto vinculado (categoría "Sueldos")
DELETE /api/empleados/{id}/pagos/{pago}     <- eliminar pago -> borra gasto vinculado (devuelve saldo)
POST   /api/proyectos/{id}/empleados        <- asignar desde el proyecto
DELETE /api/proyectos/{id}/empleados/{emp}  <- desasignar desde el proyecto
```

Sin wrapper `data:`. Ver [[Backend - API#wrapper data en respuestas]].

### Comportamiento de pagos, gasto vinculado y saldo (⚠️ desde migración 0057)
Un pago de personal **ES un gasto**. Al registrar (`POST /empleados/{id}/pagos`):
1. Valida que la `moneda` del pago coincida con la del banco/caja (422 si no).
2. Crea un `Gasto` (tipo `OPERATIVO`, categoría **"Sueldos"** via `firstOrCreate`, `realizado=true`, IVA 0, `tasa_cambio` de dolarapi.com), fechado al **primer día del período** (`Carbon::create(periodo_anio, periodo_mes, 1)`). **Ese gasto es la ÚNICA fuente del descuento de saldo** (`restarSaldo`).
3. Crea el `PagoPersonal` con `gasto_id`, `periodo_mes`, `periodo_anio`.

Así el sueldo aparece en [[Frontend#Gastos]] (`/gastos`) y en el [[Dashboard UI Skill|Dashboard]] ("Gastos del Período") del mes seleccionado. Descripción del gasto: `"{TipoLabel} {Mes} {Año} — {empleado}"` (+ descripción libre, truncada a 100).

Al eliminar: si el pago tiene `gasto_id`, se borra el gasto (que devuelve el saldo via `sumarSaldo`); pagos legacy (pre-0057) usan fallback de saldo directo.

**⚠️ Período ≠ fecha de pago.** `periodo_mes`/`periodo_anio` definen en qué mes impacta el gasto; `fecha` es cuándo se pagó realmente.

Ver [[Reglas de Negocio#Bancos y Cajas - Saldo automatico]].

### Relacion Eloquent - punto critico
```php
->withPivot(['rol_proyecto', 'fecha_inicio', 'fecha_fin']);
// NO ->withTimestamps() — la tabla no tiene timestamps
```

Ver [[Errores Comunes#withTimestamps en la relacion proyecto_empleado]].

## Frontend

### Paginas
```
pages/staff/index.vue    <- listado
pages/staff/nuevo.vue    <- formulario de alta
pages/staff/[id].vue     <- ficha (3 tabs: Info / Proyectos / Pagos)
```

### Tab Informacion
Formulario editable: nombre, cargo, email, telefono, tipo contrato, fecha ingreso, salario base, moneda, notas.

### Tab Proyectos
Lista proyectos asignados con rol. Formulario inline para asignar. Actualizacion local del estado sin recargar. Ver [[Errores Comunes#cargar completo causa error DOM]].

### Tab Pagos
Formulario: tipo (SUELDO/BONO/AGUINALDO/**ADELANTO/COMISION/OTRO**), **Período** (`<input type="month">` → mes/año), fecha de pago, monto, moneda, banco/caja, descripcion. El dropdown banco/caja se **filtra por la moneda** elegida. Boton "Usar salario base" pre-rellena monto+moneda. Nota visible: "Se registra como gasto del período en Sueldos". Historial muestra **período** + fecha de pago + banco; badges por tipo (6 colores); resumen de totales por tipo presente.

### En Proyecto (`pages/proyectos/[id].vue`)
Seccion "Personal asignado" con lista, asignar/desasignar inline.

## Tipo de contrato

| Enum | Badge |
|------|-------|
| TIEMPO_COMPLETO | verde "Full time" |
| MEDIO_TIEMPO | azul "Part time" |
| CONTRATO | naranja "Contrato" |
| DIRECTOR | violeta "Director" |
| FREELANCE | - |

## Tipos de pago (`pagos_personal.tipo`)

`SUELDO`, `BONO`, `AGUINALDO`, `ADELANTO`, `COMISION`, `OTRO` (los 3 últimos agregados en migración 0057 al enum). Todos generan gasto vinculado en categoría "Sueldos".

---

## Ver tambien

- [[Base de Datos#empleados]] - Esquema de tablas
- [[Backend - API#Staff y Empleados]] - Endpoints
- [[Reglas de Negocio#Personal - Asignacion a Proyectos]] - Reglas de asignacion
- [[Errores Comunes]] - Bugs con relaciones pivot
