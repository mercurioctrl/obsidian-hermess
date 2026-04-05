---
jira_key: "COM-45"
aliases: ["COM-45"]
summary: "API - Feat - Modificar un provedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-19 09:58"
updated: "2026-01-29 10:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-45"
---

# COM-45: API - Feat - Modificar un provedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-19 09:58 |
| Actualizado | 2026-01-29 10:05 |
| Etiquetas | ninguna |
| Jira | [COM-45](https://bluinc.atlassian.net/browse/COM-45) |

## Relaciones

- **Padre:** [[COM-6 - Listar proveedores|COM-6]] Listar proveedores
- **blocks:** [[COM-46 - APP - Feat - Modificar un proveedor|COM-46]] APP - Feat - Modificar un proveedor
- **relates to:** [[COM-277 - APP - Refactor - AltaEdición de Proveedores - Añadir selector de empresa|COM-277]] APP - Refactor - Alta/Edición de Proveedores -> Añadir selector de empresa
- **is cloned by:** [[COM-278 - API - Refactor - Modificar un proveedor - Incorporar companyCode|COM-278]] API - Refactor - Modificar un proveedor ->  Incorporar companyCode

## Descripcion

Crearemos el recurso necesario para modificar un proveedor

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
    "localitieId": 14233
  }
  ]
```

Tabla a operar

```
SELECT * FROM [NewBytes_DBF].[dbo].[FP_Proveedores]
```
