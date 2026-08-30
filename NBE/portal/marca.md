# Marca

Parte de [[portal]].

Todo lo visual se tomó de **nbe.com.ar**, no se inventó. Cada valor está verificado contra el
CSS o el DOM del sitio.

## Logo

Es un **SVG inline en la cabecera** del sitio, no un archivo. Se extrajo del DOM y quedó en
`components/NbeLogo.vue`, con dos cambios:

- **Se quitaron el `<mask>` y el `<clipPath>`**: eran de canvas completo (no-ops), pero sus `id`
  fijos habrían colisionado al renderizar el logo dos veces en la misma página — el sidebar se
  monta duplicado para el drawer mobile.
- **`fill="white"` → `currentColor`**: en el sitio va siempre sobre el header azul; en el portal
  tiene que funcionar en claro y oscuro.

Calculando los bounding boxes de los 14 paths sale un corte limpio: `variant="full"`
(`viewBox 0 0 152 40`, isotipo + wordmark) y `variant="mark"` (`0 0 40 40`, solo el isotipo,
recortado por viewBox).

`favicon.ico` y los PNG de 64/512 se bajaron del original.

## Paleta

| Origen en el sitio | Hex | En el portal |
|---|---|---|
| `.cabecera-desktop` | `#173aaf` | `accent-700` |
| `.btn-primario` | `#1f4ce1` | `accent-600` |
| `.btn-primario:hover` | `#487fd0` | `accent-400` |
| `.stock span.alto` | `#2ca346` | `stock-alto` |
| `.stock span.medio` | `#ffc700` | `stock-medio` |
| `.stock span.bajo` | `#ff7300` | `stock-bajo` |

La escala `accent` 50–950 son tintes y sombras de esos tres azules, con los originales clavados
en 400/600/700. La escala neutra `ink` es propia y no viene del sitio.

**El azul se reserva** para la cabecera del sidebar y la columna del login; el resto es neutro
con `accent-600` para acciones primarias. Un portal de trabajo con toda la superficie azul se
vuelve difícil de leer.

## Tipografía

**Work Sans** 400/500/600/700, igual que el sitio.

## Semáforo de stock

`StockBadge` dibuja **punto de color + etiqueta**, igual que `.stock span:before` del original.
No es un chip con fondo: se lee mejor en tablas densas.

Única desviación deliberada: en modo claro el `#ffc700` sobre blanco no alcanza contraste, así
que el **texto** usa un ámbar más oscuro (`#b38b00`) y el **punto** mantiene el amarillo. En
oscuro va el original.

## Ver también

- [[arquitectura]] · [[contexto]]
