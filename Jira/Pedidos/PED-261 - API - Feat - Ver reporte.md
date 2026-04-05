---
jira_key: "PED-261"
aliases: ["PED-261"]
summary: "API - Feat - Ver reporte"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-13 17:00"
updated: "2023-11-14 10:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-261"
---

# PED-261: API - Feat - Ver reporte

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-13 17:00 |
| Actualizado | 2023-11-14 10:12 |
| Etiquetas | ninguna |
| Jira | [PED-261](https://bluinc.atlassian.net/browse/PED-261) |

## Relaciones

- **Padre:** [[PED-253 - Listar reportes|PED-253]] Listar reportes
- **blocks:** [[PED-262 - APP - Feat - Ver reporte|PED-262]] APP - Feat - Ver reporte

## Descripcion

Agregaremos el recurso para obtener el detalle de un reporte

```
GET {API_URL}/v1/reports/{clave}
```

[adjunto]
Se debe obtener

- Descripción


- Fecha


- Creador


- Responsable


- Tipo


- Estado


- Cuerpo


- Mensajes
