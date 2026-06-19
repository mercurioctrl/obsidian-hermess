# Feature: Ranking de vendedores (travel miles → puntos)

**Ramas:** `rankingTravelVendedores` (base, ambos repos) + `ranking-vendedores-puntos` (ajuste, solo front) · **Fecha:** 2026-06-17/19

Pestaña **"Ranking de vendedores"** en el dashboard, junto a "Ranking de aceleración". Rankea a los vendedores por la suma total de **puntos** (travel miles) que generan **sus clientes** al cumplir objetivos del juego **NB Travel Mundial de resellers**. Al hacer clic en un vendedor se abre un modal con el desglose por cumplimiento.

## Regla

Por vendedor, sumar `miles` de la tabla `[NB_WEB].[dbo].[travelMiles]` de todos los clientes que le pertenecen. Une `travelMiles.clientId → clientes.ID_CLIENTE → clientes.ID_VENDEDOR → agentes.ID_VENDEDOR`. No filtra por grupo (a diferencia del ranking de clientes, que mezcla `acelerator` + millas).

## Backend — `api-rest-pedidos-laravel`

Endpoints (en `routes/api.php`):
- **`GET /v1/clientsObjectives/acelerateRankingSellers`** → ranking por total de puntos.
  - `ObjectivesController::GetSellerAceleratorRanking` → `ObjectivesService::GetSellerAceleratorRanking` (castea, ordena desc, asigna `position`) → `ObjectivesRepository::GetSellerAceleratorRanking` (suma `miles` agrupando por vendedor; `LTRIM/RTRIM` por partes en el nombre + `CONCAT` por los espacios sucios de `cnbrage`/`capeage`).
- **`GET /v1/clientsObjectives/sellers/{sellerId}/travelMiles`** → desglose por cumplimiento.
  - `ObjectivesController::GetSellerTravelMiles` → `TravelMilesObjectivesService::getSellerTravelMiles` → `TravelMilesObjectivesRepository::getSellerMilesBreakdown`.
  - Devuelve **una fila por cumplimiento** (no agrupado): cliente, objetivo (via `travelMilesObjectives`), descripción puntual, `miles` y `completedAt` (`travelMiles.createdAt`), **ordenado por fecha desc**. La suma coincide con el total del ranking.

### Esquema relevante
- `travelMiles`: `clientId`, `miles`, `objetiveId`, `description`, `createdAt`, `yearWeek`.
- `travelMilesObjectives`: `id`, `name`, `description`, `miles`, `active` (id 99 = "El Oraculo" / prode).

## Frontend — `pedidos-web-app-v1`

- `pages/dashboard/rankingSellers.vue` — tabla (Posición, Vendedor, **Puntos**) + modal de desglose (Cliente, Objetivo, Fecha, **Puntos**). Vendedor clickeable abre el modal. Incluye un `a-alert` descriptivo del juego.
- `store/dashboard.js` — state `rankingSellers`, mutations `SET_RANKING_SELLERS`/`SET_PAGINATION_RANKING_SELLERS`, actions `getRankingSellers`/`updatePaginationRankingSellers`, getters `rankingSellers` y `columnRankingSellers`.
- `components/Table/TabMenuDashboard.vue` — ítem de menú `dashboard-rankingSellers`.

## Ajuste "Puntos" (rama `ranking-vendedores-puntos`)

- Renombrado **"Millas" → "Puntos"** en la tabla, el modal (columna, título y total).
- Agregada la descripción de la sección: *"Acá los vendedores pueden visualizar la suma total de puntos por acciones especiales realizadas en el juego NB Travel Mundial de resellers."*
- Commit front `33cd990`. Cherry-pick a `gamma`: `9c96dc1` (base, porque el front nunca había llegado a gamma) + `860ec08` (ajuste).

## Git

| Repo | Development/development | Gamma/gamma |
|---|---|---|
| Backend | `bd063bdc` (merge ff) | cherry-pick `491b00c8` |
| Frontend | base mergeada por PR | cherry-pick `9c96dc1` + `860ec08` |

> **Lección:** el front de la base se mergeó a `development` pero al principio **no** a `gamma`; la app llamaba al endpoint y daba "route could not be found" hasta mergear/cherry-pickear también el backend. Identidad de commits: `Catriel <catrielmercurio@gmail.com>`.

## Deploy
- Backend: rutas nuevas → `php artisan route:clear && config:clear`.
- Frontend: rebuild (`API_HOST` se bakea en build).

## Ver también
- [[feature-incentivo-netac]] — otra feature de dashboard de la misma tanda
- [[arquitectura]] — patrón Controller → Service → Repository
- [[changelog#2026-06-17 — Ranking de vendedores (travel miles) + Incentivo Netac]]
