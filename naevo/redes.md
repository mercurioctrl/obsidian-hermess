# Redes & Marketing

Estrategia de redes sociales de NÆVO y pipeline de generación de imágenes de posts. Todo vive en `redes/` en la raíz del repo (contenido **untracked**, no commiteado a git — es material de marca, no código).

## Decisión clave: comunicar antes del producto

Se resolvió **arrancar a comunicar en redes aunque el producto todavía no salió**, con una **Fase 0 de comunidad + lista de espera** (8 semanas pre-lanzamiento, `L-8 → L-0`). No se vende un producto inexistente: se construye autoridad educativa en longevidad (NAD+, NMN, espermidina), se captura waitlist y se genera expectativa para llegar al día 0 con audiencia. Único riesgo gestionado: no dar fecha exacta hasta tener stock.

## Estructura de `redes/`

```
redes/
├── README.md                    índice + decisión pre-lanzamiento + KPIs
├── guia-de-marca-social.md      paleta, tono, bio, hashtags, do/don't
├── calendario-contenido.md      plan semana a semana (L-8→L-0), red por red
├── instagram/  estrategia.md · copys.md (15 captions) · briefs-visuales.md · imagenes/
├── tiktok/     estrategia.md · guiones.md (10 guiones)
├── youtube/    estrategia.md · guiones.md (videos largos + shorts)
├── linkedin/   estrategia.md · copys.md (6 posts)
└── _assets/    generar_posts.py + fonts/ + img/  (pipeline de imágenes)
```

Prioridad por red en Fase 0: **Instagram + TikTok** cargan el 80% (awareness + waitlist); YouTube (autoridad SEO evergreen) y LinkedIn (partners/B2B) siembran a largo plazo.

## Pipeline de imágenes (reproducible)

`redes/_assets/generar_posts.py` (Python + Pillow) genera **8 posts de Instagram 1080×1350** en `redes/instagram/imagenes/`. Correr:

```bash
python3 redes/_assets/generar_posts.py
```

Se calcaron los estilos **reales del sitio** (de `frontend/tailwind.config.js`, no del landing viejo):

| Token | Valor |
|---|---|
| navy | `#07142e` |
| navy-deep | `#030a1c` |
| azul editorial / umbra | `#1530e6` |
| cream | `#f7f5ef` |
| gold | `#c0a062` |
| cian | `#00cdcc` |

- **Fuentes:** Manrope (6 pesos) + Instrument Serif — las fuentes reales del sitio, bajadas completas de Google Fonts (las bundled estaban subseteadas). En `_assets/fonts/`.
- **Logo NÆVO:** extraído de la etiqueta Luteína en 3 variantes (dark / white / white+hoja cian). El `logo.png` del repo estaba vacío.
- **Frascos:** recortados a fondo transparente con GrabCut/máscara (OpenCV). Solo existen renders de **Luteína** y **Prebiótico** (de `Naevo-informacion/.../Etiquetas modelos descartados/`).

### Los 8 posts generados

Manifiesto · Bienestar inteligente · Las 4 líneas · NAD+ (con gráfico) · Lo que NO vas a encontrar · Founding members (CTA waitlist) · Producto Luteína (frasco) · Teaser "se viene" (frasco en silueta).

## Estado y pendientes

- ✅ Estrategia completa (12 docs) + 8 imágenes IG generadas.
- ⏳ **Frasco NÆVO Longevity (NMN 300 mg)** — el producto estrella NO tiene render aún; su post se genera reemplazando `luteina.png` cuando exista.
- ⏳ Versiones **Stories 1080×1920** y frames para **Reels/TikTok**.
- ⏳ Lead magnet / landing de waitlist que conecte con las redes.

## Nota de entorno

Esta sesión corrió en **Linux** (`/var/www/naevo`) con ImageMagick, OpenCV y Pillow disponibles — a diferencia de sesiones previas en macOS donde solo había PIL (ver [[changelog]]).

## Ver también

- [[naevo|Índice]]
- [[contexto|Contexto y decisiones]]
- [[changelog|Changelog]]
- [[stack|Stack]]
