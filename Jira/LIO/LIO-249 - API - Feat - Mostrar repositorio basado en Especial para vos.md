---
jira_key: "LIO-249"
aliases: ["LIO-249"]
summary: "API - Feat - Mostrar repositorio basado en \"Especial para vos\""
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-06 12:55"
updated: "2025-03-10 10:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-249"
---

# LIO-249: API - Feat - Mostrar repositorio basado en "Especial para vos"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-06 12:55 |
| Actualizado | 2025-03-10 10:13 |
| Etiquetas | ninguna |
| Jira | [LIO-249](https://bluinc.atlassian.net/browse/LIO-249) |

## Relaciones

- **Padre:** [[LIO-166]] Catalogos y sincronizaciones
- **has action item:** [[LIO-251]] APP - Refactor - Agregar al catalogo la seccion "Especial para vos" y enlazarla en la home

## Descripcion

Quiero ver productos recomendados en la sección **"Especial para vos"**, basados en mis intereses, visitas y artículos agregados al carrito, para descubrir nuevas opciones relevantes sin necesidad de buscarlas manualmente.

```
GET {API_V4}/v4/specialForYou?search=&offset=0
```

### 📌 **Criterios de Aceptación**

✅ **1. Productos basados en el carrito de compras**

- Extraer las categorías de los productos agregados en las tablas:

- `[LO].[dbo].[carritoExpress]`


- `[LO].[dbo].[carrito]`




- Mostrar productos dentro de las mismas categorías, excluyendo los que ya están en el carrito.



✅ **2. Productos basados en historial de visitas**

- Consultar `[LO].[dbo].[productosVisitas]` para identificar los productos más visitados por el usuario.


- Mostrar productos de categorías similares a los visitados recientemente.



✅ **3. Alternativa cuando no hay datos suficientes**

- Si el usuario no tiene historial de carrito, visitas ni intereses registrados, mostrar:

- **Los productos más vendidos de la plataforma (ultimos 15 dias).**


- **Las mejores ofertas actuales en base a descuentos aplicados en la columna descuentos de**` CS.dbo.productos`** (ultimos 15 dias).**


- **Nuevos lanzamientos o productos en tendencia en el último mes (ultimos 15 dias)**
