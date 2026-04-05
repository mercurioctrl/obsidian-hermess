---
jira_key: "COM-73"
aliases: ["COM-73"]
summary: "API - Posición arancelaria e impuestos - Resultados de búsqueda no coincidentes"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-03-15 17:34"
updated: "2024-03-20 15:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-73"
---

# COM-73: API - Posición arancelaria e impuestos - Resultados de búsqueda no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-15 17:34 |
| Actualizado | 2024-03-20 15:27 |
| Etiquetas | ninguna |
| Jira | [COM-73](https://bluinc.atlassian.net/browse/COM-73) |

## Relaciones

- **Padre:** [[COM-1 - Bases y repositorios|COM-1]] Bases y repositorios
- **blocks:** [[COM-66 - API - Refactor - Extracción de datos - posición arancelaria e impuestos|COM-66]] API - Refactor - Extracción de datos - posición arancelaria e impuestos 

## Descripcion

Los aranceles que obtengo de la búsqueda no coinciden con los del sitio de VUCE.

[adjunto]
[adjunto]
Dato extra:
Quizás sería bueno que estos se obtuvieran del recurso

```
https://qa.ci.vuce.gob.ar/tributaciones/obtenerOperacion?posicion={$position}&operacion=I
```
