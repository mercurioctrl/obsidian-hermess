# Investigación Notebooks — GIGABYTE por país (A16 + Aero X16)

Entregable de **investigación de mercado + estrategia** para las notebooks gaming GIGABYTE (series **Gaming A16** y **Aero X16**, tomadas del archivo `LAP + MONIS (2).xlsx`), con salida en **4 landings HTML tipo deck**, una por país: **Argentina, Chile, Uruguay y Paraguay**.

- **Ubicación:** `/var/www/Informe gigabyte/por pais/investigacion-notebooks/`
- **Fecha:** 2026-07 · **Estado:** entregado (precios sujetos a re-validación de stock).
- Relacionado con [[informe-landing]] (mismo cliente/carpeta, pero **otro entregable**: acá es análisis de producto + pauta por país, no el pitch de centralización).

## Qué contiene cada landing (10 secciones)

Hero → **Mercado** (contexto, impuestos, estacionalidad) → **Modelos + precios locales** → **Competencia por tier de GPU** (4050/5050/5060/5070 vs ASUS/Lenovo/Acer/HP/MSI/Dell) → **Demanda / SEO / keywords** → **Posicionamiento** → **Estrategia go-to-market** → **Campañas creativas** (con copy) → **Planes de ads $500 / $1.000 USD** (split de canales) → **Oportunidades / Riesgos** → Footer con fuentes.

## Cómo se genera (data-driven)

- **`generar_landings.py`** — template HTML/CSS (design system GIGABYTE) + renderers de sección. Recorre `PAISES` y escribe un HTML por país + valida.
- **`data_paises.py`** — todo el contenido por país en dicts (`ARGENTINA`, `CHILE`, `URUGUAY`, `PARAGUAY`). Para actualizar un precio/tienda: editar el dato (cada uno con su `u` = URL) y correr `python3 generar_landings.py`.
- **`index.html`** — portada con las 4 tarjetas de país.
- Verificación de render: `google-chrome-stable --headless --screenshot`.

## Convención de enlaces (pedido del usuario)

**Toda tienda / marketplace / precio / fuente citada es un enlace clicable** (`target="_blank"`) a la fuente real:
- Chips de tienda bajo cada tarjeta de modelo (ej. `FullH4rd ↗`, `Nissei ↗`).
- Nombres de modelo clicables en las tablas de competencia.
- Footer **"Fuentes (clic para abrir)"** con todas las fuentes verificadas.

## Hallazgos clave por país

- **GTM propio por país:** AR `GTM-WTVW6RK8` · CL `GTM-TG88FTK8` · UY `GTM-5VJ88N45` · PY `GTM-K97RQ7VJ`.
- 🇦🇷 **Argentina:** post-Impuesto PAIS; diferencial = Aero X16 QHD+ a precio de 5060 FHD + cuotas. Riesgo #1: **stock intermitente**.
- 🇨🇱 **Chile:** notebooks exentas de arancel → **líder de precio** (A16 5050 ≈ $999.990; 5060 con 1TB). Se gana en comparadores **SoloTodo / Knasta**.
- 🇺🇾 **Uruguay:** mayor poder adquisitivo pero mercado chico; competidor real = **importar de EE.UU. (TiendaMia)** → mensaje anti-importación.
- 🇵🇾 **Paraguay:** IVA 10% + Ciudad del Este → **mejor relación precio/spec** (i7+1TB al precio de i5+512 rival); target = **turista de compras AR/BR** (pauta ES+PT).

## Dato de producto a respetar en la comunicación

- El **A16 limita la GPU a ~85W** → **no** comunicar "máximo rendimiento"; posicionar por **valor / pantalla / última generación RTX 50**.
- **GIGABYTE es challenger en notebooks** (fuerte en componentes) → la pauta necesita construir awareness.
- Diferenciales: **A16 = precio/spec**; **Aero X16 = QHD+/OLED + Ryzen AI + Copilot+** (segmento creador+gamer).

## ⚠ Desviación de marca (a revisar)

Estos landings replican el template **"por pais"** (pauta centralizada), que usa **gradiente RGB, texto cian/magenta y banderas emoji**. Esto **contradice la regla de marca** documentada en [[contexto]] / [[memoria]] para el deck `informe-landing` (**texto solo naranja/blanco, sin emojis, estética AORUS**). Pendiente: decidir si estos decks de investigación deben migrarse a la regla estricta de marca o si el estilo "por pais" es aceptable para uso interno/reseller.

## Ver también
- [[informe-landing]] · [[contexto]] · [[changelog]] · [[stack]]
