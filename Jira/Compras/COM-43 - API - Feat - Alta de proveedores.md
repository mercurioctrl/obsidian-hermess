---
jira_key: "COM-43"
aliases: ["COM-43"]
summary: "API - Feat - Alta de proveedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-19 09:20"
updated: "2024-02-21 15:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-43"
---

# COM-43: API - Feat - Alta de proveedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-19 09:20 |
| Actualizado | 2024-02-21 15:40 |
| Etiquetas | ninguna |
| Jira | [COM-43](https://bluinc.atlassian.net/browse/COM-43) |

## Relaciones

- **Padre:** [[COM-6 - Listar proveedores|COM-6]] Listar proveedores
- **blocks:** [[COM-44 - APP - Feat - Alta de proveedores|COM-44]] APP - Feat - Alta de proveedores
- **is blocked by:** [[COM-59 - API - Alta de proveedores - Datos no obligatorios|COM-59]] API - Alta de proveedores - Datos no obligatorios

## Descripcion

Crearemos el recurso necesario para dar de alta un nuevo proveedor que asignara un id incremental (esto ya lo hace la db) y un `providerCode` que sea consecuente con el id, pero en el formato correcto según la nomenclatura vigente (misma cantidad de caracteres y con los ceros a la izquierda)

```
POST {{API_URL}}/v1/providers
```

```
[
  {
    
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
