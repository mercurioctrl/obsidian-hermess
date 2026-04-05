---
jira_key: "SNB-1487"
aliases: ["SNB-1487"]
summary: "LIOWAPP - Confirmar pedido - Costo envío"
status: "Finalizada"
type: "Nueva función"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-02-06 00:37"
updated: "2024-03-17 21:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-1487"
---

# SNB-1487: LIOWAPP - Confirmar pedido - Costo envío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Nueva función |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-06 00:37 |
| Actualizado | 2024-03-17 21:39 |
| Etiquetas | ninguna |
| Jira | [SNB-1487](https://bluinc.atlassian.net/browse/SNB-1487) |

## Relaciones

*Sin relaciones*

## Descripcion

Realizaremos una modificación en el recurso que se ejecuta al efectuar una compra a través de Libre Opción. Este cambio consistirá en ajustar el código para que, al guardar el costo de envío, se registre ahora en dólares en lugar de pesos.

```
{{API_URL}}/pedidos/checkout/confirmar
```
