---
jira_key: "ADATA-384"
summary: "API - Feat - Agregar KeywordMatch para buscar dentro del nombre de los clientes"
status: "Revisión"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-29 21:30"
updated: "2026-03-30 10:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-384"
---

# ADATA-384: API - Feat - Agregar KeywordMatch para buscar dentro del nombre de los clientes

| Campo | Valor |
|-------|-------|
| Estado | Revisión (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-29 21:30 |
| Actualizado | 2026-03-30 10:15 |
| Etiquetas | ninguna |
| Jira | [ADATA-384](https://bluinc.atlassian.net/browse/ADATA-384) |

## Descripción

### Resumen

Se requiere agregar un campo `keywordMatch` en la tabla de clientes. Esto permitirá realizar búsquedas parciales por el nombre de los clientes en los reportes.

### Contexto

Los reportes actuales no incluyen los CUIT, solo los nombres de los clientes. Por ello, es necesario implementar un sistema que permita buscar por nombres parciales.

### Criterios de aceptación

- Agregar el parámetro `keywordMatch` en la tabla de clientes de la base de datos.


- El valor inicial de `keywordMatch` será el nombre completo del cliente.


- Permitir la edición del parámetro `keywordMatch` para usar solo un fragmento del nombre.


- La edición se realizará a través del siguiente recurso:

```
{API_URL}/api/v1/clients/{clientId}
```



### 

Recordar hacer el fix para que al crear un cliente, se guarde en este campo tambien el nombre del mismo
