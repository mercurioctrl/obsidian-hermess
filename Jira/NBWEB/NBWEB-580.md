---
jira_key: "NBWEB-580"
summary: "API - Feat - Carrito -> Cerrar ventas y mostrar un mensaje según se indico en el cms"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-09-15 08:37"
updated: "2024-04-16 12:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-580"
---

# NBWEB-580: API - Feat - Carrito -> Cerrar ventas y mostrar un mensaje según se indico en el cms

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-15 08:37 |
| Actualizado | 2024-04-16 12:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-580](https://bluinc.atlassian.net/browse/NBWEB-580) |

## Descripción

En la api de NB crearemos un recurso que nos permita evitar que se procese un carrito en caso de que se definiera así en el CMS y mostrar el mensaje definido para esa ocasión.

Modificaremos el recurso 

```
POST {{API_URL}}/v1/carrito/procesar
```
