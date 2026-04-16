# Backend - Modelos Eloquent

Ubicacion: `mini-saas/backend/app/Models/`

## Enums disponibles

Ubicacion: `app/Enums/`

| Enum | Valores |
|------|---------|
| `RolUsuario` | ADMIN, USUARIO |
| `EstadoPresupuesto` | BORRADOR, ENVIADO, APROBADO, RECHAZADO, CANCELADO, FACTURADO |
| `Moneda` | ARS, USD |
| `TipoMovimiento` | CARGO, PAGO, AJUSTE_POSITIVO, AJUSTE_NEGATIVO |
| `TipoGasto` | OPERATIVO, RETIRO, PROYECTO |

> Los enums se castean en los modelos. Ver [[Errores Comunes#Controlador devuelve Eloquent collection directa]] y comparar siempre con el enum directo, no con string ni `->value`.

## Modelos

### Usuario
```php
fillable: nombre, email, password, rol, activo, permisos
casts:    rol -> RolUsuario, activo -> boolean, permisos -> array
metodos:
  esAdmin(): bool
  tienePermiso(string $permiso): bool
```

Ver [[Modulo Permisos]] para el sistema completo de permisos.

### Cliente
```php
fillable: nombre, email, telefono, empresa, cuit_dni, direccion, moneda_default,
          notas, activo, persona_contacto, mercury_customer_id
casts:    moneda_default -> Moneda, activo -> boolean
relaciones:
  hasMany(Presupuesto)
  hasMany(MovimientoCuenta)
  hasMany(ClienteTelefono) -> telefonos()  [desde 2026-04-15, orderBy id]
atributos computados:
  saldo: array con claves ARS y USD
```

Eager-load `telefonos` en `ClienteController::index` y `show`. `ClienteResource` siempre expone el array (id, nombre, codigo_area, numero, tipo).

### ClienteTelefono
```php
table:    cliente_telefonos
fillable: cliente_id, nombre, codigo_area, numero, tipo
$touches = ['cliente']  // toca updated_at del cliente
relaciones:
  belongsTo(Cliente)
```

`tipo` es string plano (no enum), valores aceptados: `WHATSAPP` (default), `LLAMADA`, `FIJO`. Validación con `Rule::in([...])` en `ClienteController::agregarTelefono`. Ver [[Modulo WhatsApp Inbox]].

### Presupuesto
```php
fillable: numero, cliente_id, fecha, estado, moneda, tasa_cambio, subtotal, descuento,
          descuento_tipo, iva_monto, total, vigencia_dias, observaciones,
          banco_caja_cobro_id, created_by
casts:    estado -> EstadoPresupuesto, moneda -> Moneda
relaciones:
  belongsTo(Cliente)
  belongsTo(Usuario, 'created_by') -> creador()
  hasMany(ItemPresupuesto) [ordenados por 'orden']
  hasMany(MovimientoCuenta)
  hasOne(Proyecto)
  belongsToMany(Etiqueta) via 'presupuesto_etiqueta'
metodos:
  recalcularTotales(): void
  puedeTransicionarA(EstadoPresupuesto): bool
```

Ver [[Reglas de Negocio#Presupuestos - Flujo de estados]] y [[Reglas de Negocio#Etiquetas de Presupuestos]].

### ItemPresupuesto
```php
table:    items_presupuesto
fillable: presupuesto_id, descripcion, cantidad, precio_unitario,
          iva_porcentaje, iva_monto, subtotal, orden
comportamiento:
  booted() -> en 'saving': auto-calcula subtotal y iva_monto
  $touches = ['presupuesto']  // toca updated_at del padre
```

### Proyecto
```php
fillable: presupuesto_id, cliente_id, nombre, estado, fecha_inicio, fecha_fin_est, notas, created_by
relaciones:
  belongsTo(Presupuesto)
  hasMany(Gasto)
  hasMany(PruebaEjecucion)
  hasMany(ProyectoAdjunto)
  hasMany(ProyectoJiraBoard)
  belongsToMany(Empleado) via 'proyecto_empleado'
    withPivot: rol_proyecto, fecha_inicio, fecha_fin
    SIN withTimestamps()   // Ver [[Errores Comunes]]
atributos computados:
  rentabilidad: { ingreso, gastos, resultado, margen%, moneda }
```

### Gasto
```php
fillable: tipo, descripcion, monto, moneda, fecha, categoria,
          proyecto_id, usuario_id, tasa_cambio, banco_caja_id
relaciones:
  belongsTo(Proyecto)
  belongsTo(Usuario)
  belongsTo(BancoCaja)
```

> `categoria` es un string plano, NO una relacion Eloquent. No usar `with('categoria')`.

### BancoCaja
```php
table:    bancos_cajas
fillable: tipo, nombre, descripcion, usuario_id, moneda, saldo_inicial, saldo_actual, activo
metodos:
  restarSaldo(float $monto): void
  sumarSaldo(float $monto): void
```

Ver [[Reglas de Negocio#Bancos y Cajas - Saldo automatico]].

### Configuracion
```php
table:    configuracion (singleton, siempre 1 fila)
fillable: ..., mercury_api_key, mercury_account_id, mercury_banco_caja_id,
          inbox_api_url, inbox_api_token
nota:     mp_access_token, stripe_secret_key, mercury_api_key, inbox_api_token
          NO se exponen en GET /config.
          Flags booleanos: mp_tiene_token, stripe_tiene_token,
          mercury_tiene_key, inbox_tiene_token
```

Contiene credenciales de [[Medios de Pago]] y del [[Modulo WhatsApp Inbox]].

### Empleado
Ver [[Modulo Personal]] para documentacion completa.

### ProyectoAdjunto
```php
table:    proyecto_adjuntos
fillable: proyecto_id, tipo, nombre, url, path, mime_type, size, public_token
relaciones:
  belongsTo(Proyecto)
metodos:
  asegurarPublicToken(): string
```

`asegurarPublicToken()` (desde 2026-04-15) genera `bin2hex(random_bytes(32))` (64 chars hex) y lo persiste si todavía no existe. Se usa para compartir el adjunto por WhatsApp via URL pública sin auth. Ver [[Modulo WhatsApp Inbox#Public token para acceso sin auth]].

### PruebaEjecucion (Activacion)
```php
table:    pruebas_ejecucion
fillable: proyecto_id, numero, periodo_desde, periodo_hasta, notas,
          descripcion_ia, descripcion_ia_cant_hitos
relaciones:
  belongsTo(Proyecto)
  hasMany(HitoEjecucion) [ordenados por 'orden']
```

### HitoEjecucion
```php
table:    hitos_ejecucion
fillable: prueba_ejecucion_id, orden, descripcion, categoria_servicio,
          actividad_especifica, qc, qe, qb, fecha, estado,
          jira_issue_key, jira_issue_summary
```

## HTTP Resources (API Resources)

Estos envuelven la respuesta en `{ "data": {...} }`. Ver [[Backend - API#wrapper data en respuestas]].

| Resource | Usado en |
|----------|---------|
| UsuarioResource | GET /auth/me, GET/POST/PUT /usuarios |
| ClienteResource | GET/POST/PUT /clientes/{id} |
| PresupuestoResource | GET/POST/PUT /presupuestos/{id} |
| GastoResource | GET/POST/PUT /gastos (incluye campo `editable`) |

**Sin Resource** (JSON directo): proyectos, bancos-cajas, dashboard, staff, empleados, cuenta-corriente, etiquetas

---

## Ver tambien

- [[Base de Datos]] - Esquema de tablas
- [[Backend - API]] - Endpoints que usan estos modelos
- [[Modulo Permisos]] - Enmascaramiento en Resources
- [[Errores Comunes]] - Bugs con modelos y relaciones
