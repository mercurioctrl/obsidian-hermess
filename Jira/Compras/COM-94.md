---
jira_key: "COM-94"
summary: "API - Refactor - Retornar 404 en caso de no obtener resultados externos al buscar posición arancelaria"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-05-15 17:02"
updated: "2024-05-22 04:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-94"
---

# COM-94: API - Refactor - Retornar 404 en caso de no obtener resultados externos al buscar posición arancelaria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-05-15 17:02 |
| Actualizado | 2024-05-22 04:20 |
| Etiquetas | ninguna |
| Jira | [COM-94](https://bluinc.atlassian.net/browse/COM-94) |

## Descripción

Ejemplo de al no encontrar datos externos de posición.

```
{
    "errors": {
        "status": 404,
        "title": "No se encontro la posición arancelaria fuentesssss",
        "file": "/var/www/app/app/Services/TariffPosition/Search/TariffPositionSearchService.php",
        "line": 54
    }
}
```
