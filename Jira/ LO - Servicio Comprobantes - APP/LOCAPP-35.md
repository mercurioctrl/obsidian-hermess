---
jira_key: "LOCAPP-35"
summary: "API - Refactor - Agregar a la volanta el parametro \"dropshipping\" y el parametro para saber si esta unido con algun otro pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-04-09 13:46"
updated: "2024-04-21 22:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-35"
---

# LOCAPP-35: API - Refactor - Agregar a la volanta el parametro "dropshipping" y el parametro para saber si esta unido con algun otro pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-09 13:46 |
| Actualizado | 2024-04-21 22:54 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-35](https://bluinc.atlassian.net/browse/LOCAPP-35) |

## Descripción

Modificaremos el recurso 

```
{API_URL}/v2/operationalOrder/{pedido}
```

Para que retorne un parametro para saber si es dropshipping y otro para saber si tiene algun pedido unido (ya sea como host o huesped)
