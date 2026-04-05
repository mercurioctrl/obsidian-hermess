---
jira_key: "POS-147"
aliases: ["POS-147"]
summary: "API - Feat - Finalizar una postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-22 18:03"
updated: "2022-10-18 14:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-147"
---

# POS-147: API - Feat - Finalizar una postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-22 18:03 |
| Actualizado | 2022-10-18 14:20 |
| Etiquetas | ninguna |
| Jira | [POS-147](https://bluinc.atlassian.net/browse/POS-147) |

## Relaciones

- **Padre:** [[POS-21 - Solucion de postventa|POS-21]] Solucion de postventa
- **Subtarea:** [[POS-148 - API - Feat - Si la solucion implica retiro de mercaderia, agregar al correo una|POS-148]] API - Feat - Si la solucion implica retiro de mercaderia, agregar al correo una palabra clave usando el servicio para este fin
- **is blocked by:** [[POS-146 - API - Feat - Comprobar finalizacion pendiente posible|POS-146]] API - Feat - Comprobar finalizacion pendiente / posible
- **blocks:** [[POS-163 - APP - Feat - Finalizar una postventa|POS-163]] APP - Feat - Finalizar una postventa

## Descripcion

```
PATCH {API_URL}/v1/isReady/{aftersaleId}/isReady
```

Según la lógica mencionada en [link](https://lioteam.atlassian.net/browse/POS-146)

Mover una postventa (siempre que es posible) a finalizada.

Adicionalmente **se debe enviar un correo **Dando cuenta de cual fue la solución.
