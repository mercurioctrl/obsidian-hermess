# Módulo: Dashboard

Pantalla de inicio del ERP (`frontend/pages/index.vue`, endpoint `GET /api/dashboard` →
`DashboardController`). En **2026-09-08** se **rediseñó** a pedido del usuario: se quitó casi
todo y quedó enfocado en operación diaria + visibilidad de POEs.

## Estado actual (post 2026-09-08)

La página muestra **solo**:
1. **Tareas — estado actual** + **Próximos 14 días** (la fila que ya existía). Ver [[modulos/tareas]].
2. **POEs subidas** — tabla nueva con las evidencias que cargaron los partners desde el link
   del reclamo. Columnas: **Reseller · Acción (envío) · POEs · Última subida**.

Se **eliminaron** del dashboard: KPIs (clientes/ingresos/gastos/resultado/cobrado/deuda),
gráfico Ingresos vs Gastos (12 meses), últimas órdenes de venta, cuentas corrientes/deudores,
ventas por estado + top clientes, y productos por distribuidor (con sus helpers de script).
El endpoint `/dashboard` sigue devolviendo todos esos bloques (por si se reusan), solo que el
front ya no los pinta.

## Tabla de POEs subidas

- **Datos** (`poes_subidas` en `DashboardController`): sobre `reclamo_evidencia_archivos` JOIN
  `reclamos_evidencia`, agrupado **en PHP** por empresa+campaña (no `GROUP BY`, para poder
  incluir el detalle de archivos). Cada fila trae `empresa`, `campania`, `accion`, `archivos`
  (conteo), `ultima` (última subida) y **`files[]`** con `{nombre, url, subido_en}`.
- **Columna "Acción (envío)"**: resuelve el título de la [[modulos/campanas|acción de marketing]]
  vía `acciones_marketing.envio_campania = reclamos_evidencia.campania`, **solo si la columna
  existe** (`Schema::hasColumn`); si no (la mig 0116 no está aplicada en dev), cae al slug de la
  campaña. Linkea a `/envios/{campania}`.
- **Descarga (badge 📎)**: el chip de POEs es un **botón**. Con **1 archivo** descarga directo;
  con **más de uno** abre un **modal** (`<Modal>`) con la lista para elegir cuál bajar.
  La descarga es un `<a download target=_blank>`; cross-origin (S3 en otro dominio) puede abrir
  en pestaña nueva en vez de forzar la bajada.

Todo el circuito de POEs (reclamo + subida por token + historial) vive en
[[modulos/reclamo-evidencias]] / [[modulos/envios]].

## Historia previa

El dashboard original (2026-06) tenía 6 KPIs + pixel bar chart + tareas + calendario + OV +
deudores + productos por distri. Ese diseño quedó documentado en [[gigaErp#Estado actual (2026-06-11) — commit `d08b3a4`|el índice]].

## Ver también

- [[modulos/reclamo-evidencias]] · [[modulos/envios]] — de dónde salen las POEs
- [[modulos/tareas]] — la otra mitad del dashboard
- [[changelog#2026-09-08 — Dashboard reducido + descarga de POEs|changelog]] · [[troubleshooting]]
