# Modulo de Permisos de Usuario

Sistema de control de acceso granular por usuario. Migracion `0035`.

## Concepto general

- Los **ADMIN** siempre tienen todos los permisos implicitamente
- Los **USUARIO** (no admin) tienen por defecto ningun permiso especial
- Los permisos se asignan individualmente desde la pantalla de Usuarios (solo admins)
- El enmascaramiento se aplica **en el backend** — valores sensibles nunca llegan al [[Frontend]]

## Permisos disponibles

### Funcionalidades

| Clave | Descripcion |
|-------|-------------|
| `VER_MONTOS_SALDOS` | Puede ver valores monetarios. Sin permiso, todos los montos se muestran como `***` |

### Secciones visibles (frontend)

Controlan que items del sidebar se muestran y si se puede navegar a esa ruta. El bloqueo es puramente de navegacion. Ver [[Frontend#Middleware]].

| Clave | Seccion |
|-------|---------|
| `VER_SECCION_DASHBOARD` | Dashboard (`/`) |
| `VER_SECCION_PERSONAL` | Personal (`/staff`) |
| `VER_SECCION_CLIENTES` | Clientes |
| `VER_SECCION_PRESUPUESTOS` | Presupuestos |
| `VER_SECCION_CUENTA_CORRIENTE` | Cuenta Corriente |
| `VER_SECCION_GASTOS` | Gastos |
| `VER_SECCION_BANCOS_CAJAS` | Bancos y Cajas |
| `VER_SECCION_MERCURY` | Mercury |
| `VER_SECCION_MERCADOPAGO` | MercadoPago |
| `VER_SECCION_PROYECTOS` | Proyectos |
| `VER_SECCION_ACTIVACIONES` | Activaciones |

## Backend

### Modelo Usuario
```php
protected $fillable = [..., 'permisos'];
protected $casts = ['permisos' => 'array'];

public function tienePermiso(string $permiso): bool
{
    if ($this->esAdmin()) return true;
    return in_array($permiso, $this->permisos ?? []);
}
```

Ver [[Backend - Modelos#Usuario]].

### Donde se enmascara VER_MONTOS_SALDOS

Patron:
```php
$verMontos = auth()->user()?->tienePermiso('VER_MONTOS_SALDOS') ?? false;
// campo => $verMontos ? $valor_real : null
```

**API Resources:**
- PresupuestoResource: tasa_cambio, subtotal, descuento, iva_monto, total
- ItemPresupuestoResource: precio_unitario, iva_monto, subtotales
- GastoResource: monto, tasa_cambio
- MovimientoCuentaResource: monto, tasa_cambio
- ClienteResource: saldo, presupuestos[].total

**Controllers (inline):**
- BancoCajaController: saldo_inicial, saldo_actual, movimientos
- EmpleadoController: salario_base, pagos[].monto
- ProyectoController: rentabilidad, gastos[].monto
- DashboardService: ingresos, gastos, resultado

## Frontend

### Store auth.ts
```ts
const verMontos = computed(() =>
  usuario.value?.rol === 'ADMIN' ||
  (usuario.value?.permisos ?? []).includes('VER_MONTOS_SALDOS')
)
```

### Renderizado
```vue
<span v-if="item.total === null">***</span>
<span v-else>{{ formatCurrency(item.total) }}</span>
```

Verificacion siempre `=== null` (estricta), nunca falsy.

### Pagina usuarios/index.vue
- Columna Permisos con badges (verde=activo, gris=inactivo)
- ADMIN muestra "Todos los permisos"
- Boton escudo (solo para no-admins): abre modal con checkboxes
- Guardar: `PUT /api/usuarios/{id}` con `{ permisos: [...] }`

## Bug critico topDeudores

`null != 0` es `true` en PHP. Filtrar con valores reales primero, enmascarar despues. Ver [[Errores Comunes#Filtrar por campo que luego se enmascara con null]].

## Agregar un nuevo permiso

1. Definir la clave (ej: `'PUEDE_EXPORTAR'`)
2. Agregar chequeo en controllers/resources
3. Agregar al array `PERMISOS_DISPONIBLES` en `frontend/pages/usuarios/index.vue`
4. No hace falta migracion — `permisos` es JSON libre

---

## Ver tambien

- [[Backend - Modelos#Usuario]] - Modelo con metodo tienePermiso
- [[Frontend#Middleware]] - Permisos de seccion en navegacion
- [[Backend - API]] - Endpoints que aplican enmascaramiento
- [[Errores Comunes]] - Bugs de enmascaramiento
