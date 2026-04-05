---
jira_key: "SNB-866"
aliases: ["SNB-866"]
summary: "No se ven correctamente tiendas oficiales en libre opcion"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-06-23 08:29"
updated: "2023-07-19 15:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-866"
---

# SNB-866: No se ven correctamente tiendas oficiales en libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-23 08:29 |
| Actualizado | 2023-07-19 15:34 |
| Etiquetas | ninguna |
| Jira | [SNB-866](https://bluinc.atlassian.net/browse/SNB-866) |

## Relaciones

*Sin relaciones*

## Descripcion

[link](https://www.libreopcion.com/tienda-oficial/ducky-channel?to=5687) 



Al parecer lo que esta molestando es el recurso

```
https://api.libreopcion.com/api/official-stores/videos/brand-id/5687/limit/3
```



Que a su vez se conecta probablemente al servicio official stores.

Debemos debugear el problema para lograr que muestre los videos correctamente.

Por otro lado, existiendo la posibilidad de que no tenga videos, o genere un error no deberia romperse (esto es algo de front)
