# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

`Gestión X` es la carpeta de **estrategia de negocio de LibreOpción** (marketplace/importador de tecnología en Argentina) dentro de la bóveda de Obsidian. No es código: combina **notas de estrategia (MOC)**, **datos reales de ventas** (`meses/`) y **entregables web** (sitios HTML + un cubo de datos interactivo). Las convenciones de la bóveda (wikilinks, índices, idioma) viven en el `CLAUDE.md` raíz del vault — no se repiten acá.

## Comandos

No hay build/test/lint. Las únicas operaciones reales:

```bash
# Regenerar los datos del cubo desde los CSV de meses/ (correr si cambia meses/)
python3 gen-cube-data.py            # escribe cube-data.js

# Previsualizar un entregable (macOS)
open Cubo-Datos-LibreOpcion.html
open Plan-Estrategico-LibreOpcion-Marca.html
```

Los HTML son **autocontenidos salvo**: Chart.js por CDN, `cube-data.js` (solo el cubo) y la carpeta `assets/` (logos). Para compartir un HTML hay que llevar también esos archivos relativos.

## Arquitectura

### Pipeline de datos del cubo
`meses/*.csv` → `gen-cube-data.py` → `cube-data.js` → `Cubo-Datos-LibreOpcion.html`

`gen-cube-data.py` deriva **categoría** y **marca** desde el texto de la descripción (no hay columnas limpias; ver las funciones `categoria()` y `BRANDS`/`marca()`), y emite 4 consts: `MONTHS`, `SKUS={sku:[detalle,categoria,marca]}`, `FACTS=[[mes,sku,cantidad,venta,costo,renta]]` (item-group) y `OPS` (grilla pre-agregada por mes×pago×envío×vendedor). El cubo `Cubo-Datos-LibreOpcion.html` es una app vanilla JS que pivotea estos arrays (tabla dinámica + explorador de evolución mensual).

### Dos granos de datos que NO se pueden cruzar (lo más importante)
- **`item-group_*.csv`** = producto × mes → tiene SKU, categoría, **marca**, costo, renta, cantidad. **No** tiene medio de pago/envío.
- **`grilla_*.csv`** = orden × mes → tiene **pago, envío, vendedor**, renta. **No** tiene SKU/categoría.

No hay clave común producto↔orden, así que el cubo (y cualquier análisis) tiene **dos caras** que solo comparten Mes y Rentabilidad. No intentar unirlas.

### Las notas (MOC numerado)
`00 - Índice Gestión X.md` es el **hub**: toda nota nueva debe agregarse ahí y cross-linkearse. Las **01–09** son la investigación original; las **10–19** son la **estrategia revisada con datos reales** (la columna vertebral del plan vigente). Varias notas **revisan** decisiones anteriores (ej. la 10 reemplaza el posicionamiento de precio de la 06; la 18 corrigió un borrador propio). Al cambiar una decisión: agregar un callout de revisión, **no** sobrescribir el razonamiento previo en silencio.

### Entregables web
Tres versiones del mismo plan + el cubo, todas en marca LibreOpción (azul `#0044a4`, naranja `#ff5a36`, verde/amarillo, fuente Roboto Condensed; header/footer negros con el logo de `assets/`):
- `Plan-Estrategico-LibreOpcion-Marca.html` — versión recomendada para socios (incluye link al cubo).
- `...-SaaS.html` (dashboard claro, pixel-charts) y `...html` (deck oscuro, Chart.js) — variantes de estilo.

## Caveats de los datos (releer antes de analizar)

- **Anclar el análisis en el ÚLTIMO TRIMESTRE (mar–may 2026), no en los 12 meses.** El promedio anual está contaminado por el período de pérdidas de 2025 (margen negativo, RAM/SSD vendidos a pérdida); ese problema ya está curado. En Argentina el contexto cambia rápido.
- En `item-group`, las líneas **`COSTO FINANCIERO`** (ingreso por cuotas con interés) y **`SERVICIO DE TRANSPORTE`/`FLETE`** (costo del envío gratis) **no son productos** — excluirlas para margen de producto limpio (el generador las marca categoría `· ...` y marca `—`).
- Los valores de los CSV están en **u$s**; la columna `Cotizacion` da el tipo de cambio ARS.
- **Encoding mixto**: los `grilla_*` son UTF-8, otros archivos latin-1 → siempre intentar UTF-8 con fallback a latin-1.
- El **proveedor** (≈90% LASET, intra-grupo) se descartó como dimensión de exploración a pedido del usuario: usar **marca**.
