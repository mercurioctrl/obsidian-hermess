# Módulo Remitos

Desde un **presupuesto** se puede **generar un remito** que nace del detalle de ítems del presupuesto,
pero es **independiente y editable**: editarlo **NO modifica el presupuesto original**. Se pueden generar
**varios remitos por presupuesto** (ej. entregas parciales).

Remito **tradicional argentino**: sólo **descripción + cantidad**, sin precios ni total. No es comprobante
fiscal — es constancia de entrega de bienes/servicios. PDF con formato BLU (mismo Browsershot/Chromium
que el presupuesto).

Implementado 2026-08-23 (migración 0102). Ver también [[Backend - API]], [[Base de Datos]] y [[Modulo Contabilidad]].

## Modelo de datos (migración 0102)

**`remitos`**: `presupuesto_id` (FK cascadeOnDelete), `numero` (unique, `REM-{AAAAMM}-NNN`),
`fecha` (date, editable), `observaciones` (text nullable), `created_by` (FK usuarios nullOnDelete), timestamps.

**`remito_items`** (sin timestamps): `remito_id` (FK cascadeOnDelete), `descripcion` (string 500),
`cantidad` (decimal 12,2), `orden`. ⚠️ **Sin precios por decisión de producto.**

## Backend

- **Modelos:** `Remito` (relaciones `presupuesto`, `items`, `creador`; **sin `$touches`** — no toca
  `presupuesto.updated_at`), `RemitoItem` (`$timestamps=false`). `Presupuesto::remitos()` hasMany latest.
- **`RemitoController`**
  - `index(Presupuesto)` — remitos del presupuesto (`withCount('items')`, latest), Resource collection.
  - `store(Presupuesto)` — **copia los ítems del presupuesto** al remito nuevo (transacción). 201.
  - `show` / `update` / `destroy`.
  - `update` — sincroniza ítems con **delete + recreate** (reasigna `orden` por índice), actualiza
    `fecha`/`observaciones`. **No toca el presupuesto.**
  - `pdf` — auth por sesión **o** `?token=` (como el PDF de presupuesto). **No** requiere
    `VER_MONTOS_SALDOS` (el remito no lleva montos).
- **`PdfService::renderRemitoPdf(Remito)`** — renderiza `pdf.remito` con Browsershot A4.
- **Blade `pdf/remito.blade.php`** — mismo estilo BLU que `presupuesto-preview`. ⚠️ Logo via
  `@include('pdf._logo')` (renderiza el `<img>`); **NO** `pdf.partials.logo` (define `$bluLogoBase64`
  en scope local del include → "Undefined variable" en el padre). Ver [[Errores Comunes]].

### Rutas
```
GET    /api/remitos/{remito}/pdf?token=          (fuera de auth, sin montos)
GET    /api/presupuestos/{presupuesto}/remitos   (index)
POST   /api/presupuestos/{presupuesto}/remitos   (store — copia ítems)
GET    /api/remitos/{remito}                       (show)
PUT    /api/remitos/{remito}                       (update — sync ítems, no toca presupuesto)
DELETE /api/remitos/{remito}                       (destroy)
```

## Frontend

- **`pages/remitos/[id].vue`** — ver/editar: `fecha`, ítems (agregar/quitar/subir/bajar, descripción +
  cantidad), observaciones. Botones **PDF** (`?token=authStore.token`), **Eliminar**, **Guardar**.
  Aviso ámbar "editar no modifica el presupuesto". Valida ≥1 ítem con descripción.
- **`pages/presupuestos/[id].vue`** — grupo **"Remito"** en el menú **"Más"**: "Generar remito"
  (POST → navega a `/remitos/{id}`) + lista de remitos existentes.

## Limitaciones / futuro
- No hay listado global ni sección en el sidebar (entrypoint = el presupuesto).
- No se envía por email/WhatsApp (sólo descarga PDF).
- Sin precios ni numeración por punto de venta AFIP (el `REM-...` es interno).

## Ver también
- [[Modulo Contabilidad]] — otro documento derivado del presupuesto (fiscal, con montos)
- [[Errores Comunes]] — gotcha del logo en blades PDF
- [[Frontend]] · [[Backend - API]] · [[Base de Datos]]
- [[changelog#2026-08-23]]
