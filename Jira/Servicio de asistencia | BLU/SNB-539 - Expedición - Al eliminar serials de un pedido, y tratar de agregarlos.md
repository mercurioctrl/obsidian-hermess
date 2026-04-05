---
jira_key: "SNB-539"
aliases: ["SNB-539"]
summary: "Expedición - Al eliminar serials de un pedido, y tratar de agregarlos nuevamente por intervalos da error"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2023-02-01 11:45"
updated: "2023-02-02 10:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-539"
---

# SNB-539: Expedición - Al eliminar serials de un pedido, y tratar de agregarlos nuevamente por intervalos da error

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2023-02-01 11:45 |
| Actualizado | 2023-02-02 10:19 |
| Etiquetas | ninguna |
| Jira | [SNB-539](https://bluinc.atlassian.net/browse/SNB-539) |

## Relaciones

*Sin relaciones*

## Descripcion

Buen día, 
En envios borre 4 serials de un mouse de la orden 10289834 pedido X000200543427 

Los serials fueron:
`[{"serials":["31F95974000234","31F95974000235","31F95974000236","31F95974000237"]}]`

La eliminacion se realiza correctamente, pero al intentar agregarlos nuevamente por intervalos, muestra el siguiente error:


```
{
    "msg": "No fue posible agregar los siguientes serial no estan habilitados o no pertenecen al Item.",
    "serials": [
        "31F95974000234",
        "31F95974000235",
        "31F95974000236",
        "31F95974000237"
    ],
    "success": false
}
```



Pero al listar los serials del producto aparecen que si fueron agregados
