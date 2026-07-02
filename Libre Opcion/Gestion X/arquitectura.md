---
tipo: arquitectura
proyecto: LibreOpción
area: Gestión / Datos
creado: 2026-07-01
tags:
  - libreopcion
  - arquitectura
  - datos
  - pipeline
---

# Arquitectura — Gestión X

`Gestión X` no es código: es **estrategia + datos + entregables web**. Esta nota mapea los **pipelines de datos** (scripts Python que transforman CSV/reportes en JS/MD) y los **entregables HTML**. Las convenciones de la bóveda viven en el `CLAUDE.md` raíz; los caveats de datos, en el `CLAUDE.md` de esta carpeta.

## Pipelines de datos

Tres pipelines independientes, cada uno con su generador reproducible:

### 1 · Cubo de datos (12 meses)
`meses/*.csv` → `gen-cube-data.py` → `cube-data.js` → [[Cubo-Datos-LibreOpcion.html|Cubo de Datos]]

Deriva **categoría** y **marca** desde el texto de la descripción (funciones `categoria()` y `marca()`/`BRANDS`). Emite `MONTHS`, `SKUS`, `FACTS` (item-group) y `OPS` (grilla). App vanilla JS que pivotea (tabla dinámica + evolución mensual). **Dos granos que no se cruzan** (item-group vs grilla): solo comparten Mes y Rentabilidad.

### 2 · Combos y PCs armables (vs Compra Gamer)
`items/catalogoDistribuidoraJulio.csv` + `adjuntos/…CompraGamer.xlsx` → `gen-combos-match.py` → [[combos-armables]]

Replica los kits de actualización y PCs de escritorio de [[09 - Estudio de Catálogo - Compra Gamer|Compra Gamer]] con el stock propio. Parsea CPU/mother/RAM/SSD/GPU del texto, matchea contra el catálogo (exacto/sustituto/lejano/falta) y arma cada combo a **costo+utilidad**. Reglas: RAM nunca cruza generación de DDR (usa varios módulos); fuente por wattaje (evita SFX en ATX); CPU sustituto por cercanía de `TIER`. Salida embebida en la [[Plan-Estrategico-LibreOpcion-Marca.html|landing Marca]] (sección "arrancar ya"). Alimenta [[16 - Armador, Combos Dinamicos y Builds de la Comunidad]].

### 3 · Ventas mensuales + proyección de compra
`benefits-report.php` (gestion.saftel.com, 1 POST por mes) → `items/ventas-por-sku-2026.csv` → `gen-ventas-forecast.py` → `ventas-data.js` → [[Ventas-y-Proyeccion-LibreOpcion.html|Ventas & Proyección]]

Agrega ventas por **SKU × mes** (ene–jun 2026), deriva categoría/marca (mismas funciones que el cubo) y calcula la **proyección de compra 6 meses adelante**. Dashboard navegable mes a mes (Chart.js) + tabla de compra jul–dic + tabla agrupada por marca. Detalle del método y del origen de datos en [[contexto]].

## Entregables web

Todos en marca LibreOpción (azul `#0044a4`, naranja `#ff5a36`, Roboto Condensed + Inter, logo en `assets/`, **emojis planos monocromos vía Noto Emoji**):

- [[Plan-Estrategico-LibreOpcion-Marca.html|Plan Estratégico (Marca)]] — versión recomendada para socios; hub que linkea al cubo y al dashboard de ventas/proyección.
- [[Cubo-Datos-LibreOpcion.html|Cubo de Datos]] — pivot OLAP interactivo.
- [[Ventas-y-Proyeccion-LibreOpcion.html|Ventas & Proyección]] — ventas mes a mes + compra proyectada.
- Variantes de estilo del plan: `…-SaaS.html` (dashboard claro) y `…​.html` (deck oscuro).

## Ver también
- [[contexto]] — orígenes de datos, decisiones y método de forecast
- [[00 - Índice Gestión X]]
