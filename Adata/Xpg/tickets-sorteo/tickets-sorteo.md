# tickets-sorteo

Generadores **HTML imprimibles** (blanco y negro) para el sorteo de **ADATA PARADISE Brasil 2026**. Cada `.html` arma hojas A4 listas para imprimir desde el navegador (Imprimir → PDF, con "Gráficos de fondo" activado). No usa framework: HTML + CSS + un poco de JS.

Ubicación en disco: `/var/www/adata/tickets-sorteo/`

## Archivos generadores

- **tickets.html** — Tickets de sorteo numerados usando la imagen real `ticket-muestra.png` como fondo; solo **reemplaza el número rojo** (vertical izquierdo + talón) tapando el "012345" original con un parche del color exacto del papel. 10 por hoja (2×5).
- **remite.html** — Ticket de sorteo con **talón cortable**: mitad izquierda `¡SUERTE!` + logo ADATA PARADISE (grises) + Nº; línea de corte punteada con **tijera** (SVG); mitad derecha trofeo + `★ SORTEO ★` + Nº. Rango configurable (`DESDE`/`HASTA`), 10 por hoja.
- **cartelitos.html** — Cartelitos con **nombres** para poner en bolsas: logo ADATA PARADISE (grises) + nombre grande. Tamaño de fuente **uniforme** auto-ajustado al nombre más largo. 10 por hoja. Lista en el array `NOMBRES`.

## Assets

- `XPG_LOGO_ADATA PARADISE_BRASIL.png` / `.ai` — logo oficial a color / vectorial.
- `XPG_LOGO_ADATA PARADISE_BRASIL_gris.png` — versión **escala de grises** (para impresión B&W), generada con PIL manteniendo transparencia.
- `trofeo.png` — icono trofeo negro (estrella + rayos).
- `sorteo.png` — banner `★ SORTEO ★`.
- `ticket-muestra.png` — foto del ticket base (ADATA PARADISE + Blu.) usada de fondo en tickets.html.
- `qr-blu.png` — QR a https://blustudioinc.com (descartado del diseño final).

## Ver también

- [[contexto]] — decisiones y reglas del proyecto
- [[changelog]] — registro de lo trabajado
- [[Xpg/Xpg|Xpg]] · [[adata-paradise-3d/adata-paradise-3d|adata-paradise-3d]]

_Última sincronización: 2026-08-26_
