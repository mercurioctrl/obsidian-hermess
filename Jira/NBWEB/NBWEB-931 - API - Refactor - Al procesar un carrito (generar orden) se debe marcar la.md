---
jira_key: "NBWEB-931"
aliases: ["NBWEB-931"]
summary: "API - Refactor - Al procesar un carrito (generar orden) se debe marcar la empresa que esta primero"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-27 12:11"
updated: "2024-11-30 04:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-931"
---

# NBWEB-931: API - Refactor - Al procesar un carrito (generar orden) se debe marcar la empresa que esta primero

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-27 12:11 |
| Actualizado | 2024-11-30 04:44 |
| Etiquetas | ninguna |
| Jira | [NBWEB-931](https://bluinc.atlassian.net/browse/NBWEB-931) |

## Relaciones

- **Padre:** [[NBWEB-619]] Generar ordenes

## Descripcion

Usaremos el primer (o único valor si es el caso) que se encuentra en el `.env` en el atrbuto`COMPANY_CODES`

Para poder almacenar al crearlo en la cabecera de la orden (`[NewBytes_DBF].[dbo].[pedclit].companyCode`)

Si no se encuentra, se guarda `null`

```
POST {API_URL}/v1/carrito/process
```
