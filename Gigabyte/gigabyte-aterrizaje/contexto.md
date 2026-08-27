# Contexto

Decisiones del usuario, reglas de negocio y aprendizajes de [[gigabyte-aterrizaje/gigabyte-aterrizaje|gigabyte-aterrizaje]].

## Reglas de negocio

- Es un sitio **informativo, sin compra**: cada producto muestra sus vendedores y enlaza a la web de cada uno (`url_ficha`), no se procesan pedidos.
- Solo marca **GIGABYTE** (`fabricante=Gigabyte`).
- Solo estos vendedores (whitelist): VENEX, MAXIMUS, MEXX, ARMYTECH, FULL HARD, GAMING CITY, HARDCORE COMPUTACION. **RETEC** y **COMPUFAN** los pidió el cliente pero **no existen** como fuente en partpicker → quedan pre-configurados con `enabled:false` ("dejalos por ahora").
- Estética objetivo definida por el usuario: **AORUS** (aorus.com/graphics-cards). AORUS bloquea scraping (403), así que la paleta se replicó de memoria (negro + naranja).

## Decisiones tomadas en sesión

- Stack **Nuxt 3 + Tailwind** (elegido por el usuario, coincide con gigaErp).
- Catálogo **Gigabyte completo** (no solo GPUs).
- Ficha con **solo los 7 resellers** (no mostrar mayoristas).
- **Fondos de imagen**: elegida la opción "panel claro + `mix-blend-multiply`" para eliminar los recuadros blancos.
- **Logo oficial** GIGABYTE en el header (reemplazó el monograma "G") + iconos de categoría de línea estilo AORUS.
- **Tema claro/oscuro** con conmutador.
- **Git**: subir a `git@github.com:BluIncStudio/giga-partpicker.git` **sin firma de Claude** (autor Catriel).

## Aprendizajes / gotchas

- Node 18 no alcanza para Nuxt 3.17 → se instaló Node 20 portable.
- El módulo `@nuxtjs/tailwindcss` rompía con error de `import.meta` en postcss → se usó PostCSS nativo.
- Bug de filtros: el cliente mandaba `categoria=undefined` (string) → 0 resultados. Se arregló en cliente (query limpio) y server (ignora `"undefined"`/`"null"`).
- Bug del toggle de tema: `useCookie` suelto no sincroniza entre componentes → mover el estado a `useState`.

## Próximos pasos posibles

- Dockerfile (aún no en el repo).
- Sumar RETEC/COMPUFAN cuando existan como source.
- Opción: respetar `prefers-color-scheme` en la primera visita.

## Ver también

- [[gigabyte-aterrizaje/gigabyte-aterrizaje|gigabyte-aterrizaje]] · [[gigabyte-aterrizaje/arquitectura|arquitectura]] · [[gigabyte-aterrizaje/changelog|changelog]]
