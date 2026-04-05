---
jira_key: "PED-1285"
aliases: ["PED-1285"]
summary: "API - Feat - Clientes nuevos Vs Clientes nuevos Objetivo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-26 08:53"
updated: "2026-02-03 08:19"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1285"
---

# PED-1285: API - Feat - Clientes nuevos Vs Clientes nuevos Objetivo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-26 08:53 |
| Actualizado | 2026-02-03 08:19 |
| Etiquetas | esperandoDependencia |
| Jira | [PED-1285](https://bluinc.atlassian.net/browse/PED-1285) |

## Relaciones

- **Padre:** [[PED-299]] Objetivos y Desafios
- **is cloned by:** [[PED-1291]] API - Review - Clientes nuevos Vs Clientes nuevos Objetivo -> Filtros no coincidentes
- **has action item:** [[PED-1294]] APP - Feat - Agregar objetivo de clientes en el mes actual, por vendedor

## Descripcion

Se creará un recurso de **objetivos de clientes** cuyo propósito es exponer, por vendedor, el estado de avance en la captación de clientes activos.

Un **cliente activo** se define como aquel que posee al menos una compra registrada en los **últimos 3 meses**, utilizando el campo
`[NewBytes_DBF].[dbo].[clientes].ULTIMA_COMPRA` como criterio temporal.

Para cada vendedor se deberán calcular y exponer los siguientes valores:

- **amount**: cantidad actual de clientes activos asociados al vendedor.


- **targetAmount**: objetivo de clientes activos definido para el vendedor, almacenado en
`[NewBytes_DBF].[dbo].[agentes].monthlyClientTargetAmount`.


- **percentageAchieved**: porcentaje de avance del objetivo, calculado como
`(amount / targetAmount) * 100`, expresado como valor entero.



El recurso devolverá un listado con estos datos para todos los vendedores.

Endpoint:

```
GET {API_URL}/v1/objectives/totalClients

```

Ejemplo de respuesta:

```
{
    "response": [
        {
            "sellerId": 100,
            "sellerDescription": "Opcion Libre",
            "amount": 1978,
            "targetAmount": 230962,
            "percentageAchieved": 1
        },
        {
            "sellerId": 51,
            "sellerDescription": "Lautaro Soto",
            "amount": 186,
            "targetAmount": 400052,
            "percentageAchieved": 0
        },
        {
            "sellerId": 47,
            "sellerDescription": "Antonella Garcia",
            "amount": 105,
            "targetAmount": 151570,
            "percentageAchieved": 0
        },
        {
            "sellerId": 41,
            "sellerDescription": "Natalia Sheridaim",
            "amount": 277,
            "targetAmount": 275755,
            "percentageAchieved": 0
        },
        {
            "sellerId": 30,
            "sellerDescription": "Albarracin Julian",
            "amount": 162,
            "targetAmount": 304410,
            "percentageAchieved": 0
        }
    ],
    "pagination": {
        "total": 7,
        "current": 1,
        "pageSize": 5
    }
}

```

---

### Criterios de aceptación

- El endpoint `GET /v1/objectives/totalClients` debe responder correctamente con HTTP 200.


- El campo **amount** debe reflejar exclusivamente clientes con `ULTIMA_COMPRA` dentro de los últimos 3 meses.


- El campo **targetAmount** debe obtenerse desde `[NewBytes_DBF].[dbo].[agentes].monthlyClientTargetAmount`.


- El campo **percentageAchieved** debe calcularse en base a `amount` y `targetAmount` y devolverse como entero.


- Todos los vendedores con objetivo configurado deben estar incluidos en la respuesta.







Filtros agregados: no son obligatorios ni afectan la respuesta general.

- **months**: Cantidad de meses hacia atrás para considerar clientes activos (default: 3)


- **between**: Rango de fechas específico en formato dd-mm-yyyy_dd-mm-yyyy (sobrescribe months)


- **sellerId**: Filtra por un vendedor específico usando su ID


- **companyCode**: Filtra vendedores por código de empresa


- **active**: Filtra por estado del vendedor (1=activo, 0=inactivo)


- **minPercentage**: Porcentaje mínimo de cumplimiento de objetivo


- **maxPercentage**: Porcentaje máximo de cumplimiento de objetivo


- **minTarget**: Objetivo mínimo de clientes que debe tener configurado el vendedor


- **includeNoTarget**: Incluye vendedores sin objetivo configurado (default: false)


- **search**: Busca por nombre o apellido del vendedor


- **sortBy**: Campo por el cual ordenar (sellerId, amount, targetAmount, percentageAchieved, sellerDescription)


- **sortOrder**: Dirección del ordenamiento (asc o desc)


- **page**: Número de página para paginación (default: 1)


- **perPage**: Cantidad de resultados por página (default: 15)





Los ejemplos estan en postman.
