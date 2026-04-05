---
jira_key: "PED-1216"
aliases: ["PED-1216"]
summary: "API - Feat - Listar marcas con fondos (totales disponibles)"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-01-05 07:51"
updated: "2026-01-12 10:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1216"
---

# PED-1216: API - Feat - Listar marcas con fondos (totales disponibles)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 07:51 |
| Actualizado | 2026-01-12 10:23 |
| Etiquetas | ninguna |
| Jira | [PED-1216](https://bluinc.atlassian.net/browse/PED-1216) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **has action item:** [[PED-1217]] APP - Feat - Dashboard de Marcas (Totales por marca)
- **is cloned by:** [[PED-1248]] API - Refactor - Listar marcas con fondos (totales disponibles) - Eliminar espacios vacíos en marcas

## Descripcion

### Qué hay que hacer

Crear un recurso que liste **marcas** (de `NB_WEB.dbo.marcas`) junto con los **totales de fondos** asociados a cada una, separados por moneda (ARS/USD) y con saldos calculados **sin vistas**.
Este endpoint resuelve el caso “quiero ver de un vistazo cuánto tengo disponible por marca” sin que el front tenga que agrupar ni paginar fondos.

---

## Endpoint

```
GET /v1/marketing/brands?activeOnly={0|1}&currencyId={1|2}&q={texto}&currentPage=1&itemsPerPage=20
```

### Parámetros (querystring)

- `activeOnly` (default `1`): si `1`, solo fondos sin vencimiento o con vencimiento futuro.


- `currencyId` (opcional): filtra a una moneda (2 ARS o  1 USD). Si no viene, devuelve ambas si existen.


- `q` (opcional): búsqueda simple sobre `marcas.referencia` (LIKE).


- `currentPage`, `itemsPerPage`: paginación por marca.



---

## Ejemplo request

```
GET /v1/marketing/brands?activeOnly=1&currentPage=1&itemsPerPage=20
```

## Ejemplo response (200)

```
{
  "pagination": {
        "total": 1293,
        "current": 3,
        "pageSize": 15
    }
  "list": [
    {
      "brandId": 12,
      "brandRef": "ASUS",
      "brandImage": "https://.../asus.png",
      "totals": {
       "1":{
          "currencyId": 1,
          "amountOriginalTotal": 5000.00,
          "allocatedTotal": 1200.00,
          "spentTotal": 600.00,
          "availableToAllocateTotal": 3800.00,
          "availableCashTotal": 4400.00
        }
      }
    },
    {
      "brandId": 18,
      "brandRef": "MSI",
      "brandImage": null,
      "totals": {
          "1":// -->la key es el currencyId 
          { 
            currencyId: 1,
            amountOriginalTotal: 2000,
            allocatedTotal: 0,
            spentTotal: 0,
            availableToAllocateTotal: 2000,
            availableCashTotal: 2000
          },
          "2": 
          {
            currencyId: 2,
            amountOriginalTotal: 1500000,
            allocatedTotal: 300000,
            spentTotal: 100000,
            availableToAllocateTotal: 1200000,
            availableCashTotal: 1400000
          }
        }
    }
  ]
}

```

---

## SQL Server (tablas involucradas)

**No se crean tablas nuevas.** Se usan:

- `NB_WEB.dbo.marcas`


- `NB_WEB.dbo.Marketing_Funds`


- `NB_WEB.dbo.Marketing_FundStats`



---

## Lógica de cálculo

Por cada marca y moneda:

- `amountOriginalTotal = SUM(Funds.AmountOriginal)`


- `allocatedTotal = SUM(FundStats.AllocatedTotal)`


- `spentTotal = SUM(FundStats.SpentTotal)`


- `availableToAllocateTotal = SUM(Funds.AmountOriginal - FundStats.AllocatedTotal)`


- `availableCashTotal = SUM(Funds.AmountOriginal - FundStats.SpentTotal)`



---

### Índices recomendados (para que vuele)

- En `Marketing_Funds` (si no lo agregaste todavía):

- `IX_MFunds_BrandId_Currency` (`BrandId`, `Currency`, `ExpiresAt`) *(o *`BrandId,Currency`* + otro por *`ExpiresAt`*)*




- En `marcas` (opcional):

- índice por `referencia` si `q` se usa mucho *(ojo que LIKE “%texto%” no lo aprovecha bien; si querés búsqueda buena, ahí sí hablaríamos de full-text o cambiar patrón)*





---

## Criterios de aceptación

- El endpoint devuelve **solo marcas que tienen al menos 1 fondo** (por el JOIN a `Marketing_Funds`).


- Los totales se devuelven **por moneda** (ARS/USD) dentro de `totals{}`.


- `activeOnly=1` excluye fondos vencidos; `activeOnly=0` incluye todo.


- Si `currencyId` está presente, solo devuelve totales de esa moneda.


- La respuesta es paginable por marca (aunque internamente haya varias filas por moneda) y ordena por `marcas.referencia` asc.
