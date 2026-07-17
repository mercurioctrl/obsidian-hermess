# Investigación Notebooks — GIGABYTE por país (A16 + Aero X16)

Entregable de **investigación de mercado + estrategia** para las notebooks gaming GIGABYTE (series **Gaming A16** y **Aero X16**, tomadas del archivo `LAP + MONIS (2).xlsx`), con salida en **4 landings HTML tipo deck**, una por país: **Argentina, Chile, Uruguay y Paraguay**.

- **Ubicación:** `/var/www/Informe gigabyte/por pais/investigacion-notebooks/`
- **Fecha original:** 2026-07 · **Última profundización:** 2026-07-17 · **Estado:** entregado + profundizado (precios sujetos a re-validación de stock).
- Relacionado con [[informe-landing]] (mismo cliente/carpeta, pero **otro entregable**: acá es análisis de producto + pauta por país, no el pitch de centralización).

## Profundización 2026-07-17 (research verificado)

Se corrió un **workflow multi-agente** (31 agentes, ~620 búsquedas/fetches web, con un pase de **verificación adversarial** que contrasta cada cifra contra su fuente vía WebFetch). Los resultados se integraron a `data_paises.py` + `generar_landings.py` y se regeneraron los 4 HTML. La data cruda verificada quedó en `research_out/*.json`; el script de integración es `enrich_data.py`. Backups: `data_paises.py.bak`, `generar_landings.py.bak`.

**Hallazgo transversal (el más importante):** GIGABYTE **capa la GPU a 85 W de TGP** en toda la línea (A16 y Aero X16, 5050/5060/5070, incluido Dynamic Boost), mientras rivales corren la **misma** RTX 5060 a 100-115 W (Lenovo LOQ 15, ASUS TUF, Acer Nitro). Medido por Notebookcheck y PC Gamer: la RTX 5070 de la A16 "apenas se despega" de una 5060 bien alimentada. **Regla de comunicación:** nunca vender por fps brutos ni "máximo rendimiento" → vender por precio/valor, panel (QHD+ 2560×1600 / OLED), batería, Copilot+/Ryzen AI y garantía. La honestidad sobre el TGP es un activo defendible.

## Qué contiene cada landing (11 secciones)

Hero → **Mercado** (contexto, impuestos verificados, estacionalidad, cifras con fuente) → **Modelos + precios locales** (re-verificados en vivo, con stock y nivel de confianza por SKU) → **🆕 Rendimiento real & benchmarks** (cap 85 W TGP + fps reales de reviews citadas) → **Competencia por tier de GPU** (4050/5050/5060/5070 vs ASUS/Lenovo/Acer/HP/MSI/Dell) + **movidas vigentes de rivales** → **Demanda / SEO / keywords** (con volumen estimado + intención + dificultad, tabla) → **Posicionamiento** → **Estrategia go-to-market** + **playbook táctico ampliado** (7-12 jugadas: título + racional + táctica) → **Campañas creativas** (con copy) → **Planes de ads $500 / $1.000 USD** (split de canales) → **Oportunidades / Riesgos** → Footer con fuentes (35-46 por país, verificadas).

## Cómo se genera (data-driven)

- **`generar_landings.py`** — template HTML/CSS (design system GIGABYTE) + renderers de sección. Recorre `PAISES` y escribe un HTML por país + valida.
- **`data_paises.py`** — todo el contenido por país en dicts (`ARGENTINA`, `CHILE`, `URUGUAY`, `PARAGUAY`). Campos nuevos tras la profundización: `product_truth`, `benchmarks`, `keywords_detail`, `playbook`, `competitor_moves`, `tax_note`, `narrative`, `research_date`. Para actualizar un precio/tienda: editar el dato (cada uno con su `u` = URL) y correr `python3 generar_landings.py`.
- **`enrich_data.py`** — script que combina lo editorial existente con la data verificada de `research_out/*.json` y reescribe `data_paises.py`.
- **`index.html`** — portada con las 4 tarjetas de país.
- Verificación de render: `google-chrome-stable --headless --screenshot`.

## Convención de enlaces (pedido del usuario)

**Toda tienda / marketplace / precio / fuente citada es un enlace clicable** (`target="_blank"`) a la fuente real: chips de tienda bajo cada tarjeta de modelo, nombres clicables en tablas de competencia/benchmarks, y footer "Fuentes (clic para abrir)".

## Hallazgos clave por país (actualizados 2026-07-17)

- **GTM propio por país:** AR `GTM-WTVW6RK8` · CL `GTM-TG88FTK8` · UY `GTM-5VJ88N45` · PY `GTM-K97RQ7VJ`.
- 🇦🇷 **Argentina:** stock **delgadísimo** y sesgado a entrada — solo el A16 5050 confirmado con stock (Mexx ~$2,43 M, 11% OFF); Aero X16 5060 mayormente **agotado**; 5070 en ML no scrapeable. **Corrección fiscal clave:** la baja de aranceles a 0% de ene-2026 fue **solo** celulares y consolas — las **notebooks mantienen arancel 8%** (Decreto 136/2023) + IVA 21% + tasa 3%. Fuga transfronteriza vía courier (US$3.000) a neutralizar con garantía/cuotas. Hot Sale 11-13 may · CyberMonday 2-4 nov.
- 🇨🇱 **Chile:** challenger de **precio**, no de rendimiento. A16 5050 = el más barato de Chile ($1.089.990, Dust2); 5060 con 1TB de fábrica. El **IVA digital 19%** (desde oct-2025) neutraliza el arbitraje de importación → viento de cola para stock local + garantía formal. Se gana en **SoloTodo/Knasta**. Precio-gancho del Aero 5070 es volátil y de marketplace gris (mover a canal oficial). CyberDay 1-3 jun · CyberMonday 5-7 oct.
- 🇺🇾 **Uruguay:** GIGABYTE ya en góndola y **por debajo de ASUS ROG/MSI** (A16 5060 desde USD 1.779 PCStore; config Core Ultra 9 + 5070 WQXGA USD 2.523). E-commerce maduro (USD 2.552 M, +34%; 67% compró online, líder LatAm; 69% paga con crédito → cuotas decisivas). **Brecha SEO enorme:** SERP casi vacío de contenido comparativo/review → first-mover barato. Peso estable (~40,18 UYU) da previsibilidad de precio que AR no tiene.
- 🇵🇾 **Paraguay:** **mejor relación precio/spec** tier por tier (i7+1TB al precio de i5/512 rival), IVA 10% + Ciudad del Este. El eje transfronterizo **se movió de Argentina a Brasil** (compras BR +107%, AR −36%, electrónica AR −69%; brecha erosionada). Play prioritario: **geo-targeting fronterizo en portugués** (CDE + Foz do Iguaçu) + SEM de marca/modelo (competencia local casi nula). Régimen de Turismo de Compras (RTC, Decretos 2063/2024 y 2167/2024) exime IVA al turista en 6 ciudades. **Ojo:** la "tasa IVA efectiva 1,25%" que circula NO está respaldada — no usarla.

## Dato de producto a respetar en la comunicación

- El **cap de 85 W TGP** (ver arriba) → **no** comunicar "máximo rendimiento"; posicionar por valor / pantalla / batería / Copilot+ / última generación RTX 50.
- **GIGABYTE es challenger en notebooks** (fuerte en componentes) → prestar el equity de las placas de video ("brand borrowing") y construir awareness.
- Diferenciales: **A16 = precio/spec + batería 76 Wh**; **Aero X16 = QHD+/OLED + Ryzen AI + Copilot+ (NPU 50 TOPS)** (segmento creador+gamer, "Blue Ocean").

## ⚠ Desviación de marca (a revisar)

Estos landings replican el template **"por pais"** (pauta centralizada), que usa **gradiente RGB, texto cian/magenta y banderas emoji**. Esto **contradice la regla de marca** documentada en [[contexto]] / [[memoria]] para el deck `informe-landing` (**texto solo naranja/blanco, sin emojis, estética AORUS**). Las secciones nuevas (2026-07-17) mantuvieron el estilo "por pais" por consistencia con el deck. **Pendiente:** decidir si estos decks de investigación deben migrarse a la regla estricta de marca o si el estilo "por pais" es aceptable para uso interno/reseller.

## Ver también
- [[informe-landing]] · [[contexto]] · [[changelog]] · [[stack]]
