# Memoria — informe-landing

Espejo de la memoria de Claude del proyecto (`~/.claude/projects/-var-www-Informe-gigabyte/memory/`), organizada por tipo.

## Proyecto
- **Qué es**: presentación/landing HTML (no app) que pitchea a GIGABYTE centralizar el paid media con BLU. Deck interno de **16 slides** (contenido base de `Ventajas Gigabyte.docx`; los 2 últimos slides agregados — privacidad Meta Ads + escenarios GTM — salen del Excel `Gigabyte - Acceso Meta Ads para resellers y GTM.xlsx`). Repo `BluIncStudio/informe-gigabyte-landing` (rama `main`). Ver [[contexto]].
- **Arquitectura**: un solo `index.html` autocontenido (~776 KB, fuentes woff2 + imágenes en base64), sistema de slides + componentes AORUS + capa de herramientas (editor / presentación / edición de textos / export). **Dos variantes**: `index.html` (interna, con BLU, 16 slides) y `reseller.html` (de cara al reseller, sin BLU, 7 slides, con sección de instalación de píxeles/tags + botón Copiar). Ver [[arquitectura]].
- **Entregable aparte — Investigación Notebooks** (2026-07): análisis de mercado + 4 landings HTML por país (AR/CL/UY/PY) de las notebooks GIGABYTE **Gaming A16** y **Aero X16** (del `LAP + MONIS (2).xlsx`). Generación data-driven: `generar_landings.py` + `data_paises.py` en `por pais/investigacion-notebooks/`. Convención: toda tienda/precio/fuente citada es un enlace clicable. Producto: A16 capa GPU a ~85W (no prometer "máximo rendimiento"); GIGABYTE es challenger en notebooks. Ver [[investigacion-notebooks]].

## Feedback / estilo (cómo trabajar)
- Texto **solo naranja `#FF6400` o blanco**; los colores de marca solo como gráficos. Esquemas con estética **AORUS**. Iconos SVG monoline, no emojis.
- En layouts SÍ/NO usar **naranja (positivo) / gris neutro (negativo)**, nunca mint/magenta en texto.
- Coherencia entre esquemas: clonar el patrón de los slides 02/03 (header de panel con barra naranja, contenedores sólidos, escala de fuentes/iconos).
- Persistencia **sin base de datos** → localStorage + export horneado.
- Git: nunca `Co-Authored-By`, los commits son del usuario. Simplicidad sobre complejidad, no agregar features no pedidas.

## Referencia
- Manual de Marca: `elementosMarca/Manual de Marca - nolinks.pdf`.
- Assets de marca: `elementosMarca/` (logos, fonts) y `EjemplosDiapositivas/` (fondos).
- Fuente de los slides de privacidad/medición: `Gigabyte - Acceso Meta Ads para resellers y GTM.xlsx` (hojas *Meta* y *GTM*).

## Ver también
- [[informe-landing]] · [[arquitectura]] · [[stack]] · [[contexto]] · [[changelog]]
