---
jira_key: "NBE-237"
aliases: ["NBE-237"]
summary: "APP - Refactor - Conectar Banners al recurso y segmento de banners 3"
status: "Listo"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-22 08:54"
updated: "2026-01-23 17:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBE-237"
---

# NBE-237: APP - Refactor - Conectar Banners al recurso y segmento de banners 3

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-22 08:54 |
| Actualizado | 2026-01-23 17:14 |
| Etiquetas | ninguna |
| Jira | [NBE-237](https://bluinc.atlassian.net/browse/NBE-237) |

## Relaciones

- **Padre:** [[NBE-81]] Sitio Web_Etapa 3
- **action item from:** [[NBE-142]] API - Refactor - Admin para Subir banners 
- **implements:** [[NBE-230]] Enero: Subir Banners 

## Descripcion

Al igual que al inicio con el sitio [link](http://nb.com.ar) , donde asignamos segmentos de banners por ID y definimos distintas zonas para cargarlos dinámicamente desde el CMS, aplicaremos el mismo criterio al banner principal de [link](http://nbe.com.ar) .

Para esto utilizaremos el **segmento con ID 3**, consumiendo el recurso:

```
https://api.nbe.com.ar/v1/banners/3
```

La lógica es la misma: se mostrarán los banners que devuelva el repositorio, respetando su orden y, en caso de tener link, se abrirán en una nueva pestaña.
