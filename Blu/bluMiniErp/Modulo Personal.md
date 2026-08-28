# Modulo Personal (Empleados)

Gestion completa de empleados: alta, asignacion a proyectos y pagos.

## Tablas involucradas

- `empleados` - datos del empleado. Columnas nuevas (2026-08): `direccion` (mig 0090); `fecha_nacimiento` + bancarios `banco`, `tipo_cuenta`, `cbu`, `alias_cbu`, `titular`, `cuil` (mig 0091)
- `proyecto_empleado` - pivot de asignaciones (sin timestamps)
- `pagos_personal` - historial de pagos. Cada pago genera un **gasto vinculado** que descuenta saldo de [[Base de Datos#bancos_cajas|bancos_cajas]] (migración 0057: `periodo_mes`, `periodo_anio`, `gasto_id`)
- `feriados` - feriados nacionales (mig 0092): `fecha` (unique), `nombre`, `tipo`. Ver sección [[#Área de empleado y vacaciones (Mi Área) (2026-08)]]

Ver columnas detalladas en [[Base de Datos#empleados]].

## Backend

### Rutas API
```
GET    /api/empleados                       <- listado (filtros: activo, q)
GET    /api/empleados/sueldos-pendientes     <- recordatorio: sueldos del mes vencido sin cobrar (⚠️ ANTES del apiResource)
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

**⚠️ Período ≠ fecha de pago ≠ mes en curso.** `periodo_mes`/`periodo_anio` definen en qué mes impacta el gasto; `fecha` es cuándo se pagó realmente. El **gasto** se fecha al **día 1 del mes del período** (`Carbon::create(anio, mes, 1)`), NO a `now()` ni a la fecha de pago (ej: período 5/2026 → gasto `2026-05-01` aunque se pague el 16/06).

**Interacción con el Dashboard.** "Gastos del Período" suma `gastos` por `fecha` y **por defecto muestra el mes actual**. Un sueldo imputado a otro mes no aparece mirando el mes en curso — hay que mover el filtro de período del Dashboard. No es bug: confusión real porque el selector "Período" del form defaultea al mes actual. Ver [[Errores Comunes#El gasto de un pago de sueldo aparece en el mes en curso (no es bug)]].

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
pages/staff/index.vue      <- listado
pages/staff/nuevo.vue      <- formulario de alta
pages/staff/[id].vue       <- ficha (3 tabs: Info / Proyectos / Pagos)
pages/staff/ausencias.vue  <- ausencias del equipo
pages/staff/simulador.vue  <- simulador de aumentos (ver abajo)
```

### Simulador de aumentos (2026-08-25, PR #41)
Pantalla **`/staff/simulador`** (botón "Simular aumentos" en el header de Personal). Planifica aumentos:
seleccionás uno o más empleados (checkbox / "todos") y aplicás aumentos **porcentuales (%)** o
**nominales ($)** — en masa a los seleccionados ("Aplicar a seleccionados") o ajustando cada uno en su fila.
Muestra por empleado el **sueldo nuevo** y el **extra/mes**, y al pie los **totales por moneda** (actual ·
nuevo · extra/mes; ARS y USD no se mezclan) + resumen de **extra por mes** y **por año** (× 12).
- **100% client-side** (what-if, sin persistencia → sin backend ni migración). Lee `GET /empleados`,
  usa `empleados.salario_base` + `moneda_salario`.
- Respeta `VER_MONTOS_SALDOS`: si los sueldos vienen enmascarados (`salario_base === null`), muestra un
  aviso en lugar de la tabla. Montos con `fmtM` (modo privacidad). Ver [[Modulo Permisos]].

### Tab Informacion
Formulario editable: nombre, cargo, email, telefono, **direccion**, tipo contrato, fecha ingreso, **fecha nacimiento**, salario base, moneda, notas + sección **Datos bancarios** (banco, tipo cuenta, CBU/CVU, alias, titular, CUIL). Ver [[#Área de empleado y vacaciones (Mi Área) (2026-08)]].

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

## Vínculo Empleado ↔ Usuario del sistema (2026-06-30)

- `empleados.usuario_id` (migración 0066): FK nullable **unique** a `usuarios` (1:1), `nullOnDelete`. Relaciones `Empleado::usuario()` / `Usuario::empleado()`.
- En el detalle del empleado (tab Información, card "Usuario del sistema") se puede **crear** un usuario (prefill nombre/email), **vincular** uno existente o **desvincular** (no borra la cuenta). Solo **admin**. Endpoints `POST/PUT/DELETE /api/empleados/{id}/usuario`.
- El usuario **creado desde Personal** nace acotado: rol `USUARIO`, `permisos: ['VER_SECCION_TAREAS']`, sin `VER_MONTOS_SALDOS`. Pensado para que el empleado solo gestione sus tareas. Ver [[Modulo Tareas]] y [[Modulo Permisos]].

---

## Área de empleado y vacaciones (Mi Área) (2026-08)

Vista **self-service** `/mi-area` para que cada colaborador vea sus propios datos. Aparece para cualquier usuario con **empleado vinculado** (`empleados.usuario_id`); un usuario que solo es empleado (no admin, sin `VER_SECCION_DASHBOARD`) **aterriza ahí al loguear**. NavItem "Mi Área" en el sidebar gateado por `usuario.tiene_empleado` (campo nuevo en `UsuarioResource`). **No** expone sueldos → no depende de `VER_MONTOS_SALDOS`.

- **Backend:** `MiAreaController@show` → `GET /api/mi-area` (JSON directo). Sin ficha → `{tiene_empleado:false}`. Devuelve: `empleado` (correo, teléfono, dirección, **fecha de cumpleaños**, inicio de actividades, tipo contrato), `rol` (área, reporta a, propósito, responsabilidades — desde [[Modulo People Performance|Rol & Expectativas]]), `banco` (banco, tipo cuenta, CBU/CVU, alias, titular, CUIL), `vacaciones` y `feriados` del año.
- **Frontend:** `pages/mi-area/index.vue` — cards Mis datos · Mi rol · Datos bancarios (CBU/alias con botón copiar) · Vacaciones · **Política de Vacaciones** (colapsable) · **Feriados {año}** (listado, pasados atenuados). Las cards de rol/banco se ocultan si están vacías.
- **Carga de datos:** los campos nuevos (dirección, cumpleaños, bancarios) los edita el **admin** en `/staff/[id]` tab Información (sección "Datos bancarios"); validación en `EmpleadoController::reglasDatosBancarios()`.

### Vacaciones — días hábiles + feriados

- **Asignados automáticos por antigüedad:** `Empleado::diasVacacionesAsignados()` = `<=5→14`, `<=10→21`, `<=20→28`, `>20→35`. `antiguedadAnios()` calcula años al 31/12.
- **⚠️ Se cuentan en DÍAS HÁBILES (política Blu, no ley):** `diasHabilesEntre()` excluye sábados, domingos y **feriados nacionales** (tabla `feriados`). Los 14/21/28/35 se interpretan como hábiles (beneficio adicional al régimen legal). `vacacionesTomadas()`/`vacacionesDetalle()` suman `ausencias` con `motivo='Vacaciones'` del año, recortadas al año.
- **Feriados:** modelo `Feriado` + `Feriado::fechasEntre($d,$h)`. Seeder `FeriadosSeeder` (idempotente, **2025+2026**, fuente argentina.gob.ar). Correr al empezar cada año con las fechas nuevas: `php artisan db:seed --class=FeriadosSeeder --force`. También se muestran en el [[Modulo Calendario]].

### Días extra de vacaciones (premio) (2026-08)

Días libres extra otorgados a un empleado (premios) que **suman a los días disponibles mientras no venzan**. Se pueden cargar varios, cada uno con su cantidad, motivo y vencimiento.

- **Tabla `vacaciones_extra`** (migración `0093`): `empleado_id`, `dias` (decimal, permite 0.5), `motivo` (observación), `fecha_otorgado`, `fecha_vencimiento`, `usuario_id`. Modelo `VacacionExtra`.
- `Empleado::diasExtraVigentes()` suma solo los **no vencidos** (`fecha_vencimiento >= hoy`); `vacacionesExtraDetalle(bool $soloVigentes)` lista con flag `vencido`. Un extra vencido queda en el historial pero deja de sumar.
- **Cálculo:** `dias_disponibles = asignados (antigüedad, hábiles) + extra vigentes`; `dias_restantes = max(0, disponibles − tomados)`.
- **Endpoints** (`EmpleadoController`): `GET/POST /api/empleados/{id}/vacaciones-extra` (POST body: `dias`, `motivo`, `fecha_vencimiento`, `fecha_otorgado?`) y `DELETE /api/empleados/{id}/vacaciones-extra/{extra}`. Devuelven `{ items, resumen }`.
- **Frontend:** se gestionan en `/staff/[id]` **tab Ausencias** (card "Días extra de vacaciones": form + lista con badge vigente/vencido + resumen del año). En **Mi Área**, la card de Vacaciones muestra "Disponibles" con desglose `base + extra` y lista los extra vigentes con su vencimiento.

### Recordatorio de sueldos pendientes del mes vencido (PR #52/#53, 2026-08-27)

Recordatorio en `/staff` de **qué empleados activos aún no cobraron el sueldo del mes vencido**. Como se paga **a mes vencido**, el período a cobrar es siempre el **mes anterior**: arrancado agosto, lista a quienes no tienen registrado el sueldo de julio, hasta que se paga.

- **`GET /empleados/sueldos-pendientes`** (`EmpleadoController::sueldosPendientes`, declarada **antes del apiResource** para que `sueldos-pendientes` no caiga como `{empleado}`). Período = `Carbon::now()->subMonthNoOverflow()`. Toma **activos** que ya estaban en la empresa dentro del período (`fecha_ingreso <= fin de mes` o sin fecha) y **sin `PagoPersonal` tipo `SUELDO`** para ese `periodo_mes`/`periodo_anio`. El monto respeta `VER_MONTOS_SALDOS`. Devuelve `{ periodo_mes, periodo_anio, periodo_label, total, pagados, pendientes[] }`.
- **Frontend (`staff/index.vue`):** card **ámbar** "Sueldos de {mes} pendientes de cobro · N de M" con un chip por persona; cuando no queda ninguno, card **verde** "Todos cobraron el sueldo de {mes}". No bloquea la página si el endpoint falla.
- **Deep-link al pago (PR #53):** el chip enlaza a **`/staff/{id}?tab=pagos&sueldo=1`**. `staff/[id].vue` en `cargar()` lee `?tab` (abre esa pestaña) y `?sueldo` (precarga `formPago`): tipo SUELDO, período = mes vencido, **monto = salario base**, moneda del salario, **fecha de pago = día 5 del mes en curso**, y banco/caja autoseleccionado si hay uno solo de esa moneda. Queda listo para **Registrar pago**. Reusa el `pagoVacio()` existente (ya defaultea tipo SUELDO + período mes vencido).
- La fecha de pago (día 5) queda como **`fecha_real`** del gasto generado; el gasto se sigue imputando al **día 1 del período** (ver [[Reglas de Negocio#Imputación contable vs fecha real (2026-08-27)]]).

---

## Ver tambien

- [[Modulo People Performance]] - RRHH sobre Personal: rol&expectativas, competencias, objetivos, ausencias, actividad GitHub/Jira (2026-07-14)
- [[Modulo Reservas Reuniones]] - Mi Área enlaza a "Mi Disponibilidad"; las ausencias del empleado bloquean los slots reservables
- [[Modulo Tareas]] - Tareas asignadas al usuario del empleado
- [[Base de Datos#empleados]] - Esquema de tablas
- [[Backend - API#Staff y Empleados]] - Endpoints
- [[Reglas de Negocio#Personal - Asignacion a Proyectos]] - Reglas de asignacion
- [[Errores Comunes]] - Bugs con relaciones pivot
