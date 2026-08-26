# contexto

Contexto y decisiones del proyecto [[tickets-sorteo]].

## Objetivo

Material imprimible para el evento/sorteo **ADATA PARADISE Brasil 2026**: tickets de sorteo numerados y cartelitos con nombres para bolsas de regalo.

## Reglas y decisiones del usuario

- **Impresión en blanco y negro**: el logo a color se convirtió a **escala de grises** (`_gris.png`). Se descartó usar el `.ai` vectorial directo porque no se puede incrustar en HTML/navegador.
- **QR descartado**: se llegó a generar `qr-blu.png` (→ https://blustudioinc.com) pero se quitó del diseño final del remite.
- **Numeración**: tickets de 001 a 070. Los primeros 001–045 ya se imprimieron; para completar hasta 70 se generan **solo los faltantes 046–070** (variables `DESDE`/`HASTA` en remite.html).
- **Talón cortable**: el ticket final tiene dos mitades con el **mismo número** (para que cada mitad conserve el Nº al cortar), separadas por línea punteada con **tijera**.
- **Cartelitos con nombres**:
  - Nombres agrupados van en **cartelitos separados** (Diego / Mayra; Mariano Rios / Hernan).
  - Se **quita** lo que está entre paréntesis y comentarios ("(Compragamer)", "(nuevo PM Newtree)", "Si es que van").
  - "- Elit" se mantiene (no está entre paréntesis).
  - **Tamaño de fuente uniforme** para todos los nombres (el mayor que entre en todos), no auto-fit individual.

## Técnicas usadas

- **Unidades de contenedor** (`cqh`/`container-type:size`) para que textos e imágenes escalen con el tamaño de cada ticket/cartelito.
- **Auto-ajuste por JS**: mide `scrollWidth/scrollHeight` vs la celda y baja la fuente hasta que entra; en cartelitos se aplica el mismo tamaño a todos.
- Números rojos en tickets.html: se muestrearon los colores reales con PIL (rojo ≈ `#c93230`, papel ≈ `#f6f1eb`) y se ubicaron por porcentaje sobre la imagen de fondo.
- **Verificación visual**: renders con `google-chrome-stable --headless --screenshot` + recortes con PIL para revisar alineación antes de dar por hecho.

## Cómo imprimir

Abrir el `.html` en el navegador → botón "Imprimir / Guardar PDF" (o Ctrl+P) → A4 → activar **"Gráficos de fondo"**.

## Ver también

- [[tickets-sorteo]] · [[changelog]]
