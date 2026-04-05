---
jira_key: "COM-87"
aliases: ["COM-87"]
summary: "API - Refactor - Agregar/Editar un item no debe tener como campo obligatorio la posicion arancelaria"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2024-04-24 09:36"
updated: "2024-05-07 20:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-87"
---

# COM-87: API - Refactor - Agregar/Editar un item no debe tener como campo obligatorio la posicion arancelaria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2024-04-24 09:36 |
| Actualizado | 2024-05-07 20:27 |
| Etiquetas | ninguna |
| Jira | [COM-87](https://bluinc.atlassian.net/browse/COM-87) |

## Relaciones

- **causes:** [[COM-83 - APP - Feat - Agregar item a una orden de compra|COM-83]] APP - Feat - Agregar item a una orden de compra
- **is blocked by:** [[COM-89 - API - AgregarEditar Item - Posición arancelaría indefinida|COM-89]] API - Agregar/Editar Item - Posición arancelaría indefinida 

## Descripcion

```
           {
                "id": 104829,
                "price": {
                    "value": 50,
                    "iva": 21,
                },
                "amount": 6,
                "position": "4823.69.00.200M",<-- No obligatorio
            },
```
