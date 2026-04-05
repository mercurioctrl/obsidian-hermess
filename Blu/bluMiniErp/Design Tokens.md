# Design Tokens

Especificacion visual completa para el sistema de UI del dashboard.

## Paleta de colores

### Neutrals (95% de la UI)
| Token | Hex | Uso |
|-------|-----|-----|
| bg-main | `#F5F5F0` | Fondo de pagina |
| bg-sidebar | `#F7F7F2` | Fondo sidebar |
| bg-card | `#FFFFFF` | Cards |
| bg-card-hover | `#FAFAF5` | Card hover |
| bg-nav-active | `#1A1A1A` | Nav item activo |
| border-default | `#E8E8E3` | Bordes, dividers |
| border-light | `#F0F0EB` | Separadores sutiles |

### Texto
| Token | Hex | Uso |
|-------|-----|-----|
| text-primary | `#1A1A1A` | Headlines, numeros grandes |
| text-secondary | `#6B6B63` | Body text |
| text-tertiary | `#9B9B93` | Placeholder, disabled |
| text-label | `#8B8B83` | Labels de KPI (uppercase) |
| text-nav | `#4A4A43` | Nav items inactivos |

### Accent
| Token | Hex | Uso |
|-------|-----|-----|
| accent-positive | `#2D8C5A` | Badges positivos |
| accent-negative | `#C0392B` | Badges negativos |

## Tipografia

### Font Families
```
--font-primary: 'Inter', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

### Type Scale
| Elemento | Size | Weight | Font | Extra |
|----------|------|--------|------|-------|
| KPI label | 11px | 500 | mono | tracking-[0.1em] uppercase |
| KPI value | 32px | 600 | sans | tracking-tight |
| Chart title | 11px | 500 | mono | tracking-[0.1em] uppercase |
| Sidebar section | 11px | 500 | sans | tracking-[0.05em] uppercase |
| Sidebar nav item | 14px | 400 | sans | - |
| Breadcrumb | 13px | 400 | sans | - |

## Espaciado

Multiplos de 4px. Ritmo: 8-16-24-32.

| Contexto | Valor | Tailwind |
|----------|-------|----------|
| Card padding | 24px | `p-6` |
| Gap entre cards | 24px | `gap-6` |
| Sidebar padding x | 20px | `px-5` |
| Main content padding | 32px | `p-8` |
| Breadcrumb bar height | 56px | `h-14` |

## Bordes y Radius

| Elemento | Radius | Tailwind |
|----------|--------|----------|
| Cards | 12px | `rounded-xl` |
| Nav items | 8px | `rounded-lg` |
| Inputs | 8px | `rounded-lg` |
| Chart dots | 2px | `rounded-sm` |

## Sombras

Diseno flat, casi sin sombras.

| Elemento | Tailwind |
|----------|----------|
| Cards | `shadow-none` o `shadow-sm` |
| Dropdowns | `shadow-md` |
| Tooltips | `shadow-lg` |

## Iconografia

Lucide icons via `nuxt-icon`. Siempre con prefijo `lucide:`. Ver [[Frontend#Iconos]] y [[Errores Comunes#Iconos sin prefijo lucide]].

---

## Ver tambien

- [[Componentes UI]] - Componentes que usan estos tokens
- [[Layout System]] - Layout que aplica estos tokens
- [[Page Templates]] - Paginas compuestas con estos tokens
- [[Dashboard UI Skill]] - Skill que aplica este sistema
