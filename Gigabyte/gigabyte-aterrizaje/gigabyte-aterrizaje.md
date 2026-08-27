# gigabyte-aterrizaje

Sitio de aterrizaje / **catálogo GIGABYTE** tipo e-commerce **sin compra**: navegar, buscar y ver la ficha de productos con sus distintos vendedores, precio en ARS y link directo a la web de cada uno. Los datos salen de la API **BluPartPicker**, filtrados a `fabricante=Gigabyte` + whitelist de resellers.

## Resumen

- **Tipo:** app Nuxt 3 SSR (no es estática). Server routes hacen de proxy contra partpicker y ocultan la API key.
- **Marca:** GIGABYTE / AORUS — negro + naranja `#f96f1e`, tipografía Rajdhani/Chakra Petch, cards angulares.
- **Catálogo:** ~336 productos Gigabyte agrupados por `oracular_sku` (modelo 1 producto → N vendedores). Precios ya en ARS.
- **Resellers activos (7):** VENEX, MAXIMUS, MEXX, ARMYTECH, FULL HARD, GAMING CITY, HARDCORE. Pendientes (no existen como source): RETEC, COMPUFAN.
- **Features:** búsqueda + filtros (categoría/vendedor/stock) + orden + paginación; ficha con tabla de vendedores; logo oficial; iconos de categoría; **tema claro/oscuro**; normalización de fondos de imagen.
- **Repo:** `git@github.com:BluIncStudio/giga-partpicker.git` (rama `main`).
- **Local:** `/var/www/gigabyte/gigabyte-aterrizaje/`.

## Notas

- [[arquitectura]] — proxy, agrupación por `oracular_sku`, caché, endpoints internos, páginas.
- [[stack]] — Nuxt 3, Tailwind (PostCSS nativo), Node 20, dependencias.
- [[design-system]] — paleta, tokens de tema (CSS vars), tipografía, componentes, logo/iconos.
- [[api-partpicker]] — endpoints usados, auth y mapeo de resellers a sources.
- [[contexto]] — decisiones del usuario, reglas de negocio, gotchas.
- [[changelog]] — registro de lo trabajado por fecha.
- [[memoria]] — espejo de la memoria de Claude del proyecto.

## Ver también

- [[Gigabyte]]
- [[informe-landing/informe-landing|informe-landing]] — deck de paid media del mismo cliente (fase previa/paralela).
- [[gigaErp/gigaErp|gigaErp]] — ERP interno; también consume partpicker.
- [[BluPartPicker]] — la API de datos.

_Última sincronización: 2026-08-27_
