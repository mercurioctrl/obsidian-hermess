---
tipo: contexto
proyecto: LibreOpción
area: Gestión / Datos
creado: 2026-07-01
tags:
  - libreopcion
  - contexto
  - datos
  - decisiones
---

# Contexto — Gestión X

Reglas de negocio, orígenes de datos y decisiones que no se leen del código. Complementa [[arquitectura]] y el `CLAUDE.md` de la carpeta.

## Orígenes de datos

### Reporte de ventas por SKU (gestion.saftel.com)
El sistema de gestión **Saftel** expone `benefits-report.php`, que devuelve **ventas por SKU** de un rango de fechas (HTML con tabla `#grid-basic`). Es la fuente de `items/ventas-por-sku-2026.csv` y del dashboard de ventas/proyección.

- **Endpoint:** `POST https://gestion.saftel.com/procesar/reports/benefits-report.php`
- **Auth:** cookie `PHPSESSID` (sesión del navegador logueado; caduca — hay que refrescarla).
- **Params clave:** `fechap`/`fecha1p` = rango `DD-MM-YYYY`, `porp=3`, `empresa=LibreOpcion`, `TYPE=VER`, `async=1`.
- **Un request por mes.** Se bajaron ene–jun 2026 (leap: feb tiene 28 en 2026).
- **Columnas reales:** la fila trae 13 celdas para 10 headers. Mapeo correcto: ID · Ultimo Ingreso · ID Fab · Detalle · Cantidad · **Costo U (unit)** · **Costo Total** · **Venta Total** · **Ganancia** · **Benf/Cost %** · **Benf/Vent %** · Cotización · Proveedor.
- Totales de cabecera: COSTO, VENTA, GANANCIA, BEN C (s/costo), BEN V (s/venta), COMP (en ARS).

### Catálogo de la distribuidora
`items/catalogoDistribuidoraJulio.csv` (~1.367 items, NB/LASET). Trae `PRECIO USD CON UTILIDAD` (costo+utilidad cargada). Base de los [[combos-armables|combos]].

## Método de proyección de compra (forecast)

Definido en `gen-ventas-forecast.py`. Objetivo: **cuánto comprar de cada SKU mes a mes, 6 meses adelante** (jul–dic 2026).

- **Base por SKU** = promedio ponderado del **último trimestre** (abr·may·jun con peso 1·2·3 hacia junio). Se ancla al último trimestre porque en Argentina el contexto cambia rápido (mismo criterio que el FODA, ver [[18 - Analisis Performance Ventas 12 Meses (FODA)]]).
- **Crecimiento** = tasa mensual compuesta **por categoría** (no por SKU, para bajar ruido), acotada a **±10-15%/mes**.
- **Proyección** = `base × g^k` para k=1..6, redondeado hacia arriba (compra).
- **Se descartan** SKUs sin recurrencia (vendidos en <2 meses) y las líneas no-producto (`· Financiero`, `· Envío (costo)`).
- **Resultado:** ~563 SKUs, compra total 6m ≈ **u$s 1,04M** (jul u$s157k → dic u$s193k).

> [!warning] Limitación conocida
> Es **demanda esperada**, no orden de compra final: **no descuenta el stock actual** ni mínimos de proveedor. Pendiente: si aparece el stock por SKU, convertir a **compra neta** (demanda − stock).

## Decisiones de la sesión (2026-07-01)

- **Hueco de gama media AM5:** la línea AM5 propia es toda alta gama X3D; los combos de Ryzen no-X3D (7600, 8500G/8600G/8700G, 9600X, 9700X) solo se cubren con un 7800X3D (más caro). **Comprar 1-2 CPUs AM5 baratos** para competir. Ver [[combos-armables]] y [[16 - Armador, Combos Dinamicos y Builds de la Comunidad]].
- **Combos de 3 familias** replicables ya: CPU+Mother (26), GPU+Fuente (3), Gabinete+Fuente (2), + variante CPU+Mother+RAM. Más 15 PCs armadas (oficina → gamer tope).
- **Emojis planos:** todos los entregables HTML usan **Noto Emoji** (plano monocromo, toma el color del texto) para verse igual en cualquier dispositivo y no depender del emoji 3D del sistema.

## Pendientes / próximos pasos
- Convertir la proyección en **orden de compra neta** (restar stock actual).
- Opcional: forecast **por SKU** (más fino) o con estacionalidad, en vez de por categoría.
- Sumar más meses al dashboard (mismo curl cambiando fechas + `MONTHS` en el generador).
- Cruzar ventas reales vs [[combos-armables|combos de arranque]] para ver qué ya se vende suelto y a qué margen.

## Ver también
- [[arquitectura]] · [[memoria]] · [[changelog]] · [[combos-armables]] · [[09 - Estudio de Catálogo - Compra Gamer]] · [[00 - Índice Gestión X]]
