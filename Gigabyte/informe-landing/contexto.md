# Contexto — informe-landing

## De qué se trata
Pieza para **vender internamente** a GIGABYTE la idea de **centralizar el paid media** (Google + Meta Ads) con la agencia **BLU**, en lugar de campañas aisladas por reseller. Modelo: GIGABYTE define estrategia/presupuestos, BLU ejecuta/optimiza/reporta, los resellers reciben tráfico calificado. El header la marca como "Información interna · Emiliano Sánchez".

## Reglas de marca (no negociables)
- **Texto solo naranja `#FF6400` o blanco** (+ grises neutros). Nunca cian/magenta/azul/verde en la tipografía.
- Colores de marca (cian, magenta, azul, verde AERO) **solo como elementos gráficos**, nunca en texto.
- Iconos SVG monoline custom, no emojis.
- Esquemas con estética **AORUS** (monocromo + naranja, esquinas en bisel).
- Detalle: ver [[gigabyte-marca-estilo]] en la memoria de Claude.

## Variante reseller (`reseller.html`)
- Se pidió una **segunda versión de cara al reseller**: GIGABYTE invitando al reseller, "no se puede decir todo" (no es el pitch interno).
- **No se nombra a BLU** → "GIGABYTE coordina" (interlocutor único).
- Secciones elegidas: ventajas para el reseller, campaña de ejemplo, caso de éxito + por qué centralizar (algoritmo/píxel) + **herramientas para instalar el tag manager y el píxel de Meta con explicación de cómo hacerlo**.
- En la variante reseller, el **ROAS 277 se quita** del caso (dato sensible) → se reemplaza por "Tu costo de gestión: $0".
- Tags incluidos con botón copiar: **GTM, Meta Pixel, Google tag/GA4, conversión Google Ads**, con IDs de ejemplo.

## Decisiones del usuario
- **ROAS 277** del caso de éxito se dejó textual del `Ventajas Gigabyte.docx` en la versión **interna** (aunque parezca un typo de 2,77x); se **oculta** en la versión reseller.
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
