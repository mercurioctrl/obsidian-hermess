---
jira_key: "COB-28"
aliases: ["COB-28"]
summary: "API - Feat - Listar saldos de caja"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-17 20:23"
updated: "2022-12-05 14:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-28"
---

# COB-28: API - Feat - Listar saldos de caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-17 20:23 |
| Actualizado | 2022-12-05 14:44 |
| Etiquetas | ninguna |
| Jira | [COB-28](https://bluinc.atlassian.net/browse/COB-28) |

## Relaciones

- **Padre:** [[COB-15]] Cajas
- **Subtarea:** [[COB-38]] API - Feat - Paginado
- **Subtarea:** [[COB-91]] API - Review - Solo estoy viendo el saldo de una caja
- **Subtarea:** [[COB-96]] API - Feat - Filtrar por nombre del propietario de la caja
- **Subtarea:** [[COB-106]] API - Refactor - Mostrar solo aquellas que tienen saldo para evitar lo que se muestra en las imagenes
- **Subtarea:** [[COB-360]] API - Refactor - Introducir parametro para filtrar aquellas que tienen saldos distintos de cero
- **blocks:** [[COB-40]] APP - Feat - Listar movimientos caja
- **blocks:** [[COB-78]] APP - Feat - Listar saldos de caja
- **blocks:** [[COB-97]] APP - Feat - Filtarar por caja
- **blocks:** [[COB-107]] APP - Refactor - Filtrar por nombre de caja

## Descripcion

```
GET {{API_URL}}/v1/boxBalance/{boxId}
```

Retorna:

```json
[
    {
        "id": 72,
        "description": "BANCO SANTANDER RIO S.A.",
        "oldId": 1,
        "accountId": 3,
        "balanceAmountDollar": 63629,
        "balanceAmountPesos": 1610864331.69,
        "initialBalance": 0
    },
    {
        "id": 16,
        "description": "CITIBANK N.A.",
        "oldId": 6,
        "accountId": 6,
        "balanceAmountDollar": 21050,
        "balanceAmountPesos": 6797.67,
        "initialBalance": 0
    },
    {
        "id": 7,
        "description": "BANCO DE GALICIA Y BUENOS AIRES S.A.",
        "oldId": 2,
        "accountId": 2,
        "balanceAmountDollar": 1378555.46,
        "balanceAmountPesos": 4464956751.95,
        "initialBalance": 0
    }
]
```



Ejemplo:

```sql
SELECT PGM_USUARIOS.[USU_IDENTIFICACION]
,[MC_FORMAS_PAGO].FP_DESCRIPCION
,[SC_IMPORTE]
,[SC_FECHAPROCESO]
,PGM_USUARIOS.id
FROM [NEW_BYTES].[dbo].[MC_SALDOS_CAJA]
INNER JOIN NEW_BYTES.dbo.PGM_USUARIOS ON PGM_USUARIOS.USU_IDENTIFICACION = MC_SALDOS_CAJA.USU_IDENTIFICACION
LEFT JOIN NEW_BYTES.dbo.MC_FORMAS_PAGO ON MC_SALDOS_CAJA.ID_FORMAPAGO = MC_FORMAS_PAGO.ID_FORMAPAGO
WHERE PGM_USUARIOS.id =27
```
