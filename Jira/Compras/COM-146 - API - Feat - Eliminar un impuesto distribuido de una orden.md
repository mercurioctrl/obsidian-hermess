---
jira_key: "COM-146"
aliases: ["COM-146"]
summary: "API - Feat - Eliminar un impuesto distribuido de una orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-11-08 17:10"
updated: "2024-11-21 22:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-146"
---

# COM-146: API - Feat - Eliminar un impuesto distribuido de una orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-08 17:10 |
| Actualizado | 2024-11-21 22:24 |
| Etiquetas | ninguna |
| Jira | [COM-146](https://bluinc.atlassian.net/browse/COM-146) |

## Relaciones

- **Padre:** [[COM-77 - Editar orden de compra|COM-77]] Editar orden de compra
- **has action item:** [[COM-147 - APP - Feat - Agregar Editar Eliminar impuestos distribuidos|COM-147]] APP - Feat - Agregar / Editar / Eliminar impuestos distribuidos

## Descripcion

Agregaremos un recurso que nos permita ELIMINAR los impuestos distribuidos que tiene una orden determinada.

Para eso enviaremos solo el objeto `distributeTaxes` con la informacion necesaria de la siguiente forma, alterando o creando los registros dentro de `[NewBytes_DBF].[dbo].[pedproi]`

```
DELETE {API_URL}/v1/providerOrder/11368
```

```
"distributeTaxes": [  <<<<<-----------------NUEVO
      {
      "id": 3
      },              
  ],
```

[adjunto]
