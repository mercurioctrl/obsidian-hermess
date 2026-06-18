# Memoria — informe-landing

Espejo de la memoria de Claude del proyecto (`~/.claude/projects/-var-www-Informe-gigabyte/memory/`), organizada por tipo.

## Proyecto
- **Qué es**: presentación/landing HTML (no app) que pitchea a GIGABYTE centralizar el paid media con BLU. Deck de 14 slides, contenido base de `Ventajas Gigabyte.docx`. Repo `BluIncStudio/informe-gigabyte-landing` (rama `main`). Ver [[contexto]].
- **Arquitectura**: un solo `index.html` autocontenido (~776 KB, fuentes woff2 + imágenes en base64), sistema de slides + componentes AORUS + capa de herramientas (editor / presentación / edición de textos / export). **Dos variantes**: `index.html` (interna, con BLU) y `reseller.html` (de cara al reseller, sin BLU, con sección de instalación de píxeles/tags + botón Copiar). Ver [[arquitectura]].

## Feedback / estilo (cómo trabajar)
- Texto **solo naranja `#FF6400` o blanco**; los colores de marca solo como gráficos. Esquemas con estética **AORUS**. Iconos SVG monoline, no emojis.
- Coherencia entre esquemas: clonar el patrón de los slides 02/03 (header de panel con barra naranja, contenedores sólidos, escala de fuentes/iconos).
- Persistencia **sin base de datos** → localStorage + export horneado.

## Referencia
- Manual de Marca: `elementosMarca/Manual de Marca - nolinks.pdf`.
- Assets de marca: `elementosMarca/` (logos, fonts) y `EjemplosDiapositivas/` (fondos).

## Ver también
- [[informe-landing]] · [[arquitectura]] · [[stack]] · [[contexto]] · [[changelog]]
