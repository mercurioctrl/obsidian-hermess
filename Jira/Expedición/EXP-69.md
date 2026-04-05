---
jira_key: "EXP-69"
summary: "API - Feat - Recurso para imprimir seriales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-15 14:47"
updated: "2023-06-21 07:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-69"
---

# EXP-69: API - Feat - Recurso para imprimir seriales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-15 14:47 |
| Actualizado | 2023-06-21 07:12 |
| Etiquetas | ninguna |
| Jira | [EXP-69](https://bluinc.atlassian.net/browse/EXP-69) |

## Descripción

```
GET {API_URL}/v1/providersOrders/{providerOrderId}/serials/{itemId}/zpl
```

Devuelve el código zpl para que la impresora pueda imprimir todos los códigos de la serie para ese producto
