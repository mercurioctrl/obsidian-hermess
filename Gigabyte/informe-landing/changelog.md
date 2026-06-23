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

## 2026-06-19

- `reseller.html`: se simplificó el caso/copys a **Resellers Argentina** (commit `e6a6f35`).

## 2026-06-23

- **`index.html`: 2 slides nuevos** sobre privacidad y medición, intercalados después de "Ventajas para el reseller" → el deck interno pasa de **14 a 16 slides**. Contenido tomado del Excel fuente `Gigabyte - Acceso Meta Ads para resellers y GTM.xlsx` (hojas *Meta* y *GTM*).
  - **Slide 12 · Privacidad · Meta Ads** ("El reseller mantiene el control. BLU solo toca lo que pauta"): dos columnas enfrentadas **SÍ puede** (verde AERO, ✓) vs **NO puede** (magenta AORUS, ✕). Deja claro que el permiso de Ads es acotado: BLU gestiona solo los anuncios de GIGABYTE y no accede a orgánico, mensajes, leads ni a la cuenta del reseller.
  - **Slide 13 · Medición · GTM** ("Cómo medimos según cuánto comparta el reseller"): 5 tarjetas, una por escenario de GTM, con caso / qué hacemos / ventaja-riesgo + chip de **fee** ("Sin costo extra" verde vs "Fee único por reseller" naranja). La opción 1 (un GTM por país, actual) lleva ribbon **RECOMENDADA**.
  - Añadidos dot de navegación y link "Privacidad" en el menú superior; eyebrows de Campaña/Caso renumerados (12/13); README actualizado a 16 slides. Los `slide-no` y el contador de presentación los recalcula el JS desde el orden del DOM, así que "/ 16" se ajusta solo.
- Commit `24812f4` pusheado a `main`. El `.xlsx` fuente se dejó **sin trackear** en el repo.

Archivos principales: `informe-gigabyte-landing/index.html` (interno), `informe-gigabyte-landing/reseller.html` (reseller).

## 2026-06-23

- **`reseller.html` simplificado a "Resellers Argentina"** (commit `e6a6f35`): se quitaron los slides de **campaña de ejemplo** y **caso de éxito**; el deck queda enfocado en el programa de pauta coordinada para resellers de Argentina. Pasó de 7 a **8 slides**.
- **2 slides nuevos** (privacidad + medición), adaptados a 2ª persona y **a GIGABYTE en vez de BLU**, con paleta de marca (naranja = positivo, gris neutro = negativo; sin mint/magenta):
  - **Privacidad · Meta Ads** (`#privacidad`, eyebrow 04): qué SÍ / qué NO puede ver GIGABYTE con el permiso de Ads acotado sobre el Business Manager del reseller (sin acceso a orgánico, mensajes ni leads).
  - **Medición · GTM** (`#gtm`, eyebrow 05): los **5 escenarios de GTM** según cuánto acceso comparta el reseller (del más eficiente al más costoso), con badge "Sin costo extra" / "Fee único" y opción 01 marcada RECOMENDADA.
- **Ocultar individualmente cada uno de los 5 escenarios GTM** desde el panel editor (sub-filas anidadas con ojito bajo el slide GTM), persistido en `deckState.cards` y excluido del export.
- **Texto de las tarjetas GTM editable**: se sumaron `.gtm-when/.gtm-k/.gtm-v/.gtm-fee` (y `.perm-list li`, `.perm-h h3`) al selector de edición de textos.
- **Toggle del badge de fee por escenario** (ícono de etiqueta en cada sub-fila del editor): muestra/oculta "Fee único" / "Sin costo extra", persistido en `deckState.fees` y excluido del export.
- **Renumeración dinámica de los escenarios GTM visibles**: al ocultar uno, las tarjetas visibles se renumeran `01, 02, 03…` en orden (sin huecos); también queda baked en el export.
- **Slide nuevo "Privacidad · Tu sitio"** (`#privacidad-sitio`, eyebrow 06, entre GTM y cierre): qué ve / NO ve el código de medición instalado. SÍ: solo eventos de la capa de usuario (clics, vistas, conversiones) con el único fin de medir las campañas. NO: cPanel, backend, bases de datos, archivos del sitio, nada no-público, otros códigos de tracking (Analytics/Meta), campañas del reseller o de terceros, ni analítica web/UX.
- Todo verificado con Chrome headless (estructura, edición, ocultado, renumeración) y **pusheado a `main`**.

Archivos principales: `informe-gigabyte-landing/reseller.html` (foco activo del proyecto).

## Ver también
- [[informe-landing]] · [[arquitectura]] · [[contexto]]
