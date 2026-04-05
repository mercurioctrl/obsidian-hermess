---
jira_key: "EXP-65"
aliases: ["EXP-65"]
summary: "API - Feat - Eliminar un serial o intervalo de seriales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-14 10:03"
updated: "2023-06-21 07:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-65"
---

# EXP-65: API - Feat - Eliminar un serial o intervalo de seriales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-14 10:03 |
| Actualizado | 2023-06-21 07:12 |
| Etiquetas | ninguna |
| Jira | [EXP-65](https://bluinc.atlassian.net/browse/EXP-65) |

## Relaciones

- **Padre:** [[EXP-11 - Feat - Serializar entrada de mercadería|EXP-11]] Feat - Serializar entrada de mercadería
- **blocks:** [[EXP-63 - APP - Feat - Herramienta borrar en modale Detalle de seriales por item|EXP-63]] APP - Feat - Herramienta borrar en modale Detalle de seriales por item

## Descripcion

```
DELETE {API_URL}/v1/providersOrders/{providerOrderId}/serials/{itemId}
```

```
{
"serials": [ 
'MMFE8YT000095',
'MMFE8YT000105'
]
}
```

Se deben eliminar los seriales para la orden y de el stock de seriales (`ST_DETALLLE_STOCK`)

Siempre hay que verificar que los seriales esten disponibles para ser eliminados (SIN FECHA DE EGRESO, EN ESTADO INICIAL Y EN DEPOSITO 1)
