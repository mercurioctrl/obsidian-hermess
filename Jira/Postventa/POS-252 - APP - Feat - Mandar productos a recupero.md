---
jira_key: "POS-252"
aliases: ["POS-252"]
summary: "APP - Feat - Mandar productos a recupero"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2023-03-29 15:37"
updated: "2023-03-30 15:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-252"
---

# POS-252: APP - Feat - Mandar productos a recupero

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2023-03-29 15:37 |
| Actualizado | 2023-03-30 15:55 |
| Etiquetas | ninguna |
| Jira | [POS-252](https://bluinc.atlassian.net/browse/POS-252) |

## Relaciones

- **Padre:** [[POS-235 - Postventa Proveedores Recepcion|POS-235]] Postventa Proveedores Recepcion
- **is blocked by:** [[POS-251 - API - Feat - Mandar productos a recupero|POS-251]] API - Feat - Mandar productos a recupero

## Descripcion

En el detalle de los finalizados, incluir un boton para recuperar los productos que esten  `isRecovery:false`  y  en estado “*Cambio*” o “*Acreditar*” 

[adjunto]


```
{{API_URL}}/v1/afterSales/{afterSaleDetailId}/finalized/recovery
```

Responde.

```
{
    "success": true,
    "msg": "El item ha sido enviado a recupero"
}

```

Y se deberia ver el item en la pestaña de recupero



Una vez marcados como recupero cambiar la variable `isRecovery:true`
