---
jira_key: "EXP-500"
aliases: ["EXP-500"]
summary: "APP - Refactor - Agregar en Retiros y en Envíos un indicador para mostrar la intervención técnica pendiente o realizada "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-07-04 11:53"
updated: "2025-07-14 10:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-500"
---

# EXP-500: APP - Refactor - Agregar en Retiros y en Envíos un indicador para mostrar la intervención técnica pendiente o realizada 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-04 11:53 |
| Actualizado | 2025-07-14 10:32 |
| Etiquetas | ninguna |
| Jira | [EXP-500](https://bluinc.atlassian.net/browse/EXP-500) |

## Relaciones

- **Padre:** [[EXP-7]] Despacho de retiros

## Descripcion

Similar a como realizamos en el caso de postventa cuando agregamos los indicadores de intervención técnica 

[adjunto]
Haremos algo similar para el caso de expedicion pero mas general: Mostraremos solo la llave de tuerca, porque a ellos no les interesa que es lo que hay que hacer sino solo si es algo que esta pendiente. 

[adjunto]
Los recursos ya cuentan con los parametrso

```
"assemblePc": true,
"updateBios": false,
"installOs": false,
"tiSuccess": null
```



Es decir que cuando cualquiera sea `true`, mostraremos la llave tuerca en rojo

Y si alguno esta en `true` pero `tiSuccess` tiene la fecha, la mostraremos en verde

Aun no me decido bien donde peude ir, pero tal vez junto a la campana de los pedidos alertados
