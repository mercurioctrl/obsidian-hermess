---
jira_key: "PED-829"
aliases: ["PED-829"]
summary: "APP - Refactor - Al recibir notificacion se debe poder abrir los reportes si el link contiene el parametro"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2024-09-23 12:24"
updated: "2024-09-27 10:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-829"
---

# PED-829: APP - Refactor - Al recibir notificacion se debe poder abrir los reportes si el link contiene el parametro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2024-09-23 12:24 |
| Actualizado | 2024-09-27 10:15 |
| Etiquetas | ninguna |
| Jira | [PED-829](https://bluinc.atlassian.net/browse/PED-829) |

## Relaciones

- **has action item:** [[PED-810]] APP - Feat - Notificaciones (primeras pruebas)

## Descripcion

Se espera en la query del link el siguiente parametro : `openReport={key del reporte}`
Ejemplo del cuerpo de una  notificacion

```
{
    "body": "El reporte [[SNB-2343]] esta esperando respuesta",
    "title": "Tiene un reporte pendiente",
    "userIds" : [7463],
    "type" : "nb",
    "data" : {
        "link" : "/dashboard?period=30&sellerId=12&clientGroup=A&openReport=[[SNB-2343]]"
       
    }
}
```

Se espera que cuando esta en primer plano no redirija a la ruta sino solo abra el reporte y en segundo plano si abra la ruta y el reporte
