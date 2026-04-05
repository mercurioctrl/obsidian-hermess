---
jira_key: "PED-789"
aliases: ["PED-789"]
summary: "APP - Feat - Agregar herramienta para listar,crear, eliminar utilidades extra para un producto y cliente determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-08-02 11:31"
updated: "2024-08-11 15:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-789"
---

# PED-789: APP - Feat - Agregar herramienta para listar,crear, eliminar utilidades extra para un producto y cliente determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-02 11:31 |
| Actualizado | 2024-08-11 15:52 |
| Etiquetas | ninguna |
| Jira | [PED-789](https://bluinc.atlassian.net/browse/PED-789) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente
- **is blocked by:** [[PED-784 - API - Refactor - Obtener productos para los cuales el cliente tiene una|PED-784]] API - Refactor - Obtener productos para los cuales el cliente tiene una utilidad extra (se debe poder leer,editar y eliminar)

## Descripcion

[adjunto]
Agregaremos una opción al menú “boton derecho” de clientes que diga “Marcar utilidad extra a un producto”.

Este levanta un modal con un listado de productos según el recurso [https://lioteam.atlassian.net/browse/PED-784](https://lioteam.atlassian.net/browse/PED-784)

Ese listado puede filtrarse con los filtros disponibles y ademas te permite eliminar de la lista un item determinado.

Adicionalmente agregaremos un accionable dentro del modal para “Agregar producto” lo que te permite incorporar con un buscador de productos una utilidad extra especifica para cada uno.
