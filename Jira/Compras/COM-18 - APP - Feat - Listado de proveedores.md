---
jira_key: "COM-18"
aliases: ["COM-18"]
summary: "APP - Feat - Listado de proveedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-02-13 16:38"
updated: "2024-02-21 16:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-18"
---

# COM-18: APP - Feat - Listado de proveedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-13 16:38 |
| Actualizado | 2024-02-21 16:33 |
| Etiquetas | ninguna |
| Jira | [COM-18](https://bluinc.atlassian.net/browse/COM-18) |

## Relaciones

- **Padre:** [[COM-6]] Listar proveedores
- **is blocked by:** [[COM-7]] API - Feat - Listar proveedores
- **is blocked by:** [[COM-36]] APP - Listado de proveedores - Id del proveedor distinto

## Descripcion

Crearemos una pestaña encargada de listar los proveedores que contenga la siguiente informacion

- id - name


- bussinessName


- Addres


- countryId - descriptionId


- countryFlagId (aca asignaremos la banderita de cada pais al id) 



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
  ...
```

En principio debemos poder buscar en el buscador general por id y por nombre.
