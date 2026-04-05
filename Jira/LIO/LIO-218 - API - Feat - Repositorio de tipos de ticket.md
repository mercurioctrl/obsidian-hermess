---
jira_key: "LIO-218"
aliases: ["LIO-218"]
summary: "API - Feat - Repositorio de tipos de ticket"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-12 13:54"
updated: "2025-02-19 17:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-218"
---

# LIO-218: API - Feat - Repositorio de tipos de ticket

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-12 13:54 |
| Actualizado | 2025-02-19 17:01 |
| Etiquetas | ninguna |
| Jira | [LIO-218](https://bluinc.atlassian.net/browse/LIO-218) |

## Relaciones

- **Padre:** [[LIO-21]] Migrar sistema de tickets para usar el de capa 1 (NB)
- **has action item:** [[LIO-226]] APP - Refactor - Conectar sistema de envio de ticket a v4

## Descripcion

Agregaremos el repositorio que contiene los tipos de ticket al que podemos pasarle el parametro `show=0/1/null` para mostrar los inactivos/activos/todos

```
GET {APIv4_URL}/v4/ticket/types?show=1
```

```
[
  {
    "id": 1,
    "description": "Quiero Cancelar la compra"
  },
  {
    "id": 2,
    "description": "Tengo un problema"
  },
  {
    "id": 3,
    "description": "Quiero cancelar la venta"
  },
  {
    "id": 4,
    "description": "Solicito asistecia de Libre Opción en el chat de la compra"
  },
  {
    "id": 5,
    "description": "Solicito asistecia de Libre Opción en el chat de la venta"
  },
  {
    "id": 6,
    "description": "Quiero devolver el producto"
  },
  {
    "id": 7,
    "description": "Importación de productos"
  }
]
```

```
SELECT TOP (1000) [id]
      ,[titulo]
      ,[activo]
      ,[eliminado]
      ,[fechaCreacion]
  FROM [LO].[dbo].[ticketsTipo]
```
