---
jira_key: "PED-818"
aliases: ["PED-818"]
summary: "API - Refactor - Modificar GetSellerObjectives para cumplir un nuevo requerimiento"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-16 07:24"
updated: "2024-09-17 01:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-818"
---

# PED-818: API - Refactor - Modificar GetSellerObjectives para cumplir un nuevo requerimiento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-16 07:24 |
| Actualizado | 2024-09-17 01:27 |
| Etiquetas | ninguna |
| Jira | [PED-818](https://bluinc.atlassian.net/browse/PED-818) |

## Relaciones

- **Padre:** [[PED-242]] Pestaña Estadisticas
- **is blocked by:** [[MKT-215]] NB_ FLOR DE INCENTIVO
- **blocks:** [[PED-819]] APP - Refactor - Modificar tabla de posiciones de GetSellerObjectives para cumplir un nuevo requerimiento
- **relates to:** [[PED-822]] API - Incentivos de capilaridad para vendedores - Sugerencia de mejora en el total de ventas

## Descripcion

```
GET {API_URL}/v1/objectives/capillarityIncentive/sellers
```

Fecha de incentivo: 16 al 30 de Septiembre

Marcas que son reactivas: AUREOX, RAIDMAX, F&D FENDA y DUCKY

Ordenaremos por cantidad de clientes distintos a los que les vendan.

```
[
    {
        "sellerId": 8,
        "sellerLName": "Andrea",
        "sellerFName": "Altamiranda",
        "TotalSales": 39584,
        "UniqueOrders": 31,
        "UniqueClients": 13 <<--- SE AGREGA para dar cuenta de los clientes unicos que compraron AUREOX, RAIDMAX, F&D FENDA y DUCKY
    },
    {
        "sellerId": 41,
        "sellerLName": "Sheridaim",
        ...
```

Ordenaremos primero por `UniqueClients` y luego por `TotalSales`
