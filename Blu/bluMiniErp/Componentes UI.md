# Componentes UI

Especificaciones de componentes reutilizables del dashboard. Todos los colores y espaciados vienen de [[Design Tokens]].

## KPI Card

Card que muestra una metrica clave con sparkline y badge de cambio.

```
+----------------------------------------------------+
|  TOTAL REVENUE                    ||||| (sparkline) |
|  $20,320                                           |
|  (i)                         +0,94 last year       |
+----------------------------------------------------+
```

- Label: `text-[11px] font-medium font-mono tracking-[0.1em] uppercase text-[#8B8B83]`
- Value: `text-[32px] font-semibold tracking-tight text-[#1A1A1A]`
- Sparkline: 5-7 barras de 3px, max 40px alto, color `#1A1A1A`
- Separador inferior: `border-[#F0F0EB]`

## Stat Badge

Indicador de cambio inline.

- Positivo: `text-[#2D8C5A]` (verde)
- Negativo: `text-[#C0392B]` (rojo)
- Neutral: `text-[#8B8B83]`

## Sales Trend Chart (Dot Matrix)

Grafico de barras con cuadrados discretos. Estilo retro-digital.

- Cada cuadrado: ~8x8px con 2px gap, `rounded-sm`
- Serie existente: `#1A1A1A` (negro)
- Serie nueva: `#8B8B83` (gris)
- Columnas invertidas (flex-col-reverse)

## Data Table

Para paginas de listado.

- Header: `text-[11px] font-medium font-mono tracking-[0.1em] uppercase text-[#8B8B83] bg-[#FAFAF5]`
- Body: `text-sm text-[#1A1A1A]`
- Row border: `border-b border-[#F0F0EB]`
- Row hover: `hover:bg-[#FAFAF5]`
- Wrapper: `bg-white rounded-xl border border-[#E8E8E3]`

## Search Input

```html
<div class="flex items-center gap-2 px-3 py-2 rounded-lg border border-[#E8E8E3] bg-white">
  <Icon name="lucide:search" class="w-4 h-4 text-[#9B9B93]" />
  <input class="text-[13px] placeholder-[#9B9B93] bg-transparent outline-none w-full" />
</div>
```

## Modal

Siempre usar con `v-model`, nunca con `v-if` + `@close`. Ver [[Errores Comunes#Componentes UI con prefijo de directorio]] y [[Frontend#Componentes UI]].

```vue
<Modal v-model="showModal">...</Modal>
```

## Period Toggle

Pill-style toggle group. Activo: `bg-white text-[#1A1A1A] font-medium shadow-sm`. Inactivo: `text-[#9B9B93]`.

## Info Button

```html
<button class="w-5 h-5 rounded-full border border-[#E8E8E3] text-[#9B9B93]">
  <Icon name="lucide:info" class="w-3 h-3" />
</button>
```

## Tooltip

- Background: white, border `#E8E8E3`, `shadow-lg`, `rounded-lg`, `p-3`

---

## Ver tambien

- [[Design Tokens]] - Colores y espaciado usados
- [[Layout System]] - Donde se posicionan estos componentes
- [[Page Templates]] - Como se componen en paginas
- [[Frontend#Componentes UI]] - Componentes del proyecto actual
