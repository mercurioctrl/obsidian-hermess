---
jira_key: "EXP-56"
summary: "API - Feat - Ingresar nuevos seriales MÚLTIPLES POR INTERVALO a un producto, dentro de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-09 15:59"
updated: "2023-06-21 07:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-56"
---

# EXP-56: API - Feat - Ingresar nuevos seriales MÚLTIPLES POR INTERVALO a un producto, dentro de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-09 15:59 |
| Actualizado | 2023-06-21 07:11 |
| Etiquetas | ninguna |
| Jira | [EXP-56](https://bluinc.atlassian.net/browse/EXP-56) |

## Descripción

Esta historia se basa en [link](https://lioteam.atlassian.net/browse/EXP-44) pero en lugar de recibir un par de intervalos, recibe pares múltiples, de la siguiente manera.

```
POST {API_URL}/v1/providersOrders/{providerOrderId}/serials/{itemId}
```

Payload:

```
[
  {
    mode:multiple-intervals, //indica el modo para la lista
    "0": [
        'MMFE8YT000095',
        'MMFE8YT000105'
        ],
    "1": [
        'MMFE9YT000095',
        'MMFE9YT000105'
        ],
    "2": [
        'MMFF1YT000095',
        'MMFF1YT000105'
        ],                
}
]

```
