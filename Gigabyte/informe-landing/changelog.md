# Changelog — informe-landing

## 2026-06-17

- Build inicial del deck GIGABYTE × BLU: presentación/landing HTML de 14 slides respetando el Manual de Marca (negro + naranja, tipografías Titillium/Teko/Aldrich, estética AORUS en los esquemas). Contenido base de `Ventajas Gigabyte.docx`.
- Iconos pasados de emojis a **SVG monoline** custom.
- Agregados slides de argumentación: centralización (algoritmo), atribución cruzada, efecto red del ML, datos/subasta/costos.
- Ajustes de marca: textos solo naranja/blanco; se sacó el magenta/azul de Situación y Reseller; mayúsculas en el cierre; header "Información interna · Emiliano Sánchez".
- Subido a GitHub `BluIncStudio/informe-gigabyte-landing` (rama `main`).
- **Modo presentación** (fullscreen) + **editor** flotante para ocultar/reordenar slides + ojito para ocultar controles.
- **Edición de textos** inline con toolbar de formato (negrita, blanco, naranja) + **control de tamaño** (A−/A+/↺) + guardado en localStorage + botón **Descargar HTML**.
- Deck hecho **autocontenido** (fuentes woff2 subseteadas + imágenes en base64) → portable.

## 2026-06-18

- **Fix**: export salía con los slides vacíos (solo el primero) porque las secciones quedaban después de los scripts → ahora se reubican antes y se marcan visibles.
- Export "viewer": el HTML descargado sale sin herramientas de edición (solo Presentar + ojito).
- **Mobile**: los esquemas (slides 02/03/06/07) ahora colapsan a 1 columna; se arregló el `.disc` centralizado que se cortaba a la derecha.
- **Fix**: "Restablecer original" ahora limpia también textos y tamaños (no solo orden/ocultos).
- **Nueva variante `reseller.html`** (deck de cara al reseller): se derivó de `index.html` por cirugía. 7 slides (hero · por qué centralizar · lo que ganás · campaña de ejemplo · caso real · **instalación** · próximos pasos). Sin pitch interno y **sin mención a BLU** ("GIGABYTE coordina"). Caso de éxito reescrito **sin el ROAS 277** (se reemplazó por "Tu costo de gestión: $0"). Header "Para Resellers".
- **Sección de instalación** nueva: snippets de **Google Tag Manager** (head + body), **Meta Pixel**, **Google tag / GA4** y **conversión Google Ads**, cada uno con botón **Copiar** (clipboard API + fallback `execCommand`). IDs de ejemplo (`GTM-XXXXXXX`, `TU_PIXEL_ID`, `G-XXXXXXXXXX`, `AW-…`) que el reseller reemplaza. Estética AORUS (paneles biselados, code-blocks monocromos), texto solo naranja/blanco/gris.

Archivos principales: `informe-gigabyte-landing/index.html` (interno), `informe-gigabyte-landing/reseller.html` (reseller).

## Ver también
- [[informe-landing]] · [[arquitectura]]
