---
jira_key: "NBWEB-699"
aliases: ["NBWEB-699"]
summary: "API - Refactor - Modificar el recurso que agrega items al carrito para que acepte enviar varios en una sola peticion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-11 09:17"
updated: "2024-04-15 04:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-699"
---

# NBWEB-699: API - Refactor - Modificar el recurso que agrega items al carrito para que acepte enviar varios en una sola peticion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-11 09:17 |
| Actualizado | 2024-04-15 04:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-699](https://bluinc.atlassian.net/browse/NBWEB-699) |

## Relaciones

- **Padre:** [[NBWEB-581 - CMS - Carrito web|NBWEB-581]] CMS - Carrito web
- **blocks:** [[NBWEB-700 - APP - Refactor - Agregar explicacion de que ahora pueden enviarse varios items|NBWEB-700]] APP - Refactor - Agregar explicacion de que ahora pueden enviarse varios items en el mismo payload para agregar al carrito, pero como algo aparte, dejando la explicacion que ya esta.
- **relates to:** [[NBWEB-708 - API - Agregar productos al carrito - Validar stock|NBWEB-708]] API - Agregar productos al carrito - Validar stock

## Descripcion

Por la misma razon que el refactor anterior, nos piden desarrrolladores de teceros su pueden hacer una sola peticion para enviar varios items a un carrrito en el recurso

```
POST {API_URL}/v1/carrito/item
```

```
[
  {
  "productId":117330,
  "amount":4,
  "type":0
  },
  {
  "productId":114530,
  "amount":1,
  "type":0
  },
  {
  "productId":237330,
  "amount":1,
  "type":0
  }
]
```

Probar bien que el recurso normal que se usa con un solo item no se rompa para el sitio
