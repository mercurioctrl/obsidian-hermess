# Contexto — informe-landing

## De qué se trata
Pieza para **vender internamente** a GIGABYTE la idea de **centralizar el paid media** (Google + Meta Ads) con la agencia **BLU**, en lugar de campañas aisladas por reseller. Modelo: GIGABYTE define estrategia/presupuestos, BLU ejecuta/optimiza/reporta, los resellers reciben tráfico calificado. El header la marca como "Información interna · Emiliano Sánchez".

## Reglas de marca (no negociables)
- **Texto solo naranja `#FF6400` o blanco** (+ grises neutros). Nunca cian/magenta/azul/verde en la tipografía.
- Colores de marca (cian, magenta, azul, verde AERO) **solo como elementos gráficos**, nunca en texto.
- Iconos SVG monoline custom, no emojis.
- Esquemas con estética **AORUS** (monocromo + naranja, esquinas en bisel).
- Detalle: ver [[gigabyte-marca-estilo]] en la memoria de Claude.

## Decisiones del usuario
- **ROAS 277** del caso de éxito se dejó textual del `Ventajas Gigabyte.docx` aunque parezca un typo de 2,77x.
- GitHub Pages **no** se activó (lo dejó así).
- Las funcionalidades de editor/textos/tamaño se piden persistentes pero **sin base de datos**: se resolvió con localStorage + botón "Descargar HTML" (export horneado y portable).
- La versión descargada debe salir **sin herramientas de edición** (solo Presentar + ojito).
- Práctica de git: features en ramas `feature/*`, luego merge a `main` y borrar la rama.

## Cosas que se intentaron / aprendizajes
- El export rompía (slides vacíos) porque el editor mueve las secciones al final del body → hay que reubicarlas antes de los scripts en el clon.
- El `.disc` centralizado del slide 07 no colapsaba en mobile por tener `grid-template-columns` inline → se vence con `!important` en el media query.
- La API REST de Obsidian (token del skill) está **rotada**: se sincroniza por acceso directo a `/var/www/obsidian-hermess/`.

## Próximos pasos posibles
- Activar GitHub Pages si se quiere URL pública.
- Reemplazar las creatividades mock de la campaña de ejemplo por imágenes reales de producto.

## Ver también
- [[informe-landing]] · [[arquitectura]] · [[changelog]]
