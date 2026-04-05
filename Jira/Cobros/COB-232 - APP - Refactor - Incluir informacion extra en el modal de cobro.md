---
jira_key: "COB-232"
aliases: ["COB-232"]
summary: "APP - Refactor - Incluir informacion extra en el modal de cobro"
status: "Gamma"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-07 11:56"
updated: "2022-11-29 11:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-232"
---

# COB-232: APP - Refactor - Incluir informacion extra en el modal de cobro

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 11:56 |
| Actualizado | 2022-11-29 11:33 |
| Etiquetas | ninguna |
| Jira | [COB-232](https://bluinc.atlassian.net/browse/COB-232) |

## Relaciones

- **Padre:** [[COB-33]] Cobrar

## Descripcion

Se debe incluir los siguientes parametros en el contexto a modal de cobro:

```
            "clientTaxNumber": "20-33457962-0",
            "paymentMethod": "Efectivo Caja",
            "estado": "Finalizado",
            "dispatch": "Retiro de cliente en Local"
```

[adjunto]
Como detalle:

Si el estado es finalizado (status 4), no se debe habilitar para cobrar.
