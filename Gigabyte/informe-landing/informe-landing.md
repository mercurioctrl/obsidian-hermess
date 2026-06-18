# Informe Gigabyte — Landing / Deck

Base de conocimiento del proyecto **informe-landing**: presentación / landing page HTML que propone centralizar la inversión de paid media (Google Ads + Meta Ads) de GIGABYTE, en lugar de campañas aisladas por reseller. Tiene una versión **interna** (con BLU) y una versión **de cara al reseller** (sin BLU, con instalación de píxeles/tags).

## Resumen

- **Tipo:** presentación / landing page estática autocontenida, sin build ni servidor. **Dos variantes**: `index.html` (interno) y `reseller.html` (de cara al reseller).
- **Marca:** GIGABYTE / AORUS — texto solo naranja `#FF6400` o blanco; estética AORUS (esquinas en bisel, monocromo + naranja) en los esquemas.
- **`index.html` (interno):** 14 slides (situación → oportunidad → argumentos de centralización → ventajas Gigabyte/reseller → campaña de ejemplo → caso de éxito).
- **`reseller.html` (reseller):** 7 slides, sin pitch interno ni mención a BLU ("GIGABYTE coordina"); caso sin el ROAS 277. Incluye una **sección de instalación** con GTM, Meta Pixel, GA4 y conversión Google Ads + botón **Copiar**.
- **Extras:** editor para ocultar/reordenar slides, edición de textos con formato y tamaño, modo presentación fullscreen, export "Descargar HTML" (viewer self-contained). Persiste en localStorage.
- **Repo:** `git@github.com:BluIncStudio/informe-gigabyte-landing.git` (rama `main`).
- **Ubicación local:** `/var/www/Informe gigabyte/informe-gigabyte-landing/`

## Notas

- [[arquitectura]] — un index.html autocontenido, slides, componentes AORUS y capa de herramientas.
- [[stack]] — HTML/CSS/JS vanilla, fuentes woff2 + imágenes base64, localStorage.
- [[contexto]] — reglas de marca, decisiones del usuario, aprendizajes.
- [[changelog]] — registro de lo trabajado por fecha.
- [[memoria]] — espejo de la memoria de Claude del proyecto.

## Ver también

- [[Gigabyte]]
- [[gigaErp]] — otro proyecto Gigabyte (ERP) en esta bóveda

_Última sincronización: 2026-06-18_
