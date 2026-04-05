---
jira_key: "COM-7"
summary: "API - Feat - Listar proveedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-09 15:43"
updated: "2024-02-20 11:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-7"
---

# COM-7: API - Feat - Listar proveedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-09 15:43 |
| Actualizado | 2024-02-20 11:22 |
| Etiquetas | ninguna |
| Jira | [COM-7](https://bluinc.atlassian.net/browse/COM-7) |

## Descripción

```
GET {{API_URL}}/v1/providers?name={name, id o businessName}&countryId={countryId}&provicenId={provicenId}&localitieId={localitieId}
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
