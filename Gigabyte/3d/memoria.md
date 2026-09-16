# Memoria — 3d

Consolidado de la memoria de Claude del proyecto
(`~/.claude/projects/-var-www-gigabyte-3d/memory/`).

## Usuario

### Impresora y tipo de trabajo

Imprime en una **Bambu Lab A1 mini**: cama de 180 × 180 × 180 mm. Todo modelo tiene que
entrar ahí; para piezas largas hay que girarlas 45° (la diagonal da 254 mm).

Hace **logos de marcas en 3D de forma recurrente**, no es un pedido aislado: en
`~/Documentos` hay carpetas de ADATA (`ADATA_PARADISE_4colores_AMS`, `..._encastre`),
D-Link (`DLINK_BOT_A1_MINI_4_COLORES`, con varias iteraciones) y ahora Gigabyte. Varias
mencionan 4 colores y encastres, así que maneja multicolor y piezas que se ensamblan.

Al pedir un modelo suele traer un **STL de referencia** del estilo que quiere (acá fue
`muestra.stl`) en vez de describirlo. Conviene analizarlo y derivar de ahí las
proporciones antes de diseñar.

## Feedback

### Prioriza el diseño por encima de la comodidad de impresión

Le propuse mover las letras al ras de la cara trasera para imprimir sin soportes.
Respondió: *"el tema es que a mi me gustaba que quede centrado"*.

**Por qué:** valora la fidelidad del diseño más que ahorrarse soportes. El costo real
eran ~1,5 g sobre 27 g de pieza, con las marcas en caras que no se ven — o sea, el
trade-off que yo había planteado como importante era despreciable, y se lo había
resuelto por mi cuenta cambiando el diseño.

**Cómo aplicarlo:** cuando haya que elegir entre cómo se ve la pieza y cómo se imprime,
mantener el diseño y **cuantificar el costo** (gramos de soporte, dónde quedan las
marcas, si se ven en uso normal) para que decida él. La variante "cómoda" va como
alternativa en un archivo aparte, nunca como reemplazo.

### Verificar la imprimibilidad antes de afirmarla

Cerré la primera entrega con "imprime sin soportes" sin haberlo calculado. Repreguntó:
*"esto se puede imprimir sin soportes?"*. Al analizarlo había 6 techos planos a 90°.

**Por qué:** una afirmación de imprimibilidad se paga con una impresión fallida de horas.

**Cómo aplicarlo:** calcularlo sobre la malla final — área de caras que miran hacia abajo
a más de 45°, distinguiendo **puente** (anclado de los dos lados, sale bien) de
**voladizo** (un solo lado, se descuelga). Rasterizar el perfil a 0,2 mm, como el slicer.
Reportar el número, no la conclusión sola.

## Referencia

### Bóveda de Obsidian

Los proyectos bajo `/var/www/gigabyte/` documentan en `Gigabyte/<proyecto>/` de la bóveda
(acá: `Gigabyte/3d/`). Acceso por el plugin **Local REST API** en
`https://localhost:27124/` con `curl -sk` y `Authorization: Bearer {token}`. La bóveda en
disco está en `/var/www/obsidian-hermess`.

## Gotchas técnicos

Los del código están en [[arquitectura#Gotchas|arquitectura]].

## Ver también

[[contexto]] · [[arquitectura]] · [[3d]]
