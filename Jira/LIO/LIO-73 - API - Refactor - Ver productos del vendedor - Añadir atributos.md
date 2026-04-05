---
jira_key: "LIO-73"
aliases: ["LIO-73"]
summary: "API - Refactor - Ver productos del vendedor - Añadir atributos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-07-21 19:41"
updated: "2024-07-23 13:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-73"
---

# LIO-73: API - Refactor - Ver productos del vendedor - Añadir atributos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-07-21 19:41 |
| Actualizado | 2024-07-23 13:49 |
| Etiquetas | ninguna |
| Jira | [LIO-73](https://bluinc.atlassian.net/browse/LIO-73) |

## Relaciones

- **Padre:** [[LIO-28 - El sitio debe funcionar correctamente, sin puntos grises o cosas que no se|LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden
- **relates to:** [[LIO-62 - API - Review - Hacer que funcione como antes el perfil para ver los productos|LIO-62]] API - Review - Hacer que funcione como antes el perfil para ver los productos del vendedor
- **is blocked by:** [[LIO-75 - API - Refactor - Ver productos del vendedor - Error al buscar atributo|LIO-75]] API - Refactor - Ver productos del vendedor - Error al buscar atributo 

## Descripcion

- Realizaremos un refactor para que al buscar por reseller también nos aparezcan los atributos de sus artículos.



```
{{API_URL}}/v4/attributes?search=bitbayres
```

[adjunto]
- Adicional a esto, como se comento en la daily, realizaremos la normalización de las categorías almacenadas para que al hacer la comparación no haya discrepancia con los acentos.



[adjunto]
