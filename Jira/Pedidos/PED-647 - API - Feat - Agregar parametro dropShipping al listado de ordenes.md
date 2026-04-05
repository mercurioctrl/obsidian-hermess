---
jira_key: "PED-647"
aliases: ["PED-647"]
summary: "API - Feat - Agregar parametro dropShipping al listado de ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-03 09:20"
updated: "2024-04-10 19:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-647"
---

# PED-647: API - Feat - Agregar parametro dropShipping al listado de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-03 09:20 |
| Actualizado | 2024-04-10 19:22 |
| Etiquetas | ninguna |
| Jira | [PED-647](https://bluinc.atlassian.net/browse/PED-647) |

## Relaciones

- **Padre:** [[PED-646 - Dropshipping|PED-646]] Dropshipping
- **blocks:** [[PED-648 - APP - Feat - Agregar parametro dropShipping al listado de ordenes|PED-648]] APP - Feat - Agregar parametro dropShipping al listado de ordenes

## Descripcion

Asi como hicimos [link](https://lioteam.atlassian.net/browse/EXP-404)  refactorizaremos 

```
GET {API_URL}/v1/orders
```

```
{
    "response": [
        {
            "date": "2024-03-27 13:06:07",
            "orderNumber": "10343447",
            "branchNumber": "0002",
            "albnumNumber": "X000200575942",
            "realAlbumNumber": "00575942",
            "clientDescription": "MERCURIO CATRIEL EDUARDO",
            "clientId": 26806,
            "orderTypeId": 2,
            "observation": "INTERNO",
            "status": "S",
            "statusId": 2,
            "dropshipping":true,
            
...
```
