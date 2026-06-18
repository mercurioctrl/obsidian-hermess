# Stack — informe-landing

Sin framework ni build. Es un **único `index.html`** estático y autocontenido.

- **HTML + CSS + JS vanilla**, todo inline en un archivo.
- **Tipografías**: Titillium Web, Teko, Aldrich (del Manual de Marca), subseteadas a **woff2** con `pyftsubset` (fontTools) y embebidas como data-URI.
- **Imágenes**: logos GIGABYTE/AORUS, fondos de marca y máscara de mascota, embebidas en base64.
- **Persistencia**: `localStorage` (claves `deckState`, `deckTexts`, `deckSizes`). Sin base de datos ni backend.
- **APIs del navegador**: `IntersectionObserver` (reveals/dots), Fullscreen API (presentación), `contenteditable` + `document.execCommand` (edición de textos), `Blob` + `download` (export).
- **Repo**: `git@github.com:BluIncStudio/informe-gigabyte-landing.git`, rama `main`.
- **Tooling de desarrollo** (no del producto): Python para editar el HTML, `google-chrome --headless --screenshot` para validar, `pyftsubset` para fuentes, ImageMagick/`pdftoppm` para preparar assets.

## Ver también
- [[informe-landing]] · [[arquitectura]]
