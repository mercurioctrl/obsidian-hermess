# Design System

Estética **AORUS / GIGABYTE**: negro profundo, acento naranja, tipografía condensada/uppercase, cortes angulares. Soporta **tema claro y oscuro** vía tokens de color con CSS variables.

## Temas (tokens)

CSS variables en `assets/css/main.css`, expuestas como colores Tailwind en `tailwind.config.ts` (`darkMode: 'class'`).

| Token | Rol | Oscuro | Claro |
|-------|-----|--------|-------|
| `bg` | fondo página | `#050505` | `#f4f5f7` |
| `surface` | cards | `#0f0f11` | `#ffffff` |
| `surface-2` | inputs/hover | `#141416` | `#eef0f3` |
| `line` / `line-2` | bordes | grises oscuros | grises claros |
| `fg` / `fg-muted` / `fg-subtle` | texto | claros | oscuros |
| `aorus-orange` | acento (fijo) | `#f96f1e` | `#f96f1e` |

Uso: `bg-bg`, `bg-surface`, `text-fg`, `border-line`, con opacidad `bg-bg/85`, etc.

## Conmutador de tema

- `composables/useTheme.ts`: **`useState` compartido** + **`useCookie`** para persistir.
  > Gotcha: NO usar `useCookie` suelto por componente (cada llamada crea un ref independiente y no sincroniza). Por eso el estado vive en `useState`.
- `app.vue` aplica la clase (`dark`/`light`) al `<html>` con `useHead` reactivo → SSR-aware, sin flash.
- `ThemeToggle.vue` (sol/luna) en el header. Default: oscuro.

## Componentes utilitarios

`.container-x`, `.display`, `.clip-angular` (corte AORUS), `.btn`/`.btn-primary`/`.btn-ghost`, `.card`/`.card-hover` (glow naranja), `.chip`, `.field`, `.product-stage` + `.product-img`.

## Logo e iconos

- **Logo oficial GIGABYTE**: SVG vectorial (`public/logos/gigabyte.svg`, `fill=currentColor`) aplicado con **máscara CSS** en `AppLogo.vue` → blanco en oscuro, oscuro en claro, naranja al hover. + favicons.
- **Iconos de categoría**: `CategoryIcon.vue`, iconos de línea mapeados por nombre (motherboard, gpu, monitor, laptop, case, cpu, cooler, psu, ram, disk, mouse, combo, box).

## Imágenes de producto (fondos blancos)

Las fotos de los resellers vienen con fondo blanco o PNG transparente. Se muestran sobre `.product-stage` (panel claro) con `.product-img` (`mix-blend-mode: multiply`) → el recuadro blanco desaparece y el producto resalta. Se mantiene claro en ambos temas a propósito. Trade-off: productos muy claros pierden algo de detalle.

## Ver también

- [[gigabyte-aterrizaje/arquitectura|arquitectura]] · [[gigabyte-aterrizaje/stack|stack]] · [[gigabyte-aterrizaje/gigabyte-aterrizaje|gigabyte-aterrizaje]]
