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

Archivo principal: `informe-gigabyte-landing/index.html`.

## Ver también
- [[informe-landing]] · [[arquitectura]]
