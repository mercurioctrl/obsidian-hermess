---
jira_key: "NBWEB-194"
aliases: ["NBWEB-194"]
summary: "API - Listar categorias iva"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-19 15:04"
updated: "2022-06-26 21:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-194"
---

# NBWEB-194: API - Listar categorias iva

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-19 15:04 |
| Actualizado | 2022-06-26 21:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-194](https://bluinc.atlassian.net/browse/NBWEB-194) |

## Relaciones

- **Padre:** [[NBWEB-130]] API - Registro y alta de cliente

## Descripcion

usando

```sql
SELECT TOP (1000) [NIVA]
      ,[Descripcion]
FROM [NewBytes_DBF].[dbo].[FP_CategoriasIVA]
```

Agregar el recurso



```
GET {{API_URL}}/v1/fiscalCategories
```

Retorna: 



```json
[
  {
    "id": 1,
    "description": "Responsable Inscripto"
  },
  {
    "id": 2,
    "description": "Responsable NO Inscripto"
  },
  {
    "id": 3,
    "description": "Consumidor Final"
  },
  {
    "id": 4,
    "description": "Exento / No Gravado"
  },
  {
    "id": 5,
    "description": "Import / Export"
  },
  {
    "id": 6,
    "description": "Responsable Monotributo"
  },
  {
    "id": 7,
    "description": "No Categorizado"
  }
]
```
