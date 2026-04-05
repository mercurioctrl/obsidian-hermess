---
jira_key: "PED-544"
aliases: ["PED-544"]
summary: "API - Refactor - Cuando eliminamos un envio, debemos eliminar tambien el \"destino final\" que lo acompaña"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-07 16:50"
updated: "2024-02-14 15:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-544"
---

# PED-544: API - Refactor - Cuando eliminamos un envio, debemos eliminar tambien el "destino final" que lo acompaña

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-07 16:50 |
| Actualizado | 2024-02-14 15:27 |
| Etiquetas | ninguna |
| Jira | [PED-544](https://bluinc.atlassian.net/browse/PED-544) |

## Relaciones

- **Padre:** [[PED-58]] Agregar / Editar Envío en las ordenes de compra
- **blocks:** [[PED-541]] APP - Feat - Maquetar cotizacion de "Destino final para el transporte"
- **relates to:** [[PED-554]] API - Destino final para el transporte - Eliminar destino final

## Descripcion

Siempre que ejecutemos la acción de remover un envío, tambien cuando editamos el mismo (agregamos o sacamos un item)

Debemos sacar tambien el destino secundario final en caso de que exista.

```
DELETE {API_URL}/v1/orders/{branch-order}/removeFinalShipping
```

[adjunto]
