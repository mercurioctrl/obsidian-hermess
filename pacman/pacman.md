# pacman

Base de conocimiento del juego Pac-Man.

Juego de Pac-Man en JavaScript vanilla sobre HTML5 Canvas, sin frameworks ni
build step. El juego corre centrado dentro de un banner promocional de
**Pac-Man Day** (1440×360); el tablero es un mapa rectangular 2:1 (una mitad
espejada).

## Stack

- JavaScript vanilla (ES5/ES6), sin módulos
- HTML5 Canvas (renderizado con doble buffer)
- Decoración del banner en HTML/CSS (animaciones CSS)
- Sin npm, sin build — se sirve con `python3 -m http.server`

## Notas del proyecto

- [[arquitectura]] — clases, bucle principal, mapa espejado, colisión, IA, banner
- [[stack]] — tecnologías y cómo correr el proyecto
- [[changelog]] — historial de cambios
- [[contexto]] — decisiones y detalles no obvios (espejado, túneles, 8 fantasmas, banner)

---

Última sincronización: 2026-05-20
