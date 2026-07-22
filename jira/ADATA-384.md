---
jira_key: ADATA-384
status: Revisión
assignee: Ezequiel manzano
assignee_email: null
reporter: Catriel Mercurio
priority: Medium
issuetype: Subtarea
project: ADATA
updated: "2026-03-30T10:15:38.825-0300"
created: "2026-03-29T21:30:22.899-0300"
url: "https://bluinc.atlassian.net/browse/ADATA-384"
tags: [jira, ADATA, revisión]
---

# ADATA-384 · API - Feat - Agregar KeywordMatch para buscar dentro del nombre de los clientes

[ADATA-384 en Jira](https://bluinc.atlassian.net/browse/ADATA-384)

## Descripción

### Resumen

Se requiere agregar un campo `keywordMatch` en la tabla de clientes. Esto permitirá realizar búsquedas parciales por el nombre de los clientes en los reportes.

### Contexto

Los reportes actuales no incluyen los CUIT, solo los nombres de los clientes. Por ello, es necesario implementar un sistema que permita buscar por nombres parciales.

### Criterios de aceptación

- Agregar el parámetro `keywordMatch` en la tabla de clientes de la base de datos.
- El valor inicial de `keywordMatch` será el nombre completo del cliente.
- Permitir la edición del parámetro `keywordMatch` para usar solo un fragmento del nombre.
- La edición se realizará a través del siguiente recurso:```
{API_URL}/api/v1/clients/{clientId}
```

###

Recordar hacer el fix para que al crear un cliente, se guarde en este campo tambien el nombre del mismo

---
_Sincronizado por jira-sidecar el 2026-06-07 22:31:45 UTC._
