---
jira_key: "COM-17"
summary: "API - Refactor - Listar proveedores -> Agregar pais"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-13 16:35"
updated: "2024-02-21 16:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-17"
---

# COM-17: API - Refactor - Listar proveedores -> Agregar pais

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-13 16:35 |
| Actualizado | 2024-02-21 16:32 |
| Etiquetas | ninguna |
| Jira | [COM-17](https://bluinc.atlassian.net/browse/COM-17) |

## Descripción

Agregaremos al listado de proveedores [link](https://lioteam.atlassian.net/browse/COM-7)  la descripción del país y su bandera

```
[
  {
    "id": 14646,
    "providerCode": "001594",
    "name": "TRENDSETTERS - DA PALACE SRL",
    "businessName": "TRENDSETTERS - DA PALACE SRL",
    "Addres": "CARLOS TEJEDOR 890",
    "countryId": 7,
    "countryDescription": "Argentina", <--NUEVO
    "countryFlagId": "34",<--NUEVO
    "provicenId": 2,
    "localitieId": 14233
  },
```
