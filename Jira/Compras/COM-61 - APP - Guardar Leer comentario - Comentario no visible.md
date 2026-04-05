---
jira_key: "COM-61"
aliases: ["COM-61"]
summary: "APP - Guardar / Leer comentario - Comentario no visible"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-02-21 15:10"
updated: "2024-02-22 14:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-61"
---

# COM-61: APP - Guardar / Leer comentario - Comentario no visible

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-21 15:10 |
| Actualizado | 2024-02-22 14:36 |
| Etiquetas | ninguna |
| Jira | [COM-61](https://bluinc.atlassian.net/browse/COM-61) |

## Relaciones

- **Padre:** [[COM-8]] Ordenes de compra
- **blocks:** [[COM-55]] APP - Feat - Guardar / Leer comentario

## Descripcion

- Al revisar el detalle de la orden, no aparece el comentario. 
`11070`



[adjunto]
Dato extra:
Este problema podría ser resultado de que el objeto de respuesta está contenido dentro de un arreglo.

```
getComment() {
        .getPurchaserComments(
          this.orderDetail.orderNumber
        )
        .then((res) => {
          this.sellerComment = res.comment <--------*
        })
    },
```

---

- De igual forma, no se visualiza la respuesta 



[adjunto]
