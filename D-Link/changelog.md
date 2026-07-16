# Changelog

## 2026-07-16
- **Nueva landing `brand-guidelines/index.html`**: versión web del PDF `Brand_Guidelines_2015`
  de D-Link (contenido 100% fiel, en inglés). Estilo basado en la landing de producto `m15-2/`,
  con el **teal oficial `#0087A9`** (no el azul de campaña). Ver [[landings]].
- **PDF gemelo** `D-Link-Brand-Guidelines.pdf` (25 págs, A4) generado con **Chrome headless**
  directo del HTML mediante un bloque `@media print` (fuerza `.reveal` visible, oculta nav fija,
  controla saltos de página; índice en flexbox). **NO usa `md2pdf.py`** (ese script es md→PDF).

## 2026-07-02
- **Documentación + memoria:** actualizado `CLAUDE.md` (arquitectura, agencia Blu, herramientas) y
  la memoria del proyecto (3 notas: proyecto, [[contexto|Blu]], propuesta-landing). Sincronizada la bóveda.
- Creada [[pitch-punchlines-propuesta|chuleta de punchlines]] para presentar la propuesta (frases
  clave por sección + manejo de objeciones) + su PDF.
- `propuesta.html`: gate por token con input en pantalla; confetti al clickear "Avancemos →";
  se quitó el botón "Abrir pitch en slides".

## 2026-07-01
- `propuesta.html` (nueva landing, propuesta de Blu para D-Link, versión web del pitch): lockup
  co-branded **D-Link × Blu**, gate por token, paleta corporativa `#4481a7`, íconos SVG flat.
- Reescritura de copy a pedido del usuario: 4 murallas (se sumó "Fondos al canal"), grilla de
  **6 bloques de servicio** en Inversión (estilo Gigabyte), pilar Respaldado con "garantía hasta 10
  años", cierre nuevo. Presupuesto **1.800** y alcance **Argentina y Chile** solo en la propuesta.
- `index.html` (landing consumidor) y `propuesta.html`: migradas a paleta corporativa `#4481a7` +
  íconos SVG flat. Ambas movidas a la raíz del proyecto.

## 2026-06-30
- Planes por canal: [[instagram-plan]], [[facebook-plan]], [[newsletter-campana]].
- Deck ampliado a **17 slides** (se sumaron "Canales digitales" y "El recorrido").
- `index.html` consumidor creado con identidad D-Link.
- Script `.claude/scripts/md2pdf.py`: PDF de cada `.md` de entregables.

## 2026-06-29
- Investigación ([[informe-mercado]] + [[analisis-catalogo]]), [[estrategia-marca]],
  [[plan-campana]] y deck del pitch. Vinculación con Obsidian.

## Ver también
[[D-Link]] · [[arquitectura]] · [[contexto]]
