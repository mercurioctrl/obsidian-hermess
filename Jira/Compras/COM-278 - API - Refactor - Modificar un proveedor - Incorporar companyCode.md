---
jira_key: "COM-278"
aliases: ["COM-278"]
summary: "API - Refactor - Modificar un proveedor ->  Incorporar companyCode"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2026-01-29 10:05"
updated: "2026-02-04 10:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-278"
---

# COM-278: API - Refactor - Modificar un proveedor ->  Incorporar companyCode

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-29 10:05 |
| Actualizado | 2026-02-04 10:32 |
| Etiquetas | ninguna |
| Jira | [COM-278](https://bluinc.atlassian.net/browse/COM-278) |

## Relaciones

- **Padre:** [[COM-6 - Listar proveedores|COM-6]] Listar proveedores
- **clones:** [[COM-45 - API - Feat - Modificar un provedor|COM-45]] API - Feat - Modificar un provedor

## Descripcion

Habilitar en el endpoint de modificación de proveedor la actualización del campo `companyCode` (empresa asociada), permitiendo que el valor recibido en el request se persista correctamente para el proveedor editado.



```
PATCH {{API_URL}}/v1/providers
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
    "localitieId": 14233,
    "companyCode": 4 <-------------------------------------- SE AGREGA
  }
  ]
```

Tabla a operar

```
SELECT * FROM [NewBytes_DBF].[dbo].[FP_Proveedores]
```
