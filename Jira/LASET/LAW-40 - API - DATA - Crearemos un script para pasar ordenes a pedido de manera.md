---
jira_key: "LAW-40"
aliases: ["LAW-40"]
summary: "API - DATA - Crearemos un script para pasar ordenes a pedido de manera secuencial"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-03 09:05"
updated: "2025-12-05 04:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-40"
---

# LAW-40: API - DATA - Crearemos un script para pasar ordenes a pedido de manera secuencial

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-03 09:05 |
| Actualizado | 2025-12-05 04:12 |
| Etiquetas | ninguna |
| Jira | [LAW-40](https://bluinc.atlassian.net/browse/LAW-40) |

## Relaciones

- **Padre:** [[LAW-30]] Onboarding de la nueva empresa en los sistemas del grupo NB

## Descripcion

Según lo conversado crearemos un script que ejecute el recurso 

```
POST {API_URL}/v1/orders
```

de manera secuencial (para que se generen todos los registros de stock y pasos necesarios como si hubiesen pasado a mano)

La idea es poder ejecutarlo de manera limpia una vez que terminamos de sincronizar

En este caso el stock debe estar importado previamente para poder justamente descontarlo de manera efectiva, y poder cumplir con las ordenes. Si no es así, que el stock no da la suma (esto puede ser porque no esta bien el corte de los ingresos), podremos agregar el stock necesario previamente para poder satisfacer los pedidos.
