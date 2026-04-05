---
jira_key: "PED-914"
aliases: ["PED-914"]
summary: "API - Refactor - Aplicar permisos a los paramtros del cliente especificados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-20 15:25"
updated: "2025-01-27 17:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-914"
---

# PED-914: API - Refactor - Aplicar permisos a los paramtros del cliente especificados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-20 15:25 |
| Actualizado | 2025-01-27 17:28 |
| Etiquetas | ninguna |
| Jira | [PED-914](https://bluinc.atlassian.net/browse/PED-914) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente

## Descripcion

Los siguientes parámetros solo pueden ser editados en el recurso 

```
GET {API_URL}/v1/clients/{clientId}
```

cuando el usuario cuenta con uno de los siguientes permisos: 

- `pm`


- `gerencia`



Los parámetros afectados son:

- `specialPrice`


- `profile`


- `companyCode`


- `currencyId`


- `salespersonId`
