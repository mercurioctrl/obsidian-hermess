---
jira_key: "PED-934"
aliases: ["PED-934"]
summary: "API - Feat - SyncUp - Liberar ordenes de LIBRE OPCION que cumplen mas de 48hs sin ser procesadas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-23 06:59"
updated: "2025-01-30 03:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-934"
---

# PED-934: API - Feat - SyncUp - Liberar ordenes de LIBRE OPCION que cumplen mas de 48hs sin ser procesadas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-23 06:59 |
| Actualizado | 2025-01-30 03:07 |
| Etiquetas | ninguna |
| Jira | [PED-934](https://bluinc.atlassian.net/browse/PED-934) |

## Relaciones

- **Padre:** [[PED-933 - Liberacion de ordenes|PED-933]] Liberacion de ordenes

## Descripcion

```
DELETE {{API_URL}}/v1/syncUp/lioOrdersUnprocessed
```

Marcaremos como eliminadas de manera “logica” todas las ordenes (en `pedclit`) que aun no fueron procesadas y pertenecen a libre opción.

## ¿cuales consideraremos como no procesadas?

Todas aquellas que estan en `cestado=P` o no tienen su consecuente en la tabla `albclit`



El tiempo por defecto es 48hs, pero el parámetro LIO_ORDERS_EXPIRE debe encontrarse disponible par poder setearlo en las variables de entorno
