# Landing — Ejemplo de anuncios a ejecutar

Entregable **separado** del deck [[informe-landing]]: una landing HTML que le muestra al cliente (GIGABYTE) **cómo se van a ver los anuncios reales** de la campaña **Familia GIGA40** antes de ponerlos a rodar, en su contexto de plataforma (Meta + Google) y por cada reseller.

- **Ubicación:** `/var/www/Informe gigabyte/landing-ejemplo-ads/campana-q2-familia-giga40.html` (autocontenida, assets locales en `assets/`).
- **Fuentes de datos:**
  - `BLU X GIGABYTE - BLU CUADRO.csv` → plan de medios (país, reseller, producto foco, presupuesto, link de Facebook, sitio).
  - `Familia GIGA40-…/Familia GIGA40/Redes+ADS/` → creatividades reales en 4 formatos: Feed **2:1** (1200×628), Square **1:1** (1080×1080), Post **4:5** (960×1200), Story **9:16** (1080×1920).
  - `Redes+ADS/Key Words Campaña 40° Aniversario (1).pdf` → **copys exactos para Meta** (por producto: Familia, Monitores, Motherboards, VGA, PSU, Watercoolers, Notebooks) + **keywords de Google** por producto/país (amplia/frase/exacta + negativas). Se cargaron tal cual en los mockups: el copy de FB/IG y la query de Search salen de este PDF (mapeados por producto foco; la query usa la variante local — AR "placa madre"/"placa de video").
- **Campaña:** GIGABYTE 40 aniversario — **"Rendimiento y Evolución"** / **"Team Up. Fight On."**, línea gamer GIGABYTE & AORUS.

## Cómo funciona

Un **selector de reseller** (estilo botón: activo naranja sólido `#FF6400` con texto negro, resto oscuro con borde) que, al cambiar de punto de venta, **actualiza en vivo los 6 mockups** con los datos reales de ese reseller (nombre, handle de Facebook, país, producto foco, sitio/CTA). Todo por JS (objeto `RESELLERS` + mapas por `foco`).

### Canal 01 — Meta Ads
- **Facebook Feed** e **Instagram Feed** con **UI realista clara** (interfaz real de las plataformas, no el tema AORUS).
- **Stories/Reels 9:16** en 4 frames de celular, cada uno asignado a un reseller real (MMSOFT·UY, MegaBytes·CL, Compumar·AR, NoXie·AR).

### Canal 02 — Google Ads (los 4 formatos)
- **Search** — SERP con "Patrocinado", favicon, business + URL, título azul, descripción y sitelinks. Query y copy varían por `foco`.
- **Red de Display** — banner insertado en un **sitio publisher realista** (nota "HardZone" con titular, capitular, párrafos, sidebar "Lo más leído") + etiqueta "Anuncios de Google / ⓘ".
- **Demand Gen · Discover & Gmail** — card del feed con fila de fuente, imagen 4:5, tag "Anuncio · url", titular y CTA.
- **YouTube · in-stream** — player con badge "Anuncio", botón "Saltar anuncios", barra de controles, progreso amarillo y banner companion. *Se sirve con video; se muestra el fotograma clave a modo de referencia.*

## Sección de estrategia (2026-07-17)

Entre el Kit de formatos y el Plan de medios hay una sección **"La estrategia detrás de las piezas"** que vuelca el dossier [[research-paid-media]] al entregable, en estética AORUS (solo naranja/blanco/gris, iconos SVG monoline) y con **fuentes accesibles clicables**. Cinco sub-bloques: (1) por qué Google y Meta con el mismo peso (captura vs generación), (2) funnel de 3 columnas con KPI por etapa, (3) qué esperar en números reales (anclas AR: CPC ~US$0,38 · CPM ~US$3,80 · ROAS 2–3× + tabla por presupuesto + banda de error), (4) cómo se mide de verdad (last-click subestima a Meta → geo-lift + GTM/Consent Mode), (5) calendario comercial por país (AR/CL/UY no se unifican). Cierra con bloque de **Fuentes** y caveat de honestidad (montos de competidores y volúmenes absolutos no son públicos). Validado en pantalla y en PDF (8 págs, sin cortes).

## Resellers foco (Familia GIGA40, del CSV)

| País | Reseller | Foco | Inversión | Destino |
|------|----------|------|-----------|---------|
| UY | MMSOFT | Familia | US$ 270 | mmsoft.com.uy |
| UY | Sampler | Familia | US$ 270 | sampler.com.uy |
| UY | Banifox | Monitores | US$ 270 | banifox.com |
| CL | MegaBytes | Monitores/MB/PSU/WC | US$ 270 | megabytes.cl |
| AR | Compumar | Motherboards y VGA | US$ 270 | *Enviar mensaje* (sin landing) |
| AR | NoXie Store | Motherboards | US$ 270 | noxiestore.com |
| AR | Compufan | Tarjetas Gráficas | US$ 270 | *Enviar mensaje* (sin landing) |

Total foco: **7 resellers × US$ 270 = US$ 1.890**. (COMPRAGAMER/Armytech quedan fuera: en el CSV van bajo la campaña "Laptops" y sin presupuesto definido.)

## Decisiones de marca / fidelidad

- El cliente pidió **máxima fidelidad**: los mockups reproducen la **UI real** de cada plataforma (fondo blanco de Meta, colores propios de Facebook/Instagram/Google). Es una **excepción consciente** a la regla "solo naranja/blanco" — se justifica porque es reproducción fiel de plataformas externas. El **chrome del deck** (hero, secciones, tablas, selector) sí sigue la estética **AORUS** oscura. Ver [[contexto]].
- Resellers sin landing en el CSV (Compumar, Compufan) → CTA **"Enviar mensaje"** (Messenger), no un sitio inventado.
- Validación con `google-chrome --headless --screenshot` en cada iteración.

## Ver también
- [[informe-landing]] · [[contexto]] · [[changelog]]
- [[research-paid-media]] — dossier de research/estrategia que alimenta la sección de estrategia
- [[investigacion-notebooks]] — otro entregable satélite del mismo proyecto
