---
jira_key: "LIO-217"
aliases: ["LIO-217"]
summary: "API - Feat - Repositorio de motivos de ticket"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-12 13:47"
updated: "2025-02-19 16:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-217"
---

# LIO-217: API - Feat - Repositorio de motivos de ticket

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-12 13:47 |
| Actualizado | 2025-02-19 16:51 |
| Etiquetas | ninguna |
| Jira | [LIO-217](https://bluinc.atlassian.net/browse/LIO-217) |

## Relaciones

- **Padre:** [[LIO-21]] Migrar sistema de tickets para usar el de capa 1 (NB)
- **has action item:** [[LIO-226]] APP - Refactor - Conectar sistema de envio de ticket a v4

## Descripcion

Agregaremos el repositorio que contiene el asunto para los distintos tipos de ticket

```
GET {APIv4_URL}/v4/ticket/issues/{ticketTypeId}
```

```
[
    {
        "id": 6,
        "description": "Con el pago"
    },
    {
        "id": 7,
        "description": "Con el envío"
    },
    {
        "id": 8,
        "description": "Con el vendedor"
    },
    {
        "id": 9,
        "description": "Con el producto"
    },
    {
        "id": 20,
        "description": "Con la factura"
    }
]
```

```
SELECT [id]
      ,[idTicketTipo]
      ,[descripcion]
      ,[activo]
      ,[eliminado]
      ,[fechaCreacion]
  FROM [LO].[dbo].[ticketsMotivo]
  WHERE idTicketTipo = ?
```
