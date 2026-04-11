	# Ronda 3 — Fix CLS mobile 0.519 (h1 sr-only) + tabular-nums + width/height pin envíos

## Fecha
2026-04-08

## Contexto

Después del deploy de la ronda 2 (commit `00185f1c6`), la medición de PageSpeed mobile dio un resultado mixto:

| Métrica mobile | Antes (ronda 2) | Después (ronda 2) | Δ |
|---|---|---|---|
| LCP (lab) | 9.0s | **6.8s** | ✅ |
| TBT | 550ms | **260ms** | ✅ gran mejora |
| Speed Index | 4.6s | **2.9s** | ✅ |
| Animaciones no compuestas | 36 | **29** | ✅ |
| **CLS** | **0** | **0.519** | ❌ regresión |
| **Score** | 54 | **46** | bajó por el CLS |

Casi todo mejoró (TBT bajó a casi la mitad, LCP -2.2s, Speed Index -1.7s) pero el CLS mobile se disparó de 0 a 0.519 y arrastró el score.

PageSpeed reportó dos shifts grandes:
- `<body>` 0.276 — todo el body se mueve
- "Hero text **Libre Opción - Tienda de tecnología online con envío gratis**" 0.242

Field data (28 días, usuarios reales): CLS = 0. El problema es exclusivo del lab.

## Diagnóstico

**Causa raíz única identificada:** el `<h1 class="sr-only">` en `app/pages/index.vue:3`:

```vue
<h1 class="sr-only">Libre Opción - Tienda de tecnología online con envío gratis</h1>
```

La clase `.sr-only` viene de Bootstrap (`node_modules/bootstrap/scss/utilities/_screenreaders.scss`):

```scss
.sr-only {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}
```

Pero el módulo critters custom (`app/modules/critters.js`) **NO matchea ningún archivo de Bootstrap como crítico** — sus `CRITICAL_SELECTORS` son `cabecera-*`, `home-*`, `layout-*`, `banner-principal`, etc. Bootstrap CSS queda en el chunk deferido (`media="print" + onload`).

### Secuencia del CLS

1. SSR renderiza `<h1 class="sr-only">Libre Opción - Tienda de tecnología online con envío gratis</h1>`
2. Primer paint: el navegador renderiza el h1 con dimensiones default (h1 grande, ~46-56px alto + márgenes ~40px), pero como el texto es largo en mobile (viewport ~375px), hace **wrap a 2-3 líneas** → ocupa **~150px de altura visible**
3. ~300ms después llega el bundle deferido con Bootstrap CSS
4. `.sr-only` se aplica → el h1 colapsa a `1×1px`
5. Body sube ~150px → shift de **0.276** (body) y **0.242** (el h1 mismo desapareciendo)

### Por qué NO era FOUT (Inter font)

PageSpeed identifica los elementos shifteados por su contenido. El reporte decía exactamente "Hero **Libre Opción - Tienda de tecnología online con envío gratis**" — texto idéntico al h1. Si fuera FOUT:

- El shift sería ~0.01-0.05, no 0.242 (FOUT solo cambia ~2-4px por línea)
- Afectaría a TODOS los textos de la página, no a uno solo
- No reportaría un elemento individual con texto literal — reportaría `<body>` o el contenedor principal

Las cuentas tampoco cierran para FOUT: 0.242 × 640px viewport = ~155px de movimiento, imposible con cambio de fuente. Calza perfecto con un h1 colapsando.

## Soluciones aplicadas (commit `02ebadd1e`)

### 1. P0 — Inline style en el h1 sr-only

`app/pages/index.vue:3`:

```vue
<!-- Inline style en lugar de class="sr-only": esa clase vive en Bootstrap CSS
     que se carga deferido por critters; sin estilos, el h1 ocupa ~150px en mobile
     hasta que llega el chunk → CLS de 0.242. -->
<h1 style="position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0">
  Libre Opción - Tienda de tecnología online con envío gratis
</h1>
```

**Por qué inline y no otras alternativas:**

| Alternativa | Por qué se descartó |
|---|---|
| Agregar `.sr-only` a `CRITICAL_SELECTORS` de critters | Inlinaría todo Bootstrap CSS al HTML inicial (~150KB extra) |
| Mover `.sr-only` a SCSS propio que matchee selectores críticos | Funciona pero frágil — depende de que el chunk se cargue |
| **Style inline** ✅ | 1 línea, no depende de NINGÚN chunk, robusto desde el primer byte |

### 2. P1 — width/height en pin de envíos

`app/components/Layouts/Cabecera/partials/Envios.vue:14-18`:

```vue
<img
  :src="`images/svgs/iconos/icon-pin.svg`"
  :alt="`recibilo en ${domicilio}`"
  width="28"
  height="25"
/>
```

PageSpeed lo audita con impacto 0 pero igual lo lista. Cambio trivial.

### 3. P1 — tabular-nums en cronómetro instant flash

`app/components/Productos/ProgresoInstantFlash.vue:516-528`:

```scss
.cronometro {
  span {
    /* ... */
    // Dígitos de ancho fijo para que el contador HH:MM:SS no shifte
    // cada segundo cuando cambian los números (ej. 09 → 10).
    font-variant-numeric: tabular-nums;
    font-feature-settings: "tnum";
  }
}
```

Cada segundo el contador cambia (`01:09:59` → `01:10:00`) y los dígitos cambian de ancho — `tabular-nums` los fuerza a ancho fijo.

## Métricas esperadas después del deploy

| Métrica mobile | Antes (ronda 2) | Esperado (ronda 3) |
|---|---|---|
| CLS | 0.519 | ~0 |
| Score | 46 | 70-80+ |

El resto de métricas (TBT, LCP, FCP, Speed Index, animaciones no compuestas) ya estaban bien — el único bloqueo del score era el CLS.

## Otros usos de `.sr-only` en el codebase (deuda latente, no urgente)

Hay 9 usos más de `class="sr-only"` que tienen el mismo bug latente pero no causan CLS visible:

| Archivo | ¿Por qué no afecta el CLS hoy? |
|---|---|
| `pages/auth/login.vue`, `restablecer-contrasena.vue`, etc. | Páginas internas, no home |
| `pages/busquedas/.../FiltrosDesktop.vue` | Búsquedas, no home |
| `pages/catalogo/partials/Pasos/PasoTres.vue` | Catálogo, no home |
| `components/Productos/Favorito.vue:12` | Está en cards del home, **PERO** el botón es `position: absolute; right: 10px` — el ensanchamiento del button flotante no empuja el flow del documento |

### Fix global recomendado (mejora futura)

Agregar la regla `.sr-only` al `<style>` (no scoped) de:
- `app/layouts/desktop.vue`
- `app/layouts/mobile.vue`

Esos archivos sí matchean `CRITICAL_SELECTORS` (`layout-desktop`, `layout-mobile`), así que la regla quedaría en el HTML inline desde el primer byte sin depender de Bootstrap. Eliminaría la deuda técnica para los 9+ usos del codebase. No urgente porque ninguno causa CLS visible.

## Hashes

- `8d7aa8477` — Fix CLS animaciones (introdujo box-shadow en mixins, regresión)
- `f9f815a04` — Refactor v3→v4 push notifications (introdujo init en factory)
- `66e95e6d6` — Lazy-load Firebase (anulado por f9f815a04, restaurado en 00185f1c6)
- `00185f1c6` — Ronda 2 (width/height imgs + box-shadow fuera de mixins + push-notification diferido)
- **`02ebadd1e`** — Esta ronda 3 (sr-only inline + pin envíos + tabular-nums)

## Lecciones aprendidas

1. **`class="sr-only"` above-the-fold es una bomba de tiempo en SSR con CSS deferido.** Bootstrap no está en el critical CSS de critters, así que cualquier elemento sr-only con texto largo y posición en el flow del body genera CLS al colapsar. Para elementos críticos, usar `style="..."` inline o agregar la regla al SCSS de un layout que sí esté en el critical CSS.

2. **PageSpeed identifica elementos shifteados por su texto literal — usar eso para diagnosticar.** Si el reporte dice "Hero 'X texto exacto'" y ese texto matchea palabra por palabra un elemento del HTML, ese ES el elemento. No es FOUT, no es genérico. Buscar el elemento por grep del texto exacto.

3. **FOUT vs colapso de elemento — distinguir por magnitud.** FOUT da CLS de 0.01-0.05. Colapso de elemento (display:none tardío, height auto → 0) da CLS de 0.1-0.5+. Si el shift es grande, NO es FOUT.

4. **Field data > lab data para CLS en producción.** El field data ya estaba en CLS=0, lo que confirmaba que el problema era de timing específico del lab (el chunk deferido tarda más en lab por el throttling 4G). Eso no significa que esté bien — los runs de lab impactan el score que ven los SEOs.

## Próximos pasos

- [ ] Re-medir mobile en PageSpeed después del push `02ebadd1e`
- [ ] Si CLS lab queda <0.1: ronda cerrada, atacar BootstrapVue tree-shake / VeeValidate lazy / vendor splitChunks
- [ ] Si queda 0.1-0.2: P2 (Inter font preload + display:optional) — está documentado en el plan
- [ ] (Opcional, no urgente) Mejora futura: `.sr-only` global en `app/layouts/desktop.vue` y `mobile.vue` para eliminar la deuda técnica de los otros 9 usos

## Ver también

- [[06-fix-cls-tbt-ronda-2]]
- [[00-resumen-diagnostico-seo-performance]]
- [[01-fix-cls-imagenes]]
- [[Libre Opcion]]
