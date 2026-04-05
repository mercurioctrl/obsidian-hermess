---
jira_key: "EXP-47"
aliases: ["EXP-47"]
summary: "API - Feat - Ingresar nuevos seriales a un producto NO SERIALIZADO, dentro de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-07 22:52"
updated: "2023-06-21 07:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-47"
---

# EXP-47: API - Feat - Ingresar nuevos seriales a un producto NO SERIALIZADO, dentro de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 22:52 |
| Actualizado | 2023-06-21 07:11 |
| Etiquetas | ninguna |
| Jira | [EXP-47](https://bluinc.atlassian.net/browse/EXP-47) |

## Relaciones

- **Padre:** [[EXP-11 - Feat - Serializar entrada de mercadería|EXP-11]] Feat - Serializar entrada de mercadería

## Descripcion

Este es el caso cuando viene mercadería no serializada o a granel y entonces deben darse de alta seriales internos (generados por nosotros en este paso).

Para esto tomaremos algún prefijo del articulo/compra y lo concatenaremos con un aparte numérica de 5 dígitos (completar con ceros a la izquierda).

De esta forma ingresaremos todos los seriales.

Este recurso es una extensión de [link](https://lioteam.atlassian.net/browse/EXP-42).

```
POST {API_URL}/v1/providersOrders/{providerOrderId}/serials/{itemId}
```

Payload:

```
[
  {
    mode:auto, //indica el modo para la lista
  }
]
```

---

Desde el Front, cuando se elije esta opción, solo se hará clic en un boton “Seriales automáticos”.
