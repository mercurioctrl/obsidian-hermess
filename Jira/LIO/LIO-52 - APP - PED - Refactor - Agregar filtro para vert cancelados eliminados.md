---
jira_key: "LIO-52"
aliases: ["LIO-52"]
summary: "APP - PED - Refactor - Agregar filtro para vert cancelados / eliminados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-06-18 12:21"
updated: "2024-06-24 17:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-52"
---

# LIO-52: APP - PED - Refactor - Agregar filtro para vert cancelados / eliminados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-18 12:21 |
| Actualizado | 2024-06-24 17:37 |
| Etiquetas | ninguna |
| Jira | [LIO-52](https://bluinc.atlassian.net/browse/LIO-52) |

## Relaciones

- **Padre:** [[LIO-28 - El sitio debe funcionar correctamente, sin puntos grises o cosas que no se|LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden
- **is blocked by:** [[LIO-51 - API - PED - Refactor - Agregar filtro para ver cancelados eliminados|LIO-51]] API - PED - Refactor - Agregar filtro para ver cancelados / eliminados

## Descripcion

[adjunto]

Agregaremos un nuevo filtro `canceladas/eliminadas` para ver las ordenes de venta que nos permita visualizar SOLO aquellas ordenes que fueron canceladas/eliminadas, es decir donde 

```
GET {API_URL}/v1/orders?&orderStatus=cancelled
```

Usaremos el recurso en [link](https://lioteam.atlassian.net/browse/LIO-51)
