# Reporte — Estado de resellers (Paid Media)

Entregable **separado** del deck [[informe-landing]] y distinto de [[landing-ejemplo-ads]]: mientras esa muestra *cómo se verán* los anuncios, esta es un **tablero de estado** que le reporta al cliente (GIGABYTE) **qué se trabajó con cada reseller** y en qué punto del setup está cada uno (Meta Ads + Google Ads).

- **Ubicación:** `/var/www/Informe gigabyte/Reportes Ads/reporte-resellers.html` (autocontenida, assets locales en `Reportes Ads/assets/` — logos GIGABYTE/40/AORUS).
- **Fuente de datos:** `Reportes Ads/BLU X GIGABYTE.xlsx` (planilla de control, más completa que el CSV que alimenta [[landing-ejemplo-ads]]). Se extrajeron las 17 columnas: quarter, campaña, país, reseller, producto foco, presupuesto, GTM (check/implementado), solicitud/conexión de FB, Meta y Google corriendo con **fecha de inicio** (fechas seriales de Excel convertidas a calendario) y ciclo de 30 días.
- **Estética:** AORUS **en modo claro** (a pedido del usuario) — fondo `#eceef1`, paneles blancos, tinta charcoal `#141417`, acento naranja `#FF6400`. Se clonó el design system de [[landing-ejemplo-ads]] (fuentes Rajdhani/Chakra Petch/Titillium, esquinas en bisel, etiquetas verticales de sección, grilla de fondo) invertido a claro. Regla de marca respetada: solo naranja/tinta/grises, **sin verde ni rojo** para estados. Footer oscuro para anclar la página y que los logos blancos se vean nativos.

## Modelo de estado (3 estados, derivados de la planilla)

El avance se muestra como un **pipeline de 4 pasos**: `GTM → Facebook Business → Meta Ads → Google Ads` (nodo naranja = listo, hueco = pendiente).

| Estado | Criterio | Resellers |
|--------|----------|-----------|
| **En vivo** (5) | Meta + Google corriendo, setup completo | MMSOFT·UY, Sampler·UY, Thot·UY, Compumar·AR, Compufan·AR |
| **En preparación** (2) | Parte del setup listo, falta salir al aire | MegaBytes·CL (FB conectado, falta GTM+salir), Armytech·AR (GTM+landing listos, falta FB+pauta) |
| **Pendiente** (2) | Por definir accesos/presupuesto | NoXie Store·AR (solicitud FB enviada), Compragamer·AR (presupuesto a definir) |

- **9 resellers** en total · **3 países** (UY/CL/AR) · **2 campañas** (Familia GIGA40, Laptops) · **US$ 270/mes** por reseller con presupuesto definido.
- Fechas de inicio reales cargadas por reseller (ej. Sampler Meta 16/07, Compumar 22/07).

## Estructura de la página

Hero → strip de 4 números → 3 cards de estado → **grid de cards por reseller** (con filtro por estado: Todos/En vivo/En preparación/Pendiente) → footer. Cada card: avatar con iniciales, badge de estado, foco, inversión, pipeline de 4 nodos con fechas, y links a Página Meta + Landing.

## Decisiones (2026-07-28)

- **Simplificación** a pedido del usuario: se quitó la tabla-anexo (duplicaba las cards), la leyenda de 4 pasos y el filtro por campaña; se aligeró cada card. La página pasó de ~4600px a ~3000px.
- **Fix de márgenes en PDF:** el `@page{margin}` se ignora cuando el diálogo de impresión usa "Márgenes: Ninguno", así que el margen lateral se metió como **padding real del contenido** (`.wrap` + `margin` lateral en header y strip). Verificado generando el PDF con Chrome headless (5 páginas, márgenes parejos). Ver [[contexto]].
- Validación visual con `google-chrome --headless --screenshot` + PDF con `--print-to-pdf` en cada iteración.

## Ver también
- [[informe-landing]] · [[contexto]] · [[changelog]]
- [[landing-ejemplo-ads]] — entregable hermano: la vista previa de los anuncios (la misma campaña, en modo oscuro). Este reporte es el **estado operativo**; esa landing es la **creativa**.
