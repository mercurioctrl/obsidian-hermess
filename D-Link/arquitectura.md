# Arquitectura del proyecto

Proyecto **NO es un repo de código**: son documentos markdown encadenados + piezas HTML
autocontenidas. No hay build, test ni lint. Vive en el web root `/var/www/d-link/`.

## Cadena de dependencia de entregables

```
01-investigacion/  →  02-estrategia-marca/  →  03-plan-campana/  →  04-pitch/
   (evidencia)          (qué + porqué)          (cómo + plata)       (cómo se cuenta)
```

Cada documento hereda del anterior. Editar uno de arriba puede invalidar afirmaciones de los de
abajo — revisar la cadena al cambiar cosas de fondo.

- **01** — [[informe-mercado]] (hallazgos con nivel de confianza) + [[analisis-catalogo]] (32 SKUs,
  define los "héroes"). `productos-dlink-argentina.json` = catálogo crudo, fuente de verdad de SKUs.
- **02** — [[estrategia-marca]]: territorio "Confiabilidad simple", 3 pilares, marca única + 2 relatos.
- **03** — [[plan-campana]] + planes por canal: [[instagram-plan]], [[facebook-plan]], [[newsletter-campana]].
- **04** — deck en slides (`04-pitch/index.html`) + [[pitch-guion-presentador]] + [[pitch-punchlines-propuesta]].
- **Raíz** — dos landings HTML de campaña: ver [[landings]].

## Piezas HTML (todas autocontenidas, sin dependencias)

| Archivo | Para quién | Paleta |
|---------|-----------|--------|
| `04-pitch/index.html` | D-Link (presentación en vivo, 17 slides) | navy `#0a1f44` + naranja `#ff7a00` |
| `index.html` (raíz) | Consumidor final | azul insignia `#4481a7` + neutros |
| `propuesta.html` (raíz) | D-Link (cliente, propuesta de Blu) | azul insignia `#4481a7` + neutros |
| `brand-guidelines/index.html` | Guía de marca como web (documento) | teal oficial `#0087A9` |
| `m15-2/index.html` | Landing de producto M15 EAGLE PRO AI | teal `#0083A5`, fuentes Inter + Plus Jakarta |

Las dos landings **de campaña** (raíz) usan la paleta corporativa `#4481a7` + íconos SVG flat.
`m15-2/` es una landing de producto con su propio sistema de estilos (fuentes self-hosted, cards,
reveal-on-scroll) y **sirvió de base visual** para `brand-guidelines/` (que adopta ese sistema pero
con el teal oficial `#0087A9`). El deck de slides conserva navy + naranja.

## Generación de PDF — dos caminos distintos
- **`md2pdf.py`** (md → PDF): convierte los `.md` de entregables (carpetas 01–04) a PDF con estilo
  de marca (navy + naranja) vía Chrome headless. Cada carpeta queda con `.md` + `.pdf`.
- **HTML → PDF directo** (Chrome headless `--print-to-pdf`): usado para
  `brand-guidelines/D-Link-Brand-Guidelines.pdf`. Requiere un bloque `@media print` en el HTML que
  fuerce `.reveal` visible (el contenido depende de IntersectionObserver), oculte la nav fija y
  controle saltos de página. Las landings de raíz NO se pasan a PDF.

## Invariantes editoriales (reglas duras)
- **Filtro de 3 pilares:** todo refuerza ANDA / FÁCIL / RESPALDADO, o no va.
- **Regla de oro:** nunca nombrar a TP-Link en comunicación al público.
- **Outlets nunca se comunican** (SKUs "CAJA DAÑADA": ODCS-942L, ODCS-2103, O311GT).
- **Beneficio, no specs** ("WiFi en toda la casa", no "AX1500 dual band").
- **Honestidad:** metas numéricas se fijan tras el mes 1, con baseline real.

## Herramientas
- `.claude/scripts/md2pdf.py` — convierte todos los `.md` de entregables (01–04) a PDF con estilo de
  marca (Chrome headless). Cada carpeta queda con `.md` + `.pdf`.

## Ver también
[[contexto]] · [[changelog]] · [[landings]] · [[D-Link]]
