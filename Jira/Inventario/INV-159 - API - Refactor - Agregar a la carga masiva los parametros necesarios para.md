---
jira_key: "INV-159"
aliases: ["INV-159"]
summary: "API - Refactor - Agregar a la carga masiva los parametros necesarios para setear/updetear los productos como serializables o no o nacionales o no"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2024-10-16 09:20"
updated: "2024-10-16 10:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-159"
---

# INV-159: API - Refactor - Agregar a la carga masiva los parametros necesarios para setear/updetear los productos como serializables o no o nacionales o no

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-16 09:20 |
| Actualizado | 2024-10-16 10:27 |
| Etiquetas | ninguna |
| Jira | [INV-159](https://bluinc.atlassian.net/browse/INV-159) |

## Relaciones

- **Padre:** [[INV-125]] Importación de catálogos

## Descripcion

```
POST {API_URL}/v1/import/xlsx
```

```
{
  file: undefined
  currency: 1
  companyCode: 04
  distribuitor: 1
  preview: 0
  mapping: {
  ...
  },
  notSerializable: true/false
}
```
