# contexto

Decisiones y detalles no obvios del proyecto.

## El mapa es espejado (rediseño "banner" 2:1)

El tablero original era una sola mitad de 28 columnas. El rediseño lo convirtió
en un mapa rectangular 2:1 espejando esa mitad: la mitad derecha es el reflejo
de la izquierda. Esto vale tanto para `graphic_map`/`logical_map` como para el
canvas de `path`.

## Gotcha: espejo del sprite ≠ espejo del pixel

Pac-Man se valida por el pixel verde en su posición **top-left** (sprite TL),
pero el sprite mide 24px. Para que la mitad derecha sea simétrica de verdad, el
espejo del path debe reflejar el **sprite** alrededor del centro del juego
(x=336), no reflejar pixel a pixel. Reflejar a nivel pixel deja los corredores
verticales corridos ~21px y Pac-Man "atraviesa" paredes en el lado derecho.

## Gotcha: path.png es 1px más angosto de lo esperado

El área jugable de `path.png` mide 335px pero la mitad gráfica del mapa mide
336px (28 tiles × 12). Ese desfase de 1px se propaga al espejar y hay que
compensarlo al posicionar el espejo.

## Túneles

Para que el wrap de los túneles laterales funcione, el espejo tiene que incluir
los márgenes del `path.png` (que contienen los datos del túnel), no sólo el área
jugable. El wrap derecho dispara al alcanzar `x = SCREEN_WIDTH`, simétrico con el
izquierdo que dispara cuando el sprite quedó completamente fuera del borde.

## Decisión: 8 fantasmas con IA idéntica

Se eligió duplicar los 4 fantasmas con **IA idéntica** (no espejada) porque es
más simple y no toca la lógica de targeting. Los 4 nuevos arrancan **desplegados**
en la mitad derecha (sin usar un "home" propio) para evitar duplicar toda la
mecánica de puerta y secuencias de salida del home.

- Pendiente / rareza conocida: cuando un fantasma del lado derecho es comido en
  modo frightened, "vuelve" al home izquierdo (el único que existe en la lógica
  de returning). Funciona, pero es raro temáticamente.

## Decisión: banner jugable de Pac-Man Day (1440×360)

El juego se enmarcó en un banner promocional de 1440×360 para el Pac-Man Day
(22 de mayo). Como el mapa es ~2:1 y el banner es 4:1, se descartaron dos
alternativas: estirar el juego a todo el ancho (distorsiona los sprites) y
rediseñar el mapa a 4:1 (rehacer todo el laberinto). Se eligió **mantener el
mapa intacto y centrado**, rellenando los costados con branding HTML/CSS. El
mundo interno sigue siendo 672×372; sólo cambia cómo se muestra.

## Cómo correr

`python3 -m http.server 8000` y abrir `http://localhost:8000`. Debe ser por HTTP,
no `file://`.

## Ver también

- [[arquitectura]] — estructura del código
- [[changelog]] — qué se cambió y cuándo
- [[pacman]] — índice del proyecto
