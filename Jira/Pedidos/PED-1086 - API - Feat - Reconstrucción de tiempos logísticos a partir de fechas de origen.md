---
jira_key: "PED-1086"
aliases: ["PED-1086"]
summary: "API - Feat - Reconstrucción de tiempos logísticos a partir de fechas de origen "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-08-20 14:28"
updated: "2025-08-26 11:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1086"
---

# PED-1086: API - Feat - Reconstrucción de tiempos logísticos a partir de fechas de origen 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-08-20 14:28 |
| Actualizado | 2025-08-26 11:14 |
| Etiquetas | ninguna |
| Jira | [PED-1086](https://bluinc.atlassian.net/browse/PED-1086) |

## Relaciones

- **Padre:** [[PED-1068]] Periodos logisticos

## Descripcion

Implementar un nuevo recurso 

```
GET /v1/statistics/logisticPerformance/validate
```

Idéntico a `/statistics/logisticPerformance`, cuyo objetivo será **obtener las fechas de cada tabla origen de las distintas áreas**.

El recurso deberá estar **desacoplado del proceso de *****syncup*** (cambio de estado) y permitirá:

- Verificar rápidamente posibles errores o desfasajes en los datos.


- Mantener la integridad y coherencia de la información entre áreas.
