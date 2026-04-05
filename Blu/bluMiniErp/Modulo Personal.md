# Modulo Personal (Empleados)

Gestion completa de empleados: alta, asignacion a proyectos y pagos.

## Tablas involucradas

- `empleados` - datos del empleado
- `proyecto_empleado` - pivot de asignaciones (sin timestamps)
- `pagos_personal` - historial de pagos (descuenta saldo de [[Base de Datos#bancos_cajas|bancos_cajas]])

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
POST   /api/empleados/{id}/pagos            <- registrar pago -> descuenta BancoCaja
DELETE /api/empleados/{id}/pagos/{pago}     <- eliminar pago -> devuelve saldo
POST   /api/proyectos/{id}/empleados        <- asignar desde el proyecto
DELETE /api/proyectos/{id}/empleados/{emp}  <- desasignar desde el proyecto
```

Sin wrapper `data:`. Ver [[Backend - API#wrapper data en respuestas]].

### Comportamiento de pagos y saldo
- Al registrar pago: `BancoCaja::restarSaldo(monto)`
- Al eliminar pago: `BancoCaja::sumarSaldo(monto)`

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
Formulario: tipo (SUELDO/BONO/AGUINALDO), monto, moneda, fecha, banco/caja, descripcion. Boton "Usar salario base" pre-rellena el monto.

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

---

## Ver tambien

- [[Base de Datos#empleados]] - Esquema de tablas
- [[Backend - API#Staff y Empleados]] - Endpoints
- [[Reglas de Negocio#Personal - Asignacion a Proyectos]] - Reglas de asignacion
- [[Errores Comunes]] - Bugs con relaciones pivot
