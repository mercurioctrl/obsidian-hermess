---
jira_key: "LIO-303"
aliases: ["LIO-303"]
summary: "APP - Refactor - Consumir y mostrar pedidos desde el nuevo recurso unificado GET /purchases"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-03-28 06:31"
updated: "2025-04-21 10:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-303"
---

# LIO-303: APP - Refactor - Consumir y mostrar pedidos desde el nuevo recurso unificado GET /purchases

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-28 06:31 |
| Actualizado | 2025-04-21 10:52 |
| Etiquetas | ninguna |
| Jira | [LIO-303](https://bluinc.atlassian.net/browse/LIO-303) |

## Relaciones

- **Padre:** [[LIO-281 - Compras|LIO-281]] Compras
- **action item from:** [[LIO-302 - APIv4 - Feat - Refactor de recurso de pedidos para unificar listado de ventas y|LIO-302]] APIv4 - Feat - Refactor de recurso de pedidos para unificar listado de ventas y compras
- **action item from:** [[LIO-298 - APIv4 - Feat - Oportunidad de mejora en listar y filtrar las compras|LIO-298]] APIv4 - Feat - Oportunidad de mejora en listar y filtrar las compras (orderStatus)

## Descripcion

Validaremos los objetos del back según lo conversado antes de comenzar la historia

Como usuario logueado, quiero visualizar mis pedidos (ya sea como comprador o vendedor) consumiendo un solo endpoint, con opciones de filtro, búsqueda y paginación, utilizando el nuevo recurso unificado del backend

Para esto ajustaremos ambas secciones “Mis Compras” / “Mis ventas” a los nuevos cambios de [link](https://lioteam.atlassian.net/browse/LIO-302) 

```
GET {API4_URL}/purchases?rol=vendedor&estado=todas&busqueda=genius&tipoStock=virtual&excluir=658220&page=1&limit=10
```

### 🧩 Contexto:

Ahora que el backend unificó los pedidos en `GET /purchases`, el frontend debe adaptarse para:

- Mostrar los pedidos desde la perspectiva que se indique (`vendedor` o `comprador`).


- Permitir aplicar filtros de estado, tipo de stock, búsqueda y exclusión.


- Soportar paginación.


- Mostrar visualmente si se trata de una venta o compra (`tipo`).



### ✅ Criterios de aceptación:

- Se muestra correctamente la lista de pedidos, diferenciando entre ventas y compras.


- El usuario puede alternar entre rol `"vendedor"` y `"comprador"` desde un selector.


- Se aplican correctamente los filtros:

- Estado (`estado`)


- Tipo de stock (`tipoStock`)


- Búsqueda (`busqueda`)




- Se visualiza paginación cuando `limit` es superado.


- El botón de “Ver más” o paginador carga correctamente la siguiente página (`page`).


- Si no hay resultados, se muestra un mensaje amigable.


- En cada ítem de la lista se muestra si fue una venta o compra, con estilo visual diferenciado (badge, color, icono, etc).
