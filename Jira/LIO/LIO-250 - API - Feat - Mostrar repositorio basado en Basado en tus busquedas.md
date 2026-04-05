---
jira_key: "LIO-250"
aliases: ["LIO-250"]
summary: "API - Feat - Mostrar repositorio basado en \"Basado en tus busquedas\""
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-06 13:00"
updated: "2025-03-10 10:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-250"
---

# LIO-250: API - Feat - Mostrar repositorio basado en "Basado en tus busquedas"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-06 13:00 |
| Actualizado | 2025-03-10 10:16 |
| Etiquetas | ninguna |
| Jira | [LIO-250](https://bluinc.atlassian.net/browse/LIO-250) |

## Relaciones

- **Padre:** [[LIO-166 - Catalogos y sincronizaciones|LIO-166]] Catalogos y sincronizaciones
- **has action item:** [[LIO-252 - APP - Refactor - Agregar al catalogo la sección Basado en tus busquedas y|LIO-252]] APP - Refactor - Agregar al catalogo la sección "Basado en tus busquedas" y enlazar en la home 

## Descripcion

Quiero ver productos recomendados en la sección **"Basado en tus búsquedas"**, basado en la tabla de intereses para el usuario. Si el usuario no esta logueado, mostrar las que no tienen un usuario especifico.

```
GET {API_V4}/v4/basedOnYourSearches?search=&offset=0
```

### 📌 **Criterios de Aceptación**

✅ **1. Productos basados en intereses del usuario**

- Extraer datos de `[LO].[dbo].[user_interests]` para conocer categorías, marcas o tipos de productos que el usuario ha indicado como favoritos.


- Priorizar productos que coincidan con estas preferencias.



✅ **2. Alternativa cuando no hay datos suficientes**

- Si el usuario no tiene historial de carrito, visitas ni intereses registrados, mostrar:

- **Un mix de **`[LO].[dbo].[user_interest]` de los ultimos 15 dias
