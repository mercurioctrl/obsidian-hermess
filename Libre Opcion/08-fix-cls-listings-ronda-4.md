# Ronda 4 — Fix CLS listings (/placas-de-video) + Inter font preload

## Fecha
2026-04-08

## Contexto

Después del deploy de la ronda 3 (commit `02ebadd1e`), midiendo el campo CrUX (28 días, usuarios reales) descubrimos que el problema NO era la home — la home está perfecta. El culpable del CrUX origin (0.34) son las **listings de categoría** (`/placas-de-video` y similares).

| URL | Desktop CLS | Mobile CLS | Estado |
|---|---|---|---|
| `/` (home) | 0.00 | 0.06 | ✅ |
| `/placas-de-video` | **0.45** | **0.37** | ❌ deficiente |
| Origin completo | **0.34** | **0.35** | ❌ |

Los productos individuales no tienen muestra suficiente para CrUX (caen a "origen"), pero las listings sí tienen MUCHA muestra y dominan el promedio. Si arreglamos las listings, baja el origin completo automáticamente.

Otras métricas listings:
- Desktop LCP: 2.8s (orange)
- Mobile LCP: 3.6s (orange)
- Mobile INP: 203ms (orange)

## Diagnóstico

### 1. Causa raíz principal: ModuloCCargando vs ModuloC altura mismatch

**El bug:** `/placas-de-video` usa `pages/busquedas/general.vue` (mapeado desde `nuxt.config.js:333` → `path: "/:busqueda"`). El layout del listing es:

```
.cont-1170
├── .left          → <Filtros> (sidebar)
└── .right
    ├── .menu-orden-vista
    └── .listado
        └── (vista=gallery) <Masonry> con 12 ModuloCCargando o ModuloC
        └── (vista=list) 6 ModuloBCargando o ModuloB
```

El skeleton renderiza durante `loading: true`. Después del fetch, **se reemplaza por las cards reales dentro de `<ClientOnly>`** (línea 103) — eso significa que SSR no renderiza las cards, solo la hidratación lo hace.

`ModuloCCargando.vue:30` tenía `height: 289px`. Pero `ModuloC.vue` (la card real) suma:
- `.imagen .producto`: `height: 180px` desktop
- `.detalle .description`: ~48px (h2 ellipsize 80 chars × line-height 16px)
- `.prices` block: ~60px
- `.cuotas`: ~25px
- `.seller`: ~20px
- `.botones-de-compra`: ~40px
- paddings + márgenes: ~7px

**Total: ~380px desktop / ~290px mobile**

Resultado: cada fila del masonry crecía ~90px al hidratar. Con 12 cards en 3 columnas = 4 filas × 90px = **360-540px de shift acumulado**, multiplicado por viewport = CLS gigante.

### 2. Sidebar de filtros sin altura reservada

`pages/busquedas/general.vue:731` tenía:

```scss
.left {
  max-width: 250px;
  border-radius: 5px;
}
```

Pero `Filtros/Index.vue` depende de `windowWidth > 768` y `windowWidth > 1024` (set en `mounted()`), así que durante SSR **renderiza un `<div>` vacío**. El `.left` arrancaba con altura 0 y crecía cuando hidrataba + llegaban los attributes async (brands, prices, categories).

Sin embargo `.left` está en un flex `cont-1170` con `justify-content: space-between`, así que en mobile (cuando el flex pasa a column) el `.left` empuja el `.right` (grid) hacia abajo cuando crece.

### 3. Banner "Recibílo en" cambiando width

`Cabecera/partials/Envios.vue:142` tiene un computed `domicilio` que depende de `isCreated` (set en `created()` solo en client). Resultado:
- SSR: `isCreated = false` → texto " Todo el país" (~12 chars)
- Client: `isCreated = true` → texto "Capital Federal CP (1234)" (~22 chars, posible wrap a 2 líneas)

El span tiene `display: block` y la caja contenedora `.cabecera-envios` tiene `max-width: 250px`. El cambio de texto ensanchaba/wrapeaba la caja → CLS en el HEADER de TODA la app, no solo en el home/listing.

### 4. FOUT de Inter (mitigación tardía)

`nuxt.config.js:704-712` cargaba Inter via `@nuxtjs/google-fonts` con `display: "swap"` y `download: false`, sin preload. Cuando Inter reemplaza la fuente del sistema fallback, hay reflow potencial. Era el P2 documentado en la ronda 3 — ahora se aplica.

## Soluciones aplicadas (commit `274bce6ee`)

### Fix 1: Sincronizar altura skeleton/card

**`ModuloCCargando.vue:30-34`:**
```scss
.productos-modulo-cargando-c {
  height: 380px;  // antes 289px
  @media (max-width: 550px) {
    height: 290px;
  }
}
```

**`ModuloC.vue:391-396`:**
```scss
.productos-modulo-c {
  min-height: 380px;
  @media (max-width: 550px) {
    min-height: 290px;
  }
}
```

Ambos sincronizados. Cualquier diferencia se multiplica por filas en el masonry, así que **deben** matchear.

### Fix 2: Reservar sidebar de filtros

**`pages/busquedas/general.vue:731-742`:**
```scss
.left {
  max-width: 250px;
  min-height: 600px;  // ← nuevo

  @media (max-width: 1024px) {
    max-width: 100%;
    min-height: 0;  // mobile usa modal de filtros, sidebar colapsado
  }
}
```

### Fix 3: Reservar espacio "Recibílo en"

**`Cabecera/partials/Envios.vue:345-352`:**
```scss
.recibilo-domicilio {
  display: block;
  min-height: 28px;  // ← nuevo
  min-width: 160px;  // ← nuevo (calza el texto largo "Capital Federal CP (1234)")
  ...
}
```

### Fix 4: Inter local + display:optional + subsets

**`nuxt.config.js:703-725`:**
```js
[
  "@nuxtjs/google-fonts",
  {
    families: { Inter: [400, 500, 700] },
    subsets: ["latin", "latin-ext"],  // sin esto baja TODOS los subsets (~600KB)
    display: "optional",              // antes "swap"
    download: true,                   // antes false
    inject: true,
    preload: true,
  },
],
```

**`app/.gitignore`:**
```
# @nuxtjs/google-fonts (download:true) — los regenera npm run build
assets/fonts/
assets/css/fonts.css
```

`display: optional` garantiza CLS=0 por FOUT — el browser usa Inter solo si está disponible en ~100ms o mantiene la fuente del sistema toda la sesión. Trade-off: en mobile slow algunos usuarios ven Source Sans Pro/system. Como Cloudflare cachea los `.woff2`, los usuarios recurrentes ya tienen Inter cargada.

## Métricas esperadas

| Métrica | Antes | Esperado |
|---|---|---|
| CLS desktop `/placas-de-video` (lab) | 0.45 | <0.1 |
| CLS mobile `/placas-de-video` (lab) | 0.37 | <0.1 |
| CrUX origin completo | 0.34 | bajo (al ceder las listings) |
| Inter peso | ~600KB | ~150KB (subsets latin) |
| FOUT Inter | activo | mitigado |

⚠️ El CrUX field tarda **2-4 semanas** en reflejar los cambios. El lab debería bajar ya en el próximo deploy.

## ⚠️ Atención antes de buildear

`download: true` requiere que el server donde corre `npm run build` tenga acceso saliente a `fonts.gstatic.com` y `fonts.googleapis.com`. Si el build falla con `ENOTFOUND`, hay dos opciones:

1. Whitelist los dominios en el firewall del server de build
2. Revertir a `download: false` y agregar manualmente:
   ```js
   { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "anonymous" }
   ```

## Cómo medir después del deploy

```bash
# 1. Build limpio
cd /Users/hermess/www/lo3/sitio-web-app-v3
npm ci && npm run build && npx pm2 restart all

# 2. Verificar que las fuentes se generaron
ls app/assets/fonts/  # debería listar 6 archivos Inter-{400,500,700}-{latin,latin-ext}.woff2

# 3. PSI 3 veces sobre /placas-de-video
# https://pagespeed.web.dev/analysis?url=https://www.libreopcion.com.ar/placas-de-video
# Tanto desktop como mobile.

# 4. Field data: esperar 2-4 semanas y revisar CrUX en Search Console
```

## Hashes

- `02ebadd1e` — Ronda 3 (h1 sr-only inline, pin envíos, tabular-nums) — fija CLS HOME
- **`274bce6ee`** — Esta ronda 4 (CLS listings + Inter font config)

## Lecciones aprendidas

1. **Field data > lab data para identificar el bug real.** El lab decía CLS home 0.519 (que ya arreglamos), pero el CrUX field mostró que el problema es de ORIGEN: las listings dominan la muestra. Sin field data nos hubiéramos quedado optimizando la home eternamente.

2. **Skeleton y card real DEBEN tener la misma altura.** No "más o menos", **exactamente la misma**. Cualquier delta se multiplica por filas en grids/masonry. Es la cosa más fácil de olvidar al diseñar skeletons.

3. **`<ClientOnly>` es enemigo del CLS** cuando wrapea contenido grande. Aún si el skeleton coincide, el wrap en ClientOnly significa que SSR no pinta las cards reales — todo se pinta en hidratación. Min-height en el contenedor padre ayuda parcialmente. Lo ideal es sacar de ClientOnly cuando se puede.

4. **`@nuxtjs/google-fonts` con `subsets` por defecto baja todo el universo de glifos.** Para Argentina (latin + latin-ext) ahorrás 75% del peso. Siempre especificar subsets.

5. **`display: optional` es el único valor de `font-display` que garantiza CLS=0 por FOUT.** `swap` causa reflow, `block` causa FOIT. `optional` es la opción CLS-friendly, con el trade-off conocido de que algunos usuarios ven la fuente del sistema en mobile slow.

## Próximos pasos

- [ ] **Build + deploy** del commit `274bce6ee` con `npm ci && npm run build`
- [ ] **Verificar generación de fuentes**: `ls app/assets/fonts/` debería tener 6 archivos
- [ ] **PSI 3 veces** sobre `/placas-de-video` (mobile + desktop)
- [ ] **Re-medir home** (`/`) para confirmar que la ronda 3 sigue OK
- [ ] **Esperar CrUX field** 2-4 semanas y revisar Search Console
- [ ] Si sigue alto:
  - Sacar `<ClientOnly>` del wrap de productos en `general.vue:103-131` (riesgoso, hay que verificar Masonry SSR)
  - Atacar `BootstrapVue` tree-shake y `VeeValidate` lazy
  - Granularizar `vendor` splitChunks en `nuxt.config.js`

## Ver también

- [[06-fix-cls-tbt-ronda-2]]
- [[07-fix-cls-mobile-h1-sr-only-ronda-3]]
- [[00-resumen-diagnostico-seo-performance]]
- [[Libre Opcion]]
