---
jira_key: "NBWEB-926"
summary: "API - Refactor - Incluir internalTax si corresponde al procesar un carrito (crear pedclil)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-12 17:38"
updated: "2024-11-22 00:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-926"
---

# NBWEB-926: API - Refactor - Incluir internalTax si corresponde al procesar un carrito (crear pedclil)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-12 17:38 |
| Actualizado | 2024-11-22 00:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-926](https://bluinc.atlassian.net/browse/NBWEB-926) |

## Descripción

```
POST {API_URL}/v1/carrito/process
```

En gamma esta el ejemplo del pedido 0002-10356145 que lo cree desde internet con el item que tiene internalTax, pero creo en cero `[NewBytes_DBF].[dbo].pedclil.internaltax`
