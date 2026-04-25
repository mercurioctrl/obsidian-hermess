# Templates & Preview Switcher

Sistema dual para presentar al cliente variantes visuales del home de NAEVO sin tocar el home real.

- **Rama:** `feature/preview-switcher-tools`
- **Propósito:** galería comparativa para stakeholders con 28 variantes de estilo, todas consumiendo el mismo CMS.
- **URL:** `http://localhost:8088/preview/`

## Dos tipos de variante

El switcher en `frontend/public/preview/index.html` soporta dos modos, seleccionados dinámicamente en `load()` según prefijo del slug:

| Tipo | Dónde vive | Cómo se carga | Cuándo usar |
|------|-----------|---------------|-------------|
| **Mirror estático** (18) | `public/preview/<slug>/` | iframe apunta a `/preview/<slug>/` | Variantes que viven en una rama git propia y querés congelar el SSR de ese momento |
| **Nuxt live** (10) | `pages/templates/<slug>.vue` | iframe apunta a `/templates/<slug>` | Templates stateless que consumen CMS directo; cambian en vivo con la DB |

El patch en `load()`:

```js
const src = slug.startsWith('tpl-')
  ? '/templates/' + slug.replace(/^tpl-/, '') + '?v=' + Date.now()
  : '/preview/' + slug + '/?v=' + Date.now();
```

## Naming al cliente · blu-NN Fantasía

Todas las variantes aparecen como `blu-NN · Nombre` (ej. `blu-19 · Mantra`) — **nunca** mencionar el DS/marca que inspira el estilo. Convención presentation-only: los `value=""` de los `<option>` y slugs técnicos **no se renombran** (romperían rutas).

| # | Slug técnico | Label al cliente |
|---|--------------|------------------|
| 01-06 | original-abril, horbaach-base, contraste, header-dark, header-azul, 9-secciones-azul | Origen, Aurora, Prisma, Umbra, Cobalto, Azzurra |
| 07-11 | premium-senior, premium-sans, cientifico-lujo, apple-vision, apple-classic | Atelier, Limen, Cristal, Noctis, Solaria |
| 12-16 | huel-style, levels-style, eight-sleep, eight-sleep-azul, eight-sleep-light | Vértice, Savia, Eclipse, Nimbo, Nácar |
| 17-18 | editorial-lujo, naevo-brandbook | Claro, Insignia |
| 19-28 (tpl-*) | material3, apple-hig, polaris, carbon, fluent, antd, atlassian, chakra, shadcn, tailwind-ui | Mantra, Ítaca, Ágora, Lúmina, Fluido, Cúspide, Meridiano, Cálamo, Raíz, Orbe |

Próxima variante → **blu-29**.

## 10 templates Nuxt live (blu-19 → blu-28)

Cada uno es una página standalone bajo `pages/templates/<slug>.vue` con:
- `definePageMeta({ layout: false })`
- CSS scoped con prefijo único (m3-, ap-, po-, cb-, fl-, ad-, at-, ch-, sh-, tw-)
- Google Fonts cargadas en `useHead()`
- `<TemplateSwitcher />` flotante al final

### Data compartida

```ts
// composables/useTemplateData.ts
const { banner, heroImage, goals, badges, certs, products, footerLinks, formatPrice }
  = await useTemplateData()
```

Todos los templates consumen `/api/cms/home` — cambiás el CMS y los 10 se actualizan.

### Logo — filtro monocromático según contraste

Todos usan `<img src="/logo.svg">` en el header. Filtro CSS:

| Filtro | Templates |
|--------|-----------|
| Full color | material3, polaris, fluent, antd, atlassian, chakra, tailwind-ui |
| Mono negro (`brightness(0)`) | apple-hig, shadcn |
| Mono blanco (`brightness(0) invert(1)`) | carbon (header + footer), shadcn (footer) |

## TemplateSwitcher FAB

Componente global en `frontend/components/TemplateSwitcher.vue`. Botón flotante bottom-right **neutro** (siempre `#111` / blanco, no hereda accent del template). Panel muestra lista de los 10 con nombre `blu-NN Fantasía` + vendor `Blu Studio`.

## Panel de Ajustes · size-only

El `<details id="tools">` del switcher del `/preview/` tiene sólo **2 controles visibles**: tamaño de fuente y alto de logo. Los 5 color pickers (accent, accent2, bg, surface, text) están con `hidden` — se mantienen en el DOM para no romper JS (`currentTools`, `detectFromIframe`), pero sus valores se ignoran.

`applyToIframe(tools)` sólo inyecta:
```css
html{font-size:${fontPx}px!important}
header img[alt*="naevo" i]{height:${logoHeight}px!important;width:auto!important}
```

**Decisión del cliente:** cada variante debe mostrarse con sus colores originales. Si hace falta reactivarlos, revertir el commit `a4be121`.

## Cómo agregar una variante Nuxt nueva

1. Copiar un `pages/templates/<existente>.vue` como base, renombrar prefijo de clases.
2. Incluir `<TemplateSwitcher />` antes de cerrar `</div>`.
3. Sumar entrada a `TEMPLATES` en `composables/useTemplateData.ts` con nombre `blu-NN Fantasía`.
4. Sumar `<option value="tpl-<slug>">blu-NN · Nombre</option>` en `public/preview/index.html`.
5. Sumar preset en el objeto `PRESETS` del mismo archivo.
6. Rebuild del frontend: `docker compose build --no-cache frontend && docker compose up -d frontend`.

El SSR de Nuxt y la cache de h3 sobre `public/` requieren **rebuild obligatorio** — no alcanza con `docker cp`.

## Ver también

- [[naevo|Índice]]
- [[arquitectura|Arquitectura]]
- [[memoria|Memoria]]
- [[changelog|Changelog]]
