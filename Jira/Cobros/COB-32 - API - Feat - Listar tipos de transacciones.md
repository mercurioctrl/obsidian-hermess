---
jira_key: "COB-32"
aliases: ["COB-32"]
summary: "API - Feat - Listar tipos de transacciones"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-17 21:12"
updated: "2022-10-13 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-32"
---

# COB-32: API - Feat - Listar tipos de transacciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-17 21:12 |
| Actualizado | 2022-10-13 09:01 |
| Etiquetas | ninguna |
| Jira | [COB-32](https://bluinc.atlassian.net/browse/COB-32) |

## Relaciones

- **Padre:** [[COB-21]] Base del proyecto y formularios
- **blocks:** [[COB-72]] API - Feat - Filtrar por tipo de transaccion
- **blocks:** [[COB-73]] APP - Feat - Agregar filtro por tipo de transacción 

## Descripcion

```
GET {API_URL}/transactionTypes
```

```
[
  {
    "id": "16",
    "description": "Cta Cte - Cobrar al Cliente"
  },
  {
    "id": "1",
    "description": "Remesas Ingresos"
  },
  {
    "id": "2",
    "description": "Remesas Egresos"
  },
  {
    "id": "10",
    "description": "Entradas Varias"
  },
  {
    "id": "8",
    "description": "Salidas Varias"
  },
  {
    "id": "20",
    "description": "Pases Ingresos"
  }
  ]
```
