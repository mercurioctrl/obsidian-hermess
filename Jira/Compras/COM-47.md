---
jira_key: "COM-47"
summary: "API - Feat - Ver detalle de un provoeedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-19 10:21"
updated: "2024-02-20 18:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-47"
---

# COM-47: API - Feat - Ver detalle de un provoeedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-19 10:21 |
| Actualizado | 2024-02-20 18:14 |
| Etiquetas | ninguna |
| Jira | [COM-47](https://bluinc.atlassian.net/browse/COM-47) |

## Descripción

Crearemos el recurso necesario para LEER un proveedor

```
GET {{API_URL}}/v1/providers/{IDpROVEEDOR}
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
  }
  ]
```

Tabla a operar

```
SELECT * FROM [NewBytes_DBF].[dbo].[FP_Proveedores]
```
