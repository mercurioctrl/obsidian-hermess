# Feature: Incentivo Netac

**Rama:** `incentivoNetac` (ambos repos) · **Fecha:** 2026-06-17/19 · **Reemplaza** al "Incentivo Gigabyte" (oculto, no borrado)

Pestaña de dashboard que premia a los vendedores por unidades vendidas de productos **Netac**: por cada **12 unidades** de Memorias o Discos SSD el vendedor gana **USD 4**.

## Regla

- Marca **Netac = `articulo.Id_Marca = 211`** (el "companyCode 4" que se mencionó es el companyCode de esos artículos, no la marca).
- Categorías: **Memorias (`ID_FAMILIA = 1`)** y **Discos SSD (`ID_FAMILIA = 56`)**. Se excluye "Memorias USB" (42, pendrives).
- Premio = `floor(unidades / 12) * 4` USD (lineal, sin tope).
- Período: **10/06 al 24/06/2026** (configurable via env `NETAC_START_DATE` / `NETAC_END_DATE`).
- Conteo de venta **vía remitos** (mismo criterio que Gigabyte): `MS_REMITO_CABECERA` + `MS_VENTAS_REMITOS` con `ID_STATUS IN (2,4,3,11,10,13)` → `albclit` → `pedclit` → `pedclil` → `articulo`, filtrando por `FECHA_REMITO`.

> A diferencia de Gigabyte, **no usa** la tabla de config `dynamicGoalsSellers` (regla fija).

## Backend — `api-rest-pedidos-laravel`

Endpoints (en `routes/api.php`):
- **`GET /v1/objectives/netacIncentive`** → ranking de vendedores con unidades, premio USD, `completedSets`, `unitsToNext`, `position`, más `period`, `rule` y `totals`.
  - `ObjectivesController::GetNetacIncentive` → `ObjectivesService::GetNetacIncentive` (calcula premio) → `ObjectivesRepository::GetNetacIncentive($start,$end)`.
- **`GET /v1/objectives/netacIncentive/sellers/{sellerId}`** → detalle por línea de venta (pedido, fecha, cliente, producto, categoría, unidades) que compone el total del vendedor, via `pedclit`/`pedclil`.
  - `ObjectivesController::GetNetacIncentiveDetail` → `ObjectivesService::GetNetacIncentiveDetail` → `ObjectivesRepository::GetNetacIncentiveDetail`.

## Frontend — `pedidos-web-app-v1`

- `pages/dashboard/incentivoNetac.vue` — header con la regla + período, `a-statistic` de totales, tabla rankeada (posición, vendedor, unidades, premio USD, barra de progreso al próximo premio). **Vendedor y Unidades clickeables** abren el modal de detalle (Pedido, Fecha, Cliente, Producto, Categoría, Unid.).
- `components/Table/TabMenuDashboard.vue` — ítem Gigabyte **comentado**, agregado `dashboard-incentivoNetac`.
- `layouts/basic.vue` — ítem sidebar Gigabyte `visible:false`, agregado Netac `visible:true`.

## Git

| Repo | Development/development | Gamma/gamma |
|---|---|---|
| Backend | merge PRs `#1548`/`#1549` (`7275ca11`, `00839f94`) | cherry-pick `d7dc5ce2` + `7b88cd21` |
| Frontend | merge PRs | cherry-pick `de0a3d3` + `39f0967` |

Identidad de commits: `Catriel <catrielmercurio@gmail.com>`.

## Deploy
- Backend: rutas nuevas → `php artisan route:clear && config:clear`.
- Frontend: rebuild (`API_HOST` se bakea en build).

## Datos de la base (verificados)
- Netac articulos: 49 en Memorias, 21 en Discos SSD (todos companyCode 4).
- Prueba período 10–24/06/2026: 306 unidades totales, USD 88 en premios (Natalia 128u→USD40, Andrea 65u→USD20, ...).

## Ver también
- [[feature-ranking-vendedores]] — otra feature de dashboard de la misma tanda
- [[relacion-tablas-ped-alb]] — pedclit/pedclil/albclit (conteo de venta por remitos)
- [[relacion-tablas-articulo-stocks]] — articulo (Id_Marca, ID_FAMILIA)
- [[changelog#2026-06-17 — Ranking de vendedores (travel miles) + Incentivo Netac]]
