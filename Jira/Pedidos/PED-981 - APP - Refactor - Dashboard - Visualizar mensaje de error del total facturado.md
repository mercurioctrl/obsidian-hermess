---
jira_key: "PED-981"
aliases: ["PED-981"]
summary: "APP - Refactor - Dashboard -> Visualizar mensaje de error del total facturado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-03-29 17:08"
updated: "2025-03-31 20:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-981"
---

# PED-981: APP - Refactor - Dashboard -> Visualizar mensaje de error del total facturado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-03-29 17:08 |
| Actualizado | 2025-03-31 20:05 |
| Etiquetas | ninguna |
| Jira | [PED-981](https://bluinc.atlassian.net/browse/PED-981) |

## Relaciones

- **Padre:** [[PED-242]] Pestaña Estadisticas
- **relates to:** [[PED-280]] APP - Feat - Dashboard

## Descripcion

Se refactorizaron algunos recursos de estadísticas y reportes en el backend, los cuales ahora siguen la estructura definida al ocurrir un error.  Por lo que se deberá realizar un ajuste en el frontend para mostrar correctamente el mensaje de error.



```
{
  "success": true,                    // true o false
  "message": "Operación exitosa",     // Descripción opcional
  "data": {}                          // Objeto con datos devueltos o null
}

```



```
GET {{API_URL}}/v1/statistics/totalBilled
```

[adjunto]
