# Contexto — informe-landing

## De qué se trata
Pieza para **vender internamente** a GIGABYTE la idea de **centralizar el paid media** (Google + Meta Ads) con la agencia **BLU**, en lugar de campañas aisladas por reseller. Modelo: GIGABYTE define estrategia/presupuestos, BLU ejecuta/optimiza/reporta, los resellers reciben tráfico calificado. El header la marca como "Información interna · Emiliano Sánchez".

## Reglas de marca (no negociables)
- **Texto solo naranja `#FF6400` o blanco** (+ grises neutros). Nunca cian/magenta/azul/verde en la tipografía.
- Colores de marca (cian, magenta, azul, verde AERO) **solo como elementos gráficos**, nunca en texto.
- Iconos SVG monoline custom, no emojis.
- Esquemas con estética **AORUS** (monocromo + naranja, esquinas en bisel).
- Detalle: ver [[gigabyte-marca-estilo]] en la memoria de Claude.

## Privacidad Meta Ads + escenarios GTM (slides 12-13, interno)
Se sumaron 2 slides al deck interno para **explicar a GIGABYTE/resellers los escenarios de privacidad** del acceso a Meta Ads y de la medición con GTM. Contenido tomado del Excel fuente **`Gigabyte - Acceso Meta Ads para resellers y GTM.xlsx`** (en la raíz del repo, **sin trackear**), hojas *Meta* y *GTM*.
- **Meta Ads — permiso acotado**: con el permiso de Ads sobre la Página del reseller, BLU **sí puede** (usar la Página como identidad del anuncio, crear/editar/pausar **solo los anuncios de GIGABYTE**, ver su rendimiento, reportar) y **no puede** (publicar/ver orgánico, leer/responder mensajes, ver o descargar leads, ver seguidores/engagement, ver anuncios del reseller, entrar al Business Manager, cambiar permisos o quitarle/borrar la Página). Mensaje clave: el reseller mantiene el control; BLU solo toca lo que pauta.
- **GTM — 5 escenarios** según cuánto acceso comparta el reseller, del más eficiente al más costoso:
  1. **Un GTM por país** (actual, *recomendado*) — filtramos por URL; reutilizamos tags/variables; **sin costo extra**.
  2. **GTM por país + lectura al reseller** — ve a otros resellers y nuestro know-how; sin costo extra.
  3. **Un GTM por reseller gestionado por BLU** — dedicado desde cero, lectura; **fee único por reseller**.
  4. **El reseller instala todo** — le pasamos IDs; sin verificación ni soporte de Google, riesgo de perder datos; **fee único**.
  5. **Acceso de publicación a su GTM** — trabajamos en su cuenta; se quedan con el know-how; **fee único**.

## Variante reseller (`reseller.html`)
- Se pidió una **segunda versión de cara al reseller**: GIGABYTE invitando al reseller, "no se puede decir todo" (no es el pitch interno).
- **No se nombra a BLU** → "GIGABYTE coordina" (interlocutor único).
- Secciones elegidas: ventajas para el reseller, campaña de ejemplo, caso de éxito + por qué centralizar (algoritmo/píxel) + **herramientas para instalar el tag manager y el píxel de Meta con explicación de cómo hacerlo**.
- En la variante reseller, el **ROAS 277 se quita** del caso (dato sensible) → se reemplaza por "Tu costo de gestión: $0".
- Tags incluidos con botón copiar: **GTM, Meta Pixel, Google tag/GA4, conversión Google Ads**, con IDs de ejemplo.
- Nota: los slides de privacidad/GTM nuevos viven **solo en `index.html`** (interno); pasarlos a `reseller.html` queda pendiente si se decide.

## Decisiones del usuario
- **ROAS 277** del caso de éxito se dejó textual del `Ventajas Gigabyte.docx` en la versión **interna** (aunque parezca un typo de 2,77x); se **oculta** en la versión reseller.
- GitHub Pages **no** se activó (lo dejó así).
- Las funcionalidades de editor/textos/tamaño se piden persistentes pero **sin base de datos**: se resolvió con localStorage + botón "Descargar HTML" (export horneado y portable).
- La versión descargada debe salir **sin herramientas de edición** (solo Presentar + ojito).
- Práctica de git: features en ramas `feature/*`, luego merge a `main` y borrar la rama. (Los 2 slides de privacidad/GTM se commitearon directo a `main` por pedido — `24812f4`.)
- El `.xlsx` fuente **no** se sube al repo (queda untracked).
- **Accesos Meta del slide de instalación** (reseller): se pidió poder **editar / quitar / agregar** esos items como cualquier otro contenido → se resolvió con un mecanismo de listas editables (`data-elist` + `deckLists`). Texto por defecto: "Permiso para crear anuncios a nombre de tu página de Facebook / cuenta de Instagram".

## Cosas que se intentaron / aprendizajes
- El export rompía (slides vacíos) porque el editor mueve las secciones al final del body → hay que reubicarlas antes de los scripts en el clon.
- El `.disc` centralizado del slide 07 no colapsaba en mobile por tener `grid-template-columns` inline → se vence con `!important` en el media query.
- Los `slide-no` los recalcula el JS desde el orden del DOM → al insertar slides no hace falta renumerar a mano el "`NN / total`" (sí los eyebrow).

## Próximos pasos posibles
- Activar GitHub Pages si se quiere URL pública.
- Reemplazar las creatividades mock de la campaña de ejemplo por imágenes reales de producto.
- Evaluar llevar los slides de privacidad/GTM a `reseller.html`.

## Ver también
- [[informe-landing]] · [[arquitectura]] · [[changelog]] · [[stack]]

## Investigación Notebooks (2026-07) — decisiones
- Entregable **separado** del deck `informe-landing`: análisis de mercado + pauta de las notebooks GIGABYTE **Gaming A16** y **Aero X16** (del `LAP + MONIS (2).xlsx`), en 4 landings HTML por país. Ver [[investigacion-notebooks]].
- Generación **data-driven** (`generar_landings.py` + `data_paises.py`): se pidió poder actualizar precios/tiendas editando el dato y regenerando.
- **Toda tienda/precio/fuente citada debe ser clicable** a la fuente real (pedido explícito del usuario).
- Producto: el **A16 capa la GPU a ~85W** → no prometer "máximo rendimiento"; vender valor/pantalla/RTX 50. GIGABYTE es **challenger en notebooks**.
- **Desviación de marca conocida:** los landings de notebooks usan el estilo del template "por pais" (gradiente RGB, texto cian/magenta, banderas emoji), que **contradice** la regla "solo naranja/blanco, sin emojis, AORUS" del deck principal. Pendiente decidir si se migran a la marca estricta.

## Landing ejemplo de anuncios (2026-07) — decisiones
- Entregable **separado** del deck `informe-landing`: mostrarle al cliente **cómo se ven los anuncios reales** de la campaña **Familia GIGA40** antes de ejecutarlos. Ver [[landing-ejemplo-ads]].
- **Data-driven desde el CSV** `BLU X GIGABYTE - BLU CUADRO.csv` + creatividades reales de `Familia GIGA40/Redes+ADS/`. Todo lo personalizable (nombre, handle, país, foco, sitio/CTA) sale del objeto `RESELLERS` en JS y se elige con un **selector de reseller**.
- **Se pidió personalizar por reseller** (no genérico) → cada mockup usa los datos reales del punto de venta.
- **Fidelidad realista (excepción de marca consciente):** el cliente pidió que se vea "tal cual sale en la realidad" → los mockups reproducen la **UI real** de Facebook/Instagram/Google (fondo blanco, colores propios de cada plataforma: azul FB, gradiente IG, colores Google). Esto **rompe a propósito** la regla "solo naranja/blanco", pero solo dentro de las piezas que imitan plataformas externas; el **chrome del deck** (hero, secciones, tablas, selector) sigue AORUS oscuro.
- **Iteración de feedback:** primero se hicieron los mockups en tema oscuro AORUS → el cliente los quiso realistas claros; y los de Google "no parecían reales" → se subió la fidelidad (Search con sitelinks, Display en sitio publisher con nota real, YouTube con controles de player, Discover con fila de fuente).
- **Estilo del selector:** botones rectangulares tipo CTA del hero (activo naranja sólido con texto negro, resto oscuro con borde), en vez de pills con bisel y monograma.
- Resellers **sin landing** en el CSV (Compumar, Compufan) → CTA **"Enviar mensaje"** (Messenger), no un sitio inventado.
- **Fuera de alcance:** COMPRAGAMER y Armytech (en el CSV van bajo campaña "Laptops", sin presupuesto definido). YouTube se sirve con video real; en la landing se muestra el fotograma clave.
