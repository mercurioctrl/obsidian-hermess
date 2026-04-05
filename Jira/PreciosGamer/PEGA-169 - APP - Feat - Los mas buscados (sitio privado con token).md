---
jira_key: "PEGA-169"
aliases: ["PEGA-169"]
summary: "APP - Feat - Los mas buscados (sitio privado con token)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-09 15:57"
updated: "2025-01-20 11:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-169"
---

# PEGA-169: APP - Feat - Los mas buscados (sitio privado con token)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-09 15:57 |
| Actualizado | 2025-01-20 11:23 |
| Etiquetas | ninguna |
| Jira | [PEGA-169](https://bluinc.atlassian.net/browse/PEGA-169) |

## Relaciones

- **Padre:** [[PEGA-1 - Bases y repositorios|PEGA-1]] Bases y repositorios
- **action item from:** [[PEGA-166 - API - Feat - Repositorio Mas buscados|PEGA-166]] API - Feat - Repositorio "Mas buscados"

## Descripcion

Usando el recurso [link](https://lioteam.atlassian.net/browse/PEGA-166)  crearemos un sitio simple con una tabla para mostrar los datos de las palabras mas buscadas y la cantidad de veces buscadas.

Para esto necesitamos un token que estara como un parametro en el propio sitio 

```
https://preciosgamer.com/privateKeywords?token={token}
```

El recurso permite un between de fechas, por lo tanto podriamos integrar un picker de calendario o al menos un formulario para cambiar el intervalo de fecha
