---
jira_key: "INV-298"
aliases: ["INV-298"]
summary: "API - Review - Debemos obtener salesReserved segun el siguiente concepto y filtrando sucursal solo cuando se indica explicitamente"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-22 13:58"
updated: "2025-12-29 12:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-298"
---

# INV-298: API - Review - Debemos obtener salesReserved segun el siguiente concepto y filtrando sucursal solo cuando se indica explicitamente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-22 13:58 |
| Actualizado | 2025-12-29 12:16 |
| Etiquetas | ninguna |
| Jira | [INV-298](https://bluinc.atlassian.net/browse/INV-298) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios
- **action item from:** [[INV-240]] API - Refactor - Agregar al repositorio de stock la cantidad de ventas / resesvas realizadas 

## Descripcion

Actualizaremos el valor obtenido en `salesReserved`

```
GET {API_URL}/itemsStocks?stock=1&companyCode=4&categoryId={categoryId}&brandId={brandId}&search={title|sku|id}
```

De esta forma obtendremos el total correctamente

```
SELECT
    SUM(albclil.ncanent) AS RESERVAS
FROM NewBytes_DBF.dbo.albclil
LEFT OUTER JOIN NewBytes_DBF.dbo.albclit
    ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
WHERE albclil.ID_Articulo =  ?
```

Y al igual que hicimos en otros casos la semana pasada, solo filtraremos sucursal si se indica explicitamente, caso contrario sumaremos todas
