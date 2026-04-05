---
jira_key: "EXP-31"
aliases: ["EXP-31"]
summary: "Feat - Repositorio proveedores"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-02 14:37"
updated: "2023-02-03 15:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-31"
---

# EXP-31: Feat - Repositorio proveedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-02 14:37 |
| Actualizado | 2023-02-03 15:07 |
| Etiquetas | ninguna |
| Jira | [EXP-31](https://bluinc.atlassian.net/browse/EXP-31) |

## Relaciones

- **Padre:** [[EXP-1 - Base y Repositorios|EXP-1]] Base y Repositorios

## Descripcion

```
GET {{API_URL}}/v1/providers
```

```
[
  {
    "id": 14646,
    "providerCode": "001594",
    "name": "TRENDSETTERS - DA PALACE SRL",
    "businessName": "TRENDSETTERS - DA PALACE SRL",
    "Addres": "CARLOS TEJEDOR 890",
    "countryId": 7,
    "provicenId": 2,
    "localitieId": 14233
  },
  {
    "id": 14645,
    "providerCode": "001593",
    "name": "FRUITLOSOPHY EMPRSAS SRL",
    "businessName": "FRUITLOSOPHY EMPRSAS SRL",
    "Addres": "",
    "countryId": 7,
    "provicenId": 2,
    "localitieId": 14233
  }
  ]
```

```
SELECT * FROM [NewBytes_DBF].[dbo].[FP_Proveedores]
```
