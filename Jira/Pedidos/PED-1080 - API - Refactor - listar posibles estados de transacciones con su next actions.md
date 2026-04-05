---
jira_key: "PED-1080"
aliases: ["PED-1080"]
summary: "API - Refactor - listar posibles estados de transacciones con su next actions"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-08-08 15:44"
updated: "2025-08-19 10:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1080"
---

# PED-1080: API - Refactor - listar posibles estados de transacciones con su next actions

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-08-08 15:44 |
| Actualizado | 2025-08-19 10:40 |
| Etiquetas | ninguna |
| Jira | [PED-1080](https://bluinc.atlassian.net/browse/PED-1080) |

## Relaciones

- **Padre:** [[PED-724 - Modal Venta Market Place LO|PED-724]] Modal "Venta Market Place LO"

## Descripcion

Endpoint ya existe.

```
GET aboutMarketPlace/transaction/status
```

debe retornar:

```
[
    {
        "value": "accredited",
        "statusDetail": "¡Listo! Se acreditó tu pago.",
        "nextAction": "No se requiere acción adicional.",
        "provider": "mercadopago"
    },
    {
        "value": "partially_refunded",
        "statusDetail": "El pago se realizó con al menos un reembolso parcial.",
        "nextAction": "Revisar reembolsos parciales y comunicar al cliente si es necesario.",
        "provider": "mercadopago"
    }
]
```



Se obtiene esta informacion de la nueva tabla: `lo.dbo.payment_status_detail`



```
create table dbo.payment_status_detail
(
    id            int identity
        primary key,
    status_code   varchar(50)                not null,
    status_detail nvarchar(255)              not null,
    next_action   nvarchar(255)              not null,
    provider      varchar(50)                not null,
    created_at    datetime default getdate() not null,
    updated_at    datetime,
    deleted_at    datetime
)
```



Se refactoriza este endpoint con el objetivo de completar la información necesaria según el status_detail, a fin de indicar al cliente cómo proceder en caso de un fallo y facilitar la conversión de la orden.
