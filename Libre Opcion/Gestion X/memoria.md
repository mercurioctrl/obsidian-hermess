---
tipo: memoria
proyecto: LibreOpción
area: Gestión / Datos
creado: 2026-07-01
tags:
  - libreopcion
  - memoria
---

# Memoria — Gestión X

Consolidación de la memoria operativa de Claude para esta carpeta (espejo de `~/.claude/projects/-var-www-obsidian-hermess/memory/`). Hechos durables para retomar el proyecto sin releer todo.

## Referencia — origen de datos
- **Reporte de ventas Saftel:** `POST gestion.saftel.com/procesar/reports/benefits-report.php`, cookie `PHPSESSID` (caduca), params `fechap`/`fecha1p` (`DD-MM-YYYY`), `empresa=LibreOpcion`, `porp=3`, `TYPE=VER`. Un request por mes → ventas por SKU. 13 celdas/fila para 10 headers (mapeo en [[contexto#Reporte de ventas por SKU gestion saftel com|contexto]]).

## Proyecto — pipelines y método
- **3 pipelines** reproducibles: cubo (`gen-cube-data.py`), combos (`gen-combos-match.py`), ventas+proyección (`gen-ventas-forecast.py`). Ver [[arquitectura]].
- **Forecast de compra:** base = promedio ponderado del último trimestre × crecimiento mensual por categoría (±10-15%). **Demanda esperada, no descuenta stock** (pendiente: compra neta). Total 6m ≈ u$s 1,04M.
- **Hueco gama media AM5:** línea propia toda X3D → comprar 1-2 CPUs AM5 baratos (7600/8500G/8600G). Anclar análisis al **último trimestre**.

## Feedback — estilo de entregables
- HTML de marca: azul `#0044a4`, naranja `#ff5a36`, Roboto Condensed + Inter, logo en `assets/`, Chart.js.
- **Emojis planos monocromos** vía fuente `Noto Emoji` (no los 3D del sistema): consistentes en cualquier dispositivo y autocontenidos. Aplicar en todo HTML nuevo de la marca.

## Ver también
- [[arquitectura]] · [[contexto]] · [[changelog]] · [[00 - Índice Gestión X]]
