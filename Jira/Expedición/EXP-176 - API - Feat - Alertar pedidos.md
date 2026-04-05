---
jira_key: "EXP-176"
aliases: ["EXP-176"]
summary: "API - Feat - Alertar pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-01-25 08:50"
updated: "2023-02-23 09:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-176"
---

# EXP-176: API - Feat - Alertar pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-25 08:50 |
| Actualizado | 2023-02-23 09:40 |
| Etiquetas | ninguna |
| Jira | [EXP-176](https://bluinc.atlassian.net/browse/EXP-176) |

## Relaciones

- **Padre:** [[EXP-169]] Feat - Alertar pedidos
- **blocks:** [[EXP-177]] APP - Feat - Alertar pedido

## Descripcion

Crearemos un recurso dentro de alguno de las cabeceras de despacho (por ej: `MS_REMITOS_CABECERA`) que nos servirá para alertar el pedido. Al ejecutar el recurso:

```
PATCH {API_URL}/v1/alertOrder/{pedidoAAlertar}
```

Lo que hacemos es marcar la columna para ese pedido como alertado, y la fecha (fecha y hora,m,s) de alerta, **solo si el mismo aun no fue despachado**.

Una vez realizado, devolvemos:

```
{
  succes: true,
  "message": "Pedido alertado con exito",
}
```

```
{
  succes: false,
  "message": "El pedido no pudo ser alertado",
}
```

```
{
  succes: false,
  "message": "El pedido esta finalizado",
}
```

Algo importante es que cada vez que se ejecute el alerta, la fecha se actualiza. Esto nos servirá mas adelante para que ademas de destacar los pedidos, podamos ordenarlos primero en la lista.
