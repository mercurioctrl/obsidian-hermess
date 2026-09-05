# Changelog

Parte de [[portal]].

> El repo se creó el 2026-09-01. Las entradas anteriores a esa fecha se registraron por sesión
> de trabajo, porque el código todavía no estaba versionado.

## 2026-09-01

**Repositorio en GitHub** — `git init` y primer commit (67 archivos, 19.730 líneas) en
[New-Bytes/nbelectric-portal](https://github.com/New-Bytes/nbelectric-portal), privado, rama
`main`.

El `.gitignore` de la raíz **excluye `sitio-api-rest-v3/`**: es un clon del repo del backend, con
su propio remote, y su `app/.env-example` trae credenciales reales (base, mailers, token de
static) más el secreto JWT hardcodeado en `TokenManager.php:10`. Antes de commitear se escaneó
el contenido staged buscando esos patrones. Ver [[contexto#El backend queda fuera del repo]].

Se agregó la sección `## Obsidian` al `CLAUDE.md` del proyecto, así esta sincronización ya no
pregunta la carpeta.

## 2026-08-29

**Marca NBE** — logo, paleta, tipografía y favicon extraídos de `nbe.com.ar`. `NbeLogo.vue` con
variantes full/mark; escala `accent` derivada de los tres azules del sitio; Work Sans;
`StockBadge` reescrito como punto + etiqueta. Ver [[marca]].

**Configuración de secciones** — la navegación salió del sidebar a un registro único
(`composables/useSections.ts`) del que ahora dependen el menú, un middleware que bloquea rutas y
los enlaces cruzados. Activables con `NUXT_PUBLIC_SECTIONS` / `_OFF`. Vista de diagnóstico en Mi
cuenta. Ver [[configuracion]].

**Cotización de envío** — se incorporó `GET /carrito/calcularEnvioPara/{cp}/{idDirCli}`: el
checkout muestra una tarjeta por transporte con precio y plazo, en vez de un combo sin costo. Se
sumó también el **interés del medio de pago**, que se cobraba y no se mostraba. El resumen
desglosa mercadería / envío / interés / total, replicando el orden en que el backend los aplica.

**Apuntado a la API de NBE** — `api.nbe.com.ar/v1` (companyCode 9). Verificadas las 18 rutas del
portal contra esa instancia. Como el catálogo son solo 1.342 artículos, se eliminó el fallback a
"últimos ingresos" y ahora se carga completo con paginación en cliente.

**Fix del preflight** — el catálogo fallaba con `Failed to fetch`: `ofetch` se comía la barra
final y el preflight OPTIONS daba 404. Se agregó `useApi().catalogue()`. Ver
[[api-nbe#La barra final]].

**Secciones nuevas** — recuperación de contraseña, sub-usuarios, direcciones, compras frecuentes
y postventa de consulta.

**Lista de precios y comprobantes** — con export Excel/CSV y PDF respectivamente.

**Documentación** — se creó `docs/` en el repo (contexto, arquitectura, api, configuración,
marca, estado) más `CLAUDE.md` como memoria del proyecto.

## 2026-08-28

**MVP del pedido** — scaffold de Nuxt 3 SPA + Tailwind + Pinia, layout con sidebar de 3 grupos y
chip de cliente, login con JWT, catálogo con búsqueda y filtros, ficha de artículo, carrito
persistente, checkout con OC y comentario, y mis pedidos con detalle expandible.
