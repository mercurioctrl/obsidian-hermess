---
jira_key: "POS-38"
aliases: ["POS-38"]
summary: "API - Feat - Filtros"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-28 09:48"
updated: "2022-10-04 09:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-38"
---

# POS-38: API - Feat - Filtros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-28 09:48 |
| Actualizado | 2022-10-04 09:39 |
| Etiquetas | ninguna |
| Jira | [POS-38](https://bluinc.atlassian.net/browse/POS-38) |

## Relaciones

- **Padre:** [[POS-3]] API - Feat - Listar pre ingresos

## Descripcion

Se debe contar con filtros por fecha en el siguiente estilo

```
GET {API_URL}/v1/preAftersales/{terminos de busqueda}?between=01-01-202_101-01-2022&status=processed&failType=2
```

Los terminos de busqueda pueden incluir

- Id de pre ingreso


- id del cliente


- nombre del cliente


- nombre del producto


- numero de serie


- nombre de ususario


- fechas


- estado (si ya fue ingresado o no)


- failType



Tener en cuenta que puedo filtrar, sin necesariamente hacer match, en este estilo:

```
GET {API_URL}/v1/preAftersales/?between=01-01-202_101-01-2022&status=processed&failType=2
```
