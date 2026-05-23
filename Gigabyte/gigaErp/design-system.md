# Design System — gigaErp

Paleta, tipografía, layout y patrones visuales del ERP. Light mode minimalista.

## Paleta (hex exactos, no aproximar)

| Token | Hex | Uso |
|-------|-----|-----|
| Fondo main | `#F5F5F0` | `bg-[#F5F5F0]` — `<main>` |
| Fondo sidebar | `#F7F7F2` | `bg-[#F7F7F2]` |
| Cards/modales | `#FFFFFF` | `bg-white` |
| Hover rows/nav | `#FAFAF5` | `bg-[#FAFAF5]` |
| Nav activo | `#1A1A1A` | `bg-[#1A1A1A]` |
| Borde principal | `#E8E8E3` | `border-[#E8E8E3]` |
| Borde interno | `#F0F0EB` | separadores en cards |
| Texto primario | `#1A1A1A` | títulos, valores |
| Texto secundario | `#6B6B63` | cuerpo, descripciones |
| Texto terciario | `#9B9B93` | placeholders, labels secundarios |
| Texto nav inactivo | `#4A4A43` | nav items |
| Accent verde | `#2D8C5A` | positivo, focus, FACTURADA |
| Accent rojo | `#C0392B` | error, destructivo, ANULADA |

## Tipografía

- **Sans** — Inter (cuerpo, UI)
- **Mono** — JetBrains Mono (números, badges, TH de tabla)

| Uso | Clases |
|-----|--------|
| KPI label / TH tabla | `text-[11px] font-medium font-mono tracking-[0.1em] uppercase text-[#8B8B83]` |
| KPI valor | `text-[32px] font-semibold tracking-tight text-[#1A1A1A] tabular-nums` |
| Page title | `text-xl font-semibold text-[#1A1A1A]` |
| Input/TD | `text-sm text-[#1A1A1A]` |

## Radios y sombras

- Cards y modales: `rounded-xl` — sombras: plano (cards) / `shadow-xl` (modales) / `shadow-lg` (dropdowns)
- Inputs y botones: `rounded-lg`
- Badges: `rounded`
- Sidebar: `w-[280px]` | Topbar: `h-14` | Padding main: `p-8`

## Layout del shell

```
+--[280px sidebar]--+--[flex-1]----------------------------------+
|  Logo / org       | [h-14 topbar: breadcrumb | search]         |
|  Nav sections     +--------------------------------------------+
|  User footer      | [main: bg-[#F5F5F0] p-8] → <slot />        |
+-------------------+--------------------------------------------+
```

## Grids de página comunes

- KPI cards: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`
- Detalle 2/3 + aside 1/3: `grid grid-cols-1 lg:grid-cols-3 gap-6` + `lg:col-span-2`
- Formulario: `grid grid-cols-1 md:grid-cols-2 gap-4`

## Botones (markup completo)

### Primario
```html
<button class="px-4 py-2 text-sm font-medium bg-[#1A1A1A] text-white rounded-lg hover:bg-[#2D2D2D] transition-colors">
  Guardar
</button>
```

### Secundario (ghost)
```html
<button class="px-4 py-2 text-sm text-[#6B6B63] hover:text-[#1A1A1A] transition-colors">
  Cancelar
</button>
```

### Accent verde (acción positiva fuerte)
```html
<button class="px-4 py-2 text-sm font-medium bg-[#2D8C5A] text-white rounded-lg hover:bg-[#256b47] transition-colors">
  Aprobar
</button>
```

### Destructivo
```html
<button class="px-4 py-2 text-sm font-medium text-[#C0392B] hover:bg-red-50 rounded-lg transition-colors">
  Eliminar
</button>
```

### Con loading state
```html
<button :disabled="guardando" class="... disabled:opacity-50">
  <Icon v-if="guardando" name="lucide:loader" class="w-4 h-4 animate-spin" />
  <span v-else>Guardar</span>
</button>
```

## Card genérica

```html
<div class="bg-white rounded-xl border border-[#E8E8E3] p-6">
  <h3 class="text-sm font-medium text-[#1A1A1A] mb-4">Título</h3>
  ...
</div>
```

## Íconos

**SIEMPRE con prefijo `lucide:`** o se renderiza como texto plano.

```vue
<Icon name="lucide:search" class="w-4 h-4" />  ✅
<Icon name="search" />                          ❌
```

Tamaños comunes: `w-3.5 h-3.5` (chips), `w-4 h-4` (botones), `w-5 h-5` (banners),
`w-10 h-10` (empty states).

## Ver también

- [[componentes-ui]] — Modal, DataTable, FormField, StatusBadge con markup exacto
- [[arquitectura#Frontend]] — composables y stores
