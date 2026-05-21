# changelog

Registro de lo trabajado en el proyecto.

## 2026-05-20

Sesión enfocada en bugs del mapa espejado, duplicar los fantasmas y convertir
el juego en un banner de Pac-Man Day.

### Bugs del mapa espejado y 8 fantasmas

- **fix:** corredores del lado derecho desalineados. El playable de `path.png`
  (335px) es 1px más angosto que la mitad gráfica (336px), y el espejo del path
  se pegaba en la posición equivocada. Se reposicionó el espejo para que respete
  la simetría del sprite (eje del juego en x=336). — `2346f7f`
- **fix:** los túneles laterales — Pac-Man "desaparecía para siempre" al cruzar.
  El espejo del path no cubría el tramo de túnel derecho. Ahora se espeja el
  `path.png` completo (con sus márgenes/datos de túnel) y se recorta al pegarlo.
  Además, el wrap derecho dispara al alcanzar `x = SCREEN_WIDTH`. — `2346f7f`
- **feat:** 8 fantasmas (4 por lado). Se refactorizaron los 4 fantasmas
  hardcodeados por nombre a un array `game.ghosts`, y se agregaron 4 nuevos que
  arrancan desplegados en la mitad derecha. Misma IA que los originales. — `5713eb3`

Archivos: `lib/classes/world.js`, `lib/classes/mobile.js`, `lib/classes/game.js`,
`lib/app.js`, `lib/classes/pacman.js`, `lib/classes/inky.js`,
`lib/config/config.js`.

### Banner jugable de Pac-Man Day

- **feat:** el juego se convirtió en un banner promocional de **1440×360** para
  el Pac-Man Day (22 de mayo). El juego queda centrado (650×360, sin distorsión)
  y a los costados hay paneles de branding en HTML/CSS: logo "PAC-MAN DAY",
  fecha, decoración animada (Pac-Man masticando, fantasmas flotantes y pellets,
  todo CSS) y botón "JUGAR AHORA". El marcador y las vidas se movieron al panel
  derecho. — `6c0f508`
- `resize()` ahora fija el canvas al tamaño del juego y escala el banner entero
  con `transform: scale()` para que entre en la ventana.

Archivos: `index.html`, `style.css`, `lib/config/config.js`, `lib/app.js`.

- **chore:** se vinculó el proyecto con la bóveda de Obsidian (carpeta `pacman`),
  agregando la sección correspondiente al `CLAUDE.md`. — `27d0c30`

### Estado previo (commits anteriores)

- `d634160` — Rediseño del tablero a formato banner: mapa rectangular 2:1
  (introdujo el espejado de mitades que originó los bugs de arriba).
- `4f566d1` — reset de direcciones de los fantasmas al resetear el juego.
- `b9986fb` / `f7594ba` — idas y vueltas entre `setInterval` y
  `requestAnimationFrame` para el bucle principal.
- `0a27161` / `1fce78f` — controles táctiles (swipe) y su config.

## Ver también

- [[contexto]] — el porqué detrás de estos cambios
- [[arquitectura]] — estructura del código
- [[pacman]] — índice del proyecto
