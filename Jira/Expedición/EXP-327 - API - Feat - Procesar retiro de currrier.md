---
jira_key: "EXP-327"
aliases: ["EXP-327"]
summary: "API - Feat - Procesar retiro de currrier"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-30 09:26"
updated: "2023-06-30 14:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-327"
---

# EXP-327: API - Feat - Procesar retiro de currrier

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-30 09:26 |
| Actualizado | 2023-06-30 14:25 |
| Etiquetas | ninguna |
| Jira | [EXP-327](https://bluinc.atlassian.net/browse/EXP-327) |

## Relaciones

- **Padre:** [[EXP-325]] Feat - Pestaña seguimiento

## Descripcion

Basandonos en el recurso generado en [link](https://lioteam.atlassian.net/browse/EXP-326) 

Crearemos el recurso 

```
POST {API_URL}/v1/dropTrackingOrders
```

Payload

```
{
    "trackings" : [
    "360000844931510","360000844931520","360000844931530"
    ],
    "authorizationToken" : "D0ED291960A4FA39"
}
```

De lo que se trata es de enviar (a traves del front seleccionando) aquellos numero de tracking que acaban de retirar para marcarlos

En este paso crearemos una cabecera, para agrupar todos aquellos paquetes que fueron retirados juntos y darle algunos atributos (no es necesario para esto crear una tabla, ya que solo sesran 3 datos por le momento y pueden anexarse a pedclit)

- Recolección (lo vimos en [link](https://lioteam.atlassian.net/browse/EXP-326) Es una fecha, si no esta, quiere decir que el currier no se lo llevo)


- Entregador


- DropId (este numero se los pondremos a todos los que se van en el mismo proceso, para agruparlos y vincularlos entre si)
