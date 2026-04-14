# Changelog

Registro de cambios por fecha. Append-only — no borrar entradas previas.

## 2026-04-14 — Homepage updates (rama `feature/homepage-updates-abril-2026`)

Reestructuración visual y arquitectural del homepage + dos páginas nuevas. 7 commits pusheados a `origin`.

### Home — reorder y limpieza

- **Featured Products movido arriba** — ahora aparece justo debajo del hero, antes de wellness goals. Da visibilidad inmediata al catálogo.
- **Ciencia & Bienestar (blog preview) eliminado del home** — el contenido queda solo en `/blog`. Componente `HomeBlogPreview.vue` borrado del repo.
- **Basado en evidencia (science ingredients) eliminado del home** — movido a la nueva página `/ciencia`.
- **QualityBadges + CertificationsSection unificados** — un único componente `home/QualityBadges.vue` que ahora recibe dos props: `badges` (feature cards con descripción) + `certifications` (row bajo el título "Estándares de fabricación premium"). El viejo `CertificationsSection.vue` se eliminó.

### Páginas nuevas

- **`pages/ciencia.vue`** — hero, re-usa `HomeScienceIngredients`, lista de quality promises y certifications. Fetch a `/cms/home` (no hay endpoint dedicado).
- **`pages/profesionales.vue`** — portal para profesionales de la salud (emulando giovegen.com/profesionales/). Hero + 4 beneficios + formulario de inscripción. **TODO:** form handler apunta a endpoint inexistente `/api/professionals`.

### Nav

- Agregado link **"Profesionales"** al header (`TheHeader.vue`). Nav ahora: `Inicio | Productos | Ciencia | Blog | Profesionales`.
- `reservedSlugs` en `pages/[slug].vue` actualizado con `ciencia` y `profesionales` para evitar que el catch-all los intercepte.

### Wellness Goals — 6 columnas + hover crossfade

- Grid cambiado de `lg:grid-cols-5` a `lg:grid-cols-6` (las 6 categorías en una sola fila desktop, 2 cols mobile, 3 cols tablet).
- **Hover crossfade estilo Horbäach** — cada card tiene dos capas absolutas que se crossfade con `group-hover:opacity-0/100 transition-opacity duration-500`:
  - Default: foto lifestyle (o SVG fallback por slug).
  - Hover: foto frasco/producto (o SVG genérico sobre gradiente por slug).
- Soporta `goal.lifestyle_image_url` y `goal.product_image_url` desde el CMS si existen (hoy no existen, los SVG se muestran como placeholders).
- **TODO:** subir fotos reales a `public/images/categories/` o agregar columnas a `wellness_goals`.

### Hero — más ancho, más impactante

- `HomeHeroSlider` ahora con `min-h-[85vh]` en desktop y `h-[clamp(480px,70vw,880px)]` en mobile.
- Tipografía del título ampliada: `text-4xl md:text-6xl lg:text-7xl xl:text-8xl`.
- Overlay con gradiente más fuerte (`from-black/60 via-black/30`).
- `HomeHeroBanner` (variante sin slider) también agrandado para mantener consistencia.

### Docs

- `naevo/docs/architecture.md` actualizado con nuevo orden del home, tabla de páginas con `/ciencia` y `/profesionales`, notas en componentes (QualityBadges dos props, WellnessGoals hover crossfade, gotcha de `reservedSlugs`).

### Commits

```
5aebd05 docs: actualizar architecture.md con home reorder y nuevas páginas
71bde08 hero: min-h-[85vh], tipografía más grande para más impacto
2a3c99c wellness-goals: grid 6 cols + hover crossfade lifestyle↔producto
e8216e9 nav: agregar Profesionales + página /profesionales
fb8d0ec home: sacar Science/BlogPreview del home; crear página /ciencia
11d2301 home: unificar QualityBadges + CertificationsSection en una sola sección
8719a62 home: mover Featured Products debajo del hero
```

### Archivos tocados

- `frontend/pages/index.vue` — reorder + remove
- `frontend/pages/ciencia.vue` — nuevo
- `frontend/pages/profesionales.vue` — nuevo
- `frontend/pages/[slug].vue` — reservedSlugs
- `frontend/components/TheHeader.vue` — nav link
- `frontend/components/home/QualityBadges.vue` — dos props
- `frontend/components/home/WellnessGoals.vue` — grid + crossfade
- `frontend/components/home/HeroSlider.vue` — tamaño
- `frontend/components/home/HeroBanner.vue` — tamaño
- `frontend/components/home/BlogPreview.vue` — **eliminado**
- `frontend/components/home/CertificationsSection.vue` — **eliminado**
- `docs/architecture.md` — doc update

## Ver también

- [[naevo|Índice]]
- [[arquitectura|Arquitectura]]
- [[contexto|Contexto y TODOs]]
